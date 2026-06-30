# coding: utf-8

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


class GapColorPlugOperator(
    Float3CompoundBasePlugOperator["GapColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gapColorR", "gcr"),
        ("gapColorG", "gcg"),
        ("gapColorB", "gcb"),
    )

    gapColorR = FloatField()
    gcr = gapColorR

    gapColorG = FloatField()
    gcg = gapColorG

    gapColorB = FloatField()
    gcb = gapColorB


class GapColorAttrOperator(
    Float3CompoundBaseAttrOperator[GapColorPlugOperator]
):
    __slots__ = ()

    gapColorR = FloatField()
    gcr = gapColorR

    gapColorG = FloatField()
    gcg = gapColorG

    gapColorB = FloatField()
    gcb = gapColorB


class GapColorField(
    Float3CompoundBaseField[GapColorAttrOperator, GapColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GapColorAttrOperator
    PLUG_CLS = GapColorPlugOperator

    gapColorR = FloatField()
    gcr = gapColorR

    gapColorG = FloatField()
    gcg = gapColorG

    gapColorB = FloatField()
    gcb = gapColorB


class UColorPlugOperator(
    Float3CompoundBasePlugOperator["UColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uColorR", "ucr"),
        ("uColorG", "ucg"),
        ("uColorB", "ucb"),
    )

    uColorR = FloatField()
    ucr = uColorR

    uColorG = FloatField()
    ucg = uColorG

    uColorB = FloatField()
    ucb = uColorB


class UColorAttrOperator(
    Float3CompoundBaseAttrOperator[UColorPlugOperator]
):
    __slots__ = ()

    uColorR = FloatField()
    ucr = uColorR

    uColorG = FloatField()
    ucg = uColorG

    uColorB = FloatField()
    ucb = uColorB


class UColorField(
    Float3CompoundBaseField[UColorAttrOperator, UColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UColorAttrOperator
    PLUG_CLS = UColorPlugOperator

    uColorR = FloatField()
    ucr = uColorR

    uColorG = FloatField()
    ucg = uColorG

    uColorB = FloatField()
    ucb = uColorB


class VColorPlugOperator(
    Float3CompoundBasePlugOperator["VColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vColorR", "vcr"),
        ("vColorG", "vcg"),
        ("vColorB", "vcb"),
    )

    vColorR = FloatField()
    vcr = vColorR

    vColorG = FloatField()
    vcg = vColorG

    vColorB = FloatField()
    vcb = vColorB


class VColorAttrOperator(
    Float3CompoundBaseAttrOperator[VColorPlugOperator]
):
    __slots__ = ()

    vColorR = FloatField()
    vcr = vColorR

    vColorG = FloatField()
    vcg = vColorG

    vColorB = FloatField()
    vcb = vColorB


class VColorField(
    Float3CompoundBaseField[VColorAttrOperator, VColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VColorAttrOperator
    PLUG_CLS = VColorPlugOperator

    vColorR = FloatField()
    vcr = vColorR

    vColorG = FloatField()
    vcg = vColorG

    vColorB = FloatField()
    vcb = vColorB
