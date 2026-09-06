# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.at.scalar.unit.range.float_linear import FloatLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
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
    DoubleLinear3CompoundBaseField[
        CompBoundingBoxMinAttrOperator, CompBoundingBoxMinPlugOperator
    ]
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
    DoubleLinear3CompoundBaseField[
        CompBoundingBoxMaxAttrOperator, CompBoundingBoxMaxPlugOperator
    ]
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


class PivotOrientationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["PivotOrientationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotOrientationX", "pox"),
        ("pivotOrientationY", "poy"),
        ("pivotOrientationZ", "poz"),
    )

    pivotOrientationX = DoubleAngleField(default_value=0.0)
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField(default_value=0.0)
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField(default_value=0.0)
    poz = pivotOrientationZ


class PivotOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[PivotOrientationPlugOperator]
):
    __slots__ = ()

    pivotOrientationX = DoubleAngleField(default_value=0.0)
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField(default_value=0.0)
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField(default_value=0.0)
    poz = pivotOrientationZ


class PivotOrientationField(
    DoubleAngle3CompoundBaseField[
        PivotOrientationAttrOperator, PivotOrientationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PivotOrientationAttrOperator
    PLUG_CLS = PivotOrientationPlugOperator

    pivotOrientationX = DoubleAngleField(default_value=0.0)
    pox = pivotOrientationX

    pivotOrientationY = DoubleAngleField(default_value=0.0)
    poy = pivotOrientationY

    pivotOrientationZ = DoubleAngleField(default_value=0.0)
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

    compPivotOrientationX = DoubleAngleField(default_value=0.0)
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField(default_value=0.0)
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField(default_value=0.0)
    cpz = compPivotOrientationZ


class CompPivotOrientationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[CompPivotOrientationPlugOperator]
):
    __slots__ = ()

    compPivotOrientationX = DoubleAngleField(default_value=0.0)
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField(default_value=0.0)
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField(default_value=0.0)
    cpz = compPivotOrientationZ


class CompPivotOrientationField(
    DoubleAngle3CompoundBaseField[
        CompPivotOrientationAttrOperator, CompPivotOrientationPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CompPivotOrientationAttrOperator
    PLUG_CLS = CompPivotOrientationPlugOperator

    compPivotOrientationX = DoubleAngleField(default_value=0.0)
    cpx = compPivotOrientationX

    compPivotOrientationY = DoubleAngleField(default_value=0.0)
    cpy = compPivotOrientationY

    compPivotOrientationZ = DoubleAngleField(default_value=0.0)
    cpz = compPivotOrientationZ
