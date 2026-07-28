# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
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


class RippleOriginPlugOperator(
    Float2CompoundBasePlugOperator["RippleOriginAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rippleOriginU", "rcu"),
        ("rippleOriginV", "rcv"),
    )

    rippleOriginU = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcu = rippleOriginU

    rippleOriginV = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcv = rippleOriginV


class RippleOriginAttrOperator(
    Float2CompoundBaseAttrOperator[RippleOriginPlugOperator]
):
    __slots__ = ()

    rippleOriginU = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcu = rippleOriginU

    rippleOriginV = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcv = rippleOriginV


class RippleOriginField(
    Float2CompoundBaseField[RippleOriginAttrOperator, RippleOriginPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RippleOriginAttrOperator
    PLUG_CLS = RippleOriginPlugOperator

    rippleOriginU = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcu = rippleOriginU

    rippleOriginV = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    rcv = rippleOriginV


class BoxMinPlugOperator(Float2CompoundBasePlugOperator["BoxMinAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boxMinU", "bu1"),
        ("boxMinV", "bv1"),
    )

    boxMinU = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bu1 = boxMinU

    boxMinV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bv1 = boxMinV


class BoxMinAttrOperator(Float2CompoundBaseAttrOperator[BoxMinPlugOperator]):
    __slots__ = ()

    boxMinU = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bu1 = boxMinU

    boxMinV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bv1 = boxMinV


class BoxMinField(
    Float2CompoundBaseField[BoxMinAttrOperator, BoxMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoxMinAttrOperator
    PLUG_CLS = BoxMinPlugOperator

    boxMinU = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bu1 = boxMinU

    boxMinV = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    bv1 = boxMinV


class BoxMaxPlugOperator(Float2CompoundBasePlugOperator["BoxMaxAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boxMaxU", "bu2"),
        ("boxMaxV", "bv2"),
    )

    boxMaxU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bu2 = boxMaxU

    boxMaxV = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bv2 = boxMaxV


class BoxMaxAttrOperator(Float2CompoundBaseAttrOperator[BoxMaxPlugOperator]):
    __slots__ = ()

    boxMaxU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bu2 = boxMaxU

    boxMaxV = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bv2 = boxMaxV


class BoxMaxField(
    Float2CompoundBaseField[BoxMaxAttrOperator, BoxMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoxMaxAttrOperator
    PLUG_CLS = BoxMaxPlugOperator

    boxMaxU = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bu2 = boxMaxU

    boxMaxV = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)
    bv2 = boxMaxV
