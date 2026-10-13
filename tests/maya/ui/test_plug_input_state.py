# coding: utf-8
"""入力接続の表示状態と、値が変わらないキー編集の通知を検証する。"""

from __future__ import annotations

import pytest
from maya import cmds
from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from bd_util.maya.ui import (
    MayaFloatPlugsBinding,
    inspect_plug_input_state,
    resolve_float_plug,
)
from bd_util.ui import qt


def _events() -> None:
    """Maya通知を受けた次のQtイベントまで状態を同期する。"""
    for _ in range(4):
        qt.QApplication.processEvents()


@pytest.fixture
def scene(new_scene):
    """接続状態を独立して検証できる二つのtransformを用意する。"""
    owner = qt.QObject()
    nodes = (cmds.createNode("transform"), cmds.createNode("transform"))
    cmds.currentTime(1)
    yield nodes, owner
    owner.deleteLater()
    _events()


def _plug(path: str) -> om.MPlug:
    """テスト用のMaya属性をAPI参照へ変換する。"""
    return om.MSelectionList().add(path).getPlug(0)


def test_four_states_use_exact_current_time_without_writing(scene) -> None:
    """現在キー・他時刻キー・一般接続・未接続を読み取る。"""
    nodes, _owner = scene
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    cmds.connectAttr(nodes[1] + ".tx", nodes[0] + ".tz")
    cmds.flushUndo()
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "keyed"
    assert inspect_plug_input_state(_plug(nodes[0] + ".tz")) == "connected"
    assert inspect_plug_input_state(_plug(nodes[0] + ".ry")) == "unconnected"
    cmds.currentTime(5.25)
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "animated"
    cmds.setKeyframe(nodes[0] + ".tx", time=5.25, value=3)
    cmds.flushUndo()
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "keyed"
    assert (
        inspect_plug_input_state(
            _plug(nodes[0] + ".tx"), time=om.MTime(5.2501, om.MTime.uiUnit())
        )
        == "animated"
    )
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_parent_connection_and_nonstandard_curve_are_connected(scene) -> None:
    """親接続と独自時間入力を現在時刻キーと取り違えない。"""
    nodes, _owner = scene
    source = cmds.createNode("multiplyDivide")
    cmds.connectAttr(source + ".output", nodes[0] + ".translate")
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "connected"
    cmds.setKeyframe(nodes[1] + ".ty", time=1, value=3)
    curve = cmds.listConnections(nodes[1] + ".ty", source=True)[0]
    driver = cmds.createNode("addDoubleLinear")
    cmds.connectAttr(driver + ".output", curve + ".input", force=True)
    assert inspect_plug_input_state(_plug(nodes[1] + ".ty")) == "connected"


def test_pair_blend_and_constraint_classify_children_of_connected_parent(
    scene,
) -> None:
    """属性名ではなく直結元の型で、compound子属性も分類する。"""
    nodes, _owner = scene
    blend = cmds.createNode("pairBlend")
    constraint = cmds.createNode("scaleConstraint")
    cmds.connectAttr(blend + ".outRotate", nodes[0] + ".rotate")
    cmds.connectAttr(constraint + ".constraintScale", nodes[1] + ".scale")
    cmds.connectAttr(blend + ".outTranslateX", nodes[1] + ".tx")
    cmds.connectAttr(constraint + ".constraintScaleX", nodes[0] + ".sx")
    for axis in "xyz":
        assert (
            inspect_plug_input_state(_plug(nodes[0] + ".r" + axis))
            == "pair_blend"
        )
        assert (
            inspect_plug_input_state(_plug(nodes[1] + ".s" + axis))
            == "constraint"
        )
    assert inspect_plug_input_state(_plug(nodes[1] + ".tx")) == "pair_blend"
    assert inspect_plug_input_state(_plug(nodes[0] + ".sx")) == "constraint"


def test_driven_key_expression_and_animation_layer_are_distinct(scene) -> None:
    """属性名に依存せず、直結する特殊な入力元を区別する。"""
    nodes, _owner = scene
    driver = cmds.createNode("transform")
    cmds.addAttr(
        driver, longName="control", attributeType="double", keyable=True
    )
    cmds.setDrivenKeyframe(
        nodes[0] + ".tx", currentDriver=driver + ".control", value=3
    )
    cmds.expression(string=f"{nodes[0]}.ty = {driver}.ty * 2;")
    layer = cmds.animLayer("ProbeLayer", attribute=[nodes[0] + ".rz"])
    cmds.setKeyframe(nodes[0] + ".rz", time=1, value=5, animLayer=layer)

    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "driven_key"
    assert inspect_plug_input_state(_plug(nodes[0] + ".ty")) == "expression"
    assert (
        inspect_plug_input_state(_plug(nodes[0] + ".rz")) == "animation_layer"
    )
    plain_blend = cmds.createNode("animBlendNodeAdditiveDA")
    cmds.connectAttr(plain_blend + ".output", nodes[1] + ".rx")
    assert inspect_plug_input_state(_plug(nodes[1] + ".rx")) == "connected"


