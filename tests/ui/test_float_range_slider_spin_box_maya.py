# coding: utf-8
from dataclasses import dataclass
from functools import partial

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util import Nodes
from bd_util.ui import FloatLabel, FloatRangeSliderSpinBox, qt
from bd_util.maya.ui import (
    MayaFloatBinding,
    MayaFloatPlugBinding,
    resolve_float_plug,
)
from bd_util.maya.ui.binding._float_edit import FloatEditUndo
from bd_util._sample.maya.ui.float_sample import maya_plug, maya_view, minimal


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    cmds.file(new=True, force=True)
    units = cmds.currentUnit(q=True, linear=True), cmds.currentUnit(
        q=True, angle=True
    )
    undo_enabled = cmds.undoInfo(q=True, state=True)
    cmds.currentUnit(linear="cm", angle="deg")
    cmds.undoInfo(state=True)
    owner = qt.QWidget()
    node = Nodes().existing.transform(cmds.createNode("transform"))
    yield owner, node
    for module in (maya_plug, maya_view, minimal):
        module.dispose()
    owner.deleteLater()
    flush()
    assert FloatEditUndo._active is None
    cmds.currentUnit(linear=units[0], angle=units[1])
    cmds.undoInfo(state=undo_enabled)


@pytest.mark.parametrize("source", ["maya", "python"])
@pytest.mark.parametrize("attribute", ["tx", "rx", "sx"])
def test_bound_edits_follow_units_preserve_values_and_create_no_undo(
    scene, source, attribute
):
    owner, node = scene

    @dataclass
    class Data:
        value: float = 10

    data = Data()
    path = f"{node.cmd_access_name}.{attribute}"
    cmds.setAttr(path, 10)
    plug = resolve_float_plug(node.cmd_access_name, attribute)
    binding = (
        MayaFloatPlugBinding(plug, parent=owner)
        if source == "maya"
        else MayaFloatBinding.from_attribute(
            data, "value", maya_plug=plug, parent=owner
        )
    )
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=100,
        decimals=12,
        minimum_decimals=12,
        maximum_decimals=12,
        minimum_width=80,
        maximum_width=70,
        value_width=100,
        minimum_show_buttons=False,
        maximum_show_buttons=False,
        value_show_buttons=False,
    )
    second = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-20,
        maximum=20,
        decimals=12,
        minimum_enabled=False,
        maximum_enabled=False,
        value_enabled=False,
    )
    label = FloatLabel(binding, owner, decimals=12)
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    original = binding.value
    cmds.currentUnit(linear="m", angle="rad")
    flush()
    presentation = binding.view_model.presentation
    assert editor.maximum_spin_box.value() == pytest.approx(
        presentation.to_display(100)
    )
    assert editor.minimum_spin_box.suffix() == editor.spin_box.suffix()
    assert editor.floatRange() == (-100, 100)
    assert not second.minimum_spin_box.isEnabled()
    assert not second.maximum_spin_box.isEnabled()
    assert not second.spin_box.isEnabled()
    assert (
        editor.minimum_spin_box.minimumWidth()
        == editor.minimum_spin_box.maximumWidth()
        == 80
    )
    assert (
        editor.maximum_spin_box.minimumWidth()
        == editor.maximum_spin_box.maximumWidth()
        == 70
    )
    assert (
        editor.spin_box.minimumWidth() == editor.spin_box.maximumWidth() == 100
    )
    assert (
        editor.spin_box.buttonSymbols()
        == qt.QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
    )
    cmds.flushUndo()

    # 表示単位の両端入力だけでは、正本・他Viewの範囲・Maya履歴を変更しない。
    editor.minimum_spin_box.setValue(presentation.to_display(-50))
    editor.maximum_spin_box.setValue(presentation.to_display(150))
    assert editor.floatRange() == pytest.approx((-50, 150))
    assert second.floatRange() == (-20, 20)
    assert binding.value == original
    assert plug.get() == pytest.approx(original)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    assert FloatEditUndo._active is None

    editor.slider.setSliderDown(True)
    for position in (200, 500, 750):
        editor.slider.setValue(position)
        assert binding.value == pytest.approx(plug.get())
        assert editor.spin_box.text() == label.text()
        assert second.spin_box.text() == label.text()
        if source == "python":
            assert data.value == binding.value
    # 範囲変更で進行中のドラッグを確定し、次のMaya操作をUndoへ混ぜない。
    editor.setFloatRange(-5, 5)
    final = binding.value
    assert final == pytest.approx(100)
    assert not binding.view_model.is_editing
    assert FloatEditUndo._active is None
    assert editor.slider.value() == 1000
    cmds.setAttr(f"{node.cmd_access_name}.ty", 3)
    cmds.undo()
    flush()
    assert binding.value == final
    cmds.undo()
    flush()
    assert binding.value == pytest.approx(original)
    assert editor.floatRange() == (-5, 5)
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    assert binding.value == pytest.approx(final)


