# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_layer_float import OutTransparencyField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiLayerFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiLayerFloat"

    outValue = FloatField()
    out = outValue

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    enable1 = BoolField()

    name1 = DataStringField()

    input1 = FloatField()

    mix1 = FloatField()

    enable2 = BoolField()

    name2 = DataStringField()

    input2 = FloatField()

    mix2 = FloatField()

    enable3 = BoolField()

    name3 = DataStringField()

    input3 = FloatField()

    mix3 = FloatField()

    enable4 = BoolField()

    name4 = DataStringField()

    input4 = FloatField()

    mix4 = FloatField()

    enable5 = BoolField()

    name5 = DataStringField()

    input5 = FloatField()

    mix5 = FloatField()

    enable6 = BoolField()

    name6 = DataStringField()

    input6 = FloatField()

    mix6 = FloatField()

    enable7 = BoolField()

    name7 = DataStringField()

    input7 = FloatField()

    mix7 = FloatField()

    enable8 = BoolField()

    name8 = DataStringField()

    input8 = FloatField()

    mix8 = FloatField()
