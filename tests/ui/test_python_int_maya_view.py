# coding: utf-8
"""Python整数とMaya属性を共有するQt Viewとサンプルを検証する。"""

from dataclasses import dataclass

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util._sample.maya.ui.int_sample import maya_view
from bd_util.maya.ui import MayaIntBinding, MayaIntPlugView, resolve_int_plug
from bd_util.ui import IntBinding, IntLabel, IntSpinBox, qt


@dataclass
class Data:
    """UIから編集するPython側の整数正本。"""

    value: int = 128


def flush():
    """予約されたQt入力と所有者破棄を処理する。"""
    for _ in range(3):
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        qt.QApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    """サンプルと同じ三種類の整数属性を準備する。"""
    cmds.file(new=True, force=True)
    cmds.undoInfo(state=True)
    node = cmds.createNode("transform")
    for name, kind in (
        ("byteValue", "byte"),
        ("shortValue", "short"),
        ("longValue", "long"),
    ):
        cmds.addAttr(node, longName=name, attributeType=kind, keyable=True)
    owner = qt.QWidget()
    yield node, owner
    maya_view.dispose()
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def test_shared_spin_boxes_and_label_preserve_int32_and_independent_owners(
    scene,
):
    """複数のQt Viewが確定整数を共有し、個別破棄で正本を終了しない。"""
    node, owner = scene
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data,
        "value",
        maya_plug=resolve_int_plug(node, "longValue"),
        parent=owner,
    )
    first = IntSpinBox(binding, owner)
    second = IntSpinBox(binding.view_model, owner, single_step=10)
    label = IntLabel(binding, owner)
    first.setValue(2**31 - 1)
    assert (
        second.value()
        == data.value
        == cmds.getAttr(node + ".longValue")
        == 2**31 - 1
    )
    assert label.text() == str(2**31 - 1)
    first.deleteLater()
    flush()
    assert not binding.is_disposed
    cmds.setAttr(node + ".longValue", -(2**31))
    flush()
    assert data.value == second.value() == -(2**31)
    assert label.text() == str(-(2**31))


@pytest.mark.parametrize("failure", [False, True])
def test_owner_destruction_or_failed_construction_releases_callbacks(
    scene, failure
):
    """予約中のMaya入力を所有者破棄後に適用せず、生成失敗も即座に解放する。"""
    node, owner = scene
    plug = resolve_int_plug(node, "longValue")
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    if failure:
        cmds.setAttr(node + ".longValue", lock=True)
        with pytest.raises(RuntimeError):
            MayaIntBinding.from_attribute(
                Data(), "value", maya_plug=plug, parent=owner
            )
        assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
        flush()
        assert not owner.children()
    else:
        data = Data()
        binding = MayaIntBinding.from_attribute(
            data, "value", maya_plug=plug, parent=owner
        )
        child = IntSpinBox(binding, owner)
        survivor = IntSpinBox(binding)
        cmds.setAttr(node + ".longValue", 50)
        owner.deleteLater()
        flush()
        assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
        assert data.value == 128
        assert binding.is_disposed
        assert not qt.isValid(child)
        assert not survivor.isEnabled()
        survivor.deleteLater()


def test_separate_view_owner_destruction_keeps_python_qt_editable(scene):
    """Maya側だけの破棄後もPython正本とQt編集を継続する。"""
    node, owner = scene
    binding = IntBinding.from_attribute(Data(), "value", parent=owner)
    view_owner = qt.QObject()
    plug = resolve_int_plug(node, "longValue")
    view = MayaIntPlugView(binding.view_model, plug, view_owner)
    spin = IntSpinBox(binding, owner)
    view_owner.deleteLater()
    flush()
    assert view.is_disposed
    assert spin.isEnabled()
    spin.setValue(10)
    assert binding.value == 10
    assert cmds.getAttr(node + ".longValue") == 128
    replacement = MayaIntPlugView(binding.view_model, plug, owner)
    assert replacement.is_synchronized


