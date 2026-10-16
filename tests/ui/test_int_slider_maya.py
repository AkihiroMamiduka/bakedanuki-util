# coding: utf-8
"""整数SliderのMaya同期、連続Undoと中断時の解放を検証する。"""

from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    MayaIntBinding,
    MayaIntPlugBinding,
    MayaIntPlugsBinding,
    resolve_float_plug,
    resolve_int_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util.ui import FloatSlider, IntLabel, IntSlider, IntSpinBox, qt


@dataclass
class Data:
    """Mayaへ同期するPython整数正本。"""

    value: int = 10


def flush():
    """Maya callback後のQt処理と遅延破棄を完了する。"""
    for _ in range(3):
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    """単一・複数整数属性と独立command用のtransformを用意する。"""
    cmds.file(new=True, force=True)
    undo = cmds.undoInfo(query=True, state=True)
    auto = cmds.autoKeyframe(query=True, state=True)
    cmds.undoInfo(state=True)
    cmds.autoKeyframe(state=False)
    nodes = tuple(cmds.createNode("transform") for _ in range(2))
    for node in nodes:
        for name, kind in (
            ("byteValue", "byte"),
            ("shortValue", "short"),
            ("longValue", "long"),
        ):
            cmds.addAttr(node, longName=name, attributeType=kind, keyable=True)
            cmds.setAttr(node + "." + name, 10)
    owner = qt.QWidget()
    yield owner, nodes
    if qt.isValid(owner):
        owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.autoKeyframe(state=auto)
    cmds.undoInfo(state=undo)


def binding_for(owner, node, attribute="longValue", source="maya"):
    """二種類の正本を同じ整数属性へ接続する。"""
    plug = resolve_int_plug(node, attribute)
    if source == "maya":
        return MayaIntPlugBinding(plug, parent=owner)
    return MayaIntBinding.from_attribute(
        Data(), "value", maya_plug=plug, parent=owner
    )


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["byteValue", "shortValue", "longValue"])
def test_drag_live_sync_and_undo_redo_once(scene, source, attribute):
    """各整数型と両同期方向で、ドラッグ全体を一回Undoにまとめる。"""
    owner, nodes = scene
    binding = binding_for(owner, nodes[0], attribute, source)
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    spin = IntSpinBox(binding, owner)
    label = IntLabel(binding, owner)
    cmds.flushUndo()
    slider.setSliderDown(True)
    for position in (60, 70, 80):
        slider.setValue(position)
        flush()
        assert binding.value == spin.value() == position
        assert label.text() == str(position)
        assert cmds.getAttr(nodes[0] + "." + attribute) == position
    slider.setSliderDown(False)
    assert cmds.undoInfo(query=True, undoName=True) == "IntSlider"
    cmds.undo()
    flush()
    assert binding.value == spin.value() == 10
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == 80
    assert cmds.undoInfo(query=True, redoQueueEmpty=True)


@pytest.mark.parametrize(
    "finish",
    [
        "release",
        "hide",
        "disable",
        "range",
        "dispose",
        "delete_slider",
        "delete_owner",
        "time",
        "registry",
    ],
)
@pytest.mark.parametrize("source", ["maya", "python"])
def test_interruptions_close_before_unrelated_command(scene, finish, source):
    """各中断でUndoと時刻監視を閉じ、後続commandの履歴を分離する。"""
    from bd_util.maya.ui.callback import dispose_owned_callbacks

    owner, nodes = scene
    binding = binding_for(owner, nodes[0], source=source)
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    slider.show()
    flush()
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(60)
    assert FloatEditUndo._active is not None
    if finish == "release":
        slider.setSliderDown(False)
    elif finish == "hide":
        slider.hide()
    elif finish == "disable":
        slider.setEnabled(False)
    elif finish == "range":
        slider.setIntRange(0, 200)
    elif finish == "dispose":
        binding.dispose()
    elif finish == "delete_slider":
        slider.deleteLater()
    elif finish == "delete_owner":
        owner.deleteLater()
    elif finish == "time":
        cmds.currentTime(cmds.currentTime(query=True) + 1)
    else:
        callback_owner = binding if source == "python" else binding.store
        dispose_owned_callbacks(callback_owner)
    flush()
    assert FloatEditUndo._active is None
    cmds.setAttr(nodes[0] + ".ty", 5)
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".ty") == 0
    assert cmds.getAttr(nodes[0] + ".longValue") == 60
    if finish == "time":
        # 時刻変更command自体のUndoは値ドラッグとは別に戻す
        cmds.undo()
        flush()
        assert cmds.getAttr(nodes[0] + ".longValue") == 60
    cmds.undo()
    flush()
    assert cmds.getAttr(nodes[0] + ".longValue") == 10


def test_noop_disabled_undo_and_same_time_reevaluation(scene):
    """無変更では履歴を作らず、Undo無効と同時刻再評価を維持する。"""
    owner, nodes = scene
    binding = binding_for(owner, nodes[0])
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setSliderDown(False)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    slider.setSliderDown(True)
    cmds.currentTime(cmds.currentTime(query=True))
    assert binding.view_model.is_editing
    slider.setSliderDown(False)
    cmds.undoInfo(state=False)
    slider.setSliderDown(True)
    slider.setValue(80)
    slider.setSliderDown(False)
    assert binding.value == 80
    assert not cmds.undoInfo(query=True, state=True)


