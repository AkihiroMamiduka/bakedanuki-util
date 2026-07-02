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
from ..custom.at.scalar_compound.numeric_compound.float_compound.float2_compound._base import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class WaveHeight_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveHeight_InterpEnumAttrOperator(EnumAttrOperator):
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


class WaveHeight_InterpEnumField(
    EnumField[WaveHeight_InterpEnumAttrOperator, WaveHeight_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveHeight_InterpEnumAttrOperator
    PLUG_CLS = WaveHeight_InterpEnumPlugOperator


class WaveTurbulence_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveTurbulence_InterpEnumAttrOperator(EnumAttrOperator):
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


class WaveTurbulence_InterpEnumField(
    EnumField[WaveTurbulence_InterpEnumAttrOperator, WaveTurbulence_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulence_InterpEnumAttrOperator
    PLUG_CLS = WaveTurbulence_InterpEnumPlugOperator


class WavePeaking_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WavePeaking_InterpEnumAttrOperator(EnumAttrOperator):
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


class WavePeaking_InterpEnumField(
    EnumField[WavePeaking_InterpEnumAttrOperator, WavePeaking_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WavePeaking_InterpEnumAttrOperator
    PLUG_CLS = WavePeaking_InterpEnumPlugOperator


class UvCoordPlugOperator(
    Float2CompoundBasePlugOperator["UvCoordAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uCoord", "u"),
        ("vCoord", "v"),
    )

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordAttrOperator(
    Float2CompoundBaseAttrOperator[UvCoordPlugOperator]
):
    __slots__ = ()

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField()
    u = uCoord

    vCoord = FloatField()
    v = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField()
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField()
    fsy = uvFilterSizeY


class ColorGainPlugOperator(
    Float3CompoundBasePlugOperator["ColorGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorGainR", "cgr"),
        ("colorGainG", "cgg"),
        ("colorGainB", "cgb"),
    )

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField()
    cgr = colorGainR

    colorGainG = FloatField()
    cgg = colorGainG

    colorGainB = FloatField()
    cgb = colorGainB


class ColorOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ColorOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorOffsetR", "cor"),
        ("colorOffsetG", "cog"),
        ("colorOffsetB", "cob"),
    )

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField()
    cor = colorOffsetR

    colorOffsetG = FloatField()
    cog = colorOffsetG

    colorOffsetB = FloatField()
    cob = colorOffsetB


class DefaultColorPlugOperator(
    Float3CompoundBasePlugOperator["DefaultColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("defaultColorR", "dcr"),
        ("defaultColorG", "dcg"),
        ("defaultColorB", "dcb"),
    )

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField()
    dcr = defaultColorR

    defaultColorG = FloatField()
    dcg = defaultColorG

    defaultColorB = FloatField()
    dcb = defaultColorB


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    ocr = outColorR

    outColorG = FloatField()
    ocg = outColorG

    outColorB = FloatField()
    ocb = outColorB


class WindUVPlugOperator(
    Float2CompoundBasePlugOperator["WindUVAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("windU", "wiu"),
        ("windV", "wiv"),
    )

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WindUVAttrOperator(
    Float2CompoundBaseAttrOperator[WindUVPlugOperator]
):
    __slots__ = ()

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WindUVField(
    Float2CompoundBaseField[WindUVAttrOperator, WindUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindUVAttrOperator
    PLUG_CLS = WindUVPlugOperator

    windU = FloatField()
    wiu = windU

    windV = FloatField()
    wiv = windV


class WaveHeightPlugOperator(
    CompoundPlugOperator["WaveHeightAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveHeight_Position", "whp"),
        ("waveHeight_FloatValue", "whfv"),
        ("waveHeight_Interp", "whi"),
    )

    waveHeight_Position = FloatField()
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField()
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField()
    whi = waveHeight_Interp


class WaveHeightAttrOperator(
    CompoundAttrOperator[WaveHeightPlugOperator]
):
    __slots__ = ()

    waveHeight_Position = FloatField()
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField()
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField()
    whi = waveHeight_Interp


class WaveHeightField(
    CompoundField[WaveHeightAttrOperator, WaveHeightPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveHeightAttrOperator
    PLUG_CLS = WaveHeightPlugOperator


class WaveTurbulencePlugOperator(
    CompoundPlugOperator["WaveTurbulenceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveTurbulence_Position", "wtbp"),
        ("waveTurbulence_FloatValue", "wtbfv"),
        ("waveTurbulence_Interp", "wtbi"),
    )

    waveTurbulence_Position = FloatField()
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField()
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField()
    wtbi = waveTurbulence_Interp


class WaveTurbulenceAttrOperator(
    CompoundAttrOperator[WaveTurbulencePlugOperator]
):
    __slots__ = ()

    waveTurbulence_Position = FloatField()
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField()
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField()
    wtbi = waveTurbulence_Interp


class WaveTurbulenceField(
    CompoundField[WaveTurbulenceAttrOperator, WaveTurbulencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulenceAttrOperator
    PLUG_CLS = WaveTurbulencePlugOperator


class WavePeakingPlugOperator(
    CompoundPlugOperator["WavePeakingAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wavePeaking_Position", "wpp"),
        ("wavePeaking_FloatValue", "wpfv"),
        ("wavePeaking_Interp", "wpi"),
    )

    wavePeaking_Position = FloatField()
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField()
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField()
    wpi = wavePeaking_Interp


class WavePeakingAttrOperator(
    CompoundAttrOperator[WavePeakingPlugOperator]
):
    __slots__ = ()

    wavePeaking_Position = FloatField()
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField()
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField()
    wpi = wavePeaking_Interp


class WavePeakingField(
    CompoundField[WavePeakingAttrOperator, WavePeakingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WavePeakingAttrOperator
    PLUG_CLS = WavePeakingPlugOperator
