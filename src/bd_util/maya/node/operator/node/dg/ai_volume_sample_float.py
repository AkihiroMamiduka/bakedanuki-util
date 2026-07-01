# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_volume_sample_float import (
    OutTransparencyField,
    PositionOffsetField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
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


class AiVolumeSampleFloat(DG):
    __slots__ = ()

    NODE_TYPE = "aiVolumeSampleFloat"

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

    volumeType = VolumeTypeEnumField()
    volume_type = volumeType

    sdfOffset = FloatField()
    sdf_offset = sdfOffset

    sdfBlend = FloatField()
    sdf_blend = sdfBlend

    sdfInvert = BoolField()
    sdf_invert = sdfInvert

    inputMin = FloatField()
    input_min = inputMin

    inputMax = FloatField()
    input_max = inputMax

    contrast = FloatField()

    contrastPivot = FloatField()
    contrast_pivot = contrastPivot

    bias = FloatField()

    gain = FloatField()

    outputMin = FloatField()
    output_min = outputMin

    outputMax = FloatField()
    output_max = outputMax

    clampMin = BoolField()
    clamp_min = clampMin

    clampMax = BoolField()
    clamp_max = clampMax
