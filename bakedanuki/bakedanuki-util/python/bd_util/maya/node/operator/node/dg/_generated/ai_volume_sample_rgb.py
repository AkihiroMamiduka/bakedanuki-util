# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_volume_sample_rgb import (
    OutColorField,
    OutTransparencyField,
    PositionOffsetField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedAiVolumeSampleRgb(DG):
    __slots__ = ()

    NODE_TYPE = "aiVolumeSampleRgb"

    outColor = OutColorField(default_value=(0.0, 0.0, 0.0), writable=False)
    out = outColor
    outColorR = outColor.outColorR
    outr = outColorR
    outColorG = outColor.outColorG
    outg = outColorG
    outColorB = outColor.outColorB
    outb = outColorB

    outTransparency = OutTransparencyField(default_value=(0.0, 0.0, 0.0), writable=False)
    ot = outTransparency
    outTransparencyR = outTransparency.outTransparencyR
    otr = outTransparencyR
    outTransparencyG = outTransparency.outTransparencyG
    otg = outTransparencyG
    outTransparencyB = outTransparency.outTransparencyB
    otb = outTransparencyB

    channel = DataStringField()

    positionOffset = PositionOffsetField(default_value=(0.0, 0.0, 0.0))
    position_offset = positionOffset
    positionOffsetX = positionOffset.positionOffsetX
    position_offsetx = positionOffsetX
    positionOffsetY = positionOffset.positionOffsetY
    position_offsety = positionOffsetY
    positionOffsetZ = positionOffset.positionOffsetZ
    position_offsetz = positionOffsetZ

    interpolation = InterpolationEnumField(default_value=1)

    gamma = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=3.0)

    hueShift = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    hue_shift = hueShift

    saturation = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)

    contrast = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)

    contrastPivot = FloatField(default_value=0.18000000715255737, soft_min_value=0.0, soft_max_value=1.0)
    contrast_pivot = contrastPivot

    exposure = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)

    multiply = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)

    add = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
