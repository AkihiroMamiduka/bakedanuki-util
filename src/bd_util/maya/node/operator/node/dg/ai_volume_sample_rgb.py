# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_volume_sample_rgb import (
    OutColorField,
    OutTransparencyField,
    PositionOffsetField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class InterpolationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CLOSEST = 0
    TRILINEAR = 1
    TRICUBIC = 2


class InterpolationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CLOSEST = 0
    TRILINEAR = 1
    TRICUBIC = 2

    NAME_MAP = {
        CLOSEST: "closest",
        TRILINEAR: "trilinear",
        TRICUBIC: "tricubic",
    }


class InterpolationEnumField(
    EnumField[InterpolationEnumAttrOperator, InterpolationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolationEnumAttrOperator
    PLUG_CLS = InterpolationEnumPlugOperator


class AiVolumeSampleRgb(DG):
    __slots__ = ()

    NODE_TYPE = "aiVolumeSampleRgb"

    outColor = OutColorField()
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField()
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    channel = DataStringField()

    positionOffset = PositionOffsetField()
    position_offset = positionOffset
    positionOffsetX = positionOffset.positionOffsetX
    position_offsetx = positionOffsetX
    positionOffsetY = positionOffset.positionOffsetY
    position_offsety = positionOffsetY
    positionOffsetZ = positionOffset.positionOffsetZ
    position_offsetz = positionOffsetZ

    interpolation = InterpolationEnumField()

    gamma = FloatField()

    hueShift = FloatField()
    hue_shift = hueShift

    saturation = FloatField()

    contrast = FloatField()

    contrastPivot = FloatField()
    contrast_pivot = contrastPivot

    exposure = FloatField()

    multiply = FloatField()

    add = FloatField()
