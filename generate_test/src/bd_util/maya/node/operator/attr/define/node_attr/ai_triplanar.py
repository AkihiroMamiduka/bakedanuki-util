# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
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


class InputPlugOperator(
    Float3CompoundBasePlugOperator["InputAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputR", "inputr"),
        ("inputG", "inputg"),
        ("inputB", "inputb"),
    )

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
    inputb = inputB


class InputAttrOperator(
    Float3CompoundBaseAttrOperator[InputPlugOperator]
):
    __slots__ = ()

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
    inputb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField()
    inputr = inputR

    inputG = FloatField()
    inputg = inputG

    inputB = FloatField()
    inputb = inputB


class InputYPlugOperator(
    Float3CompoundBasePlugOperator["InputYAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputYR", "input_Yr"),
        ("inputYG", "input_Yg"),
        ("inputYB", "input_Yb"),
    )

    inputYR = FloatField()
    input_Yr = inputYR

    inputYG = FloatField()
    input_Yg = inputYG

    inputYB = FloatField()
    input_Yb = inputYB


class InputYAttrOperator(
    Float3CompoundBaseAttrOperator[InputYPlugOperator]
):
    __slots__ = ()

    inputYR = FloatField()
    input_Yr = inputYR

    inputYG = FloatField()
    input_Yg = inputYG

    inputYB = FloatField()
    input_Yb = inputYB


class InputYField(
    Float3CompoundBaseField[InputYAttrOperator, InputYPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputYAttrOperator
    PLUG_CLS = InputYPlugOperator

    inputYR = FloatField()
    input_Yr = inputYR

    inputYG = FloatField()
    input_Yg = inputYG

    inputYB = FloatField()
    input_Yb = inputYB


class InputZPlugOperator(
    Float3CompoundBasePlugOperator["InputZAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputZR", "input_Zr"),
        ("inputZG", "input_Zg"),
        ("inputZB", "input_Zb"),
    )

    inputZR = FloatField()
    input_Zr = inputZR

    inputZG = FloatField()
    input_Zg = inputZG

    inputZB = FloatField()
    input_Zb = inputZB


class InputZAttrOperator(
    Float3CompoundBaseAttrOperator[InputZPlugOperator]
):
    __slots__ = ()

    inputZR = FloatField()
    input_Zr = inputZR

    inputZG = FloatField()
    input_Zg = inputZG

    inputZB = FloatField()
    input_Zb = inputZB


class InputZField(
    Float3CompoundBaseField[InputZAttrOperator, InputZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputZAttrOperator
    PLUG_CLS = InputZPlugOperator

    inputZR = FloatField()
    input_Zr = inputZR

    inputZG = FloatField()
    input_Zg = inputZG

    inputZB = FloatField()
    input_Zb = inputZB


class ScalePlugOperator(
    Float3CompoundBasePlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleAttrOperator(
    Float3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField()
    scalex = scaleX

    scaleY = FloatField()
    scaley = scaleY

    scaleZ = FloatField()
    scalez = scaleZ


class RotatePlugOperator(
    Float3CompoundBasePlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rotatex"),
        ("rotateY", "rotatey"),
        ("rotateZ", "rotatez"),
    )

    rotateX = FloatField()
    rotatex = rotateX

    rotateY = FloatField()
    rotatey = rotateY

    rotateZ = FloatField()
    rotatez = rotateZ


class RotateAttrOperator(
    Float3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = FloatField()
    rotatex = rotateX

    rotateY = FloatField()
    rotatey = rotateY

    rotateZ = FloatField()
    rotatez = rotateZ


class RotateField(
    Float3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = FloatField()
    rotatex = rotateX

    rotateY = FloatField()
    rotatey = rotateY

    rotateZ = FloatField()
    rotatez = rotateZ


class OffsetPlugOperator(
    Float3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
        ("offsetZ", "offsetz"),
    )

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ


class OffsetAttrOperator(
    Float3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField()
    offsetx = offsetX

    offsetY = FloatField()
    offsety = offsetY

    offsetZ = FloatField()
    offsetz = offsetZ
