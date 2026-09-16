# coding: utf-8
from dataclasses import dataclass
import sys

import pytest
from maya import cmds

from bd_util.maya.ui import MayaEnumPlugBinding, resolve_enum_plug
from bd_util.ui import (
    EnumBinding,
    EnumComboBox,
    EnumDefinition,
    EnumLabel,
    EnumRadioButtonGroup,
    EnumViewModel,
    qt,
)

DEFINITION = EnumDefinition.from_mapping(
    {-2: "Negative", 0: "Off", 5: "Preview", 10: "Final"}
)


@dataclass
class Data:
    mode: int = 5


def flush():
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def selected_values(view):
    return [
        item.value
        for item in view.view_model.definition.items
        if view.button_for_value(item.value).isChecked()
    ]


@pytest.mark.parametrize(
    "orientation", [qt.Qt.Orientation.Horizontal, qt.Qt.Orientation.Vertical]
)
def test_shared_views_sparse_values_unknown_and_large_integers(
    qt_application, orientation
):
    large = 2**80
    definition = EnumDefinition.from_mapping(
        {-2: "Negative", 5: "Preview", large: "Large"}
    )
    data = Data()
    binding = EnumBinding.from_attribute(data, "mode", definition=definition)
    radio = EnumRadioButtonGroup(binding, orientation=orientation)
    linked = EnumRadioButtonGroup(binding.view_model)
    combo = EnumComboBox(binding)
    label = EnumLabel(binding)
    values = []
    executed = []
    binding.changed.connect(values.append)
    binding.view_model.set_value_command.executed.connect(executed.append)
    try:
        assert radio.orientation() == orientation
        assert selected_values(radio) == [5]
        assert radio.button_for_value(0) is None
        radio.show()
        flush()
        first, second = radio.buttons[:2]
        if orientation == qt.Qt.Orientation.Horizontal:
            assert first.x() < second.x()
        else:
            assert first.y() < second.y()
        radio.button_for_value(-2).click()
        assert data.mode == binding.value == -2
        assert selected_values(linked) == [-2]
        assert combo.currentIndex() == 0
        assert label.text() == "Negative"
        combo.setCurrentIndex(2)
        assert data.mode == large
        assert selected_values(radio) == selected_values(linked) == [large]
        assert values == executed == [-2, large]
        data.mode = 1
        binding.refresh()
        assert selected_values(radio) == selected_values(linked) == []
        assert radio.isEnabled()
        assert executed == [-2, large]
        radio.button_for_value(large).click()
        radio.button_for_value(large).click()
        assert data.mode == large
        assert values == [-2, large, 1, large]
        assert executed == [-2, large, large, large]
    finally:
        for view in (radio, linked, combo, label):
            view.deleteLater()
        binding.dispose()
        flush()


def test_definition_changes_rebuild_without_writes_and_release_old_buttons(
    qt_application,
):
    class Store:
        definition = DEFINITION
        is_available = True
        is_writable = True
        value = 5

        def read(self):
            return self.value

        def write(self, value):
            pytest.fail("定義や表示の更新では書き込まない")

    store = Store()
    binding = EnumBinding(store)
    radio = EnumRadioButtonGroup(binding)
    executed = []
    binding.view_model.set_value_command.executed.connect(executed.append)
    try:
        old = radio.buttons
        store.definition = EnumDefinition.from_mapping(
            {10: "Final", 5: "R&D", -2: "Negative"}
        )
        binding.refresh()
        assert [button.accessibleName() for button in radio.buttons] == [
            "Final",
            "R&D",
            "Negative",
        ]
        assert radio.button_for_value(5).text() == "R&&D"
        assert selected_values(radio) == [5]
        for button in old:
            assert not button.isEnabled()
            button.click()
        assert executed == []
        flush()
        assert all(not qt.isValid(button) for button in old)
        store.definition = EnumDefinition.from_mapping({10: "Final"})
        binding.refresh()
        assert binding.value == 5
        assert selected_values(radio) == []
        assert radio.isEnabled()
        store.definition = EnumDefinition()
        binding.refresh()
        assert radio.buttons == ()
        assert not radio.isEnabled()
        store.definition = DEFINITION
        binding.refresh()
        assert selected_values(radio) == [5]
        assert radio.isEnabled()
        assert executed == []
    finally:
        radio.deleteLater()
        binding.dispose()
        flush()


def test_reentrant_definition_change_during_click_keeps_latest_state(
    qt_application,
):
    class Store:
        definition = DEFINITION
        is_available = True
        is_writable = True
        value = 5

        def read(self):
            return self.value

        def write(self, value):
            self.value = value
            return value

    store = Store()
    binding = EnumBinding(store)

    def replace_definition(value):
        if value == 10:
            store.definition = EnumDefinition.from_mapping(
                {0: "Off", -2: "On"}
            )
            store.value = -2
            binding.refresh()

    binding.changed.connect(replace_definition)
    radio = EnumRadioButtonGroup(binding)
    toggled = []
    for button in radio.buttons:
        button.toggled.connect(toggled.append)
    try:
        binding.set_value(0)
        assert selected_values(radio) == [0]
        assert toggled == []
        radio.button_for_value(10).click()
        flush()
        assert binding.value == store.value == -2
        assert selected_values(radio) == [-2]
        assert radio.button_for_value(10) is None
        assert [button.text() for button in radio.buttons] == ["Off", "On"]
    finally:
        radio.deleteLater()
        binding.dispose()
        flush()