@pytest.mark.parametrize("dispose_from", ["changed", "sync_failed"])
def test_notification_can_dispose_binding_without_late_writes(
    scene, dispose_from
):
    """利用者通知中の終了要求でも無効なQt objectへ再入しない。"""
    node, owner = scene
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data,
        "value",
        maya_plug=resolve_int_plug(node, "longValue"),
        parent=owner,
    )
    spin = IntSpinBox(binding, owner)
    if dispose_from == "sync_failed":
        binding.maya_view.sync_failed.connect(lambda _error: binding.dispose())
        cmds.setAttr(node + ".longValue", lock=True)
    else:
        binding.changed.connect(lambda _value: binding.dispose())
    binding.set_value(10)
    assert binding.is_disposed
    assert data.value == 10
    assert not spin.isEnabled()


def test_reentrant_python_command_from_maya_input_keeps_latest_value(scene):
    """Maya入力の通知先から再編集したPython値を最終結果として採用する。"""
    node, owner = scene
    data = Data()
    binding = MayaIntBinding.from_attribute(
        data,
        "value",
        maya_plug=resolve_int_plug(node, "longValue"),
        parent=owner,
    )

    def replace(value):
        """一回目の通知から二回目の値を確定する。"""
        if value == 10:
            binding.set_value(20)

    binding.changed.connect(replace)
    cmds.setAttr(node + ".longValue", 10)
    flush()
    assert (
        data.value == binding.value == cmds.getAttr(node + ".longValue") == 20
    )
    assert binding.maya_view.is_synchronized


def test_sample_shared_views_direct_assignment_refresh_pending_and_reopen(
    scene,
):
    """サンプルで共有入力、外部変更、再同期、再表示とcallback解除を確認する。"""
    node, _ = scene
    data = maya_view.MayaIntSampleData()
    plug = resolve_int_plug(node, "longValue")
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    window = maya_view.show(node, data)
    widget = window.widget
    assert widget.long_binding.store.instance is data
    widget.long_spin_box.setValue(30)
    assert data.long_value == widget.linked_long_spin_box.value() == 30
    assert widget.long_label.text() == "30"
    widget.set_data_button.click()
    assert data.long_value == 100
    assert cmds.getAttr(node + ".longValue") == 30
    widget.refresh_button.click()
    assert cmds.getAttr(node + ".longValue") == 100
    widget.byte_spin_box.setValue(300)
    widget.retry_button.click()
    assert data.byte_value == 300
    assert cmds.getAttr(node + ".byteValue") == 200
    assert "Pending" in widget.result_label.text()
    widget.byte_spin_box.setValue(200)
    cmds.setAttr(node + ".longValue", lock=True)
    widget.long_spin_box.setValue(50)
    widget.retry_button.click()
    assert "Pending" in widget.result_label.text()
    cmds.setAttr(node + ".longValue", lock=False)
    widget.retry_button.click()
    assert "Pending" not in widget.result_label.text()
    window.close()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
    assert data.long_value == 50
    assert cmds.objExists(node)
    replacement = maya_view.show(node, data)
    assert replacement.widget.data is data
    assert replacement.widget.long_binding.value == 50


def test_sample_partial_initialization_and_demo_preserve_scene(scene):
    """途中失敗したBindingも解放し、demoは既存sceneを消去しない。"""
    node, _ = scene
    plug = resolve_int_plug(node, "longValue")
    before = tuple(om.MMessage.nodeCallbacks(plug.plug.node()))
    cmds.setAttr(node + ".shortValue", lock=True)
    with pytest.raises(RuntimeError):
        maya_view.show(node)
    assert tuple(om.MMessage.nodeCallbacks(plug.plug.node())) == before
    flush()
    data = maya_view.MayaIntSampleData(long_value=123)
    window = maya_view.show_demo(data)
    assert cmds.objExists(node)
    assert window.widget.data is data
    assert cmds.getAttr(window.node_name + ".byteValue") == 128
    assert cmds.getAttr(window.node_name + ".longValue") == 123
    assert window.widget.short_binding.view_model.presentation.minimum is None
