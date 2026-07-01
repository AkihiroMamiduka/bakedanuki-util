# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.dt.matrix import DataMatrixField


class FourByFourMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "fourByFourMatrix"

    in00 = DoubleField()
    i00 = in00

    in01 = DoubleField()
    i01 = in01

    in02 = DoubleField()
    i02 = in02

    in03 = DoubleField()
    i03 = in03

    in10 = DoubleField()
    i10 = in10

    in11 = DoubleField()
    i11 = in11

    in12 = DoubleField()
    i12 = in12

    in13 = DoubleField()
    i13 = in13

    in20 = DoubleField()
    i20 = in20

    in21 = DoubleField()
    i21 = in21

    in22 = DoubleField()
    i22 = in22

    in23 = DoubleField()
    i23 = in23

    in30 = DoubleField()
    i30 = in30

    in31 = DoubleField()
    i31 = in31

    in32 = DoubleField()
    i32 = in32

    in33 = DoubleField()
    i33 = in33

    output = DataMatrixField()
    o = output
