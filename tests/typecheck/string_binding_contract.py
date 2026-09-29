# coding: utf-8
from dataclasses import dataclass
from typing import assert_type

from bd_util.maya.ui import (
    MayaStringBinding,
    MayaStringPlugBinding,
    MayaStringPlugStore,
    MayaStringPlugView,
    resolve_string_plug,
)
from bd_util.ui import (
    PythonStringAttributeStore,
    SetStringCommand,
    StringBinding,
    StringLabel,
    StringLineEdit,
    StringValue,
    StringViewModel,
    qt,
)


@dataclass
class Data:
    """型推論を検証するPython正本。"""

    name: str = "start"


def check_contract(owner: qt.QObject, widget: qt.QWidget) -> None:
    """公開APIから具体型と補完対象を辿れることを固定する。"""
    binding = StringBinding.from_attribute(Data(), "name", parent=owner)
    assert_type(binding, StringBinding[PythonStringAttributeStore[Data]])
    assert_type(binding.store.instance, Data)
    assert_type(binding.value, str)
    assert_type(binding.changed, qt.QtCore.SignalInstance)
    assert_type(binding.view_model, StringViewModel)
    assert_type(binding.view_model.value, StringValue)
    assert_type(binding.view_model.set_value_command, SetStringCommand)
    assert_type(binding.set_value("next"), bool)
    assert_type(binding.refresh(), bool)
    line = StringLineEdit(binding, widget)
    assert_type(line.view_model, StringViewModel)
    assert_type(line.isInputEnabled(), bool)
    assert_type(line.hasConflict(), bool)
    assert_type(line.setInputEnabled(False), None)
    StringLabel(binding.view_model, widget)
    plug = resolve_string_plug("joint1", "otherType")
    maya_binding = MayaStringBinding.from_attribute(
        Data(), "name", maya_plug=plug, parent=owner
    )
    assert_type(
        maya_binding, MayaStringBinding[PythonStringAttributeStore[Data]]
    )
    assert_type(maya_binding.maya_view, MayaStringPlugView | None)
    plug_binding = MayaStringPlugBinding(plug, parent=owner)
    assert_type(plug_binding.store, MayaStringPlugStore)
    assert_type(plug_binding.value, str)
    StringLineEdit(plug_binding, widget)
    StringLabel(plug_binding, widget)
