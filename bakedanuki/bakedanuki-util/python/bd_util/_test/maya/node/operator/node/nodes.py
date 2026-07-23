# coding: utf-8

# self
from ......maya.node.nodes import Nodes


def main():
    test_transform()


def test_transform():
    # Nodes
    nodes = Nodes()

    # NodeCreator
    name = "test_nodes_node"
    nodes.create.transform(name=name)

    # mod
    nodes.modifier_manager.do_it_dag()

    # ExistingNode
    node = nodes.existing.transform(name)
    node.translate.set(1, 2, 3)
    node.rotate.set(45, 90, 135)
    node.scale.set(7, 8, 9)

    # mod
    nodes.modifier_manager.do_it_dag()
    nodes.modifier_manager.do_it_dg()
