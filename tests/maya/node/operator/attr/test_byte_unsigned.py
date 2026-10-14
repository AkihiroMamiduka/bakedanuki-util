# coding: utf-8
from maya import cmds

from bd_util.maya.ui import resolve_int_plug


def test_byte_operator_preserves_unsigned_values_with_modifier(new_scene):
    """byteの128～255をModifierManager経由でも符号反転させない。"""
    node = cmds.createNode("transform")
    cmds.addAttr(node, longName="unsignedByte", attributeType="byte")
    plug = resolve_int_plug(node, "unsignedByte")
    for value in (128, 255):
        plug.set(value)
        plug.node.modifier_manager.do_it_dg()
        assert plug.get() == cmds.getAttr(node + ".unsignedByte") == value