@pytest.mark.parametrize("value_enabled", [False, True])
def test_value_enabled_survives_parent_lock_connection_and_units(
    scene, value_enabled
):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    editor = FloatRangeSliderSpinBox(
        binding,
        owner,
        minimum=-100,
        maximum=100,
        value_enabled=value_enabled,
        minimum_decimals=1,
        maximum_decimals=2,
    )
    path = f"{node.cmd_access_name}.translate"
    cmds.setAttr(path, lock=True)
    flush()
    assert not editor.spin_box.isEnabled()
    assert not editor.slider.isEnabled()
    cmds.setAttr(path, lock=False)
    flush()
    assert editor.spin_box.isEnabled() is value_enabled
    assert editor.slider.isEnabled()
    source = cmds.createNode("transform")
    cmds.connectAttr(f"{source}.translate", path)
    cmds.setAttr(f"{source}.tx", 25)
    flush()
    assert binding.value == editor.spin_box.value() == 25
    assert not editor.spin_box.isEnabled()
    assert not editor.slider.isEnabled()
    cmds.disconnectAttr(f"{source}.translate", path)
    cmds.currentUnit(linear="m")
    flush()
    assert editor.spin_box.value() == 0.25
    assert editor.spin_box.isEnabled() is value_enabled
    assert editor.slider.isEnabled()
    assert editor.minimumDecimals() == 1
    assert editor.maximumDecimals() == 2
    editor.slider.setValue(750)
    assert binding.value == 50
    assert editor.spin_box.value() == 0.5
    assert editor.minimum_spin_box.isEnabled()
    assert editor.maximum_spin_box.isEnabled()


def test_locked_parent_allows_range_settings_and_deletion_keeps_shared_callbacks(
    scene,
):
    owner, node = scene
    binding = MayaFloatPlugBinding(node.translate.translateX, parent=owner)
    before = tuple(om.MMessage.nodeCallbacks(node.m_obj))
    editor = FloatRangeSliderSpinBox(binding, owner, minimum=-100, maximum=100)
    cmds.setAttr(f"{node.cmd_access_name}.translate", lock=True)
    flush()
    assert not editor.slider.isEnabled()
    assert not editor.spin_box.isEnabled()
    assert editor.minimum_spin_box.isEnabled()
    cmds.flushUndo()
    editor.minimum_spin_box.setValue(-1)
    assert editor.floatRange() == (-1, 100)
    assert binding.value == 0
    assert cmds.undoInfo(q=True, undoQueueEmpty=True)
    editor.deleteLater()
    flush()
    assert tuple(om.MMessage.nodeCallbacks(node.m_obj)) == before
    cmds.setAttr(f"{node.cmd_access_name}.translate", lock=False)
    assert binding.set_value(5)
    binding.dispose()
    assert not tuple(om.MMessage.nodeCallbacks(node.m_obj))


@pytest.mark.parametrize("module", [maya_plug, maya_view, minimal])
def test_samples_expose_bound_controls_with_independent_ranges(scene, module):
    _, node = scene
    window = (
        module.show()
        if module is minimal
        else module.show(node.cmd_access_name)
    )
    editor = (
        window.widget.editor
        if module is minimal
        else window.widget.translate_x_editor
    )
    assert isinstance(editor, FloatRangeSliderSpinBox)
    assert editor.minimumDecimals() == (2 if module is minimal else 0)
    assert editor.maximumDecimals() == (2 if module is minimal else 0)
    assert (
        editor.minimum_spin_box.prefix()
        == editor.maximum_spin_box.prefix()
        == ""
    )
    assert (
        editor.minimum_spin_box.minimumWidth()
        == editor.minimum_spin_box.maximumWidth()
        == (30 if module is maya_plug else 80)
    )
    assert (
        editor.maximum_spin_box.minimumWidth()
        == editor.maximum_spin_box.maximumWidth()
        == (30 if module is maya_plug else 80)
    )
    assert (
        editor.spin_box.minimumWidth() == editor.spin_box.maximumWidth() == 100
    )
    assert (
        editor.spin_box.buttonSymbols()
        == qt.QtWidgets.QAbstractSpinBox.ButtonSymbols.NoButtons
    )
    original = editor.view_model.value.value
    editor.maximum_spin_box.setValue(0.75)
    assert editor.view_model.value.value == original
    if module is minimal:
        assert window.widget.linked_editor.floatRange() == (0, 1)
        assert not window.widget.linked_editor.minimum_spin_box.isEnabled()
        assert not window.widget.linked_editor.maximum_spin_box.isEnabled()
        assert not window.widget.linked_editor.spin_box.isEnabled()
        assert window.widget.linked_editor.slider.isEnabled()
        assert window.widget.linked_editor.minimumDecimals() == 1
        assert window.widget.linked_editor.maximumDecimals() == 3
    elif module is maya_view:
        assert not window.widget.linked_translate_x_editor.spin_box.isEnabled()
        assert window.widget.linked_translate_x_editor.slider.isEnabled()
    window.close()
    flush()
    assert not qt.isValid(editor)


@pytest.mark.parametrize("module", [maya_plug, maya_view, minimal])
def test_sample_layout_preserves_explicit_slider_width(
    scene, module, monkeypatch
):
    _, node = scene
    monkeypatch.setattr(
        module,
        "FloatRangeSliderSpinBox",
        partial(FloatRangeSliderSpinBox, slider_width=64),
    )
    window = (
        module.show()
        if module is minimal
        else module.show(node.cmd_access_name)
    )
    editor = (
        window.widget.editor
        if module is minimal
        else window.widget.translate_x_editor
    )
    assert editor.slider.minimumWidth() == editor.slider.maximumWidth() == 64
    assert editor.slider.width() == 64