def test_mute_tracks_active_flag_and_unconnected_nonkeyable(scene) -> None:
    """muteの実効状態と未接続かつキー設定不可の表示を検証する。"""
    nodes, owner = scene
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    cmds.mute(nodes[0] + ".tx")
    mute_node = cmds.listConnections(nodes[0] + ".tx", source=True)[0]
    cmds.setAttr(nodes[0] + ".ty", keyable=False, channelBox=True)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")],
        track_input_state=True,
        parent=owner,
    )

    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "muted"
    assert binding.target_states[0].input_state == "muted"
    assert inspect_plug_input_state(_plug(nodes[0] + ".ty")) == "nonkeyable"
    assert inspect_plug_input_state(_plug(nodes[0] + ".tz")) == "unconnected"
    cmds.connectAttr(nodes[1] + ".ty", nodes[0] + ".ty")
    assert inspect_plug_input_state(_plug(nodes[0] + ".ty")) == "connected"
    cmds.setAttr(mute_node + ".mute", False)
    _events()
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "keyed"
    assert binding.target_states[0].input_state == "keyed"


def test_key_altered_differs_from_off_frame_animation(scene) -> None:
    """キー値を残した現在値の手動変更だけをKey Alteredとする。"""
    nodes, owner = scene
    path = nodes[0] + ".sx"
    cmds.setKeyframe(path, time=1, value=2)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "sx")],
        track_input_state=True,
        key_animated=True,
        parent=owner,
    )
    assert binding.target_states[0].input_state == "keyed"
    cmds.setAttr(path, 5)
    _events()
    assert cmds.keyframe(path, query=True, valueChange=True) == [2.0]
    assert inspect_plug_input_state(_plug(path)) == "key_altered"
    assert binding.target_states[0].input_state == "key_altered"
    cmds.currentTime(5)
    _events()
    assert inspect_plug_input_state(_plug(path)) == "animated"
    assert binding.target_states[0].input_state == "animated"


@pytest.mark.parametrize(
    ("attribute", "key_value", "altered_value"),
    [
        ("tx", 2.25, 5.0),
        ("rx", 12.5, 20.0),
        ("sx", 3.5, 4.0),
        ("visibility", 1, 0),
        ("mode", 1, 2),
    ],
)
def test_key_altered_supports_attribute_value_types(
    scene, attribute: str, key_value: float, altered_value: float
) -> None:
    """距離・角度・無単位・真偽・列挙の差をキー評価値で判定する。"""
    nodes, _owner = scene
    if attribute == "mode":
        cmds.addAttr(
            nodes[0],
            longName="mode",
            attributeType="enum",
            enumName="A:B:C",
            keyable=True,
        )
    path = nodes[0] + "." + attribute
    cmds.setKeyframe(path, time=1, value=key_value)
    assert inspect_plug_input_state(_plug(path)) == "keyed"
    cmds.setAttr(path, altered_value)
    assert inspect_plug_input_state(_plug(path)) == "key_altered"
    assert (
        inspect_plug_input_state(
            _plug(path), time=om.MTime(5, om.MTime.uiUnit())
        )
        == "animated"
    )


def test_time_editor_clip_is_classified_only_while_driving(scene) -> None:
    """Time Editorの実接続がある間だけAnimation Clipと判定する。"""
    nodes, owner = scene
    path = nodes[0] + ".tx"
    cmds.setKeyframe(path, time=1, value=1)
    cmds.setKeyframe(path, time=10, value=2)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")],
        track_input_state=True,
        parent=owner,
    )
    assert binding.target_states[0].input_state == "keyed"
    cmds.select(nodes[0])
    cmds.timeEditorComposition("ProbeComposition", createTrack=True)
    clip = cmds.timeEditorClip(
        "ProbeClip",
        addSelectedObjects=True,
        type=["animCurveTL"],
        track="ProbeComposition:0",
    )
    _events()
    assert inspect_plug_input_state(_plug(path)) == "animation_clip"
    assert binding.target_states[0].input_state == "animation_clip"
    assert cmds.timeEditor(drivingClipsForAttr=path) == [clip]
    cmds.timeEditor(mute=True)
    try:
        _events()
        assert inspect_plug_input_state(_plug(path)) == "unconnected"
        assert binding.target_states[0].input_state == "unconnected"
    finally:
        cmds.timeEditor(mute=False)
    _events()
    assert inspect_plug_input_state(_plug(path)) == "animation_clip"
    assert binding.target_states[0].input_state == "animation_clip"
    cmds.timeEditorClip(edit=True, removeClip=True, clipId=clip)
    _events()
    assert inspect_plug_input_state(_plug(path)) == "unconnected"
    assert binding.target_states[0].input_state == "unconnected"


