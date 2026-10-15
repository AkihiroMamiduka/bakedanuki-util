# coding: utf-8
"""接続された整数属性の標準入力、精度保持とUndoを検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    MayaIntOffsetEdit,
    MayaIntValueEdit,
    MayaNodeValueSnapshot,
    MayaScalarValueSnapshot,
    MayaScalarValueTransfer,
    apply_plugs_values,
    apply_scalar_value_transfer,
    apply_scalar_value_transfer_to_paths,
    apply_scalar_value_to_paths,
    resolve_int_plug,
)
from bd_util.ui import qt


def flush():
    """Maya通知とQtの遅延破棄を処理する。"""
    for _ in range(3):
        qt.QApplication.processEvents()
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.fixture(params=["byte", "short", "long"])
def scene(new_scene, request):
    """整数型ごとに専用属性を作り、Auto Keyと監視を後始末する。"""
    auto = cmds.autoKeyframe(query=True, state=True)
    cmds.autoKeyframe(state=False)
    cmds.undoInfo(state=True)
    owner = qt.QObject()
    nodes = tuple(cmds.createNode("transform") for _ in range(3))
    for node in nodes:
        cmds.addAttr(
            node, longName="count", attributeType=request.param, keyable=True
        )
    yield nodes, owner, request.param
    cmds.autoKeyframe(state=False)
    owner.deleteLater()
    flush()
    cmds.autoKeyframe(state=auto)


def animate(path):
    """小数キーを含む整数属性をキーのない時刻で評価する。"""
    cmds.setKeyframe(path, time=1, value=2.25)
    cmds.setKeyframe(path, time=10, value=8.75)
    cmds.keyTangent(
        path, edit=True, inTangentType="linear", outTangentType="linear"
    )
    cmds.currentTime(5)
    return cmds.listConnections(path, source=True, destination=False)[0]


def bind(nodes, owner, **options):
    """型を保った整数入力と接続状態の監視を有効にする。"""
    return MayaIntPlugsBinding(
        tuple(resolve_int_plug(node, "count") for node in nodes),
        parent=owner,
        track_input_state=True,
        **options,
    )


def curves():
    """全カーブの小数キーと接線を比較できるsnapshotを返す。"""
    return tuple(
        (
            curve,
            tuple(cmds.keyframe(curve, query=True, timeChange=True) or ()),
            tuple(cmds.keyframe(curve, query=True, valueChange=True) or ()),
            tuple(
                cmds.keyTangent(curve, query=True, inTangentType=True) or ()
            ),
            tuple(
                cmds.keyTangent(curve, query=True, outTangentType=True) or ()
            ),
        )
        for curve in sorted(cmds.ls(type="animCurve") or ())
    )


@pytest.mark.parametrize("auto", [False, True])
def test_time_input_noop_and_mixed_targets(scene, auto):
    """通常値と時間カーブを一度で変更し、小数キーまでUndoで戻す。"""
    nodes, owner, kind = scene
    path = nodes[0] + ".count"
    curve = animate(path)
    before = curves()
    initial = cmds.getAttr(path)
    cmds.setAttr(nodes[2] + ".count", lock=True)
    binding = bind(nodes, owner, edit_connected=True)
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    assert binding.target_states[0].input_state == "animated"
    assert binding.writable_count == 2
    assert binding.set_value(200)
    flush()
    assert binding.value == cmds.getAttr(path) == 200
    assert type(binding.value) is int
    assert cmds.getAttr(nodes[1] + ".count") == 200
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == (
        3 if auto else 2
    )
    assert binding.target_states[0].input_state == (
        "keyed" if auto else "key_altered"
    )
    cmds.undo()
    flush()
    assert binding.value == initial
    assert cmds.getAttr(nodes[1] + ".count") == 0
    assert curves() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == 200
    cmds.currentTime(6)
    cmds.currentTime(5)
    flush()
    assert binding.value == (200 if auto else initial)


def test_single_noop_keeps_fractional_curve_and_validates_options(scene):
    """同じ整数評価値を再入力しても元の小数キーやUndoを変更しない。"""
    nodes, owner, _kind = scene
    animate(nodes[0] + ".count")
    before = curves()
    plug = resolve_int_plug(nodes[0], "count")
    default = MayaIntPlugBinding(plug, parent=owner)
    assert not default.view_model.set_value_command.can_execute
    binding = MayaIntPlugBinding(plug, edit_connected=True, parent=owner)
    cmds.autoKeyframe(state=True)
    cmds.flushUndo()
    assert not binding.set_value(binding.value)
    assert curves() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    with pytest.raises(ValueError):
        MayaIntPlugBinding(
            plug, key_animated=True, edit_connected=True, parent=owner
        )
    with pytest.raises(TypeError):
        MayaIntPlugBinding(plug, edit_connected=1, parent=owner)


@pytest.mark.parametrize("auto", [False, True])
def test_sdk_input_undo_and_driver_reevaluation(scene, auto):
    """SDKには整数の一時値だけを入力し、キーを維持する。"""
    nodes, owner, _kind = scene
    path, driver = nodes[0] + ".count", nodes[1] + ".tx"
    cmds.setDrivenKeyframe(
        path, currentDriver=driver, driverValue=0, value=2.25
    )
    cmds.setDrivenKeyframe(
        path, currentDriver=driver, driverValue=10, value=8.75
    )
    before = curves()
    binding = bind(nodes[:1], owner, edit_connected=True)
    initial = binding.value
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    assert binding.target_states[0].input_state == "driven_key"
    assert binding.set_value(42)
    flush()
    assert binding.value == 42
    binding.refresh()
    assert binding.value == 42
    assert curves() == before
    cmds.undo()
    flush()
    assert binding.value == initial
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    cmds.setAttr(driver, 10)
    flush()
    assert binding.value == cmds.getAttr(path)
    assert binding.value != 42
    assert curves() == before


@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize("weight", [0, 0.5, 1])
@pytest.mark.parametrize("override", [False, True])
def test_layer_matches_native_input(scene, auto, weight, override):
    """Layerの整数合成結果とキーをMaya標準setAttrと比較する。"""
    nodes, owner, kind = scene
    path = nodes[0] + ".count"
    animate(path)
    layer = cmds.animLayer("intLayer", attribute=path, override=override)
    if kind == "byte":
        assert not cmds.animLayer(layer, query=True, attribute=True)
        assert (
            bind(nodes[:1], owner, edit_connected=True)
            .target_states[0]
            .input_state
            == "animated"
        )
        return
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.setKeyframe(path, animLayer=layer, time=1, value=1)
    cmds.setKeyframe(path, animLayer=layer, time=10, value=3)
    cmds.setAttr(layer + ".weight", weight)
    cmds.currentTime(5)
    initial, before = cmds.getAttr(path), curves()
    cmds.autoKeyframe(state=auto)
    # 同じsceneで標準コマンドの結果を取得し、Undo後にBinding入力と比べる
    cmds.undoInfo(openChunk=True, chunkName="NativeIntInput")
    try:
        cmds.setAttr(path, 42)
    finally:
        cmds.undoInfo(closeChunk=True)
    expected, expected_curves = cmds.getAttr(path), curves()
    if cmds.undoInfo(query=True, undoName=True) != "NativeIntInput":
        cmds.undo()
    assert cmds.undoInfo(query=True, undoName=True) == "NativeIntInput"
    cmds.undo()
    assert curves() == before
    binding = bind(nodes[:1], owner, edit_connected=True)
    assert binding.target_states[0].input_state == "animation_layer"
    assert binding.view_model.set_value_command.can_execute
    cmds.flushUndo()
    assert binding.set_value(42)
    flush()
    assert binding.value == expected
    assert curves() == expected_curves
    cmds.undo()
    flush()
    assert binding.value == initial
    assert curves() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize(
    "apply",
    [
        apply_scalar_value_transfer,
        apply_scalar_value_transfer_to_paths,
        apply_scalar_value_to_paths,
    ],
)
@pytest.mark.parametrize("policy", ["edit_connected", "key_animated"])
def test_paste_and_explicit_key_policy(scene, apply, policy):
    """三つのPaste入口と常時キー入力でも整数の接続方針を通す。"""
    nodes, owner, kind = scene
    path = nodes[0] + ".count"
    animate(path)
    transfer = MayaScalarValueTransfer(
        (MayaNodeValueSnapshot((MayaScalarValueSnapshot("count", kind, 42),)),)
    )
    args = (
        (transfer,)
        if apply is apply_scalar_value_transfer
        else (("count",), transfer)
    )
    cmds.flushUndo()
    before = curves()
    result = apply(nodes[:1], *args, **{policy: True})
    assert result.changed and not result.excluded
    assert cmds.getAttr(path) == 42
    if policy == "edit_connected":
        assert curves() == before
    cmds.undo()
    assert curves() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    binding = bind(nodes[:1], owner, key_animated=True)
    assert binding.set_value(43)
    assert cmds.keyframe(path, query=True, time=(5, 5), valueChange=True) == [
        43
    ]


def test_atomic_offset_and_limit_validation(scene):
    """整数差分と範囲外入力を接続先全体で事前検証する。"""
    nodes, owner, _kind = scene
    animate(nodes[0] + ".count")
    cmds.addAttr(nodes[1] + ".count", edit=True, minValue=0, maxValue=10)
    first = bind(nodes[:1], owner, edit_connected=True)
    second = bind(nodes[1:2], owner, edit_connected=True)
    before = curves()
    initial = first.value
    cmds.autoKeyframe(state=True)
    cmds.flushUndo()
    with pytest.raises(ValueError):
        apply_plugs_values(
            [MayaIntValueEdit(first, 20), MayaIntValueEdit(second, 20)]
        )
    assert curves() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    assert apply_plugs_values(
        [MayaIntOffsetEdit(first, 1), MayaIntOffsetEdit(second, 1)]
    )
    assert first.value == initial + 1
    assert second.value == 1
    cmds.undo()
    flush()
    assert first.value == initial and second.value == 0
    assert curves() == before


@pytest.mark.parametrize(
    "value",
    [
        -2147483649.0,
        -32768.5,
        -2.5,
        -0.5,
        0.5,
        255.5,
        32767.5,
        2147483647.0,
        2147483647.5,
    ],
)
def test_integer_curve_conversion_is_not_key_altered(scene, value):
    """小数補間と境界でのDG整数変換を手動変更と取り違えない。"""
    nodes, owner, _kind = scene
    path = nodes[0] + ".count"
    cmds.setKeyframe(path, time=1, value=value)
    cmds.currentTime(1)
    binding = bind(nodes[:1], owner, edit_connected=True)
    assert binding.target_states[0].input_state == "keyed"
    # 32-bit端でも1だけの手動変更を相対誤差で見落とさない
    next_value = binding.value - 1 if binding.value > 0 else 1
    assert binding.set_value(next_value)
    assert binding.target_states[0].input_state == "key_altered"


@pytest.mark.parametrize("auto", [False, True])
def test_later_failure_restores_fractional_keys(scene, monkeypatch, auto):
    """後続失敗時に一時値と小数キーを復旧し、Auto Keyを維持する。"""
    nodes, owner, _kind = scene
    animate(nodes[0] + ".count")
    binding = bind(nodes[:2], owner, edit_connected=True)
    initial, before = binding.value, curves()
    cmds.autoKeyframe(state=auto)
    original = cmds.setAttr

    def fail_later(name, *args, **kwargs):
        """後続の通常属性への新規値だけを拒否する。"""
        if name.rsplit("|", 1)[-1] == nodes[1] + ".count" and args == (42,):
            raise RuntimeError("later failure")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(cmds, "setAttr", fail_later)
    with pytest.raises(RuntimeError, match="later failure"):
        binding.set_value(42)
    flush()
    assert binding.value == initial
    assert cmds.getAttr(nodes[1] + ".count") == 0
    assert curves() == before
    assert cmds.autoKeyframe(query=True, state=True) is auto
