# coding: utf-8

# maya
from maya import cmds

# self
from ......maya.node.bd_node import BDNode


def main():
    test_transform()


def test_transform():
    name = "test_bd_node"
    cmds.createNode("transform", name=name)

    node = BDNode.transform(name)
    node.translate.set(1, 2, 3)
    node.rotate.set(45, 90, 135)
    node.scale.set(7, 8, 9)

    node.modifier_manager.do_it_dag()
    node.modifier_manager.do_it_dg()
