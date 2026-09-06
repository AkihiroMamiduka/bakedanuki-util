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


class Out_line_uvPlugOperator(
    Float2CompoundBasePlugOperator["Out_line_uvAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("out_line_uvX", "out_line_uvx"),
        ("out_line_uvY", "out_line_uvy"),
    )

    out_line_uvX = FloatField(default_value=0.0, writable=False)
    out_line_uvx = out_line_uvX

    out_line_uvY = FloatField(default_value=0.0, writable=False)
    out_line_uvy = out_line_uvY


class Out_line_uvAttrOperator(
    Float2CompoundBaseAttrOperator[Out_line_uvPlugOperator]
):
    __slots__ = ()

    out_line_uvX = FloatField(default_value=0.0, writable=False)
    out_line_uvx = out_line_uvX

    out_line_uvY = FloatField(default_value=0.0, writable=False)
    out_line_uvy = out_line_uvY


class Out_line_uvField(
    Float2CompoundBaseField[Out_line_uvAttrOperator, Out_line_uvPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Out_line_uvAttrOperator
    PLUG_CLS = Out_line_uvPlugOperator

    out_line_uvX = FloatField(default_value=0.0, writable=False)
    out_line_uvx = out_line_uvX

    out_line_uvY = FloatField(default_value=0.0, writable=False)
    out_line_uvy = out_line_uvY


class BackgroundColorPlugOperator(
    Float3CompoundBasePlugOperator["BackgroundColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("backgroundColorR", "background_colorr"),
        ("backgroundColorG", "background_colorg"),
        ("backgroundColorB", "background_colorb"),
    )

    backgroundColorR = FloatField(default_value=1.0)
    background_colorr = backgroundColorR

    backgroundColorG = FloatField(default_value=1.0)
    background_colorg = backgroundColorG

    backgroundColorB = FloatField(default_value=1.0)
    background_colorb = backgroundColorB


class BackgroundColorAttrOperator(
    Float3CompoundBaseAttrOperator[BackgroundColorPlugOperator]
):
    __slots__ = ()

    backgroundColorR = FloatField(default_value=1.0)
    background_colorr = backgroundColorR

    backgroundColorG = FloatField(default_value=1.0)
    background_colorg = backgroundColorG

    backgroundColorB = FloatField(default_value=1.0)
    background_colorb = backgroundColorB


class BackgroundColorField(
    Float3CompoundBaseField[
        BackgroundColorAttrOperator, BackgroundColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = BackgroundColorAttrOperator
    PLUG_CLS = BackgroundColorPlugOperator

    backgroundColorR = FloatField(default_value=1.0)
    background_colorr = backgroundColorR

    backgroundColorG = FloatField(default_value=1.0)
    background_colorg = backgroundColorG

    backgroundColorB = FloatField(default_value=1.0)
    background_colorb = backgroundColorB


class ColorPlugOperator(Float3CompoundBasePlugOperator["ColorAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "colorr"),
        ("colorG", "colorg"),
        ("colorB", "colorb"),
    )

    colorR = FloatField(default_value=0.0)
    colorr = colorR

    colorG = FloatField(default_value=0.0)
    colorg = colorG

    colorB = FloatField(default_value=0.0)
    colorb = colorB


class ColorAttrOperator(Float3CompoundBaseAttrOperator[ColorPlugOperator]):
    __slots__ = ()

    colorR = FloatField(default_value=0.0)
    colorr = colorR

    colorG = FloatField(default_value=0.0)
    colorg = colorG

    colorB = FloatField(default_value=0.0)
    colorb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=0.0)
    colorr = colorR

    colorG = FloatField(default_value=0.0)
    colorg = colorG

    colorB = FloatField(default_value=0.0)
    colorb = colorB


class OffsetPlugOperator(Float2CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
    )

    offsetX = FloatField(default_value=0.5)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.5)
    offsety = offsetY


class OffsetAttrOperator(Float2CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetX = FloatField(default_value=0.5)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.5)
    offsety = offsetY


class OffsetField(
    Float2CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField(default_value=0.5)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.5)
    offsety = offsetY


class ShiftPerLayerPlugOperator(
    Float2CompoundBasePlugOperator["ShiftPerLayerAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shiftPerLayerX", "shift_per_layerx"),
        ("shiftPerLayerY", "shift_per_layery"),
    )

    shiftPerLayerX = FloatField(default_value=0.0)
    shift_per_layerx = shiftPerLayerX

    shiftPerLayerY = FloatField(default_value=0.0)
    shift_per_layery = shiftPerLayerY


class ShiftPerLayerAttrOperator(
    Float2CompoundBaseAttrOperator[ShiftPerLayerPlugOperator]
):
    __slots__ = ()

    shiftPerLayerX = FloatField(default_value=0.0)
    shift_per_layerx = shiftPerLayerX

    shiftPerLayerY = FloatField(default_value=0.0)
    shift_per_layery = shiftPerLayerY


class ShiftPerLayerField(
    Float2CompoundBaseField[
        ShiftPerLayerAttrOperator, ShiftPerLayerPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShiftPerLayerAttrOperator
    PLUG_CLS = ShiftPerLayerPlugOperator

    shiftPerLayerX = FloatField(default_value=0.0)
    shift_per_layerx = shiftPerLayerX

    shiftPerLayerY = FloatField(default_value=0.0)
    shift_per_layery = shiftPerLayerY
