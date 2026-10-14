# coding: utf-8

from ......maya.node.nodes import Nodes


def main():
    test_transform()


def test_transform():
    # Nodes
    bd_nodes = Nodes()

    # NodeCreator
    name = "test_nodes_node"
    bd_nodes.create.transform(name=name)

    # mod
    bd_nodes.modifier_manager.do_it_dag()

    # ExistingNode
    node = bd_nodes.existing.transform(name)
    node.translate.set(1, 2, 3)
    node.rotate.set(45, 90, 135)
    node.scale.set(7, 8, 9)

    # mod
    bd_nodes.modifier_manager.do_it_dag()
    bd_nodes.modifier_manager.do_it_dg()
