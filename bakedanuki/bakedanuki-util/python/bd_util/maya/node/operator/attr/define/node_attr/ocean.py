# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.float import FloatField
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


class WaveHeight_InterpEnumPlugOperator(
    EnumPlugOperator["WaveHeight_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveHeight_InterpEnumAttrOperator(
    EnumAttrOperator[WaveHeight_InterpEnumPlugOperator]
):
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
    EnumField[
        WaveHeight_InterpEnumAttrOperator, WaveHeight_InterpEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = WaveHeight_InterpEnumAttrOperator
    PLUG_CLS = WaveHeight_InterpEnumPlugOperator


class WaveTurbulence_InterpEnumPlugOperator(
    EnumPlugOperator["WaveTurbulence_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WaveTurbulence_InterpEnumAttrOperator(
    EnumAttrOperator[WaveTurbulence_InterpEnumPlugOperator]
):
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
    EnumField[
        WaveTurbulence_InterpEnumAttrOperator,
        WaveTurbulence_InterpEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulence_InterpEnumAttrOperator
    PLUG_CLS = WaveTurbulence_InterpEnumPlugOperator


class WavePeaking_InterpEnumPlugOperator(
    EnumPlugOperator["WavePeaking_InterpEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class WavePeaking_InterpEnumAttrOperator(
    EnumAttrOperator[WavePeaking_InterpEnumPlugOperator]
):
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
    EnumField[
        WavePeaking_InterpEnumAttrOperator, WavePeaking_InterpEnumPlugOperator
    ]
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

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordAttrOperator(Float2CompoundBaseAttrOperator[UvCoordPlugOperator]):
    __slots__ = ()

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvCoordField(
    Float2CompoundBaseField[UvCoordAttrOperator, UvCoordPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvCoordAttrOperator
    PLUG_CLS = UvCoordPlugOperator

    uCoord = FloatField(default_value=0.0)
    u = uCoord

    vCoord = FloatField(default_value=0.0)
    v = vCoord


class UvFilterSizePlugOperator(
    Float2CompoundBasePlugOperator["UvFilterSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvFilterSizeX", "fsx"),
        ("uvFilterSizeY", "fsy"),
    )

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeAttrOperator(
    Float2CompoundBaseAttrOperator[UvFilterSizePlugOperator]
):
    __slots__ = ()

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
    fsy = uvFilterSizeY


class UvFilterSizeField(
    Float2CompoundBaseField[UvFilterSizeAttrOperator, UvFilterSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvFilterSizeAttrOperator
    PLUG_CLS = UvFilterSizePlugOperator

    uvFilterSizeX = FloatField(default_value=0.0)
    fsx = uvFilterSizeX

    uvFilterSizeY = FloatField(default_value=0.0)
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

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainAttrOperator(
    Float3CompoundBaseAttrOperator[ColorGainPlugOperator]
):
    __slots__ = ()

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgb = colorGainB


class ColorGainField(
    Float3CompoundBaseField[ColorGainAttrOperator, ColorGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorGainAttrOperator
    PLUG_CLS = ColorGainPlugOperator

    colorGainR = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgr = colorGainR

    colorGainG = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
    cgg = colorGainG

    colorGainB = FloatField(default_value=1.0, min_value=0.0, max_value=2.0)
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

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ColorOffsetPlugOperator]
):
    __slots__ = ()

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cob = colorOffsetB


class ColorOffsetField(
    Float3CompoundBaseField[ColorOffsetAttrOperator, ColorOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorOffsetAttrOperator
    PLUG_CLS = ColorOffsetPlugOperator

    colorOffsetR = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cor = colorOffsetR

    colorOffsetG = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
    cog = colorOffsetG

    colorOffsetB = FloatField(default_value=0.0, min_value=0.0, max_value=2.0)
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

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorAttrOperator(
    Float3CompoundBaseAttrOperator[DefaultColorPlugOperator]
):
    __slots__ = ()

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcb = defaultColorB


class DefaultColorField(
    Float3CompoundBaseField[DefaultColorAttrOperator, DefaultColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DefaultColorAttrOperator
    PLUG_CLS = DefaultColorPlugOperator

    defaultColorR = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcr = defaultColorR

    defaultColorG = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    dcg = defaultColorG

    defaultColorB = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
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

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    ocb = outColorB


class WindUVPlugOperator(Float2CompoundBasePlugOperator["WindUVAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("windU", "wiu"),
        ("windV", "wiv"),
    )

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WindUVAttrOperator(Float2CompoundBaseAttrOperator[WindUVPlugOperator]):
    __slots__ = ()

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WindUVField(
    Float2CompoundBaseField[WindUVAttrOperator, WindUVPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WindUVAttrOperator
    PLUG_CLS = WindUVPlugOperator

    windU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    wiu = windU

    windV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    wiv = windV


class WaveHeightPlugOperator(CompoundPlugOperator["WaveHeightAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("waveHeight_Position", "whp"),
        ("waveHeight_FloatValue", "whfv"),
        ("waveHeight_Interp", "whi"),
    )

    waveHeight_Position = FloatField(default_value=0.0)
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField(default_value=0.0)
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField(default_value=0)
    whi = waveHeight_Interp


class WaveHeightAttrOperator(CompoundAttrOperator[WaveHeightPlugOperator]):
    __slots__ = ()

    waveHeight_Position = FloatField(default_value=0.0)
    whp = waveHeight_Position

    waveHeight_FloatValue = FloatField(default_value=0.0)
    whfv = waveHeight_FloatValue

    waveHeight_Interp = WaveHeight_InterpEnumField(default_value=0)
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

    waveTurbulence_Position = FloatField(default_value=0.0)
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField(default_value=0.0)
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField(default_value=0)
    wtbi = waveTurbulence_Interp


class WaveTurbulenceAttrOperator(
    CompoundAttrOperator[WaveTurbulencePlugOperator]
):
    __slots__ = ()

    waveTurbulence_Position = FloatField(default_value=0.0)
    wtbp = waveTurbulence_Position

    waveTurbulence_FloatValue = FloatField(default_value=0.0)
    wtbfv = waveTurbulence_FloatValue

    waveTurbulence_Interp = WaveTurbulence_InterpEnumField(default_value=0)
    wtbi = waveTurbulence_Interp


class WaveTurbulenceField(
    CompoundField[WaveTurbulenceAttrOperator, WaveTurbulencePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WaveTurbulenceAttrOperator
    PLUG_CLS = WaveTurbulencePlugOperator


class WavePeakingPlugOperator(CompoundPlugOperator["WavePeakingAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("wavePeaking_Position", "wpp"),
        ("wavePeaking_FloatValue", "wpfv"),
        ("wavePeaking_Interp", "wpi"),
    )

    wavePeaking_Position = FloatField(default_value=0.0)
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField(default_value=0.0)
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField(default_value=0)
    wpi = wavePeaking_Interp


class WavePeakingAttrOperator(CompoundAttrOperator[WavePeakingPlugOperator]):
    __slots__ = ()

    wavePeaking_Position = FloatField(default_value=0.0)
    wpp = wavePeaking_Position

    wavePeaking_FloatValue = FloatField(default_value=0.0)
    wpfv = wavePeaking_FloatValue

    wavePeaking_Interp = WavePeaking_InterpEnumField(default_value=0)
    wpi = wavePeaking_Interp


class WavePeakingField(
    CompoundField[WavePeakingAttrOperator, WavePeakingPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WavePeakingAttrOperator
    PLUG_CLS = WavePeakingPlugOperator
