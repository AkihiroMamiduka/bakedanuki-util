# coding: utf-8
"""scalar resolverの共有範囲と、実体・型・DAG経路の鮮度を検証する。"""

import pytest
from maya import cmds
from maya.api import OpenMaya as om

from bd_util.maya.ui import (
    resolve_bool_plug,
    resolve_enum_plug,
    resolve_float_plug,
    resolve_int_plug,
    resolve_string_plug,
    shared_scalar_plug_nodes,
)


def test_scalar_resolvers_share_only_within_the_explicit_scope(new_scene):
    """五種類のresolverは明示範囲内だけnodeを共有し、値や型は共有しない。"""
    node = cmds.createNode("network")
    for name, kind in (
        ("amount", "double"),
        ("count", "long"),
        ("enabled", "bool"),
    ):
        cmds.addAttr(node, longName=name, attributeType=kind)
    cmds.addAttr(node, longName="mode", attributeType="enum", enumName="A:B")
    cmds.addAttr(node, longName="label", dataType="string")
    before = resolve_float_plug(node, "amount")
    with shared_scalar_plug_nodes():
        plugs = (
            resolve_float_plug(node, "amount"),
            resolve_int_plug(node, "count"),
            resolve_bool_plug(node, "enabled"),
            resolve_enum_plug(node, "mode"),
            resolve_string_plug(node, "label"),
        )
        assert all(plug.node is plugs[0].node for plug in plugs)
        assert plugs[0].node is not before.node
        assert len({plug.plug.name() for plug in plugs}) == 5
    after = resolve_float_plug(node, "amount")
    assert after.node is not plugs[0].node
    assert after.node is not before.node
    cmds.setAttr(node + ".amount", 3.5)
    assert plugs[0].plug.asDouble() == after.plug.asDouble() == 3.5


def test_nested_scope_and_exception_restore_the_previous_scope(new_scene):
    """入れ子と例外で外側の共有範囲を壊さず、終了後の操作は独立させる。"""
    node = cmds.createNode("transform")
    with shared_scalar_plug_nodes():
        outer = resolve_float_plug(node, "tx").node
        with pytest.raises(ValueError, match="中断"):
            with shared_scalar_plug_nodes():
                inner = resolve_float_plug(node, "ty").node
                assert inner is not outer
                raise ValueError("中断")
        assert resolve_float_plug(node, "tz").node is outer
    assert resolve_float_plug(node, "tx").node is not outer


def test_scope_rechecks_attribute_paths_and_recreated_types(new_scene):
    """nodeを共有してもalias・誤った親path・再作成後の型違いを受理しない。"""
    node = cmds.createNode("network")
    cmds.addAttr(node, ln="group", at="compound", numberOfChildren=1)
    cmds.addAttr(node, ln="amount", at="double", parent="group")
    cmds.aliasAttr("amountAlias", node + ".group.amount")
    with shared_scalar_plug_nodes():
        first = resolve_float_plug(node, "group.amount")
        for invalid in ("amountAlias", "wrong.amount"):
            with pytest.raises(AttributeError):
                resolve_float_plug(node, invalid)
        cmds.deleteAttr(node + ".group")
        cmds.addAttr(node, ln="amount", at="long")
        with pytest.raises(TypeError):
            resolve_float_plug(node, "amount")
        assert resolve_int_plug(node, "amount").node is first.node


def test_scope_does_not_follow_a_recreated_node_with_the_same_name(new_scene):
    """同名でも実体が異なるnodeは、新しいwrapperへ結ぶ。"""
    node = cmds.createNode("transform", name="scalarSharedReplacement")
    with shared_scalar_plug_nodes():
        first = resolve_float_plug(node, "tx")
        cmds.delete(node)
        replacement = cmds.createNode("transform", name=node)
        assert replacement == node
        second = resolve_float_plug(replacement, "ty")
        assert second.node is not first.node
        cmds.setAttr(second.node.cmd_access_name + ".ty", 7.0)
        assert second.plug.asDouble() == 7.0


def _assert_fresh_dag_target(node_name, attribute, value):
    """通常resolverと名前・実体・書込み先が一致することを確認する。"""
    shared = resolve_float_plug(node_name, attribute)
    # 入れ子の独立範囲を使い、同じ現行sceneから新しいwrapperを生成する
    with shared_scalar_plug_nodes():
        fresh = resolve_float_plug(node_name, attribute)
    assert shared.node.m_obj == fresh.node.m_obj
    assert shared.plug == fresh.plug
    assert shared.node.cmd_access_name == fresh.node.cmd_access_name
    cmds.setAttr(shared.node.cmd_access_name + "." + attribute, value)
    assert fresh.plug.asDouble() == value
    return shared


def test_scope_rechecks_the_dag_path_after_ancestor_reparent(new_scene):
    """構築途中の祖先reparent後も、fresh resolverと同じ対象へ書き込む。"""
    first_parent = cmds.createNode("transform")
    second_parent = cmds.createNode("transform")
    ancestor = cmds.createNode("transform", parent=first_parent)
    leaf = cmds.createNode("transform", parent=ancestor)
    with shared_scalar_plug_nodes():
        previous = resolve_float_plug(leaf, "tx")
        cmds.parent(ancestor, second_parent)
        path = om.MDagPath.getAPathTo(previous.plug.node()).fullPathName()
        current = _assert_fresh_dag_target(path, "ty", 8.0)
        assert current.node.m_obj == previous.node.m_obj


def test_scope_replaces_an_invalidated_instance_path(new_scene):
    """選択経路を残して別instanceを削除しても、消えた経路を再使用しない。"""
    first_parent = cmds.createNode("transform")
    second_parent = cmds.createNode("transform")
    leaf = cmds.createNode("transform", parent=first_parent)
    cmds.parent(leaf, second_parent, addObject=True)
    with shared_scalar_plug_nodes():
        previous = resolve_float_plug(leaf, "tx")
        cached_path = previous.node.cmd_access_name
        paths = om.MDagPath.getAllPathsTo(previous.plug.node())
        selected_path = next(
            path.fullPathName()
            for path in paths
            if path.fullPathName() != cached_path
        )
        cmds.parent(cached_path, removeObject=True)
        assert cmds.objExists(selected_path)
        current = _assert_fresh_dag_target(selected_path, "ty", 9.0)
        assert current.node is not previous.node
        assert current.node.cmd_access_name == selected_path
