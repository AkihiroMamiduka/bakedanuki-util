# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_float_to_matrix import OutTransparencyField
from ....attr.define.std.at.flt_matrix import FltMatrixField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField


class GeneratedAiFloatToMatrix(DG):
    __slots__ = ()

    NODE_TYPE = "aiFloatToMatrix"

    outValue = FltMatrixField(writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    input00 = FloatField(default_value=1.0)
    input_00 = input00

    input01 = FloatField(default_value=0.0)
    input_01 = input01

    input02 = FloatField(default_value=0.0)
    input_02 = input02

    input03 = FloatField(default_value=0.0)
    input_03 = input03

    input10 = FloatField(default_value=0.0)
    input_10 = input10

    input11 = FloatField(default_value=1.0)
    input_11 = input11

    input12 = FloatField(default_value=0.0)
    input_12 = input12

    input13 = FloatField(default_value=0.0)
    input_13 = input13

    input20 = FloatField(default_value=0.0)
    input_20 = input20

    input21 = FloatField(default_value=0.0)
    input_21 = input21

    input22 = FloatField(default_value=1.0)
    input_22 = input22

    input23 = FloatField(default_value=0.0)
    input_23 = input23

    input30 = FloatField(default_value=0.0)
    input_30 = input30

    input31 = FloatField(default_value=0.0)
    input_31 = input31

    input32 = FloatField(default_value=0.0)
    input_32 = input32

    input33 = FloatField(default_value=1.0)
    input_33 = input33
