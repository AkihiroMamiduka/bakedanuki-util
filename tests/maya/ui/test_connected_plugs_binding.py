# coding: utf-8
"""標準の接続属性入力と通知、複数対象、失敗復旧を検証する。"""

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaBoolPlugsBinding,
    MayaEditSession,
    MayaEnumPlugsBinding,
    MayaFloatOffsetEdit,
    MayaFloatPlugsBinding,
    MayaFloatValueEdit,
    apply_plugs_values,
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
)
from bd_util.ui import qt


def flush():
    """遅延通知と所有者の破棄を処理する。"""
    for _ in range(3):
        qt.QApplication.processEvents()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )


@pytest.fixture
def scene(new_scene):
    """Auto Keyと単位を保存し、各検証専用の属性を用意する。"""
    auto = cmds.autoKeyframe(query=True, state=True)
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    cmds.autoKeyframe(state=False)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    owner = qt.QObject()
    nodes = [cmds.createNode("transform") for _ in range(3)]
    yield nodes, owner
    cmds.autoKeyframe(state=False)
    owner.deleteLater()
    flush()
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.autoKeyframe(state=auto)


def animate(plug, first=2.0, last=8.0):
    """既存カーブを作り、キーのない時刻を評価する。"""
    cmds.setKeyframe(plug, time=1, value=first)
    cmds.setKeyframe(plug, time=10, value=last)
    cmds.currentTime(5)
    return cmds.listConnections(plug, source=True, destination=False)[0]


def bind(nodes, owner, attribute="tx"):
    """対象順を保って標準入力を明示的に有効にする。"""
    return MayaFloatPlugsBinding(
        [resolve_float_plug(node, attribute) for node in nodes],
        parent=owner,
        edit_connected=True,
        track_input_state=True,
    )


def add_layer(plug):
    """既存曲線へ選択中の加算レイヤーを加える。"""
    layer = cmds.animLayer("editLayer", attribute=plug)
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.setKeyframe(plug, animLayer=layer, time=1, value=1)
    cmds.setKeyframe(plug, animLayer=layer, time=10, value=3)
    cmds.currentTime(5)
    return layer


