# coding: utf-8
"""compound配下のbool編集と親属性の状態変化を検証する。"""

import pytest
from maya import cmds

from bd_util.maya.ui import MayaBoolPlugBinding, resolve_bool_plug
from bd_util.ui import qt


def _flush() -> None:
    """Maya callbackが予約したQt更新を処理する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()


def _create_node(name: str) -> str:
    """boolを子に持つcompound属性を追加する。"""
    node = cmds.createNode("transform", name=name)
    cmds.addAttr(
        node, longName="options", attributeType="compound", numberOfChildren=1
    )
    cmds.addAttr(
        node,
        longName="enabled",
        attributeType="bool",
        parent="options",
        keyable=True,
    )
    return node


def test_bool_child_respects_parent_lock_and_connection(new_scene) -> None:
    """親のlock・接続へ追従し、解除後は再び子を編集できる。"""
    source = _create_node("compoundSource")
    target = _create_node("compoundTarget")
    binding = MayaBoolPlugBinding(resolve_bool_plug(target, "options.enabled"))
    try:
        assert binding.set_value(True)
        assert cmds.getAttr(target + ".enabled")
        cmds.setAttr(target + ".options", lock=True)
        _flush()
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.set_value(False)
        cmds.setAttr(target + ".options", lock=False)
        _flush()
        assert binding.view_model.set_value_command.can_execute
        cmds.connectAttr(source + ".options", target + ".options")
        _flush()
        assert not binding.view_model.set_value_command.can_execute
        assert not binding.value
        cmds.setAttr(source + ".enabled", True)
        cmds.getAttr(target + ".enabled")
        _flush()
        assert binding.value
        cmds.disconnectAttr(source + ".options", target + ".options")
        _flush()
        assert binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()


def test_bool_child_parent_delete_disposes_binding(new_scene) -> None:
    """親compoundの削除後に古い子plugへアクセスしない。"""
    node = _create_node("deletedCompound")
    binding = MayaBoolPlugBinding(resolve_bool_plug(node, "enabled"))
    try:
        cmds.deleteAttr(node + ".options")
        _flush()
        assert not binding.store.is_available
        assert not binding.view_model.set_value_command.can_execute
        assert binding.store.is_disposed
    finally:
        binding.dispose()


def test_bool_child_of_array_is_rejected(new_scene) -> None:
    """未展開の配列要素をscalar編集対象へ読み替えない。"""
    node = cmds.createNode("transform")
    cmds.addAttr(
        node,
        longName="records",
        attributeType="compound",
        numberOfChildren=1,
        multi=True,
    )
    cmds.addAttr(
        node, longName="enabled", attributeType="bool", parent="records"
    )
    with pytest.raises(TypeError, match="配列"):
        resolve_bool_plug(node, "records.enabled")
