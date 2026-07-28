# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
    Float2CompoundBaseAttrOperator,
    Float2CompoundBasePlugOperator,
    Float2CompoundBaseField,
)


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField(default_value=0.0, writable=False)
    outr = outColorR

    outColorG = FloatField(default_value=0.0, writable=False)
    outg = outColorG

    outColorB = FloatField(default_value=0.0, writable=False)
    outb = outColorB


class OutTransparencyPlugOperator(
    Float3CompoundBasePlugOperator["OutTransparencyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outTransparencyR", "otr"),
        ("outTransparencyG", "otg"),
        ("outTransparencyB", "otb"),
    )

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[
        OutTransparencyAttrOperator, OutTransparencyPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField(default_value=0.0, writable=False)
    otr = outTransparencyR

    outTransparencyG = FloatField(default_value=0.0, writable=False)
    otg = outTransparencyG

    outTransparencyB = FloatField(default_value=0.0, writable=False)
    otb = outTransparencyB


class UvcoordsPlugOperator(
    Float2CompoundBasePlugOperator["UvcoordsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvcoordsX", "uvcoordsx"),
        ("uvcoordsY", "uvcoordsy"),
    )

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY


class UvcoordsAttrOperator(
    Float2CompoundBaseAttrOperator[UvcoordsPlugOperator]
):
    __slots__ = ()

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY


class UvcoordsField(
    Float2CompoundBaseField[UvcoordsAttrOperator, UvcoordsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvcoordsAttrOperator
    PLUG_CLS = UvcoordsPlugOperator

    uvcoordsX = FloatField(default_value=0.0)
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField(default_value=0.0)
    uvcoordsy = uvcoordsY


class MultiplyPlugOperator(
    Float3CompoundBasePlugOperator["MultiplyAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("multiplyR", "multiplyr"),
        ("multiplyG", "multiplyg"),
        ("multiplyB", "multiplyb"),
    )

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiplyR = FloatField(default_value=1.0)
    multiplyr = multiplyR

    multiplyG = FloatField(default_value=1.0)
    multiplyg = multiplyG

    multiplyB = FloatField(default_value=1.0)
    multiplyb = multiplyB


class OffsetPlugOperator(Float3CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetR", "offsetr"),
        ("offsetG", "offsetg"),
        ("offsetB", "offsetb"),
    )

    offsetR = FloatField(default_value=0.0)
    offsetr = offsetR

    offsetG = FloatField(default_value=0.0)
    offsetg = offsetG

    offsetB = FloatField(default_value=0.0)
    offsetb = offsetB


class OffsetAttrOperator(Float3CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetR = FloatField(default_value=0.0)
    offsetr = offsetR

    offsetG = FloatField(default_value=0.0)
    offsetg = offsetG

    offsetB = FloatField(default_value=0.0)
    offsetb = offsetB


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetR = FloatField(default_value=0.0)
    offsetr = offsetR

    offsetG = FloatField(default_value=0.0)
    offsetg = offsetG

    offsetB = FloatField(default_value=0.0)
    offsetb = offsetB


class MissingTextureColorPlugOperator(
    Float3CompoundBasePlugOperator["MissingTextureColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("missingTextureColorR", "missing_texture_colorr"),
        ("missingTextureColorG", "missing_texture_colorg"),
        ("missingTextureColorB", "missing_texture_colorb"),
    )

    missingTextureColorR = FloatField(default_value=0.0)
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField(default_value=0.0)
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField(default_value=0.0)
    missing_texture_colorb = missingTextureColorB


class MissingTextureColorAttrOperator(
    Float3CompoundBaseAttrOperator[MissingTextureColorPlugOperator]
):
    __slots__ = ()

    missingTextureColorR = FloatField(default_value=0.0)
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField(default_value=0.0)
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField(default_value=0.0)
    missing_texture_colorb = missingTextureColorB


class MissingTextureColorField(
    Float3CompoundBaseField[
        MissingTextureColorAttrOperator, MissingTextureColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MissingTextureColorAttrOperator
    PLUG_CLS = MissingTextureColorPlugOperator

    missingTextureColorR = FloatField(default_value=0.0)
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField(default_value=0.0)
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField(default_value=0.0)
    missing_texture_colorb = missingTextureColorB
