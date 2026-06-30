# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import EnumField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
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


class TaperCurvePlugOperator(
    CompoundPlugOperator["TaperCurveAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("taperCurve_Position", "cp"),
        ("taperCurve_FloatValue", "cfv"),
        ("taperCurve_Interp", "ci"),
    )

    taperCurve_Position = FloatField()
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    cfv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    ci = taperCurve_Interp


class TaperCurveAttrOperator(
    CompoundAttrOperator[TaperCurvePlugOperator]
):
    __slots__ = ()

    taperCurve_Position = FloatField()
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField()
    cfv = taperCurve_FloatValue

    taperCurve_Interp = EnumField()
    ci = taperCurve_Interp


class TaperCurveField(
    CompoundField[TaperCurveAttrOperator, TaperCurvePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TaperCurveAttrOperator
    PLUG_CLS = TaperCurvePlugOperator


class CompBoundingBoxMinPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CompBoundingBoxMinAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compBoundingBoxMinX", "cnx"),
        ("compBoundingBoxMinY", "cny"),
        ("compBoundingBoxMinZ", "cnz"),
    )

    compBoundingBoxMinX = DoubleLinearField()
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField()
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField()
    cnz = compBoundingBoxMinZ


class CompBoundingBoxMinAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompBoundingBoxMinPlugOperator]
):
    __slots__ = ()

    compBoundingBoxMinX = DoubleLinearField()
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField()
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField()
    cnz = compBoundingBoxMinZ


class CompBoundingBoxMinField(
    DoubleLinear3CompoundBaseField[CompBoundingBoxMinAttrOperator, CompBoundingBoxMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompBoundingBoxMinAttrOperator
    PLUG_CLS = CompBoundingBoxMinPlugOperator

    compBoundingBoxMinX = DoubleLinearField()
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField()
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField()
    cnz = compBoundingBoxMinZ


class CompBoundingBoxMaxPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["CompBoundingBoxMaxAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compBoundingBoxMaxX", "cxx"),
        ("compBoundingBoxMaxY", "cxy"),
        ("compBoundingBoxMaxZ", "cxz"),
    )

    compBoundingBoxMaxX = DoubleLinearField()
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField()
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField()
    cxz = compBoundingBoxMaxZ


class CompBoundingBoxMaxAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompBoundingBoxMaxPlugOperator]
):
    __slots__ = ()

    compBoundingBoxMaxX = DoubleLinearField()
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField()
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField()
    cxz = compBoundingBoxMaxZ


class CompBoundingBoxMaxField(
    DoubleLinear3CompoundBaseField[CompBoundingBoxMaxAttrOperator, CompBoundingBoxMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompBoundingBoxMaxAttrOperator
    PLUG_CLS = CompBoundingBoxMaxPlugOperator

    compBoundingBoxMaxX = DoubleLinearField()
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField()
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField()
    cxz = compBoundingBoxMaxZ
