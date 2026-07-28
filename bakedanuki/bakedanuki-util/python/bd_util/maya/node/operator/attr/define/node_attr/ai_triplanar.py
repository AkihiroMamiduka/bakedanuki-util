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


class InputPlugOperator(Float3CompoundBasePlugOperator["InputAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputR", "inputr"),
        ("inputG", "inputg"),
        ("inputB", "inputb"),
    )

    inputR = FloatField(default_value=1.0)
    inputr = inputR

    inputG = FloatField(default_value=1.0)
    inputg = inputG

    inputB = FloatField(default_value=1.0)
    inputb = inputB


class InputAttrOperator(Float3CompoundBaseAttrOperator[InputPlugOperator]):
    __slots__ = ()

    inputR = FloatField(default_value=1.0)
    inputr = inputR

    inputG = FloatField(default_value=1.0)
    inputg = inputG

    inputB = FloatField(default_value=1.0)
    inputb = inputB


class InputField(
    Float3CompoundBaseField[InputAttrOperator, InputPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputAttrOperator
    PLUG_CLS = InputPlugOperator

    inputR = FloatField(default_value=1.0)
    inputr = inputR

    inputG = FloatField(default_value=1.0)
    inputg = inputG

    inputB = FloatField(default_value=1.0)
    inputb = inputB


class InputYPlugOperator(Float3CompoundBasePlugOperator["InputYAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputYR", "input_Yr"),
        ("inputYG", "input_Yg"),
        ("inputYB", "input_Yb"),
    )

    inputYR = FloatField(default_value=1.0)
    input_Yr = inputYR

    inputYG = FloatField(default_value=1.0)
    input_Yg = inputYG

    inputYB = FloatField(default_value=1.0)
    input_Yb = inputYB


class InputYAttrOperator(Float3CompoundBaseAttrOperator[InputYPlugOperator]):
    __slots__ = ()

    inputYR = FloatField(default_value=1.0)
    input_Yr = inputYR

    inputYG = FloatField(default_value=1.0)
    input_Yg = inputYG

    inputYB = FloatField(default_value=1.0)
    input_Yb = inputYB


class InputYField(
    Float3CompoundBaseField[InputYAttrOperator, InputYPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputYAttrOperator
    PLUG_CLS = InputYPlugOperator

    inputYR = FloatField(default_value=1.0)
    input_Yr = inputYR

    inputYG = FloatField(default_value=1.0)
    input_Yg = inputYG

    inputYB = FloatField(default_value=1.0)
    input_Yb = inputYB


class InputZPlugOperator(Float3CompoundBasePlugOperator["InputZAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputZR", "input_Zr"),
        ("inputZG", "input_Zg"),
        ("inputZB", "input_Zb"),
    )

    inputZR = FloatField(default_value=1.0)
    input_Zr = inputZR

    inputZG = FloatField(default_value=1.0)
    input_Zg = inputZG

    inputZB = FloatField(default_value=1.0)
    input_Zb = inputZB


class InputZAttrOperator(Float3CompoundBaseAttrOperator[InputZPlugOperator]):
    __slots__ = ()

    inputZR = FloatField(default_value=1.0)
    input_Zr = inputZR

    inputZG = FloatField(default_value=1.0)
    input_Zg = inputZG

    inputZB = FloatField(default_value=1.0)
    input_Zb = inputZB


class InputZField(
    Float3CompoundBaseField[InputZAttrOperator, InputZPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputZAttrOperator
    PLUG_CLS = InputZPlugOperator

    inputZR = FloatField(default_value=1.0)
    input_Zr = inputZR

    inputZG = FloatField(default_value=1.0)
    input_Zg = inputZG

    inputZB = FloatField(default_value=1.0)
    input_Zb = inputZB


class ScalePlugOperator(Float3CompoundBasePlugOperator["ScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "scalex"),
        ("scaleY", "scaley"),
        ("scaleZ", "scalez"),
    )

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleAttrOperator(Float3CompoundBaseAttrOperator[ScalePlugOperator]):
    __slots__ = ()

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class ScaleField(
    Float3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = FloatField(default_value=1.0)
    scalex = scaleX

    scaleY = FloatField(default_value=1.0)
    scaley = scaleY

    scaleZ = FloatField(default_value=1.0)
    scalez = scaleZ


class RotatePlugOperator(Float3CompoundBasePlugOperator["RotateAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rotatex"),
        ("rotateY", "rotatey"),
        ("rotateZ", "rotatez"),
    )

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class RotateAttrOperator(Float3CompoundBaseAttrOperator[RotatePlugOperator]):
    __slots__ = ()

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class RotateField(
    Float3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = FloatField(default_value=0.0)
    rotatex = rotateX

    rotateY = FloatField(default_value=0.0)
    rotatey = rotateY

    rotateZ = FloatField(default_value=0.0)
    rotatez = rotateZ


class OffsetPlugOperator(Float3CompoundBasePlugOperator["OffsetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "offsetx"),
        ("offsetY", "offsety"),
        ("offsetZ", "offsetz"),
    )

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ


class OffsetAttrOperator(Float3CompoundBaseAttrOperator[OffsetPlugOperator]):
    __slots__ = ()

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ


class OffsetField(
    Float3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = FloatField(default_value=0.0)
    offsetx = offsetX

    offsetY = FloatField(default_value=0.0)
    offsety = offsetY

    offsetZ = FloatField(default_value=0.0)
    offsetz = offsetZ
