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


class RippleOriginPlugOperator(
    Float2CompoundBasePlugOperator["RippleOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rippleOriginU", "rcu"),
        ("rippleOriginV", "rcv"),
    )

    rippleOriginU = FloatField()
    rcu = rippleOriginU

    rippleOriginV = FloatField()
    rcv = rippleOriginV


class RippleOriginAttrOperator(
    Float2CompoundBaseAttrOperator[RippleOriginPlugOperator]
):
    __slots__ = ()

    rippleOriginU = FloatField()
    rcu = rippleOriginU

    rippleOriginV = FloatField()
    rcv = rippleOriginV


class RippleOriginField(
    Float2CompoundBaseField[RippleOriginAttrOperator, RippleOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RippleOriginAttrOperator
    PLUG_CLS = RippleOriginPlugOperator

    rippleOriginU = FloatField()
    rcu = rippleOriginU

    rippleOriginV = FloatField()
    rcv = rippleOriginV


class BoxMinPlugOperator(
    Float2CompoundBasePlugOperator["BoxMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boxMinU", "bu1"),
        ("boxMinV", "bv1"),
    )

    boxMinU = FloatField()
    bu1 = boxMinU

    boxMinV = FloatField()
    bv1 = boxMinV


class BoxMinAttrOperator(
    Float2CompoundBaseAttrOperator[BoxMinPlugOperator]
):
    __slots__ = ()

    boxMinU = FloatField()
    bu1 = boxMinU

    boxMinV = FloatField()
    bv1 = boxMinV


class BoxMinField(
    Float2CompoundBaseField[BoxMinAttrOperator, BoxMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoxMinAttrOperator
    PLUG_CLS = BoxMinPlugOperator

    boxMinU = FloatField()
    bu1 = boxMinU

    boxMinV = FloatField()
    bv1 = boxMinV


class BoxMaxPlugOperator(
    Float2CompoundBasePlugOperator["BoxMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boxMaxU", "bu2"),
        ("boxMaxV", "bv2"),
    )

    boxMaxU = FloatField()
    bu2 = boxMaxU

    boxMaxV = FloatField()
    bv2 = boxMaxV


class BoxMaxAttrOperator(
    Float2CompoundBaseAttrOperator[BoxMaxPlugOperator]
):
    __slots__ = ()

    boxMaxU = FloatField()
    bu2 = boxMaxU

    boxMaxV = FloatField()
    bv2 = boxMaxV


class BoxMaxField(
    Float2CompoundBaseField[BoxMaxAttrOperator, BoxMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoxMaxAttrOperator
    PLUG_CLS = BoxMaxPlugOperator

    boxMaxU = FloatField()
    bu2 = boxMaxU

    boxMaxV = FloatField()
    bv2 = boxMaxV
