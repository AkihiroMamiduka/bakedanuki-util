# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.at.unit_scalar_range.float_linear import FloatLinearField
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

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[TranslatePlugOperator]
):
    __slots__ = ()

    translateX = DoubleLinearField()
    tx = translateX

    translateY = DoubleLinearField()
    ty = translateY

    translateZ = DoubleLinearField()
    tz = translateZ


class TranslateField(
    DoubleLinear3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
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
    DoubleAngle3CompoundBasePlugOperator["RotateAttrOperator"]
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
    DoubleAngle3CompoundBaseAttrOperator[RotatePlugOperator]
):
    __slots__ = ()

    rotateX = DoubleAngleField()
    rx = rotateX

    rotateY = DoubleAngleField()
    ry = rotateY

    rotateZ = DoubleAngleField()
    rz = rotateZ


class RotateField(
    DoubleAngle3CompoundBaseField[RotateAttrOperator, RotatePlugOperator]
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
    Double3CompoundBasePlugOperator["ScaleAttrOperator"]
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
    Double3CompoundBaseAttrOperator[ScalePlugOperator]
):
    __slots__ = ()

    scaleX = DoubleField()
    sx = scaleX

    scaleY = DoubleField()
    sy = scaleY

    scaleZ = DoubleField()
    sz = scaleZ


class ScaleField(
    Double3CompoundBaseField[ScaleAttrOperator, ScalePlugOperator]
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


class PivotPlugOperator(
    FloatLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "pvx"),
        ("pivotY", "pvy"),
        ("pivotZ", "pvz"),
    )

    pivotX = FloatLinearField()
    pvx = pivotX

    pivotY = FloatLinearField()
    pvy = pivotY

    pivotZ = FloatLinearField()
    pvz = pivotZ


class PivotAttrOperator(
    FloatLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = FloatLinearField()
    pvx = pivotX

    pivotY = FloatLinearField()
    pvy = pivotY

    pivotZ = FloatLinearField()
    pvz = pivotZ


class PivotField(
    FloatLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = FloatLinearField()
    pvx = pivotX

    pivotY = FloatLinearField()
    pvy = pivotY

    pivotZ = FloatLinearField()
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

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
    ltz = localTranslateZ


class LocalTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalTranslatePlugOperator]
):
    __slots__ = ()

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
    ltz = localTranslateZ


class LocalTranslateField(
    DoubleLinear3CompoundBaseField[LocalTranslateAttrOperator, LocalTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalTranslateAttrOperator
    PLUG_CLS = LocalTranslatePlugOperator

    localTranslateX = DoubleLinearField()
    ltx = localTranslateX

    localTranslateY = DoubleLinearField()
    lty = localTranslateY

    localTranslateZ = DoubleLinearField()
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

    localDirectionX = DoubleLinearField()
    ldx = localDirectionX

    localDirectionY = DoubleLinearField()
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField()
    ldz = localDirectionZ


class LocalDirectionAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[LocalDirectionPlugOperator]
):
    __slots__ = ()

    localDirectionX = DoubleLinearField()
    ldx = localDirectionX

    localDirectionY = DoubleLinearField()
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField()
    ldz = localDirectionZ


class LocalDirectionField(
    DoubleLinear3CompoundBaseField[LocalDirectionAttrOperator, LocalDirectionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalDirectionAttrOperator
    PLUG_CLS = LocalDirectionPlugOperator

    localDirectionX = DoubleLinearField()
    ldx = localDirectionX

    localDirectionY = DoubleLinearField()
    ldy = localDirectionY

    localDirectionZ = DoubleLinearField()
    ldz = localDirectionZ


class LocalRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["LocalRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localRotateX", "lrx"),
        ("localRotateY", "lry"),
        ("localRotateZ", "lrz"),
    )

    localRotateX = DoubleAngleField()
    lrx = localRotateX

    localRotateY = DoubleAngleField()
    lry = localRotateY

    localRotateZ = DoubleAngleField()
    lrz = localRotateZ


class LocalRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[LocalRotatePlugOperator]
):
    __slots__ = ()

    localRotateX = DoubleAngleField()
    lrx = localRotateX

    localRotateY = DoubleAngleField()
    lry = localRotateY

    localRotateZ = DoubleAngleField()
    lrz = localRotateZ


class LocalRotateField(
    DoubleAngle3CompoundBaseField[LocalRotateAttrOperator, LocalRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalRotateAttrOperator
    PLUG_CLS = LocalRotatePlugOperator

    localRotateX = DoubleAngleField()
    lrx = localRotateX

    localRotateY = DoubleAngleField()
    lry = localRotateY

    localRotateZ = DoubleAngleField()
    lrz = localRotateZ


class LocalScalePlugOperator(
    Double3CompoundBasePlugOperator["LocalScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localScaleX", "lsx"),
        ("localScaleY", "lsy"),
        ("localScaleZ", "lsz"),
    )

    localScaleX = DoubleField()
    lsx = localScaleX

    localScaleY = DoubleField()
    lsy = localScaleY

    localScaleZ = DoubleField()
    lsz = localScaleZ


class LocalScaleAttrOperator(
    Double3CompoundBaseAttrOperator[LocalScalePlugOperator]
):
    __slots__ = ()

    localScaleX = DoubleField()
    lsx = localScaleX

    localScaleY = DoubleField()
    lsy = localScaleY

    localScaleZ = DoubleField()
    lsz = localScaleZ


class LocalScaleField(
    Double3CompoundBaseField[LocalScaleAttrOperator, LocalScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalScaleAttrOperator
    PLUG_CLS = LocalScalePlugOperator

    localScaleX = DoubleField()
    lsx = localScaleX

    localScaleY = DoubleField()
    lsy = localScaleY

    localScaleZ = DoubleField()
    lsz = localScaleZ


class GravityPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["GravityAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("gravityX", "gx"),
        ("gravityY", "gy"),
        ("gravityZ", "gz"),
    )

    gravityX = DoubleLinearField()
    gx = gravityX

    gravityY = DoubleLinearField()
    gy = gravityY

    gravityZ = DoubleLinearField()
    gz = gravityZ


class GravityAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[GravityPlugOperator]
):
    __slots__ = ()

    gravityX = DoubleLinearField()
    gx = gravityX

    gravityY = DoubleLinearField()
    gy = gravityY

    gravityZ = DoubleLinearField()
    gz = gravityZ


class GravityField(
    DoubleLinear3CompoundBaseField[GravityAttrOperator, GravityPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GravityAttrOperator
    PLUG_CLS = GravityPlugOperator

    gravityX = DoubleLinearField()
    gx = gravityX

    gravityY = DoubleLinearField()
    gy = gravityY

    gravityZ = DoubleLinearField()
    gz = gravityZ


class MagnetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MagnetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("magnX", "mx"),
        ("magnY", "my"),
        ("magnZ", "mz"),
    )

    magnX = DoubleLinearField()
    mx = magnX

    magnY = DoubleLinearField()
    my = magnY

    magnZ = DoubleLinearField()
    mz = magnZ


class MagnetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MagnetPlugOperator]
):
    __slots__ = ()

    magnX = DoubleLinearField()
    mx = magnX

    magnY = DoubleLinearField()
    my = magnY

    magnZ = DoubleLinearField()
    mz = magnZ


class MagnetField(
    DoubleLinear3CompoundBaseField[MagnetAttrOperator, MagnetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MagnetAttrOperator
    PLUG_CLS = MagnetPlugOperator

    magnX = DoubleLinearField()
    mx = magnX

    magnY = DoubleLinearField()
    my = magnY

    magnZ = DoubleLinearField()
    mz = magnZ
