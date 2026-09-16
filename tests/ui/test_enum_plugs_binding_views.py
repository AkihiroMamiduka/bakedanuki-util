# coding: utf-8
import pytest
from maya import cmds

from bd_util._sample.maya.ui.enum_sample import maya_plugs
from bd_util.maya.ui import MayaEnumPlugsBinding, resolve_enum_plug
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import EnumComboBox, EnumLabel, EnumRadioButtonGroup, qt


def flush():
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()


@pytest.fixture
def scene(qt_application, maya_standalone):
    nodes = [cmds.createNode("transform") for _ in range(2)]
    for node, value in zip(nodes, (5, 0)):
        cmds.addAttr(
            node,
            longName="mode",
            attributeType="enum",
            enumName="Off=0:Preview=5:Final=10",
        )
        cmds.setAttr(node + ".mode", value)
    owner = qt.QWidget()
    yield nodes, owner
    maya_plugs.dispose()
    if qt.isValid(owner):
        owner.deleteLater()
    flush()
    cmds.delete(nodes)


def test_shared_views_apply_same_selection_and_undo_group(scene):
    nodes, owner = scene
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], parent=owner
    )
    radio = EnumRadioButtonGroup(binding, owner)
    combo = EnumComboBox(binding, owner)
    label = EnumLabel(binding, owner)
    cmds.undoInfo(state=True)
    cmds.flushUndo()
    assert radio.button_for_value(5).isChecked()
    assert combo.currentIndex() == 1
    assert label.text() == "Preview"
    assert binding.is_mixed
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    radio.button_for_value(5).click()
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [5, 5]
    assert not binding.is_mixed
    cmds.undo()
    flush()
    assert binding.is_mixed
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)
    cmds.redo()
    flush()
    combo.setCurrentIndex(2)
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [10, 10]
    assert radio.button_for_value(10).isChecked()
    assert label.text() == "Final"


def test_definition_changes_update_views_and_preserve_local_input_state(scene):
    nodes, owner = scene
    binding = MayaEnumPlugsBinding(
        [resolve_enum_plug(node, "mode") for node in nodes], parent=owner
    )
    radio = EnumRadioButtonGroup(binding, owner)
    combo = EnumComboBox(binding, owner)
    label = EnumLabel(binding, owner)
    radio.setInputEnabled(False)
    cmds.addAttr(nodes[0] + ".mode", edit=True, enumName="Off=0:Final=10")
    flush()
    assert not combo.isEnabled()
    assert combo.currentIndex() == -1
    assert label.text() == "未定義 (5)"
    assert radio.button_for_value(5) is None
    assert not any(button.isChecked() for button in radio.buttons)
    cmds.addAttr(nodes[1] + ".mode", edit=True, enumName="Off=0:Final=10")
    flush()
    assert combo.isEnabled()
    assert not radio.isEnabled()
    combo.setCurrentIndex(1)
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [10, 10]
    assert radio.button_for_value(10).isChecked()
    binding.dispose()
    flush()
    assert not combo.isEnabled()
    assert not radio.isEnabled()


def test_sample_shows_mixed_state_apply_and_releases_callbacks(scene):
    nodes, owner = scene
    window = maya_plugs.show(nodes, "mode")
    assert "混在" in window.state_label.text()
    assert "2/2" in window.state_label.text()
    assert window.label.text() == "Preview"
    window.apply_button.click()
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [5, 5]
    assert "一致" in window.state_label.text()
    cmds.setAttr(nodes[1] + ".mode", 0)
    cmds.setAttr(nodes[1] + ".mode", lock=True)
    flush()
    assert "1/2" in window.state_label.text()
    assert "ロック" in window.targets_label.text()
    window.radio_group.button_for_value(10).click()
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [10, 0]
    assert "混在" in window.state_label.text()
    registries = window.binding.findChildren(MayaCallbackRegistry)
    window.close()
    flush()
    assert not qt.isValid(window)
    assert all(not registry.callback_ids for registry in registries)
    reopened = maya_plugs.show(nodes, "mode")
    assert reopened.binding.value == 10
    assert reopened.binding.is_mixed


def test_sample_definition_failure_and_undefined_representative(scene):
    nodes, owner = scene
    cmds.addAttr(
        nodes[1] + ".mode", edit=True, enumName="Off=0:Different=5:Final=10"
    )
    with pytest.raises(ValueError, match="enum定義"):
        maya_plugs.show(nodes, "mode")
    cmds.addAttr(
        nodes[1] + ".mode", edit=True, enumName="Off=0:Preview=5:Final=10"
    )
    cmds.setAttr(nodes[0] + ".mode", 1)
    window = maya_plugs.show(nodes, "mode")
    assert not window.apply_button.isEnabled()
    assert window.combo_box.isEnabled()
    window.combo_box.setCurrentIndex(2)
    assert window.apply_button.isEnabled()
    assert [cmds.getAttr(node + ".mode") for node in nodes] == [10, 10]
