# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.matrix import DataMatrixField


class GeneratedFourByFourMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "fourByFourMatrix"

    in00 = DoubleField(default_value=1.0)
    i00 = in00

    in01 = DoubleField(default_value=0.0)
    i01 = in01

    in02 = DoubleField(default_value=0.0)
    i02 = in02

    in03 = DoubleField(default_value=0.0)
    i03 = in03

    in10 = DoubleField(default_value=0.0)
    i10 = in10

    in11 = DoubleField(default_value=1.0)
    i11 = in11

    in12 = DoubleField(default_value=0.0)
    i12 = in12

    in13 = DoubleField(default_value=0.0)
    i13 = in13

    in20 = DoubleField(default_value=0.0)
    i20 = in20

    in21 = DoubleField(default_value=0.0)
    i21 = in21

    in22 = DoubleField(default_value=1.0)
    i22 = in22

    in23 = DoubleField(default_value=0.0)
    i23 = in23

    in30 = DoubleField(default_value=0.0)
    i30 = in30

    in31 = DoubleField(default_value=0.0)
    i31 = in31

    in32 = DoubleField(default_value=0.0)
    i32 = in32

    in33 = DoubleField(default_value=1.0)
    i33 = in33

    output = DataMatrixField(writable=False)
    o = output