@pytest.mark.parametrize("mode", ["reject", "normalize", "raise_after"])
def test_setter_actuals_restore_selection(qt_application, monkeypatch, mode):
    class Model:
        _mode = 5

        @property
        def mode(self):
            return self._mode

        @mode.setter
        def mode(self, value):
            if mode == "normalize":
                self._mode = 1
            elif mode == "raise_after":
                self._mode = -2
                raise ValueError("setter failed")

    errors = []
    monkeypatch.setattr(sys, "excepthook", lambda *error: errors.append(error))
    data = Model()
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    radio = EnumRadioButtonGroup(binding)
    try:
        radio.button_for_value(10).click()
        assert binding.value == data.mode
        expected = [] if mode == "normalize" else [data.mode]
        assert selected_values(radio) == expected
        assert len(errors) == (1 if mode == "raise_after" else 0)
        if errors:
            assert isinstance(errors[0][1], ValueError)
    finally:
        radio.deleteLater()
        binding.dispose()
        flush()


def test_local_input_state_and_readonly_store(qt_application):
    @dataclass(frozen=True)
    class Frozen:
        mode: int = 5

    readonly = EnumBinding.from_attribute(
        Frozen(), "mode", definition=DEFINITION
    )
    readonly_radio = EnumRadioButtonGroup(readonly)
    data = Data()
    binding = EnumBinding.from_attribute(data, "mode", definition=DEFINITION)
    radio = EnumRadioButtonGroup(binding)
    linked = EnumRadioButtonGroup(binding)
    try:
        assert not readonly_radio.isEnabled()
        readonly_radio.button_for_value(10).click()
        assert selected_values(readonly_radio) == [5]
        radio.setInputEnabled(False)
        assert not radio.isInputEnabled()
        radio.button_for_value(10).click()
        assert data.mode == 5
        linked.button_for_value(-2).click()
        assert selected_values(radio) == [-2]
        assert not radio.isEnabled()
        binding.refresh()
        assert not radio.isEnabled()
        radio.setInputEnabled(True)
        assert radio.isEnabled()
        with pytest.raises(TypeError):
            radio.setInputEnabled(1)
        with pytest.raises(TypeError):
            radio.button_for_value(True)
        with pytest.raises(ValueError):
            EnumRadioButtonGroup(binding, orientation="diagonal")
    finally:
        for view in (radio, linked, readonly_radio):
            view.deleteLater()
        binding.dispose()
        readonly.dispose()
        flush()


@pytest.mark.parametrize("ending", ["dispose", "owner", "during_change"])
def test_binding_end_disables_input(qt_application, ending):
    owner = qt.QObject()
    data = Data()
    binding = EnumBinding.from_attribute(
        data, "mode", definition=DEFINITION, parent=owner
    )
    radio = EnumRadioButtonGroup(binding)
    if ending == "dispose":
        binding.dispose()
    elif ending == "owner":
        owner.deleteLater()
    else:
        binding.changed.connect(lambda _value: binding.dispose())
        radio.button_for_value(-2).click()
    flush()
    assert not radio.isEnabled()
    radio.button_for_value(10).click()
    assert data.mode == (-2 if ending == "during_change" else 5)
    with pytest.raises(RuntimeError):
        _ = radio.view_model
    radio.deleteLater()
    if qt.isValid(owner):
        owner.deleteLater()
    flush()


def test_view_deletion_keeps_shared_memory_view_model(qt_application):
    vm = EnumViewModel(5, definition=DEFINITION)
    radio = EnumRadioButtonGroup(vm)
    linked = EnumRadioButtonGroup(vm)
    try:
        vm.value.changed.connect(
            lambda _value: radio.deleteLater() if qt.isValid(radio) else None
        )
        radio.button_for_value(10).click()
        flush()
        assert not qt.isValid(radio)
        assert not vm.is_disposed
        linked.button_for_value(-2).click()
        assert vm.value.value == -2
        assert selected_values(linked) == [-2]
    finally:
        linked.deleteLater()
        vm.dispose()
        vm.deleteLater()
        flush()


def test_maya_plug_radio_undo_locks_and_definition_changes(
    qt_application, maya_standalone
):
    node = cmds.createNode("network")
    cmds.addAttr(
        node,
        longName="mode",
        attributeType="enum",
        enumName="Negative=-2:Off=0:Preview=5:Final=10",
    )
    path = node + ".mode"
    cmds.setAttr(path, 5)
    binding = MayaEnumPlugBinding(resolve_enum_plug(node, "mode"))
    radio = EnumRadioButtonGroup(binding)
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert selected_values(radio) == [5]
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        radio.button_for_value(-2).click()
        assert cmds.getAttr(path) == -2
        cmds.undo()
        flush()
        assert selected_values(radio) == [5]
        assert cmds.undoInfo(query=True, undoQueueEmpty=True)
        cmds.redo()
        flush()
        assert selected_values(radio) == [-2]
        cmds.setAttr(path, lock=True)
        assert not radio.isEnabled()
        radio.setInputEnabled(False)
        cmds.setAttr(path, lock=False)
        assert not radio.isEnabled()
        radio.setInputEnabled(True)
        assert radio.isEnabled()
        cmds.setAttr(path, 5)
        cmds.addAttr(path, edit=True, enumName="Off=0:Final=10")
        flush()
        assert selected_values(radio) == []
        assert radio.button_for_value(5) is None
        assert cmds.getAttr(path) == 5
        cmds.undo()
        flush()
        assert selected_values(radio) == [5]
        cmds.redo()
        flush()
        assert selected_values(radio) == []
        radio.button_for_value(10).click()
        assert cmds.getAttr(path) == 10
    finally:
        radio.deleteLater()
        binding.dispose()
        cmds.delete(node)
        flush()
