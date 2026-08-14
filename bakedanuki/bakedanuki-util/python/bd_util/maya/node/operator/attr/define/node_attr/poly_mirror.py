# coding: utf-8

from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class PivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "px"),
        ("pivotY", "py"),
        ("pivotZ", "pz"),
    )

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField(default_value=0.0)
    px = pivotX

    pivotY = DoubleLinearField(default_value=0.0)
    py = pivotY

    pivotZ = DoubleLinearField(default_value=0.0)
    pz = pivotZ


class ScalePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ScalePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("scalePivotX", "spx"),
        ("scalePivotY", "spy"),
        ("scalePivotZ", "spz"),
    )

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class ScalePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ScalePivotPlugOperator]
):
    __slots__ = ()

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class ScalePivotField(
    DoubleLinear3CompoundBaseField[
        ScalePivotAttrOperator, ScalePivotPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ScalePivotAttrOperator
    PLUG_CLS = ScalePivotPlugOperator

    scalePivotX = DoubleLinearField(default_value=0.0)
    spx = scalePivotX

    scalePivotY = DoubleLinearField(default_value=0.0)
    spy = scalePivotY

    scalePivotZ = DoubleLinearField(default_value=0.0)
    spz = scalePivotZ


class MirrorPlaneCenterPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["MirrorPlaneCenterAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mirrorPlaneCenterX", "pcx"),
        ("mirrorPlaneCenterY", "pcy"),
        ("mirrorPlaneCenterZ", "pcz"),
    )

    mirrorPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField(default_value=0.0)
    pcz = mirrorPlaneCenterZ


class MirrorPlaneCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MirrorPlaneCenterPlugOperator]
):
    __slots__ = ()

    mirrorPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField(default_value=0.0)
    pcz = mirrorPlaneCenterZ


class MirrorPlaneCenterField(
    DoubleLinear3CompoundBaseField[
        MirrorPlaneCenterAttrOperator, MirrorPlaneCenterPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MirrorPlaneCenterAttrOperator
    PLUG_CLS = MirrorPlaneCenterPlugOperator

    mirrorPlaneCenterX = DoubleLinearField(default_value=0.0)
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField(default_value=0.0)
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField(default_value=0.0)
    pcz = mirrorPlaneCenterZ


class MirrorPlaneRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["MirrorPlaneRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mirrorPlaneRotateX", "rx"),
        ("mirrorPlaneRotateY", "ry"),
        ("mirrorPlaneRotateZ", "rz"),
    )

    mirrorPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = mirrorPlaneRotateZ


class MirrorPlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MirrorPlaneRotatePlugOperator]
):
    __slots__ = ()

    mirrorPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = mirrorPlaneRotateZ


class MirrorPlaneRotateField(
    DoubleAngle3CompoundBaseField[
        MirrorPlaneRotateAttrOperator, MirrorPlaneRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MirrorPlaneRotateAttrOperator
    PLUG_CLS = MirrorPlaneRotatePlugOperator

    mirrorPlaneRotateX = DoubleAngleField(default_value=0.0)
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField(default_value=0.0)
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField(default_value=0.0)
    rz = mirrorPlaneRotateZ