@pytest.mark.parametrize("auto", [False, True])
def test_time_input_mixed_targets_undo_and_reevaluation(scene, auto):
    """Auto Keyに従った一時値またはキーと通常属性を一回で戻す。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    initial = cmds.getAttr(nodes[0] + ".tx")
    cmds.setAttr(nodes[2] + ".tx", lock=True)
    binding = bind(nodes, owner)
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    assert binding.set_value(12)
    flush()
    assert binding.value == 12
    assert binding.writable_count == 2
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == (
        3 if auto else 2
    )
    assert binding.target_states[0].input_state == (
        "keyed" if auto else "key_altered"
    )
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(initial)
    assert cmds.getAttr(nodes[1] + ".tx") == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == 12
    cmds.currentTime(6)
    cmds.currentTime(5)
    flush()
    assert binding.value == pytest.approx(12 if auto else initial)


@pytest.mark.parametrize("auto", [False, True])
def test_sdk_edit_survives_refresh_without_changing_curve(scene, auto):
    """SDK入力を一時値として保持し、ドライバー変更だけで再評価する。"""
    nodes, owner = scene
    driven = nodes[0] + ".tx"
    driver = nodes[1] + ".ty"
    cmds.setDrivenKeyframe(
        driven, currentDriver=driver, driverValue=0, value=0
    )
    cmds.setDrivenKeyframe(
        driven, currentDriver=driver, driverValue=10, value=10
    )
    curve = cmds.listConnections(driven, source=True, destination=False)[0]
    binding = bind(nodes[:1], owner)
    cmds.autoKeyframe(state=auto)
    assert binding.set_value(42)
    flush()
    assert binding.value == 42
    assert cmds.keyframe(curve, query=True, valueChange=True) == [0, 10]
    assert binding.target_states[0].edit_description
    binding.refresh()
    assert binding.value == 42
    cmds.setAttr(driver, 10)
    flush()
    assert binding.value == 10
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2


@pytest.mark.parametrize("auto", [False, True])
def test_layer_input_and_selection_description_refresh(scene, auto):
    """レイヤーの合成値を標準経路で入力し、対象変更の説明も同期する。"""
    nodes, owner = scene
    plug = nodes[0] + ".tx"
    animate(plug)
    layer = add_layer(plug)
    binding = bind(nodes[:1], owner)
    initial = binding.value
    cmds.autoKeyframe(state=auto)
    assert binding.set_value(42)
    flush()
    assert binding.value == 42
    assert layer in binding.target_states[0].edit_description
    cmds.currentTime(6)
    cmds.currentTime(5)
    flush()
    assert binding.value == pytest.approx(42 if auto else initial)
    cmds.animLayer(layer, edit=True, selected=False, preferred=False)
    cmds.animLayer("BaseAnimation", edit=True, selected=True, preferred=True)
    flush()
    assert "BaseAnimation" in binding.target_states[0].edit_description


@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize(
    "attribute,units,value,expected",
    [
        ("tx", {"linear": "m"}, 125.0, 1.25),
        ("rx", {"angle": "rad"}, 90.0, 1.5707963267948966),
    ],
)
def test_units_for_native_time_input(
    scene, auto, attribute, units, value, expected
):
    """公開単位から現在のMaya単位へ変換して入力する。"""
    nodes, owner = scene
    animate(nodes[0] + "." + attribute)
    cmds.currentUnit(**units)
    binding = bind(nodes[:1], owner, attribute)
    cmds.autoKeyframe(state=auto)
    assert binding.set_value(value)
    assert binding.value == pytest.approx(value)
    assert cmds.getAttr(nodes[0] + "." + attribute) == pytest.approx(expected)


@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize("kind", ["bool", "enum"])
def test_native_discrete_connected_input(scene, auto, kind):
    """boolとenumもAuto Keyに従い入力とUndoを行う。"""
    nodes, owner = scene
    if kind == "bool":
        attribute, initial, value = "visibility", 1, False
        factory, resolver = MayaBoolPlugsBinding, resolve_bool_plug
    else:
        attribute, initial, value = "mode", 0, 2
        cmds.addAttr(
            nodes[0],
            longName=attribute,
            attributeType="enum",
            enumName="A:B:C",
            keyable=True,
        )
        factory, resolver = MayaEnumPlugsBinding, resolve_enum_plug
    curve = animate(nodes[0] + "." + attribute, initial, initial)
    binding = factory(
        [resolver(nodes[0], attribute)], parent=owner, edit_connected=True
    )
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    assert binding.set_value(value)
    assert binding.value == value
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == (
        3 if auto else 2
    )
    cmds.undo()
    flush()
    assert binding.value == initial
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2


@pytest.mark.parametrize("auto", [False, True])
def test_connected_multirow_drag_one_undo(scene, auto):
    """連続した複数行入力と相対値変更を一回のUndoへまとめる。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    first = bind(nodes[:1], owner)
    second = bind(nodes[1:2], owner)
    initial = first.value
    session = MayaEditSession(owner)
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    session.begin()
    apply_plugs_values(
        [MayaFloatValueEdit(first, 12), MayaFloatValueEdit(second, 3)],
        edit_session=session,
    )
    apply_plugs_values(
        [MayaFloatOffsetEdit(first, 2), MayaFloatOffsetEdit(second, 1)],
        edit_session=session,
    )
    session.finish()
    assert (first.value, second.value) == (14, 4)
    cmds.undo()
    flush()
    assert first.value == pytest.approx(initial)
    assert second.value == 0
    assert cmds.keyframe(curve, query=True, keyframeCount=True) == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


@pytest.mark.parametrize("layered", [False, True])
@pytest.mark.parametrize("auto", [False, True])
def test_later_failure_restores_curves_values_and_autokey(
    scene, monkeypatch, layered, auto
):
    """後続失敗時に自動キーを残さず、入力前の一時値と設定を復旧する。"""
    nodes, owner = scene
    plug = nodes[0] + ".tx"
    animate(plug)
    if layered:
        add_layer(plug)
    cmds.setAttr(plug, 7.5)
    curves = cmds.ls(type="animCurve")
    before = {
        curve: (
            cmds.keyframe(curve, query=True, timeChange=True),
            cmds.keyframe(curve, query=True, valueChange=True),
        )
        for curve in curves
    }
    binding = bind(nodes[:2], owner)
    cmds.autoKeyframe(state=auto)
    original = cmds.setAttr

    def fail_later(name, *args, **kwargs):
        """後続の通常属性への新規値だけを拒否する。"""
        if name.split(".", 1)[0].rsplit("|", 1)[-1] == nodes[1] and args == (
            42,
        ):
            raise RuntimeError("later failure")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(cmds, "setAttr", fail_later)
    with pytest.raises(RuntimeError, match="later failure"):
        binding.set_value(42)
    flush()
    assert binding.value == pytest.approx(7.5)
    assert cmds.getAttr(nodes[1] + ".tx") == 0
    assert cmds.autoKeyframe(query=True, state=True) is auto
    assert curves == cmds.ls(type="animCurve")
    after = {
        curve: (
            cmds.keyframe(curve, query=True, timeChange=True),
            cmds.keyframe(curve, query=True, valueChange=True),
        )
        for curve in curves
    }
    assert after == before


