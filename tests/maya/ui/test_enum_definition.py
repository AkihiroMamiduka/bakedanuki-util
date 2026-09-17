# coding: utf-8
"""Bindingを作らないenum定義調査の契約。"""

import pytest
from maya import cmds

from bd_util import Nodes
from bd_util.maya.ui import read_enum_definition, resolve_enum_plug
from bd_util.ui import EnumDefinition


def test_read_builtin_definition_uses_scene_without_writing(new_scene):
    """標準enumの実定義を読み、scene・現在値・Undo履歴を維持する。"""
    name = cmds.createNode("transform")
    node = Nodes().existing.transform(name)
    cmds.setAttr(name + ".rotateOrder", 5)
    cmds.flushUndo()
    cmds.file(modified=False)
    definition = read_enum_definition(node.rotateOrder)
    assert [item.name for item in definition.items] == [
        "xyz",
        "yzx",
        "zxy",
        "xzy",
        "yxz",
        "zyx",
    ]
    assert cmds.getAttr(name + ".rotateOrder") == 5
    assert not cmds.file(query=True, modified=True)
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_read_sparse_child_definition_follows_edits_and_undo(new_scene):
    """compound子の負数・飛び番と定義変更を毎回の実定義で判定する。"""
    node = cmds.createNode("transform")
    cmds.addAttr(
        node, longName="group", attributeType="compound", numberOfChildren=1
    )
    cmds.addAttr(
        node,
        longName="mode",
        parent="group",
        attributeType="enum",
        enumName="Negative=-2:Off=0:Preview=5",
    )
    plug = resolve_enum_plug(node, "group.mode")
    original = read_enum_definition(plug)
    assert original == EnumDefinition.from_mapping(
        {-2: "Negative", 0: "Off", 5: "Preview"}
    )
    cmds.addAttr(node + ".mode", edit=True, enumName="Negative=-2:Off=0:New=5")
    assert not read_enum_definition(plug).matches(original)
    cmds.undo()
    assert read_enum_definition(plug) == original


def test_read_definition_keeps_undefined_current_value(new_scene):
    """飛び番の間にある未定義の現在値を修正せずに定義だけを返す。"""
    node = cmds.createNode("transform")
    cmds.addAttr(
        node, longName="mode", attributeType="enum", enumName="Off=0:On=5"
    )
    cmds.setAttr(node + ".mode", 2)
    cmds.flushUndo()
    definition = read_enum_definition(resolve_enum_plug(node, "mode"))
    assert definition.item_for_value(2) is None
    assert cmds.getAttr(node + ".mode") == 2
    assert cmds.undoInfo(query=True, undoQueueEmpty=True)


def test_read_definition_rejects_non_enum_plugs(new_scene):
    """enum以外の型付き属性は実行時にも拒否する。"""
    node = Nodes().existing.transform(cmds.createNode("transform"))
    with pytest.raises(TypeError, match="EnumPlugOperator"):
        read_enum_definition(node.translateX)
