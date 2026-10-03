# coding: utf-8
"""ノード名Bindingから具体Storeと既存String Viewへ型を辿る。"""

from typing import assert_type

import bd_util as bdu
from bd_util.maya.ui import MayaNodeNameBinding, MayaNodeNameStore
from bd_util.ui import (
    StringBinding,
    StringLabel,
    StringLineEdit,
    StringValue,
    StringViewModel,
    qt,
)


def check_contract(owner: qt.QObject, widget: qt.QWidget) -> None:
    """公開入口でノード名StoreとStringの共通APIを補完できることを固定する。"""
    node = bdu.Nodes().existing("sampleNode")
    binding = MayaNodeNameBinding(node, parent=owner, rename_shapes=False)
    assert_type(binding, MayaNodeNameBinding)
    assert_type(binding.store, MayaNodeNameStore)
    assert_type(binding.store.node_operator, bdu.node_types.NodeOperator)
    assert_type(binding.store.is_available, bool)
    assert_type(binding.store.is_writable, bool)
    assert_type(binding.store.is_disposed, bool)
    assert_type(binding.store.read(), str)
    assert_type(binding.store.write("requestedName"), str)
    assert_type(binding.view_model, StringViewModel)
    assert_type(binding.view_model.value, StringValue)
    assert_type(binding.value, str)
    assert_type(binding.changed, qt.QtCore.SignalInstance)
    assert_type(binding.set_value("nextName"), bool)
    assert_type(binding.refresh(), bool)
    assert_type(binding.dispose(), None)
    assert_type(StringLineEdit(binding, widget).view_model, StringViewModel)
    StringLabel(binding, widget)
    model = StringViewModel(parent=owner)
    store = MayaNodeNameStore(model, node, owner, rename_shapes=True)
    model.attach_store(store)
    assert_type(store, MayaNodeNameStore)
    assert_type(store.dispose(), None)
    _accept_string_binding(binding)


def _accept_string_binding(source: StringBinding[MayaNodeNameStore]) -> None:
    """汎用String Bindingを受ける既存Viewへ代入可能であることを固定する。"""
    assert_type(source.store, MayaNodeNameStore)
