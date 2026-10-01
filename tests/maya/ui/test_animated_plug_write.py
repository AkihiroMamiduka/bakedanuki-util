# coding: utf-8
"""直接カーブの値入力、キー情報、復旧と標準Undoを検証する。"""

import math

import pytest
from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from bd_util.maya.ui.binding._animated_plug_write import (
    animation_edit_reason,
    prepare_animated_plug_write,
)


@pytest.fixture(autouse=True)
def units_and_undo(new_scene):
    """シーンと単位を独立させ、利用者のUndo設定を終了時に戻す。"""
    units = {
        kind: cmds.currentUnit(query=True, **{kind: True})
        for kind in ("angle", "linear", "time")
    }
    undo = cmds.undoInfo(query=True, state=True)
    cmds.currentUnit(angle="deg", linear="cm", time="film")
    cmds.undoInfo(state=True)
    yield
    cmds.currentUnit(**units)
    cmds.undoInfo(state=undo)


def make_target(attribute="tx"):
    """非共有の時間カーブを持つscalar属性とAPI参照を返す。"""
    node = cmds.createNode("transform")
    if attribute == "mode":
        cmds.addAttr(
            node, longName="mode", attributeType="enum", enumName="A:B:C"
        )
    path = node + "." + attribute
    values = (0, 1) if attribute in ("v", "mode") else (1, 3)
    for frame, value in zip((1, 9), values):
        cmds.setKeyframe(path, time=frame, value=value)
    plug = om.MSelectionList().add(path).getPlug(0)
    curve = oma.MFnAnimCurve(plug.sourceWithConversion().node())
    return plug, curve


def curve_state(curve):
    """値と接線ベクトルを含む全キーの比較可能な状態を取得する。"""
    return tuple(
        (
            curve.input(index).asUnits(om.MTime.kSeconds),
            curve.value(index),
            curve.inTangentType(index),
            curve.outTangentType(index),
            curve.tangentsLocked(index),
            curve.weightsLocked(index),
            curve.isBreakdown(index),
            curve.getTangentXY(index, True),
            curve.getTangentXY(index, False),
        )
        for index in range(curve.numKeys)
    )


@pytest.mark.parametrize("weighted", [False, True])
def test_existing_key_preserves_metadata_and_native_history(weighted):
    """値編集だけを行い、手動接線とbreakdownをUndo・Redoでも維持する。"""
    plug, curve = make_target()
    curve.setIsWeighted(weighted)
    curve.setTangentsLocked(0, False)
    curve.setTangent(0, om.MAngle(0.2), 0.15, True)
    curve.setTangent(0, om.MAngle(-0.4), 0.2, False)
    curve.setWeightsLocked(0, True)
    curve.setIsBreakdown(0, True)
    cmds.currentTime(1)
    before = curve_state(curve)
    cmds.flushUndo()
    write = prepare_animated_plug_write(plug, 25)
    write.apply()
    after = curve_state(curve)
    assert after[0][2:] == before[0][2:]
    assert plug.asDouble() == pytest.approx(25)
    cmds.undo()
    assert curve_state(curve) == before
    assert plug.asDouble() == pytest.approx(1)
    cmds.redo()
    assert curve_state(curve) == after
    assert plug.asDouble() == pytest.approx(25)
    write.restore()
    assert curve_state(curve) == before


@pytest.mark.parametrize("attribute", ["tx", "rx", "sx", "v", "mode"])
@pytest.mark.parametrize("existing", [False, True])
def test_unit_values_key_creation_and_rollback(attribute, existing):
    """非標準単位と離散型でも公開値を反映し、元のキー有無を復元する。"""
    plug, curve = make_target(attribute)
    cmds.currentUnit(linear="m", angle="rad")
    cmds.currentTime(1 if existing else 5)
    before = curve_state(curve)
    requested = 1 if attribute in ("v", "mode") else 125
    assert animation_edit_reason(plug) is None
    write = prepare_animated_plug_write(plug, requested)
    write.apply()
    expected = math.radians(requested) if attribute == "rx" else requested
    assert plug.asDouble() == pytest.approx(expected)
    assert curve.numKeys == (2 if existing else 3)
    if attribute in ("v", "mode") and not existing:
        assert curve.outTangentType(1) == oma.MFnAnimCurve.kTangentStep
    write.restore()
    assert curve_state(curve) == before


@pytest.mark.parametrize("weighted", [False, True])
def test_new_key_restore_keeps_neighbor_tangents(weighted):
    """新規キーを取り消しても既存の手動接線とロックを変えない。"""
    plug, curve = make_target()
    curve.setIsWeighted(weighted)
    for index in range(curve.numKeys):
        curve.setTangentsLocked(index, False)
        curve.setTangent(index, om.MAngle(0.2), 0.15, True)
        curve.setTangent(index, om.MAngle(-0.4), 0.2, False)
        curve.setWeightsLocked(index, True)
        curve.setIsBreakdown(index, True)
    cmds.currentTime(5)
    before = curve_state(curve)
    write = prepare_animated_plug_write(plug, 25)
    write.apply()
    after = curve_state(curve)
    cmds.undo()
    assert curve_state(curve) == before
    cmds.redo()
    assert curve_state(curve) == after
    write.restore()
    assert curve_state(curve) == before


@pytest.mark.parametrize("change", ["time", "units", "lock", "connection"])
def test_prepared_write_rejects_changed_context(change):
    """事前構築後の時刻・単位・lock・接続変更には書き込まない。"""
    plug, curve = make_target()
    cmds.currentTime(5)
    write = prepare_animated_plug_write(plug, 25)
    if change == "time":
        cmds.currentTime(6)
    elif change == "units":
        cmds.currentUnit(linear="m")
    elif change == "lock":
        cmds.setAttr(plug.name(), lock=True)
    else:
        replacement = cmds.createNode("animCurveTL")
        cmds.setKeyframe(replacement, time=1, value=50)
        cmds.connectAttr(replacement + ".output", plug.name(), force=True)
    before = curve_state(curve)
    with pytest.raises(RuntimeError):
        write.apply()
    assert curve_state(curve) == before


@pytest.mark.parametrize(
    "kind", ["shared", "conversion", "driven", "time_driver", "locked"]
)
def test_unsupported_connection_stays_read_only(kind):
    """複雑な接続と読み取り専用カーブは自動編集へ含めない。"""
    plug, curve = make_target()
    if kind == "shared":
        other = cmds.createNode("transform")
        cmds.connectAttr(curve.name() + ".output", other + ".tx")
    elif kind == "conversion":
        conversion = cmds.createNode("unitConversion")
        cmds.connectAttr(curve.name() + ".output", conversion + ".input")
        cmds.connectAttr(conversion + ".output", plug.name(), force=True)
    elif kind == "driven":
        driven = cmds.createNode("animCurveUL")
        cmds.connectAttr(driven + ".output", plug.name(), force=True)
    elif kind == "time_driver":
        driver = cmds.createNode("addDoubleLinear")
        cmds.connectAttr(driver + ".output", curve.name() + ".input")
    else:
        cmds.lockNode(curve.name(), lock=True)
    before = curve_state(curve)
    assert animation_edit_reason(plug) is not None
    with pytest.raises(RuntimeError):
        prepare_animated_plug_write(plug, 25)
    assert curve_state(curve) == before
