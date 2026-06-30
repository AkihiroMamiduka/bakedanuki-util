# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_imager_color_curves import (
    RampBField,
    RampGField,
    RampRField,
    RampRGBField,
)
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AiImagerColorCurves(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerColorCurves"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    workingColorSpace = DataStringField()
    working_color_space = workingColorSpace

    aiUserOptions = DataStringField()
    ai_user_options = aiUserOptions

    rampRGB = RampRGBField(multi=True)
    aiRampRGB = rampRGB

    rampR = RampRField(multi=True)
    aiRampR = rampR

    rampG = RampGField(multi=True)
    aiRampG = rampG

    rampB = RampBField(multi=True)
    aiRampB = rampB
