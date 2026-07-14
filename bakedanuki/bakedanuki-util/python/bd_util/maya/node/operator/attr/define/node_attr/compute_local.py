# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField


class TranslatePlugOperator(
    CompoundPlugOperator["TranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translateX", "tx"),
        ("translateY", "ty"),
        ("translateZ", "tz"),
    )

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class TranslateAttrOperator(
    CompoundAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class TranslateField(
    CompoundField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class RotatePlugOperator(
    CompoundPlugOperator["RotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotateX", "rx"),
        ("rotateY", "ry"),
        ("rotateZ", "rz"),
    )

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateAttrOperator(
    CompoundAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateField(
    CompoundField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class ScalePlugOperator(
    CompoundPlugOperator["ScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "sx"),
        ("scaleY", "sy"),
        ("scaleZ", "sz"),
    )

    scaleX = DoubleField(default_value=0.0)
    sx = scaleX

    scaleY = DoubleField(default_value=0.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=0.0)
    sz = scaleZ


class ScaleAttrOperator(
    CompoundAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField(default_value=0.0)
    sx = scaleX

    scaleY = DoubleField(default_value=0.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=0.0)
    sz = scaleZ


class ScaleField(
    CompoundField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = DoubleField(default_value=0.0)
    sx = scaleX

    scaleY = DoubleField(default_value=0.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=0.0)
    sz = scaleZ


class PreRPlugOperator(
    CompoundPlugOperator["PreRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PreRx", "PreRx"),
        ("PreRy", "PreRy"),
        ("PreRz", "PreRz"),
    )

    PreRx = DoubleAngleField(default_value=0.0)

    PreRy = DoubleAngleField(default_value=0.0)

    PreRz = DoubleAngleField(default_value=0.0)


class PreRAttrOperator(
    CompoundAttrOperator[PreRPlugOperator]
):
    __slots__ = ()

    PreRx = DoubleAngleField(default_value=0.0)

    PreRy = DoubleAngleField(default_value=0.0)

    PreRz = DoubleAngleField(default_value=0.0)


class PreRField(
    CompoundField[PreRAttrOperator, PreRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PreRAttrOperator
    PLUG_CLS = PreRPlugOperator

    PreRx = DoubleAngleField(default_value=0.0)

    PreRy = DoubleAngleField(default_value=0.0)

    PreRz = DoubleAngleField(default_value=0.0)


class PostRPlugOperator(
    CompoundPlugOperator["PostRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PostRx", "PostRx"),
        ("PostRy", "PostRy"),
        ("PostRz", "PostRz"),
    )

    PostRx = DoubleAngleField(default_value=0.0)

    PostRy = DoubleAngleField(default_value=0.0)

    PostRz = DoubleAngleField(default_value=0.0)


class PostRAttrOperator(
    CompoundAttrOperator[PostRPlugOperator]
):
    __slots__ = ()

    PostRx = DoubleAngleField(default_value=0.0)

    PostRy = DoubleAngleField(default_value=0.0)

    PostRz = DoubleAngleField(default_value=0.0)


class PostRField(
    CompoundField[PostRAttrOperator, PostRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostRAttrOperator
    PLUG_CLS = PostRPlugOperator

    PostRx = DoubleAngleField(default_value=0.0)

    PostRy = DoubleAngleField(default_value=0.0)

    PostRz = DoubleAngleField(default_value=0.0)
