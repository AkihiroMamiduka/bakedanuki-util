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

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateAttrOperator(
    CompoundAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateField(
    CompoundField[TranslateAttrOperator, TranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateAttrOperator
    PLUG_CLS = TranslatePlugOperator

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
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

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateAttrOperator(
    CompoundAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateField(
    CompoundField[RotateAttrOperator, RotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotateAttrOperator
    PLUG_CLS = RotatePlugOperator

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
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

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
    sz = scaleZ


class ScaleAttrOperator(
    CompoundAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
    sz = scaleZ


class ScaleField(
    CompoundField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
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

    PreRx = DoubleAngleField()

    PreRy = DoubleAngleField()

    PreRz = DoubleAngleField()


class PreRAttrOperator(
    CompoundAttrOperator[PreRPlugOperator]
):
    __slots__ = ()

    PreRx = DoubleAngleField()

    PreRy = DoubleAngleField()

    PreRz = DoubleAngleField()


class PreRField(
    CompoundField[PreRAttrOperator, PreRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PreRAttrOperator
    PLUG_CLS = PreRPlugOperator

    PreRx = DoubleAngleField()

    PreRy = DoubleAngleField()

    PreRz = DoubleAngleField()


class PostRPlugOperator(
    CompoundPlugOperator["PostRAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("PostRx", "PostRx"),
        ("PostRy", "PostRy"),
        ("PostRz", "PostRz"),
    )

    PostRx = DoubleAngleField()

    PostRy = DoubleAngleField()

    PostRz = DoubleAngleField()


class PostRAttrOperator(
    CompoundAttrOperator[PostRPlugOperator]
):
    __slots__ = ()

    PostRx = DoubleAngleField()

    PostRy = DoubleAngleField()

    PostRz = DoubleAngleField()


class PostRField(
    CompoundField[PostRAttrOperator, PostRPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PostRAttrOperator
    PLUG_CLS = PostRPlugOperator

    PostRx = DoubleAngleField()

    PostRy = DoubleAngleField()

    PostRz = DoubleAngleField()
