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


class Out_directionPlugOperator(
    Float3CompoundBasePlugOperator["Out_directionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_directionX", "out_directionx"),
        ("out_directionY", "out_directiony"),
        ("out_directionZ", "out_directionz"),
    )

    out_directionX = FloatField(default_value=0.0, writable=False)
    out_directionx = out_directionX

    out_directionY = FloatField(default_value=0.0, writable=False)
    out_directiony = out_directionY

    out_directionZ = FloatField(default_value=0.0, writable=False)
    out_directionz = out_directionZ


class Out_directionAttrOperator(
    Float3CompoundBaseAttrOperator[Out_directionPlugOperator]
):
    __slots__ = ()

    out_directionX = FloatField(default_value=0.0, writable=False)
    out_directionx = out_directionX

    out_directionY = FloatField(default_value=0.0, writable=False)
    out_directiony = out_directionY

    out_directionZ = FloatField(default_value=0.0, writable=False)
    out_directionz = out_directionZ


class Out_directionField(
    Float3CompoundBaseField[
        Out_directionAttrOperator, Out_directionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Out_directionAttrOperator
    PLUG_CLS = Out_directionPlugOperator

    out_directionX = FloatField(default_value=0.0, writable=False)
    out_directionx = out_directionX

    out_directionY = FloatField(default_value=0.0, writable=False)
    out_directiony = out_directionY

    out_directionZ = FloatField(default_value=0.0, writable=False)
    out_directionz = out_directionZ


class NearColorPlugOperator(
    Float3CompoundBasePlugOperator["NearColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("nearColorR", "near_colorr"),
        ("nearColorG", "near_colorg"),
        ("nearColorB", "near_colorb"),
    )

    nearColorR = FloatField(default_value=0.0)
    near_colorr = nearColorR

    nearColorG = FloatField(default_value=0.0)
    near_colorg = nearColorG

    nearColorB = FloatField(default_value=0.0)
    near_colorb = nearColorB


class NearColorAttrOperator(
    Float3CompoundBaseAttrOperator[NearColorPlugOperator]
):
    __slots__ = ()

    nearColorR = FloatField(default_value=0.0)
    near_colorr = nearColorR

    nearColorG = FloatField(default_value=0.0)
    near_colorg = nearColorG

    nearColorB = FloatField(default_value=0.0)
    near_colorb = nearColorB


class NearColorField(
    Float3CompoundBaseField[NearColorAttrOperator, NearColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NearColorAttrOperator
    PLUG_CLS = NearColorPlugOperator

    nearColorR = FloatField(default_value=0.0)
    near_colorr = nearColorR

    nearColorG = FloatField(default_value=0.0)
    near_colorg = nearColorG

    nearColorB = FloatField(default_value=0.0)
    near_colorb = nearColorB


class FarColorPlugOperator(
    Float3CompoundBasePlugOperator["FarColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("farColorR", "far_colorr"),
        ("farColorG", "far_colorg"),
        ("farColorB", "far_colorb"),
    )

    farColorR = FloatField(default_value=1.0)
    far_colorr = farColorR

    farColorG = FloatField(default_value=1.0)
    far_colorg = farColorG

    farColorB = FloatField(default_value=1.0)
    far_colorb = farColorB


class FarColorAttrOperator(
    Float3CompoundBaseAttrOperator[FarColorPlugOperator]
):
    __slots__ = ()

    farColorR = FloatField(default_value=1.0)
    far_colorr = farColorR

    farColorG = FloatField(default_value=1.0)
    far_colorg = farColorG

    farColorB = FloatField(default_value=1.0)
    far_colorb = farColorB


class FarColorField(
    Float3CompoundBaseField[FarColorAttrOperator, FarColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FarColorAttrOperator
    PLUG_CLS = FarColorPlugOperator

    farColorR = FloatField(default_value=1.0)
    far_colorr = farColorR

    farColorG = FloatField(default_value=1.0)
    far_colorg = farColorG

    farColorB = FloatField(default_value=1.0)
    far_colorb = farColorB
