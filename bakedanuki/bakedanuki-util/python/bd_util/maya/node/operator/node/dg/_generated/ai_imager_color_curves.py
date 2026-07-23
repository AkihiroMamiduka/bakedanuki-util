# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_color_curves import (
    RampBField,
    RampGField,
    RampRField,
    RampRGBField,
)
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiImagerColorCurves(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerColorCurves"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    workingColorSpace = DataStringField()
    working_color_space = workingColorSpace

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    rampRGB = RampRGBField(multi=True, default_value=(0.0, 0.0, 1.0), category="arnold")
    aiRampRGB = rampRGB

    rampR = RampRField(multi=True, default_value=(0.0, 0.0, 1.0), category="arnold")
    aiRampR = rampR

    rampG = RampGField(multi=True, default_value=(0.0, 0.0, 1.0), category="arnold")
    aiRampG = rampG

    rampB = RampBField(multi=True, default_value=(0.0, 0.0, 1.0), category="arnold")
    aiRampB = rampB
