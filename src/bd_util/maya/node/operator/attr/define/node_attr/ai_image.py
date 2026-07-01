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


class OutColorPlugOperator(
    Float3CompoundBasePlugOperator["OutColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColorR", "outr"),
        ("outColorG", "outg"),
        ("outColorB", "outb"),
    )

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorAttrOperator(
    Float3CompoundBaseAttrOperator[OutColorPlugOperator]
):
    __slots__ = ()

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
    outb = outColorB


class OutColorField(
    Float3CompoundBaseField[OutColorAttrOperator, OutColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorAttrOperator
    PLUG_CLS = OutColorPlugOperator

    outColorR = FloatField()
    outr = outColorR

    outColorG = FloatField()
    outg = outColorG

    outColorB = FloatField()
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

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyAttrOperator(
    Float3CompoundBaseAttrOperator[OutTransparencyPlugOperator]
):
    __slots__ = ()

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class OutTransparencyField(
    Float3CompoundBaseField[OutTransparencyAttrOperator, OutTransparencyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutTransparencyAttrOperator
    PLUG_CLS = OutTransparencyPlugOperator

    outTransparencyR = FloatField()
    otr = outTransparencyR

    outTransparencyG = FloatField()
    otg = outTransparencyG

    outTransparencyB = FloatField()
    otb = outTransparencyB


class UvcoordsPlugOperator(
    Float2CompoundBasePlugOperator["UvcoordsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("uvcoordsX", "uvcoordsx"),
        ("uvcoordsY", "uvcoordsy"),
    )

    uvcoordsX = FloatField()
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField()
    uvcoordsy = uvcoordsY


class UvcoordsAttrOperator(
    Float2CompoundBaseAttrOperator[UvcoordsPlugOperator]
):
    __slots__ = ()

    uvcoordsX = FloatField()
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField()
    uvcoordsy = uvcoordsY


class UvcoordsField(
    Float2CompoundBaseField[UvcoordsAttrOperator, UvcoordsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UvcoordsAttrOperator
    PLUG_CLS = UvcoordsPlugOperator

    uvcoordsX = FloatField()
    uvcoordsx = uvcoordsX

    uvcoordsY = FloatField()
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

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class MultiplyAttrOperator(
    Float3CompoundBaseAttrOperator[MultiplyPlugOperator]
):
    __slots__ = ()

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class MultiplyField(
    Float3CompoundBaseField[MultiplyAttrOperator, MultiplyPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiplyAttrOperator
    PLUG_CLS = MultiplyPlugOperator

    multiplyR = FloatField()
    multiplyr = multiplyR

    multiplyG = FloatField()
    multiplyg = multiplyG

    multiplyB = FloatField()
    multiplyb = multiplyB


class OffsetPlugOperator(
    Float3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetR", "offsetr"),
        ("offsetG", "offsetg"),
        ("offsetB", "offsetb"),
    )

    offsetR = FloatField()
    offsetr = offsetR

    offsetG = FloatField()
    offsetg = offsetG

    offsetB = FloatField()
    offsetb = offsetB


class OffsetAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetR = FloatField()
    offsetr = offsetR

    offsetG = FloatField()
    offsetg = offsetG

    offsetB = FloatField()
    offsetb = offsetB


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetR = FloatField()
    offsetr = offsetR

    offsetG = FloatField()
    offsetg = offsetG

    offsetB = FloatField()
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

    missingTextureColorR = FloatField()
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField()
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField()
    missing_texture_colorb = missingTextureColorB


class MissingTextureColorAttrOperator(
    Float3CompoundBaseAttrOperator[MissingTextureColorPlugOperator]
):
    __slots__ = ()

    missingTextureColorR = FloatField()
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField()
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField()
    missing_texture_colorb = missingTextureColorB


class MissingTextureColorField(
    Float3CompoundBaseField[MissingTextureColorAttrOperator, MissingTextureColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MissingTextureColorAttrOperator
    PLUG_CLS = MissingTextureColorPlugOperator

    missingTextureColorR = FloatField()
    missing_texture_colorr = missingTextureColorR

    missingTextureColorG = FloatField()
    missing_texture_colorg = missingTextureColorG

    missingTextureColorB = FloatField()
    missing_texture_colorb = missingTextureColorB