@pytest.mark.parametrize("source", ["maya", "python"])
def test_float_integer_gestures_and_direct_input_have_separate_history(
    scene, source
):
    """floatと整数の操作切替・通常入力でUndoを混在させない。"""
    owner, nodes = scene
    integer = binding_for(owner, nodes[0], source=source)
    float_plug = resolve_float_plug(nodes[0], "translateX")

    @dataclass
    class FloatData:
        """Python経由のfloat同期も整数と同じ履歴管理へ接続する。"""

        value: float = 0.0

    floating = (
        MayaFloatPlugBinding(float_plug, parent=owner)
        if source == "maya"
        else MayaFloatBinding.from_attribute(
            FloatData(), "value", maya_plug=float_plug, parent=owner
        )
    )
    int_slider = IntSlider(integer, owner, minimum=0, maximum=100)
    float_slider = FloatSlider(floating, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    int_slider.setSliderDown(True)
    int_slider.setValue(50)
    float_slider.setSliderDown(True)
    float_slider.setValue(700)
    assert not integer.view_model.is_editing
    float_slider.setSliderDown(False)
    cmds.undo()
    flush()
    assert floating.value == 0
    assert integer.value == 50
    cmds.undo()
    flush()
    assert integer.value == 10
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    int_slider.setSliderDown(True)
    int_slider.setValue(60)
    floating.set_value(30)
    assert not integer.view_model.is_editing
    cmds.undo()
    flush()
    assert floating.value == 0
    assert integer.value == 60
    cmds.undo()
    flush()
    assert integer.value == 10


def test_multiple_targets_validate_before_write_and_undo_successful_drag(
    scene,
):
    """後続属性の範囲違反で当該更新を拒否し、成功分だけ一回Undoで戻す。"""
    owner, nodes = scene
    cmds.addAttr(nodes[1] + ".longValue", edit=True, minValue=0, maxValue=50)
    binding = MayaIntPlugsBinding(
        tuple(resolve_int_plug(n, "longValue") for n in nodes), parent=owner
    )
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(40)
    with pytest.raises(ValueError):
        slider._request_value(60)
    assert not binding.view_model.is_editing
    assert all(cmds.getAttr(n + ".longValue") == 40 for n in nodes)
    cmds.undo()
    flush()
    assert all(cmds.getAttr(n + ".longValue") == 10 for n in nodes)


@pytest.mark.parametrize("source", ["maya", "python"])
def test_lock_and_node_deletion_finish_edit_without_slider_callbacks(
    scene, source
):
    """入力不可とnode削除で終了し、Slider自体はMaya callbackを持たない。"""
    owner, nodes = scene
    binding = binding_for(owner, nodes[0], source=source)
    plug = resolve_int_plug(nodes[0], "longValue")
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
    slider.setSliderDown(True)
    slider.setValue(60)
    cmds.setAttr(nodes[0] + ".longValue", lock=True)
    flush()
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    cmds.setAttr(nodes[0] + ".longValue", lock=False)
    flush()
    slider.setSliderDown(True)
    slider.setValue(70)
    cmds.delete(nodes[0])
    flush()
    assert FloatEditUndo._active is None


@pytest.mark.parametrize("source", ["maya", "python"])
def test_dispose_during_setattr_closes_after_write_returns(
    scene, source, monkeypatch
):
    """Maya書込み中の破棄要求を、command終了後に安全に反映する。"""
    owner, nodes = scene
    binding = binding_for(owner, nodes[0], source=source)
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    original = cmds.setAttr

    def write_and_dispose(*args, **kwargs):
        """Maya書込みを完了してからBindingを終了する。"""
        original(*args, **kwargs)
        binding.dispose()

    monkeypatch.setattr(cmds, "setAttr", write_and_dispose)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(40)
    monkeypatch.setattr(cmds, "setAttr", original)
    assert FloatEditUndo._active is None
    cmds.setAttr(nodes[0] + ".ty", 5)
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".longValue") == 40
    cmds.undo()
    assert cmds.getAttr(nodes[0] + ".longValue") == 10


