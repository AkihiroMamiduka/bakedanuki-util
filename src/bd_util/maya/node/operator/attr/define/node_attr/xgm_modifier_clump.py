# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ClumpScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class ClumpScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class ClumpScale_InterpEnumField(
    EnumField[ClumpScale_InterpEnumAttrOperator, ClumpScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpScale_InterpEnumAttrOperator
    PLUG_CLS = ClumpScale_InterpEnumPlugOperator


class FlatnessScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class FlatnessScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class FlatnessScale_InterpEnumField(
    EnumField[FlatnessScale_InterpEnumAttrOperator, FlatnessScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlatnessScale_InterpEnumAttrOperator
    PLUG_CLS = FlatnessScale_InterpEnumPlugOperator


class OffsetScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class OffsetScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class OffsetScale_InterpEnumField(
    EnumField[OffsetScale_InterpEnumAttrOperator, OffsetScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetScale_InterpEnumAttrOperator
    PLUG_CLS = OffsetScale_InterpEnumPlugOperator


class CurlScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CurlScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CurlScale_InterpEnumField(
    EnumField[CurlScale_InterpEnumAttrOperator, CurlScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurlScale_InterpEnumAttrOperator
    PLUG_CLS = CurlScale_InterpEnumPlugOperator


class CopyScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class CopyScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class CopyScale_InterpEnumField(
    EnumField[CopyScale_InterpEnumAttrOperator, CopyScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CopyScale_InterpEnumAttrOperator
    PLUG_CLS = CopyScale_InterpEnumPlugOperator


class NoiseScale_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class NoiseScale_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class NoiseScale_InterpEnumField(
    EnumField[NoiseScale_InterpEnumAttrOperator, NoiseScale_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseScale_InterpEnumAttrOperator
    PLUG_CLS = NoiseScale_InterpEnumPlugOperator


class ClumpScalePlugOperator(
    CompoundPlugOperator["ClumpScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clumpScale_Position", "csp"),
        ("clumpScale_FloatValue", "csfv"),
        ("clumpScale_Interp", "csi"),
    )

    clumpScale_Position = FloatField()
    csp = clumpScale_Position

    clumpScale_FloatValue = FloatField()
    csfv = clumpScale_FloatValue

    clumpScale_Interp = ClumpScale_InterpEnumField()
    csi = clumpScale_Interp


class ClumpScaleAttrOperator(
    CompoundAttrOperator[ClumpScalePlugOperator]
):
    __slots__ = ()

    clumpScale_Position = FloatField()
    csp = clumpScale_Position

    clumpScale_FloatValue = FloatField()
    csfv = clumpScale_FloatValue

    clumpScale_Interp = ClumpScale_InterpEnumField()
    csi = clumpScale_Interp


class ClumpScaleField(
    CompoundField[ClumpScaleAttrOperator, ClumpScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClumpScaleAttrOperator
    PLUG_CLS = ClumpScalePlugOperator


class CustomControlMapPlugOperator(
    Float3CompoundBasePlugOperator["CustomControlMapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("customControlMapR", "ccmr"),
        ("customControlMapG", "ccmg"),
        ("customControlMapB", "ccmb"),
    )

    customControlMapR = FloatField()
    ccmr = customControlMapR

    customControlMapG = FloatField()
    ccmg = customControlMapG

    customControlMapB = FloatField()
    ccmb = customControlMapB


class CustomControlMapAttrOperator(
    Float3CompoundBaseAttrOperator[CustomControlMapPlugOperator]
):
    __slots__ = ()

    customControlMapR = FloatField()
    ccmr = customControlMapR

    customControlMapG = FloatField()
    ccmg = customControlMapG

    customControlMapB = FloatField()
    ccmb = customControlMapB


class CustomControlMapField(
    Float3CompoundBaseField[CustomControlMapAttrOperator, CustomControlMapPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CustomControlMapAttrOperator
    PLUG_CLS = CustomControlMapPlugOperator

    customControlMapR = FloatField()
    ccmr = customControlMapR

    customControlMapG = FloatField()
    ccmg = customControlMapG

    customControlMapB = FloatField()
    ccmb = customControlMapB


class ControlMaskPlugOperator(
    Float3CompoundBasePlugOperator["ControlMaskAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("controlMaskR", "cmsr"),
        ("controlMaskG", "cmsg"),
        ("controlMaskB", "cmsb"),
    )

    controlMaskR = FloatField()
    cmsr = controlMaskR

    controlMaskG = FloatField()
    cmsg = controlMaskG

    controlMaskB = FloatField()
    cmsb = controlMaskB


class ControlMaskAttrOperator(
    Float3CompoundBaseAttrOperator[ControlMaskPlugOperator]
):
    __slots__ = ()

    controlMaskR = FloatField()
    cmsr = controlMaskR

    controlMaskG = FloatField()
    cmsg = controlMaskG

    controlMaskB = FloatField()
    cmsb = controlMaskB


class ControlMaskField(
    Float3CompoundBaseField[ControlMaskAttrOperator, ControlMaskPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ControlMaskAttrOperator
    PLUG_CLS = ControlMaskPlugOperator

    controlMaskR = FloatField()
    cmsr = controlMaskR

    controlMaskG = FloatField()
    cmsg = controlMaskG

    controlMaskB = FloatField()
    cmsb = controlMaskB


class FlatnessScalePlugOperator(
    CompoundPlugOperator["FlatnessScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("flatnessScale_Position", "flsp"),
        ("flatnessScale_FloatValue", "flsfv"),
        ("flatnessScale_Interp", "flsi"),
    )

    flatnessScale_Position = FloatField()
    flsp = flatnessScale_Position

    flatnessScale_FloatValue = FloatField()
    flsfv = flatnessScale_FloatValue

    flatnessScale_Interp = FlatnessScale_InterpEnumField()
    flsi = flatnessScale_Interp


class FlatnessScaleAttrOperator(
    CompoundAttrOperator[FlatnessScalePlugOperator]
):
    __slots__ = ()

    flatnessScale_Position = FloatField()
    flsp = flatnessScale_Position

    flatnessScale_FloatValue = FloatField()
    flsfv = flatnessScale_FloatValue

    flatnessScale_Interp = FlatnessScale_InterpEnumField()
    flsi = flatnessScale_Interp


class FlatnessScaleField(
    CompoundField[FlatnessScaleAttrOperator, FlatnessScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FlatnessScaleAttrOperator
    PLUG_CLS = FlatnessScalePlugOperator


class OffsetScalePlugOperator(
    CompoundPlugOperator["OffsetScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetScale_Position", "ofsp"),
        ("offsetScale_FloatValue", "ofsfv"),
        ("offsetScale_Interp", "ofsi"),
    )

    offsetScale_Position = FloatField()
    ofsp = offsetScale_Position

    offsetScale_FloatValue = FloatField()
    ofsfv = offsetScale_FloatValue

    offsetScale_Interp = OffsetScale_InterpEnumField()
    ofsi = offsetScale_Interp


class OffsetScaleAttrOperator(
    CompoundAttrOperator[OffsetScalePlugOperator]
):
    __slots__ = ()

    offsetScale_Position = FloatField()
    ofsp = offsetScale_Position

    offsetScale_FloatValue = FloatField()
    ofsfv = offsetScale_FloatValue

    offsetScale_Interp = OffsetScale_InterpEnumField()
    ofsi = offsetScale_Interp


class OffsetScaleField(
    CompoundField[OffsetScaleAttrOperator, OffsetScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetScaleAttrOperator
    PLUG_CLS = OffsetScalePlugOperator


class CurlScalePlugOperator(
    CompoundPlugOperator["CurlScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("curlScale_Position", "cusp"),
        ("curlScale_FloatValue", "cusfv"),
        ("curlScale_Interp", "cusi"),
    )

    curlScale_Position = FloatField()
    cusp = curlScale_Position

    curlScale_FloatValue = FloatField()
    cusfv = curlScale_FloatValue

    curlScale_Interp = CurlScale_InterpEnumField()
    cusi = curlScale_Interp


class CurlScaleAttrOperator(
    CompoundAttrOperator[CurlScalePlugOperator]
):
    __slots__ = ()

    curlScale_Position = FloatField()
    cusp = curlScale_Position

    curlScale_FloatValue = FloatField()
    cusfv = curlScale_FloatValue

    curlScale_Interp = CurlScale_InterpEnumField()
    cusi = curlScale_Interp


class CurlScaleField(
    CompoundField[CurlScaleAttrOperator, CurlScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CurlScaleAttrOperator
    PLUG_CLS = CurlScalePlugOperator


class CopyScalePlugOperator(
    CompoundPlugOperator["CopyScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("copyScale_Position", "cosp"),
        ("copyScale_FloatValue", "cosfv"),
        ("copyScale_Interp", "cosi"),
    )

    copyScale_Position = FloatField()
    cosp = copyScale_Position

    copyScale_FloatValue = FloatField()
    cosfv = copyScale_FloatValue

    copyScale_Interp = CopyScale_InterpEnumField()
    cosi = copyScale_Interp


class CopyScaleAttrOperator(
    CompoundAttrOperator[CopyScalePlugOperator]
):
    __slots__ = ()

    copyScale_Position = FloatField()
    cosp = copyScale_Position

    copyScale_FloatValue = FloatField()
    cosfv = copyScale_FloatValue

    copyScale_Interp = CopyScale_InterpEnumField()
    cosi = copyScale_Interp


class CopyScaleField(
    CompoundField[CopyScaleAttrOperator, CopyScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CopyScaleAttrOperator
    PLUG_CLS = CopyScalePlugOperator


class NoiseScalePlugOperator(
    CompoundPlugOperator["NoiseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("noiseScale_Position", "nosp"),
        ("noiseScale_FloatValue", "nosfv"),
        ("noiseScale_Interp", "nosi"),
    )

    noiseScale_Position = FloatField()
    nosp = noiseScale_Position

    noiseScale_FloatValue = FloatField()
    nosfv = noiseScale_FloatValue

    noiseScale_Interp = NoiseScale_InterpEnumField()
    nosi = noiseScale_Interp


class NoiseScaleAttrOperator(
    CompoundAttrOperator[NoiseScalePlugOperator]
):
    __slots__ = ()

    noiseScale_Position = FloatField()
    nosp = noiseScale_Position

    noiseScale_FloatValue = FloatField()
    nosfv = noiseScale_FloatValue

    noiseScale_Interp = NoiseScale_InterpEnumField()
    nosi = noiseScale_Interp


class NoiseScaleField(
    CompoundField[NoiseScaleAttrOperator, NoiseScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NoiseScaleAttrOperator
    PLUG_CLS = NoiseScalePlugOperator
