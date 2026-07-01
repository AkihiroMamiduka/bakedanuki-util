# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_float_to_matrix import OutTransparencyField
from ...attr.define.std.at.flt_matrix import FltMatrixField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AiFloatToMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToMatrix"

    outValue = FltMatrixField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input00 = FloatField()
    input_00 = input00

    input01 = FloatField()
    input_01 = input01

    input02 = FloatField()
    input_02 = input02

    input03 = FloatField()
    input_03 = input03

    input10 = FloatField()
    input_10 = input10

    input11 = FloatField()
    input_11 = input11

    input12 = FloatField()
    input_12 = input12

    input13 = FloatField()
    input_13 = input13

    input20 = FloatField()
    input_20 = input20

    input21 = FloatField()
    input_21 = input21

    input22 = FloatField()
    input_22 = input22

    input23 = FloatField()
    input_23 = input23

    input30 = FloatField()
    input_30 = input30

    input31 = FloatField()
    input_31 = input31

    input32 = FloatField()
    input_32 = input32

    input33 = FloatField()
    input_33 = input33