@pytest.mark.parametrize("maya_demo", [False, True])
def test_sample_layout_sharing_undo_and_close(scene, maya_demo):
    """初期画面で全欄を表示し、共有入力とclose時の監視解除を確認する。"""
    from bd_util._sample.maya.ui.int_sample import slider as sample

    before_nodes = set(cmds.ls(long=True))
    window = sample.show_demo() if maya_demo else sample.show()
    flush()
    try:
        widget = window.widget
        rows = widget.findChildren(sample.IntSliderSampleRow)
        for row in rows:
            for child in (row.slider, row.spin_box, row.value_label):
                assert row.rect().contains(child.geometry())
                assert not child.visibleRegion().isEmpty()
        widget.python_row.slider.setValue(7)
        assert (
            widget.linked_row.spin_box.value() == widget.data.signed_value == 7
        )
        if not maya_demo:
            assert set(cmds.ls(long=True)) == before_nodes
        else:
            assert window.node_names is not None
            first, second = window.node_names
            plug = resolve_int_plug(first, "longValue")
            maya_row = widget.maya_row
            assert maya_row is not None
            cmds.flushUndo()
            maya_row.slider.setSliderDown(True)
            maya_row.slider.setValue(120)
            maya_row.slider.setValue(150)
            maya_row.slider.setSliderDown(False)
            assert (
                cmds.getAttr(first + ".longValue")
                == cmds.getAttr(second + ".longValue")
                == 50
            )
            cmds.undo()
            flush()
            assert cmds.getAttr(first + ".longValue") == 3
            assert cmds.getAttr(second + ".longValue") == 4
            assert tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
        window.close()
        flush()
        if maya_demo:
            assert not tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
        assert FloatEditUndo._active is None
    finally:
        sample.dispose()
        flush()


@pytest.mark.parametrize("auto", [False, True])
def test_animated_integer_drag_uses_existing_key_policy(scene, auto):
    """時間カーブの整数編集をAuto Keyに従い一回Undoで復元する。"""
    owner, nodes = scene
    path = nodes[0] + ".longValue"
    cmds.setKeyframe(path, time=1, value=2.25)
    cmds.setKeyframe(path, time=10, value=8.75)
    cmds.currentTime(5)
    before_times = cmds.keyframe(path, query=True, timeChange=True)
    before_values = cmds.keyframe(path, query=True, valueChange=True)
    before_value = cmds.getAttr(path)
    binding = MayaIntPlugBinding(
        resolve_int_plug(nodes[0], "longValue"),
        parent=owner,
        edit_connected=True,
    )
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(30)
    slider.setValue(70)
    slider.setSliderDown(False)
    assert binding.value == 70
    assert cmds.keyframe(path, query=True, keyframeCount=True) == (
        3 if auto else 2
    )
    cmds.undo()
    flush()
    assert binding.value == before_value
    assert cmds.keyframe(path, query=True, timeChange=True) == before_times
    assert cmds.keyframe(path, query=True, valueChange=True) == before_values


def curve_values():
    """全カーブの時刻と小数キーを復旧比較用に保存する。"""
    return tuple(
        (
            c,
            tuple(cmds.keyframe(c, query=True, timeChange=True) or ()),
            tuple(cmds.keyframe(c, query=True, valueChange=True) or ()),
        )
        for c in sorted(cmds.ls(type="animCurve"))
    )


@pytest.mark.parametrize("source", ["sdk", "layer"])
@pytest.mark.parametrize("auto", [False, True])
def test_connected_drag_undo_preserves_original_curve_values(
    scene, source, auto
):
    """SDK・Layerの連続編集を、元の小数キーごと一回Undoで戻す。"""
    owner, nodes = scene
    path = nodes[0] + ".longValue"
    if source == "sdk":
        for driver_value, value in ((0, 2.25), (10, 8.75)):
            cmds.setDrivenKeyframe(
                path,
                currentDriver=nodes[1] + ".tx",
                driverValue=driver_value,
                value=value,
            )
    else:
        cmds.setKeyframe(path, time=1, value=2.25)
        cmds.setKeyframe(path, time=10, value=8.75)
        layer = cmds.animLayer("intSliderLayer", attribute=path)
        cmds.animLayer(layer, edit=True, selected=True, preferred=True)
        cmds.setKeyframe(path, animLayer=layer, time=1, value=1)
        cmds.setKeyframe(path, animLayer=layer, time=10, value=3)
        cmds.setAttr(layer + ".weight", 0.5)
        cmds.currentTime(5)
    before = curve_values()
    initial = cmds.getAttr(path)
    binding = MayaIntPlugBinding(
        resolve_int_plug(nodes[0], "longValue"),
        parent=owner,
        edit_connected=True,
    )
    slider = IntSlider(binding, owner, minimum=0, maximum=100)
    cmds.autoKeyframe(state=auto)
    cmds.flushUndo()
    slider.setSliderDown(True)
    slider.setValue(30)
    slider.setValue(70)
    slider.setSliderDown(False)
    assert binding.value == cmds.getAttr(path)
    assert binding.value != initial
    if source == "sdk":
        assert curve_values() == before
    cmds.undo()
    flush()
    assert binding.value == initial
    assert curve_values() == before
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_sample_partial_construction_releases_maya_callbacks(scene):
    """途中のPython同期失敗でも、先に作ったMaya Bindingを直ちに終了する。"""
    from bd_util._sample.maya.ui.int_sample import slider as sample

    _, nodes = scene
    node = nodes[0]
    cmds.addAttr(node, longName="pythonValue", attributeType="long")
    cmds.setAttr(node + ".pythonValue", lock=True)
    plug = resolve_int_plug(node, "longValue")
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    with pytest.raises(RuntimeError):
        sample.show_maya(*nodes)
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
    flush()
