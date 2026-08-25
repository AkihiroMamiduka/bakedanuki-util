# coding: utf-8
from __future__ import annotations

import pytest


def test_nodes_can_import_from_bd_util(new_scene):
    from bd_util import ModifierManager, Nodes

    modifier_manager = ModifierManager()
    nodes = Nodes(modifier_manager=modifier_manager)

    assert nodes.modifier_manager is modifier_manager
    assert nodes.create.modifier_manager is modifier_manager
    assert nodes.existing.modifier_manager is modifier_manager
    assert nodes.types is nodes.types


def test_nodes_can_import_from_maya_node_package(new_scene):
    from bd_util.maya.node import Nodes

    assert Nodes.__name__ == "Nodes"


def test_nodes_is_the_only_public_node_access_entry(new_scene):
    import bd_util
    from bd_util.maya import node as node_package

    assert "Nodes" in bd_util.__all__
    assert "NodeCreator" not in bd_util.__all__
    assert "ExistingNode" not in bd_util.__all__
    assert not hasattr(bd_util, "NodeCreator")
    assert not hasattr(bd_util, "ExistingNode")
    assert not hasattr(bd_util, "NodeTypes")
    assert node_package.__all__ == ("Nodes",)
    assert not hasattr(node_package, "ExistingNode")
    assert not hasattr(node_package, "NodeTypes")


def test_nodes_create_and_existing_share_modifier_manager(
    new_scene,
    maya_cmds,
):
    import bd_util
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    maya_cmds.createNode("transform", name="existing_transform")
    modifier_manager = bd_util.ModifierManager()
    nodes = bd_util.Nodes(modifier_manager=modifier_manager)

    created = nodes.create.transform(name="created_transform")
    existing = nodes.existing.transform("existing_transform")

    assert isinstance(created, Transform)
    assert isinstance(existing, Transform)
    assert created.modifier_manager is modifier_manager
    assert existing.modifier_manager is modifier_manager

    modifier_manager.do_it_dag()
    assert maya_cmds.objExists("created_transform")


def test_nodes_creates_shared_modifier_manager(new_scene):
    import bd_util

    nodes = bd_util.Nodes()

    assert nodes.create.modifier_manager is nodes.modifier_manager
    assert nodes.existing.modifier_manager is nodes.modifier_manager


def test_nodes_existing_auto_detects_node_type(new_scene, maya_cmds):
    import bd_util
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    maya_cmds.createNode("plusMinusAverage", name="existing_pma")
    nodes = bd_util.Nodes()

    node = nodes.existing("existing_pma")

    assert isinstance(node, PlusMinusAverage)
    assert node.modifier_manager is nodes.modifier_manager


def test_nodes_existing_rejects_different_node_type(new_scene, maya_cmds):
    import bd_util

    maya_cmds.createNode("composeMatrix", name="existing_compose_matrix")
    nodes = bd_util.Nodes()

    with pytest.raises(
        TypeError,
        match=(
            "Node type mismatch.*expected 'decomposeMatrix'.*"
            "got 'composeMatrix'"
        ),
    ):
        nodes.existing.decomposeMatrix("existing_compose_matrix")


def test_nodes_caches_accessors(new_scene):
    import bd_util

    nodes = bd_util.Nodes()
    existing_accessor = nodes.existing.decomposeMatrix

    assert nodes.create is nodes.create
    assert nodes.existing is nodes.existing
    assert nodes.types is nodes.types
    assert nodes.existing.decomposeMatrix is existing_accessor
    assert nodes.existing.__dict__["decomposeMatrix"] is existing_accessor
