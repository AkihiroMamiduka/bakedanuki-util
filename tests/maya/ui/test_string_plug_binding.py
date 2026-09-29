# coding: utf-8
from dataclasses import dataclass

import pytest
from maya import cmds

from bd_util.maya.ui import (
    MayaStringBinding,
    MayaStringPlugBinding,
    resolve_string_plug,
)
from bd_util.maya.ui.callback import MayaCallbackRegistry
from bd_util.ui import qt


@dataclass
class Data:
    """Maya Viewへ接続するPython正本。"""

    name: str = "Python"


def flush() -> None:
    """Maya callback後のQt処理を実行する。"""
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.processEvents()
    qt.QtCore.QCoreApplication.sendPostedEvents(
        None, qt.QEvent.Type.DeferredDelete
    )


def test_joint_other_type_store_external_change_and_undo(new_scene):
    """joint.otherTypeを初期読込みしMaya標準Undoへ載せる。"""
    joint = cmds.createNode("joint")
    cmds.setAttr(joint + ".type", 18)
    cmds.setAttr(joint + ".drawLabel", True)
    cmds.setAttr(joint + ".otherType", "jaw", type="string")
    binding = MayaStringPlugBinding(resolve_string_plug(joint, "otherType"))
    values = []
    binding.changed.connect(values.append)
    try:
        assert binding.value == "jaw"
        assert cmds.getAttr(joint + ".type") == 18
        assert cmds.getAttr(joint + ".drawLabel")
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        assert binding.set_value("ひざ😀")
        assert cmds.getAttr(joint + ".otherType") == "ひざ😀"
        cmds.undo()
        flush()
        assert binding.value == "jaw"
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert binding.value == "ひざ😀"
        cmds.setAttr(joint + ".otherType", "", type="string")
        flush()
        assert binding.value == ""
        assert values == ["ひざ😀", "jaw", "ひざ😀", ""]
    finally:
        binding.dispose()
        flush()


def test_unset_dynamic_string_lock_connection_rename_and_delete(new_scene):
    """未設定を空文字へ寄せ、編集可否と寿命を追跡する。"""
    node = cmds.createNode("network")
    cmds.addAttr(node, longName="text", shortName="tx", dataType="string")
    binding = MayaStringPlugBinding(resolve_string_plug(node, "tx"))
    try:
        assert cmds.getAttr(node + ".text") is None
        assert binding.value == ""
        cmds.setAttr(node + ".text", lock=True)
        flush()
        assert not binding.view_model.set_value_command.can_execute
        cmds.setAttr(node + ".text", lock=False)
        flush()
        assert binding.view_model.set_value_command.can_execute
        source = cmds.createNode("network")
        cmds.addAttr(source, longName="text", dataType="string")
        cmds.setAttr(source + ".text", "source", type="string")
        cmds.connectAttr(source + ".text", node + ".text")
        flush()
        assert binding.value == "source"
        assert not binding.view_model.set_value_command.can_execute
        cmds.disconnectAttr(source + ".text", node + ".text")
        flush()
        assert binding.view_model.set_value_command.can_execute
        renamed = cmds.rename(node, "renamedStringTarget")
        binding.set_value("renamed")
        assert cmds.getAttr(renamed + ".text") == "renamed"
        cmds.deleteAttr(renamed + ".text")
        flush()
        assert binding.store.is_disposed
        assert not binding.view_model.set_value_command.can_execute
    finally:
        binding.dispose()
        flush()


def test_resolver_rejects_wrong_type_and_array(new_scene):
    """scalar typed string以外を誤って編集しない。"""
    node = cmds.createNode("network")
    cmds.addAttr(node, longName="textArray", dataType="string", multi=True)
    cmds.addAttr(node, longName="count", attributeType="long")
    with pytest.raises(TypeError):
        resolve_string_plug(node, "count")
    with pytest.raises(TypeError):
        resolve_string_plug(node, "textArray")
    with pytest.raises(ValueError):
        resolve_string_plug(node, "textArray[0]")


def test_python_store_maya_view_sync_and_callback_release(new_scene):
    """Python正本とMaya Viewの双方向同期と終了を確認する。"""
    node = cmds.createNode("network")
    cmds.addAttr(node, longName="text", dataType="string")
    data = Data()
    binding = MayaStringBinding.from_attribute(
        data, "name", maya_plug=resolve_string_plug(node, "text")
    )
    view = binding.maya_view
    assert view is not None
    try:
        assert cmds.getAttr(node + ".text") == "Python"
        assert view.is_synchronized
        binding.set_value("UI")
        assert cmds.getAttr(node + ".text") == "UI"
        cmds.setAttr(node + ".text", "Maya", type="string")
        flush()
        assert data.name == binding.value == "Maya"
        assert view.is_synchronized
        data.name = "refresh"
        binding.refresh()
        assert cmds.getAttr(node + ".text") == "refresh"
        registries = binding.findChildren(MayaCallbackRegistry)
        assert len(registries) == 1
        binding.dispose()
        flush()
        assert registries[0].callback_ids == ()
    finally:
        binding.dispose()
        flush()


def test_python_store_maya_view_preserves_redo_after_normalization(new_scene):
    """Pythonの補正結果をMayaへ戻してもUndoのRedo履歴を消さない。"""

    class NormalizingData:
        """Maya入力を小文字へ揃える正本。"""

        def __init__(self) -> None:
            """初期値を保持する。"""
            self._name = "start"

        @property
        def name(self) -> str:
            """確定文字列を返す。"""
            return self._name

        @name.setter
        def name(self, value: str) -> None:
            """入力を小文字へ補正する。"""
            self._name = value.lower()

    node = cmds.createNode("network")
    cmds.addAttr(node, longName="text", dataType="string")
    data = NormalizingData()
    binding = MayaStringBinding.from_attribute(
        data, "name", maya_plug=resolve_string_plug(node, "text")
    )
    view = binding.maya_view
    assert view is not None
    try:
        cmds.undoInfo(state=True)
        cmds.flushUndo()
        cmds.setAttr(node + ".text", "UPPER", type="string")
        flush()
        assert data.name == binding.value == "upper"
        assert cmds.getAttr(node + ".text") == "upper"
        cmds.undo()
        flush()
        assert cmds.getAttr(node + ".text") == "UPPER"
        assert data.name == "upper"
        assert not view.is_synchronized
        assert not cmds.undoInfo(query=True, redoQueueEmpty=True)
        cmds.redo()
        flush()
        assert cmds.getAttr(node + ".text") == data.name == "upper"
        assert view.is_synchronized
    finally:
        binding.dispose()
        flush()
