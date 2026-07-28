# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.range.float_linear import FloatLinearField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)
from ..custom.at.scalar_compound.unit_compound.linear_compound.float3._base import (
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseField,
)


class TranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["TranslateAttrOperator"]
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
    DoubleLinear3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField(default_value=0.0)
    tx = translateX

    translateY = DoubleLinearField(default_value=0.0)
    ty = translateY

    translateZ = DoubleLinearField(default_value=0.0)
    tz = translateZ


class TranslateField(
    DoubleLinear3CompoundBaseField[
        TranslateAttrOperator, TranslatePlugOperator
    ]
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
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
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
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField(default_value=0.0)
    rx = rotateX

    rotateY = DoubleAngleField(default_value=0.0)
    ry = rotateY

    rotateZ = DoubleAngleField(default_value=0.0)
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
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


class ScalePlugOperator(Double3CompoundBasePlugOperator["ScaleAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scaleX", "sx"),
        ("scaleY", "sy"),
        ("scaleZ", "sz"),
    )

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleAttrOperator(Double3CompoundBaseAttrOperator[ScalePlugOperator]):
    __slots__ = ()

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class ScaleField(
    Double3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleAttrOperator
    PLUG_CLS = ScalePlugOperator

    scaleX = DoubleField(default_value=1.0)
    sx = scaleX

    scaleY = DoubleField(default_value=1.0)
    sy = scaleY

    scaleZ = DoubleField(default_value=1.0)
    sz = scaleZ


class PivotPlugOperator(
    FloatLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pvx"),
        ("pivotY", "pvy"),
        ("pivotZ", "pvz"),
    )

    pivotX = FloatLinearField(default_value=0.0)
    pvx = pivotX

    pivotY = FloatLinearField(default_value=0.0)
    pvy = pivotY

    pivotZ = FloatLinearField(default_value=0.0)
    pvz = pivotZ


class PivotAttrOperator(
    FloatLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = FloatLinearField(default_value=0.0)
    pvx = pivotX

    pivotY = FloatLinearField(default_value=0.0)
    pvy = pivotY

    pivotZ = FloatLinearField(default_value=0.0)
    pvz = pivotZ


class PivotField(
    FloatLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = FloatLinearField(default_value=0.0)
    pvx = pivotX

    pivotY = FloatLinearField(default_value=0.0)
    pvy = pivotY

    pivotZ = FloatLinearField(default_value=0.0)
    pvz = pivotZ


class LocalTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localTranslateX", "ltx"),
        ("localTranslateY", "lty"),
        ("localTranslateZ", "ltz"),
    )

    localTranslateX = DoubleLinearField(default_value=0.0)
    ltx = localTranslateX

    localTranslateY = DoubleLinearField(default_value=0.0)
    lty = localTranslateY

    localTranslateZ = DoubleLinearField(default_value=0.0)
    ltz = localTranslateZ


class LocalTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalTranslatePlugOperator]
):
    __slots__ = ()

    localTranslateX = DoubleLinearField(default_value=0.0)
    ltx = localTranslateX

    localTranslateY = DoubleLinearField(default_value=0.0)
    lty = localTranslateY

    localTranslateZ = DoubleLinearField(default_value=0.0)
    ltz = localTranslateZ


class LocalTranslateField(
    DoubleLinear3CompoundBaseField[
        LocalTranslateAttrOperator, LocalTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalTranslateAttrOperator
    PLUG_CLS = LocalTranslatePlugOperator

    localTranslateX = DoubleLinearField(default_value=0.0)
    ltx = localTranslateX

    localTranslateY = DoubleLinearField(default_value=0.0)
    lty = localTranslateY

    localTranslateZ = DoubleLinearField(default_value=0.0)
    ltz = localTranslateZ


class LocalDirectionPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["LocalDirectionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localDirectionX", "ldx"),
        ("localDirectionY", "ldy"),
        ("localDirectionZ", "ldz"),
    )

    localDirectionX = DoubleLinearField(default_value=1.0)
    ldx = localDirectionX

    localDirectionY = DoubleLinearField(default_value=0.0)
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField(default_value=0.0)
    ldz = localDirectionZ


class LocalDirectionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalDirectionPlugOperator]
):
    __slots__ = ()

    localDirectionX = DoubleLinearField(default_value=1.0)
    ldx = localDirectionX

    localDirectionY = DoubleLinearField(default_value=0.0)
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField(default_value=0.0)
    ldz = localDirectionZ


class LocalDirectionField(
    DoubleLinear3CompoundBaseField[
        LocalDirectionAttrOperator, LocalDirectionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = LocalDirectionAttrOperator
    PLUG_CLS = LocalDirectionPlugOperator

    localDirectionX = DoubleLinearField(default_value=1.0)
    ldx = localDirectionX

    localDirectionY = DoubleLinearField(default_value=0.0)
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField(default_value=0.0)
    ldz = localDirectionZ
