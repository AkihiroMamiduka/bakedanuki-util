# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
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


class TaperCurve_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class TaperCurve_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class TaperCurve_InterpEnumField(
    EnumField[TaperCurve_InterpEnumAttrOperator, TaperCurve_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TaperCurve_InterpEnumAttrOperator
    PLUG_CLS = TaperCurve_InterpEnumPlugOperator


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
    DoubleLinear3CompoundBaseField[TranslateAttrOperator, TranslatePlugOperator]
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


class ScalePlugOperator(
    Double3CompoundBasePlugOperator["ScaleAttrOperator"]
):
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


class ScaleAttrOperator(
    Double3CompoundBaseAttrOperator[ScalePlugOperator]
):
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
    DoubleLinear3CompoundBaseField[LocalTranslateAttrOperator, LocalTranslatePlugOperator]
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
    DoubleLinear3CompoundBaseField[LocalDirectionAttrOperator, LocalDirectionPlugOperator]
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


class LocalRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["LocalRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("localRotateX", "lrx"),
        ("localRotateY", "lry"),
        ("localRotateZ", "lrz"),
    )

    localRotateX = DoubleAngleField(default_value=0.0)
    lrx = localRotateX

    localRotateY = DoubleAngleField(default_value=0.0)
    lry = localRotateY

    localRotateZ = DoubleAngleField(default_value=0.0)
    lrz = localRotateZ


class LocalRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[LocalRotatePlugOperator]
):
    __slots__ = ()

    localRotateX = DoubleAngleField(default_value=0.0)
    lrx = localRotateX

    localRotateY = DoubleAngleField(default_value=0.0)
    lry = localRotateY

    localRotateZ = DoubleAngleField(default_value=0.0)
    lrz = localRotateZ


class LocalRotateField(
    DoubleAngle3CompoundBaseField[LocalRotateAttrOperator, LocalRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalRotateAttrOperator
    PLUG_CLS = LocalRotatePlugOperator

    localRotateX = DoubleAngleField(default_value=0.0)
    lrx = localRotateX

    localRotateY = DoubleAngleField(default_value=0.0)
    lry = localRotateY

    localRotateZ = DoubleAngleField(default_value=0.0)
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

    localScaleX = DoubleField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleAttrOperator(
    Double3CompoundBaseAttrOperator[LocalScalePlugOperator]
):
    __slots__ = ()

    localScaleX = DoubleField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleField(default_value=1.0)
    lsz = localScaleZ


class LocalScaleField(
    Double3CompoundBaseField[LocalScaleAttrOperator, LocalScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LocalScaleAttrOperator
    PLUG_CLS = LocalScalePlugOperator

    localScaleX = DoubleField(default_value=1.0)
    lsx = localScaleX

    localScaleY = DoubleField(default_value=1.0)
    lsy = localScaleY

    localScaleZ = DoubleField(default_value=1.0)
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

    taperCurve_Position = FloatField(default_value=0.0)
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField(default_value=0.0)
    cfv = taperCurve_FloatValue

    taperCurve_Interp = TaperCurve_InterpEnumField(default_value=0)
    ci = taperCurve_Interp


class TaperCurveAttrOperator(
    CompoundAttrOperator[TaperCurvePlugOperator]
):
    __slots__ = ()

    taperCurve_Position = FloatField(default_value=0.0)
    cp = taperCurve_Position

    taperCurve_FloatValue = FloatField(default_value=0.0)
    cfv = taperCurve_FloatValue

    taperCurve_Interp = TaperCurve_InterpEnumField(default_value=0)
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

    compBoundingBoxMinX = DoubleLinearField(default_value=0.0)
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField(default_value=0.0)
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField(default_value=0.0)
    cnz = compBoundingBoxMinZ


class CompBoundingBoxMinAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompBoundingBoxMinPlugOperator]
):
    __slots__ = ()

    compBoundingBoxMinX = DoubleLinearField(default_value=0.0)
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField(default_value=0.0)
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField(default_value=0.0)
    cnz = compBoundingBoxMinZ


class CompBoundingBoxMinField(
    DoubleLinear3CompoundBaseField[CompBoundingBoxMinAttrOperator, CompBoundingBoxMinPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompBoundingBoxMinAttrOperator
    PLUG_CLS = CompBoundingBoxMinPlugOperator

    compBoundingBoxMinX = DoubleLinearField(default_value=0.0)
    cnx = compBoundingBoxMinX

    compBoundingBoxMinY = DoubleLinearField(default_value=0.0)
    cny = compBoundingBoxMinY

    compBoundingBoxMinZ = DoubleLinearField(default_value=0.0)
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

    compBoundingBoxMaxX = DoubleLinearField(default_value=1.0)
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField(default_value=1.0)
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField(default_value=1.0)
    cxz = compBoundingBoxMaxZ


class CompBoundingBoxMaxAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[CompBoundingBoxMaxPlugOperator]
):
    __slots__ = ()

    compBoundingBoxMaxX = DoubleLinearField(default_value=1.0)
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField(default_value=1.0)
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField(default_value=1.0)
    cxz = compBoundingBoxMaxZ


class CompBoundingBoxMaxField(
    DoubleLinear3CompoundBaseField[CompBoundingBoxMaxAttrOperator, CompBoundingBoxMaxPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompBoundingBoxMaxAttrOperator
    PLUG_CLS = CompBoundingBoxMaxPlugOperator

    compBoundingBoxMaxX = DoubleLinearField(default_value=1.0)
    cxx = compBoundingBoxMaxX

    compBoundingBoxMaxY = DoubleLinearField(default_value=1.0)
    cxy = compBoundingBoxMaxY

    compBoundingBoxMaxZ = DoubleLinearField(default_value=1.0)
    cxz = compBoundingBoxMaxZ
