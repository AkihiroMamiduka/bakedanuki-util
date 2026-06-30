# coding: utf-8

from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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


class PivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotX", "px"),
        ("pivotY", "py"),
        ("pivotZ", "pz"),
    )

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotPlugOperator]
):
    __slots__ = ()

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
    pz = pivotZ


class PivotField(
    DoubleLinear3CompoundBaseField[PivotAttrOperator, PivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotAttrOperator
    PLUG_CLS = PivotPlugOperator

    pivotX = DoubleLinearField()
    px = pivotX

    pivotY = DoubleLinearField()
    py = pivotY

    pivotZ = DoubleLinearField()
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

    scalePivotX = DoubleLinearField()
    spx = scalePivotX

    scalePivotY = DoubleLinearField()
    spy = scalePivotY

    scalePivotZ = DoubleLinearField()
    spz = scalePivotZ


class ScalePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ScalePivotPlugOperator]
):
    __slots__ = ()

    scalePivotX = DoubleLinearField()
    spx = scalePivotX

    scalePivotY = DoubleLinearField()
    spy = scalePivotY

    scalePivotZ = DoubleLinearField()
    spz = scalePivotZ


class ScalePivotField(
    DoubleLinear3CompoundBaseField[ScalePivotAttrOperator, ScalePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScalePivotAttrOperator
    PLUG_CLS = ScalePivotPlugOperator

    scalePivotX = DoubleLinearField()
    spx = scalePivotX

    scalePivotY = DoubleLinearField()
    spy = scalePivotY

    scalePivotZ = DoubleLinearField()
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

    mirrorPlaneCenterX = DoubleLinearField()
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField()
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField()
    pcz = mirrorPlaneCenterZ


class MirrorPlaneCenterAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[MirrorPlaneCenterPlugOperator]
):
    __slots__ = ()

    mirrorPlaneCenterX = DoubleLinearField()
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField()
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField()
    pcz = mirrorPlaneCenterZ


class MirrorPlaneCenterField(
    DoubleLinear3CompoundBaseField[MirrorPlaneCenterAttrOperator, MirrorPlaneCenterPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorPlaneCenterAttrOperator
    PLUG_CLS = MirrorPlaneCenterPlugOperator

    mirrorPlaneCenterX = DoubleLinearField()
    pcx = mirrorPlaneCenterX

    mirrorPlaneCenterY = DoubleLinearField()
    pcy = mirrorPlaneCenterY

    mirrorPlaneCenterZ = DoubleLinearField()
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

    mirrorPlaneRotateX = DoubleAngleField()
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField()
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField()
    rz = mirrorPlaneRotateZ


class MirrorPlaneRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[MirrorPlaneRotatePlugOperator]
):
    __slots__ = ()

    mirrorPlaneRotateX = DoubleAngleField()
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField()
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField()
    rz = mirrorPlaneRotateZ


class MirrorPlaneRotateField(
    DoubleAngle3CompoundBaseField[MirrorPlaneRotateAttrOperator, MirrorPlaneRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MirrorPlaneRotateAttrOperator
    PLUG_CLS = MirrorPlaneRotatePlugOperator

    mirrorPlaneRotateX = DoubleAngleField()
    rx = mirrorPlaneRotateX

    mirrorPlaneRotateY = DoubleAngleField()
    ry = mirrorPlaneRotateY

    mirrorPlaneRotateZ = DoubleAngleField()
    rz = mirrorPlaneRotateZ
