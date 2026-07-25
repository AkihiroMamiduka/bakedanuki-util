# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_volume_sample_float import (
    OutTransparencyField,
    PositionOffsetField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
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


class VolumeTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FOG = 0
    SDF = 1


class VolumeTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FOG = 0
    SDF = 1

    NAME_MAP = {
        FOG: "fog",
        SDF: "sdf",
    }


class VolumeTypeEnumField(
    EnumField[VolumeTypeEnumAttrOperator, VolumeTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeTypeEnumAttrOperator
    PLUG_CLS = VolumeTypeEnumPlugOperator


class _GeneratedAiVolumeSampleFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiVolumeSampleFloat"

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

    volumeType = VolumeTypeEnumField(default_value=0)
    volume_type = volumeType

    sdfOffset = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    sdf_offset = sdfOffset

    sdfBlend = FloatField(default_value=0.0)
    sdf_blend = sdfBlend

    sdfInvert = BoolField(default_value=False)
    sdf_invert = sdfInvert

    inputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    input_min = inputMin

    inputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    input_max = inputMax

    contrast = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)

    contrastPivot = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    contrast_pivot = contrastPivot

    bias = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    gain = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)

    outputMin = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    output_min = outputMin

    outputMax = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    output_max = outputMax

    clampMin = BoolField(default_value=False)
    clamp_min = clampMin

    clampMax = BoolField(default_value=False)
    clamp_max = clampMax
