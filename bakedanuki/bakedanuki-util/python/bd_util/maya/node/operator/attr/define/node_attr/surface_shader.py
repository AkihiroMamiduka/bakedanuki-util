# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "ocr"),
        ("outColorG", "ocg"),
        ("outColorB", "ocb"),
    )

    outColorR = FloatField(default_value=0.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0)
    ocb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0)
    ocb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0)
    ocr = outColorR

    outColorG = FloatField(default_value=0.0)
    ocg = outColorG

    outColorB = FloatField(default_value=0.0)
    ocb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0)
    otb = outTransparencyB


class OutMatteOpacityPlugOperator(
    Float3CompoundBasePlugOperator["OutMatteOpacityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outMatteOpacityR", "omor"),
        ("outMatteOpacityG", "omog"),
        ("outMatteOpacityB", "omob"),
    )

    outMatteOpacityR = FloatField(default_value=1.0)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0)
    omob = outMatteOpacityB


class OutMatteOpacityAttrOperator(
    Float3CompoundBaseAttrOperator[OutMatteOpacityPlugOperator]
):
    __slots__ = ()

    outMatteOpacityR = FloatField(default_value=1.0)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0)
    omob = outMatteOpacityB


class OutMatteOpacityField(
    Float3CompoundBaseField[
        OutMatteOpacityAttrOperator, OutMatteOpacityPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutMatteOpacityAttrOperator
    PLUG_CLS = OutMatteOpacityPlugOperator

    outMatteOpacityR = FloatField(default_value=1.0)
    omor = outMatteOpacityR

    outMatteOpacityG = FloatField(default_value=1.0)
    omog = outMatteOpacityG

    outMatteOpacityB = FloatField(default_value=1.0)
    omob = outMatteOpacityB


class OutGlowColorPlugOperator(
    Float3CompoundBasePlugOperator["OutGlowColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outGlowColorR", "ogr"),
        ("outGlowColorG", "ogg"),
        ("outGlowColorB", "ogb"),
    )

    outGlowColorR = FloatField(default_value=0.0)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0)
    ogb = outGlowColorB


class OutGlowColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutGlowColorPlugOperator]
):
    __slots__ = ()

    outGlowColorR = FloatField(default_value=0.0)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0)
    ogb = outGlowColorB


class OutGlowColorField(
    Float3CompoundBaseField[OutGlowColorAttrOperator, OutGlowColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutGlowColorAttrOperator
    PLUG_CLS = OutGlowColorPlugOperator

    outGlowColorR = FloatField(default_value=0.0)
    ogr = outGlowColorR

    outGlowColorG = FloatField(default_value=0.0)
    ogg = outGlowColorG

    outGlowColorB = FloatField(default_value=0.0)
    ogb = outGlowColorB
