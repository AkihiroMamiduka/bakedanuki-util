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


class PositionPlugOperator(
    Float3CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "positionx"),
        ("positionY", "positiony"),
        ("positionZ", "positionz"),
    )

    positionX = FloatField(default_value=0.0, writable=False)
    positionx = positionX

    positionY = FloatField(default_value=0.0, writable=False)
    positiony = positionY

    positionZ = FloatField(default_value=0.0, writable=False)
    positionz = positionZ


class PositionAttrOperator(
    Float3CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = FloatField(default_value=0.0, writable=False)
    positionx = positionX

    positionY = FloatField(default_value=0.0, writable=False)
    positiony = positionY

    positionZ = FloatField(default_value=0.0, writable=False)
    positionz = positionZ


class PositionField(
    Float3CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator

    positionX = FloatField(default_value=0.0, writable=False)
    positionx = positionX

    positionY = FloatField(default_value=0.0, writable=False)
    positiony = positionY

    positionZ = FloatField(default_value=0.0, writable=False)
    positionz = positionZ


class Out_rgbPlugOperator(
    Float3CompoundBasePlugOperator["Out_rgbAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_rgbR", "out_rgbr"),
        ("out_rgbG", "out_rgbg"),
        ("out_rgbB", "out_rgbb"),
    )

    out_rgbR = FloatField(default_value=0.0, writable=False)
    out_rgbr = out_rgbR

    out_rgbG = FloatField(default_value=0.0, writable=False)
    out_rgbg = out_rgbG

    out_rgbB = FloatField(default_value=0.0, writable=False)
    out_rgbb = out_rgbB


class Out_rgbAttrOperator(Float3CompoundBaseAttrOperator[Out_rgbPlugOperator]):
    __slots__ = ()

    out_rgbR = FloatField(default_value=0.0, writable=False)
    out_rgbr = out_rgbR

    out_rgbG = FloatField(default_value=0.0, writable=False)
    out_rgbg = out_rgbG

    out_rgbB = FloatField(default_value=0.0, writable=False)
    out_rgbb = out_rgbB


class Out_rgbField(
    Float3CompoundBaseField[Out_rgbAttrOperator, Out_rgbPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_rgbAttrOperator
    PLUG_CLS = Out_rgbPlugOperator

    out_rgbR = FloatField(default_value=0.0, writable=False)
    out_rgbr = out_rgbR

    out_rgbG = FloatField(default_value=0.0, writable=False)
    out_rgbg = out_rgbG

    out_rgbB = FloatField(default_value=0.0, writable=False)
    out_rgbb = out_rgbB


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


class Out_vecPlugOperator(
    Float3CompoundBasePlugOperator["Out_vecAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_vecX", "out_vecx"),
        ("out_vecY", "out_vecy"),
        ("out_vecZ", "out_vecz"),
    )

    out_vecX = FloatField(default_value=0.0, writable=False)
    out_vecx = out_vecX

    out_vecY = FloatField(default_value=0.0, writable=False)
    out_vecy = out_vecY

    out_vecZ = FloatField(default_value=0.0, writable=False)
    out_vecz = out_vecZ


class Out_vecAttrOperator(Float3CompoundBaseAttrOperator[Out_vecPlugOperator]):
    __slots__ = ()

    out_vecX = FloatField(default_value=0.0, writable=False)
    out_vecx = out_vecX

    out_vecY = FloatField(default_value=0.0, writable=False)
    out_vecy = out_vecY

    out_vecZ = FloatField(default_value=0.0, writable=False)
    out_vecz = out_vecZ


class Out_vecField(
    Float3CompoundBaseField[Out_vecAttrOperator, Out_vecPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_vecAttrOperator
    PLUG_CLS = Out_vecPlugOperator

    out_vecX = FloatField(default_value=0.0, writable=False)
    out_vecx = out_vecX

    out_vecY = FloatField(default_value=0.0, writable=False)
    out_vecy = out_vecY

    out_vecZ = FloatField(default_value=0.0, writable=False)
    out_vecz = out_vecZ


class Out_vec2PlugOperator(
    Float2CompoundBasePlugOperator["Out_vec2AttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_vec2X", "out_vec2x"),
        ("out_vec2Y", "out_vec2y"),
    )

    out_vec2X = FloatField(default_value=0.0, writable=False)
    out_vec2x = out_vec2X

    out_vec2Y = FloatField(default_value=0.0, writable=False)
    out_vec2y = out_vec2Y


class Out_vec2AttrOperator(
    Float2CompoundBaseAttrOperator[Out_vec2PlugOperator]
):
    __slots__ = ()

    out_vec2X = FloatField(default_value=0.0, writable=False)
    out_vec2x = out_vec2X

    out_vec2Y = FloatField(default_value=0.0, writable=False)
    out_vec2y = out_vec2Y


class Out_vec2Field(
    Float2CompoundBaseField[Out_vec2AttrOperator, Out_vec2PlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_vec2AttrOperator
    PLUG_CLS = Out_vec2PlugOperator

    out_vec2X = FloatField(default_value=0.0, writable=False)
    out_vec2x = out_vec2X

    out_vec2Y = FloatField(default_value=0.0, writable=False)
    out_vec2y = out_vec2Y


class QueryPositionPlugOperator(
    Float3CompoundBasePlugOperator["QueryPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("queryPositionX", "query_positionx"),
        ("queryPositionY", "query_positiony"),
        ("queryPositionZ", "query_positionz"),
    )

    queryPositionX = FloatField(default_value=0.0)
    query_positionx = queryPositionX

    queryPositionY = FloatField(default_value=0.0)
    query_positiony = queryPositionY

    queryPositionZ = FloatField(default_value=0.0)
    query_positionz = queryPositionZ


class QueryPositionAttrOperator(
    Float3CompoundBaseAttrOperator[QueryPositionPlugOperator]
):
    __slots__ = ()

    queryPositionX = FloatField(default_value=0.0)
    query_positionx = queryPositionX

    queryPositionY = FloatField(default_value=0.0)
    query_positiony = queryPositionY

    queryPositionZ = FloatField(default_value=0.0)
    query_positionz = queryPositionZ


class QueryPositionField(
    Float3CompoundBaseField[
        QueryPositionAttrOperator, QueryPositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = QueryPositionAttrOperator
    PLUG_CLS = QueryPositionPlugOperator

    queryPositionX = FloatField(default_value=0.0)
    query_positionx = queryPositionX

    queryPositionY = FloatField(default_value=0.0)
    query_positiony = queryPositionY

    queryPositionZ = FloatField(default_value=0.0)
    query_positionz = queryPositionZ
