# coding:utf-8

# self
from ..maya.node.creator._core import NodeCreator


def main():
    creator = NodeCreator()

    cmp_m = creator.composeMatrix(name="cmp_m")
    mult_m = creator.multMatrix(name="mult_m")

    cmp_m.outputMatrix > mult_m.matrixIn[next]

    creator.modifier_manager.do_it_dg()
