# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
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


class PivotOffsetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PivotOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("pivotOffsetX", "px"),
        ("pivotOffsetY", "py"),
        ("pivotOffsetZ", "pz"),
    )

    pivotOffsetX = DoubleLinearField(default_value=0.0)
    px = pivotOffsetX

    pivotOffsetY = DoubleLinearField(default_value=0.0)
    py = pivotOffsetY

    pivotOffsetZ = DoubleLinearField(default_value=0.0)
    pz = pivotOffsetZ


class PivotOffsetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PivotOffsetPlugOperator]
):
    __slots__ = ()

    pivotOffsetX = DoubleLinearField(default_value=0.0)
    px = pivotOffsetX

    pivotOffsetY = DoubleLinearField(default_value=0.0)
    py = pivotOffsetY

    pivotOffsetZ = DoubleLinearField(default_value=0.0)
    pz = pivotOffsetZ


class PivotOffsetField(
    DoubleLinear3CompoundBaseField[PivotOffsetAttrOperator, PivotOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PivotOffsetAttrOperator
    PLUG_CLS = PivotOffsetPlugOperator

    pivotOffsetX = DoubleLinearField(default_value=0.0)
    px = pivotOffsetX

    pivotOffsetY = DoubleLinearField(default_value=0.0)
    py = pivotOffsetY

    pivotOffsetZ = DoubleLinearField(default_value=0.0)
    pz = pivotOffsetZ


class PreRotationPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["PreRotationAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("preRotationX", "prx"),
        ("preRotationY", "pry"),
        ("preRotationZ", "prz"),
    )

    preRotationX = DoubleAngleField(default_value=0.0)
    prx = preRotationX

    preRotationY = DoubleAngleField(default_value=0.0)
    pry = preRotationY

    preRotationZ = DoubleAngleField(default_value=0.0)
    prz = preRotationZ


class PreRotationAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[PreRotationPlugOperator]
):
    __slots__ = ()

    preRotationX = DoubleAngleField(default_value=0.0)
    prx = preRotationX

    preRotationY = DoubleAngleField(default_value=0.0)
    pry = preRotationY

    preRotationZ = DoubleAngleField(default_value=0.0)
    prz = preRotationZ


class PreRotationField(
    DoubleAngle3CompoundBaseField[PreRotationAttrOperator, PreRotationPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PreRotationAttrOperator
    PLUG_CLS = PreRotationPlugOperator

    preRotationX = DoubleAngleField(default_value=0.0)
    prx = preRotationX

    preRotationY = DoubleAngleField(default_value=0.0)
    pry = preRotationY

    preRotationZ = DoubleAngleField(default_value=0.0)
    prz = preRotationZ


class ColorPlugOperator(
    Float3CompoundBasePlugOperator["ColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("colorR", "clr"),
        ("colorG", "clg"),
        ("colorB", "clb"),
    )

    colorR = FloatField(default_value=1.0)
    clr = colorR

    colorG = FloatField(default_value=0.0)
    clg = colorG

    colorB = FloatField(default_value=0.0)
    clb = colorB


class ColorAttrOperator(
    Float3CompoundBaseAttrOperator[ColorPlugOperator]
):
    __slots__ = ()

    colorR = FloatField(default_value=1.0)
    clr = colorR

    colorG = FloatField(default_value=0.0)
    clg = colorG

    colorB = FloatField(default_value=0.0)
    clb = colorB


class ColorField(
    Float3CompoundBaseField[ColorAttrOperator, ColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorAttrOperator
    PLUG_CLS = ColorPlugOperator

    colorR = FloatField(default_value=1.0)
    clr = colorR

    colorG = FloatField(default_value=0.0)
    clg = colorG

    colorB = FloatField(default_value=0.0)
    clb = colorB
