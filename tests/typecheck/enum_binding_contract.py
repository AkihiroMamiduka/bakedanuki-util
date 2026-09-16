# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

import bd_util as bdu
from bd_util.maya.ui import (
    MayaEnumBinding,
    MayaEnumPlugBinding,
    MayaEnumPlugStore,
    MayaEnumPlugView,
    resolve_enum_plug,
)
from bd_util.ui import (
    EnumBinding,
    EnumComboBox,
    EnumDefinition,
    EnumItem,
    EnumLabel,
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
    EnumLabel(binding.view_model, widget)
    plug = resolve_enum_plug("settings", "mode")
    maya_binding = MayaEnumBinding.from_attribute(
        Data(), "mode", definition=definition, maya_plug=plug, parent=owner
    )
    assert_type(maya_binding, MayaEnumBinding[PythonEnumAttributeStore[Data]])
    assert_type(maya_binding.store.instance, Data)
    assert_type(maya_binding.maya_view, MayaEnumPlugView | None)
    EnumComboBox(maya_binding, widget)
    plug_binding = MayaEnumPlugBinding(plug, parent=owner)
    assert_type(plug_binding.store, MayaEnumPlugStore)
    assert_type(plug_binding.value, int)
    EnumLabel(plug_binding, widget)
    nodes = bdu.Nodes()
    node = nodes.existing.transform("pCube1")
    typed_binding = MayaEnumPlugBinding(node.rotateOrder, parent=owner)
    typed_binding.set_value(node.rotateOrder.XYZ)