def test_input_observers_refresh_autokey_and_dispose(scene):
    """Auto Key表示を追従させ、外部ノードの監視を破棄時に解除する。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    selection = om.MSelectionList()
    selection.add(curve)
    node = selection.getDependNode(0)
    initial = len(om.MMessage.nodeCallbacks(node))
    binding = bind(nodes[:1], owner)
    before = binding.target_states[0].edit_description
    assert len(om.MMessage.nodeCallbacks(node)) > initial
    cmds.autoKeyframe(state=True)
    flush()
    assert binding.target_states[0].edit_description != before
    binding.dispose()
    assert len(om.MMessage.nodeCallbacks(node)) == initial


@pytest.mark.parametrize("lock_target", [False, True])
def test_node_lock_poll_updates_cached_editability_without_reading_values(
    scene, monkeypatch, lock_target
):
    """Maya通知のないnodeロックを検出し、無変更時の値再評価は避ける。"""
    nodes, owner = scene
    curve = animate(nodes[0] + ".tx")
    locked_node = nodes[0] if lock_target else curve
    cmds.lockNode(locked_node, lock=True)
    binding = bind(nodes[:1], owner)
    assert not binding.view_model.set_value_command.can_execute
    cmds.lockNode(locked_node, lock=False)
    binding.store._check_input_node_locks()
    flush()
    assert binding.view_model.set_value_command.can_execute
    refreshed = []
    original = binding.store.refresh

    def record_refresh():
        """ロック無変更時に値読取りが発生しないことを記録する。"""
        refreshed.append(True)
        return original()

    monkeypatch.setattr(binding.store, "refresh", record_refresh)
    binding.store._check_input_node_locks()
    flush()
    assert not refreshed
    cmds.lockNode(locked_node, lock=True)
    binding.store._check_input_node_locks()
    flush()
    assert not binding.view_model.set_value_command.can_execute
    binding.dispose()
    assert not binding.store._input_lock_timer.isActive()


def test_edit_modes_are_opt_in_and_mutually_exclusive(scene):
    """既定の接続不可を維持し、二種類の書込み方式の同時指定を拒否する。"""
    nodes, owner = scene
    animate(nodes[0] + ".tx")
    plug = resolve_float_plug(nodes[0], "tx")
    binding = MayaFloatPlugsBinding([plug], parent=owner)
    assert not binding.set_value(42)
    with pytest.raises(ValueError, match="併用"):
        MayaFloatPlugsBinding(
            [plug], parent=owner, key_animated=True, edit_connected=True
        )


@pytest.mark.parametrize("auto", [False, True])
@pytest.mark.parametrize("fail", [False, True])
def test_multi_axis_rotation_layer_batch_and_rollback(
    scene, monkeypatch, auto, fail
):
    """回転レイヤーの三軸が経路を共有しても一括入力と復旧を行う。"""
    nodes, owner = scene
    node = nodes[0]
    cmds.setKeyframe(node + ".rotate", time=1, value=0)
    cmds.setKeyframe(node + ".rotate", time=10, value=0)
    layer = cmds.animLayer("rotationLayer", attribute=node + ".rotate")
    cmds.animLayer(layer, edit=True, selected=True, preferred=True)
    cmds.setKeyframe(node + ".rotate", time=1, value=0, animLayer=layer)
    cmds.setKeyframe(node + ".rotate", time=10, value=0, animLayer=layer)
    cmds.currentTime(5)
    bindings = [bind(nodes[:1], owner, "r" + axis) for axis in "xyz"]
    other = bind(nodes[1:2], owner)
    edits = [
        MayaFloatValueEdit(binding, value)
        for binding, value in zip(bindings, (12.0, 18.0, 23.0))
    ]
    edits.append(MayaFloatValueEdit(other, 42))
    curves = cmds.ls(type="animCurve")
    before = {
        curve: (
            cmds.keyframe(curve, q=True, timeChange=True),
            cmds.keyframe(curve, q=True, valueChange=True),
        )
        for curve in curves
    }
    original = cmds.setAttr

    def fail_last(name, *args, **kwargs):
        """三軸の適用後に通常属性への書込みを失敗させる。"""
        if name.split(".", 1)[0].rsplit("|", 1)[-1] == nodes[1] and args == (
            42,
        ):
            raise RuntimeError("batch failure")
        return original(name, *args, **kwargs)

    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    if fail:
        monkeypatch.setattr(cmds, "setAttr", fail_last)
        with pytest.raises(RuntimeError, match="batch failure"):
            apply_plugs_values(edits)
        assert [binding.value for binding in bindings] == pytest.approx(
            [0, 0, 0]
        )
    else:
        assert apply_plugs_values(edits)
        assert [binding.value for binding in bindings] == pytest.approx(
            [12, 18, 23]
        )
        cmds.undo()
        flush()
        assert [binding.value for binding in bindings] == pytest.approx(
            [0, 0, 0]
        )
    after = {
        curve: (
            cmds.keyframe(curve, q=True, timeChange=True),
            cmds.keyframe(curve, q=True, valueChange=True),
        )
        for curve in curves
    }
    assert after == before
