# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_layer_float import OutTransparencyField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiLayerFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiLayerFloat"

    outValue = FloatField(default_value=0.0, writable=False)
    out = outValue

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    enable1 = BoolField(default_value=True)

    name1 = DataStringField()

    input1 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix1 = FloatField(default_value=1.0, min_value=0.0, soft_max_value=1.0)

    enable2 = BoolField(default_value=False)

    name2 = DataStringField()

    input2 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix2 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable3 = BoolField(default_value=False)

    name3 = DataStringField()

    input3 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix3 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable4 = BoolField(default_value=False)

    name4 = DataStringField()

    input4 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix4 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable5 = BoolField(default_value=False)

    name5 = DataStringField()

    input5 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix5 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable6 = BoolField(default_value=False)

    name6 = DataStringField()

    input6 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix6 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable7 = BoolField(default_value=False)

    name7 = DataStringField()

    input7 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix7 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)

    enable8 = BoolField(default_value=False)

    name8 = DataStringField()

    input8 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    mix8 = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
