# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

import bd_util as bdu
from bd_util.maya.ui import (
    MayaEnumBinding,
    MayaEnumPlugBinding,
    MayaEnumPlugsBinding,
    MayaPlugTargetState,
    MayaEnumPlugStore,
    MayaEnumPlugView,
    resolve_enum_plug,
    read_enum_definition,
)
from bd_util.ui import (
    EnumBinding,
    EnumComboBox,
    EnumDefinition,
    EnumItem,
    EnumLabel,
    EnumRadioButtonGroup,
    EnumValue,
    EnumViewModel,
    PythonEnumAttributeStore,
    SetEnumCommand,
    qt,
)


@dataclass
class Data:
    mode: int = 5


def check_contract(owner: qt.QObject, widget: qt.QWidget) -> None:
    definition = EnumDefinition.from_mapping(
        {0: "Off", 5: "Preview", 10: "Final"}
    )
    binding = EnumBinding.from_attribute(
        Data(), "mode", definition=definition, parent=owner
    )
    assert_type(binding, EnumBinding[PythonEnumAttributeStore[Data]])
    assert_type(binding.store.instance, Data)
    assert_type(binding.value, int)
    assert_type(binding.definition, EnumDefinition)
    assert_type(binding.is_value_defined, bool)
    assert_type(binding.changed, qt.QtCore.SignalInstance)
    assert_type(binding.definition_changed, qt.QtCore.SignalInstance)
    assert_type(binding.view_model, EnumViewModel)
    assert_type(binding.view_model.value, EnumValue)
    assert_type(binding.view_model.set_value_command, SetEnumCommand)
    assert_type(definition.item_for_value(5), EnumItem | None)
    assert_type(binding.set_value(5), bool)
    assert_type(binding.refresh(), bool)
    combo = EnumComboBox(binding, widget)
    assert_type(combo.view_model, EnumViewModel)
    combo.setInputEnabled(False)
    assert_type(combo.setValueRequestHandler(lambda value: True), None)
    EnumLabel(binding.view_model, widget)
    radio = EnumRadioButtonGroup(
        binding, widget, orientation=qt.Qt.Orientation.Vertical
    )
    assert_type(radio.view_model, EnumViewModel)
    assert_type(radio.buttons, tuple[qt.QRadioButton, ...])
    assert_type(radio.button_for_value(5), qt.QRadioButton | None)
    assert_type(radio.orientation(), qt.Qt.Orientation)
    assert_type(radio.isInputEnabled(), bool)
    radio.setInputEnabled(False)
    EnumRadioButtonGroup(binding.view_model, widget)
    plug = resolve_enum_plug("settings", "mode")
    assert_type(read_enum_definition(plug), EnumDefinition)
    maya_binding = MayaEnumBinding.from_attribute(
        Data(), "mode", definition=definition, maya_plug=plug, parent=owner
    )
    assert_type(maya_binding, MayaEnumBinding[PythonEnumAttributeStore[Data]])
    assert_type(maya_binding.store.instance, Data)
    assert_type(maya_binding.maya_view, MayaEnumPlugView | None)
    EnumComboBox(maya_binding, widget)
    EnumRadioButtonGroup(maya_binding, widget)
    plug_binding = MayaEnumPlugBinding(plug, parent=owner)
    assert_type(plug_binding.store, MayaEnumPlugStore)
    assert_type(plug_binding.value, int)
    EnumLabel(plug_binding, widget)
    EnumRadioButtonGroup(plug_binding, widget)
    nodes = bdu.Nodes()
    node = nodes.existing.transform("pCube1")
    assert_type(read_enum_definition(node.rotateOrder), EnumDefinition)
    typed_binding = MayaEnumPlugBinding(node.rotateOrder, parent=owner)
    typed_binding.set_value(node.rotateOrder.XYZ)
    group = MayaEnumPlugsBinding([node.rotateOrder], parent=owner)
    assert_type(group.value, int)
    assert_type(group.definition, EnumDefinition)
    assert_type(group.view_model, EnumViewModel)
    assert_type(group.store.read(), int)
    assert_type(group.store.definition, EnumDefinition)
    assert_type(group.is_mixed, bool)
    assert_type(group.target_count, int)
    assert_type(group.writable_count, int)
    assert_type(group.target_states, tuple[MayaPlugTargetState, ...])
    assert_type(group.state_changed, qt.QtCore.SignalInstance)
    assert_type(group.edit_failed, qt.QtCore.SignalInstance)
    assert_type(group.set_value(5), bool)
    assert_type(group.apply_representative_value(), bool)
    assert_type(group.refresh(), bool)
    EnumComboBox(group, widget)
    EnumRadioButtonGroup(group, widget)
    EnumLabel(group, widget)
