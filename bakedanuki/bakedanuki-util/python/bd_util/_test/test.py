# coding:utf-8

# self
from ..maya.node.creater._core import NodeCreater


def main():
    creater = NodeCreater()

    cmp_m = creater.composeMatrix(name="cmp_m")
    mult_m = creater.multMatrix(name="mult_m")

    cmp_m.outputMatrix > mult_m.matrixIn[next]

    creater.modifier_manager.do_it_dg()