def test_read_only_curve_still_shows_keys(scene) -> None:
    """共有・ロックされたカーブも接続表示からは除外しない。"""
    nodes, _owner = scene
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    curve = cmds.listConnections(nodes[0] + ".tx", source=True)[0]
    cmds.connectAttr(curve + ".output", nodes[1] + ".tx")
    cmds.lockNode(curve, lock=True)
    cmds.setAttr(nodes[0] + ".tx", lock=True)
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "keyed"
    assert inspect_plug_input_state(_plug(nodes[1] + ".tx")) == "keyed"
    cmds.currentTime(5)
    assert inspect_plug_input_state(_plug(nodes[0] + ".tx")) == "animated"


def test_binding_tracks_equal_value_key_edits_and_time_changes(scene) -> None:
    """同値キーと一定値カーブの時刻移動だけでも状態変更を通知する。"""
    nodes, owner = scene
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    tracked = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")],
        track_input_state=True,
        key_animated=True,
        parent=owner,
    )
    default = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[1], "ty")], parent=owner
    )
    assert tracked.target_states[0].input_state == "keyed"
    assert default.target_states[0].input_state is None
    signals: list[str] = []
    tracked.state_changed.connect(
        lambda: signals.append(tracked.target_states[0].input_state or "none")
    )

    cmds.currentTime(5)
    _events()
    assert tracked.target_states[0].input_state == "animated"
    assert signals[-1] == "animated"
    cmds.setKeyframe(nodes[0] + ".tx", time=5, value=3)
    _events()
    assert tracked.target_states[0].input_state == "keyed"
    assert signals[-1] == "keyed"
    cmds.cutKey(nodes[0] + ".tx", time=(5, 5), clear=True)
    _events()
    assert tracked.target_states[0].input_state == "animated"
    assert signals[-1] == "animated"

    # 値が一定のまま時刻とキーだけを変え、表示用監視の終了も確認する
    cmds.currentTime(1)
    _events()
    assert tracked.target_states[0].input_state == "keyed"
    callback_count = len(tracked.store._registry.callback_ids)
    tracked.dispose()
    assert tracked.store._registry.callback_ids == ()
    assert callback_count > 0


def test_connection_changes_replace_curve_observation(scene) -> None:
    """接続と切断に合わせてカーブ監視を切り替える。"""
    nodes, owner = scene
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")],
        track_input_state=True,
        parent=owner,
    )
    assert binding.target_states[0].input_state == "unconnected"
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    _events()
    assert binding.target_states[0].input_state == "keyed"
    curve = oma.MFnAnimCurve(
        _plug(nodes[0] + ".tx").sourceWithConversion().node()
    ).name()
    cmds.disconnectAttr(curve + ".output", nodes[0] + ".tx")
    _events()
    assert binding.target_states[0].input_state == "unconnected"
    cmds.setKeyframe(curve, time=5, value=3)
    _events()
    assert binding.target_states[0].input_state == "unconnected"


def test_binding_reports_lock_without_hiding_input_connection(scene) -> None:
    """自身と親のロックが接続状態を隠さず通知される。"""
    nodes, owner = scene
    cmds.setKeyframe(nodes[0] + ".tx", time=1, value=3)
    binding = MayaFloatPlugsBinding(
        [resolve_float_plug(nodes[0], "tx")],
        track_input_state=True,
        parent=owner,
    )
    signals: list[bool | None] = []
    binding.state_changed.connect(
        lambda: signals.append(binding.target_states[0].is_locked)
    )
    assert binding.target_states[0].input_state == "keyed"
    assert binding.target_states[0].is_locked is False

    cmds.setAttr(nodes[0] + ".translate", lock=True)
    _events()
    assert binding.target_states[0].input_state == "keyed"
    assert binding.target_states[0].is_locked is True
    assert not binding.target_states[0].is_writable
    assert signals[-1] is True

    cmds.setAttr(nodes[0] + ".translate", lock=False)
    _events()
    assert binding.target_states[0].input_state == "keyed"
    assert binding.target_states[0].is_locked is False
    assert signals[-1] is False
