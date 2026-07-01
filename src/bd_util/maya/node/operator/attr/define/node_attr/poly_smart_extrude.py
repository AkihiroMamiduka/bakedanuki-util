# coding: utf-8

from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.at.unit_scalar_range.float_linear import FloatLinearField
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


class PivotOrientationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["PivotOrientationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotOrientationX", "pox"),
        ("pivotOrientationY", "poy"),
        ("pivotOrientationZ", "poz"),
    )

    pivotOrientationX = DoubleAngleField()
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField()
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField()
    poz = pivotOrientationZ


class PivotOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[PivotOrientationPlugOperator]
):
    __slots__ = ()

    pivotOrientationX = DoubleAngleField()
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField()
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField()
    poz = pivotOrientationZ


class PivotOrientationField(
    DoubleAngle3CompoundBaseField[PivotOrientationAttrOperator, PivotOrientationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotOrientationAttrOperator
    PLUG_CLS = PivotOrientationPlugOperator

    pivotOrientationX = DoubleAngleField()
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField()
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField()
    poz = pivotOrientationZ


class CompPivotOrientationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["CompPivotOrientationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("compPivotOrientationX", "cpx"),
        ("compPivotOrientationY", "cpy"),
        ("compPivotOrientationZ", "cpz"),
    )

    compPivotOrientationX = DoubleAngleField()
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField()
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField()
    cpz = compPivotOrientationZ


class CompPivotOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[CompPivotOrientationPlugOperator]
):
    __slots__ = ()

    compPivotOrientationX = DoubleAngleField()
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField()
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField()
    cpz = compPivotOrientationZ


class CompPivotOrientationField(
    DoubleAngle3CompoundBaseField[CompPivotOrientationAttrOperator, CompPivotOrientationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompPivotOrientationAttrOperator
    PLUG_CLS = CompPivotOrientationPlugOperator

    compPivotOrientationX = DoubleAngleField()
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField()
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField()
    cpz = compPivotOrientationZ
