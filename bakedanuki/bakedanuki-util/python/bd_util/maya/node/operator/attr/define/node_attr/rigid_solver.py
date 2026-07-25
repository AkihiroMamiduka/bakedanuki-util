# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.vector_array import DataVectorArrayField
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


class GeneralForcePlugOperator(
    CompoundPlugOperator["GeneralForceAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inputForce", "ifr"),
        ("inputTorque", "itr"),
    )

    inputForce = DataVectorArrayField()
    ifr = inputForce

    inputTorque = DataVectorArrayField()
    itr = inputTorque


class GeneralForceAttrOperator(
    CompoundAttrOperator[GeneralForcePlugOperator]
):
    __slots__ = ()

    inputForce = DataVectorArrayField()
    ifr = inputForce

    inputTorque = DataVectorArrayField()
    itr = inputTorque


class GeneralForceField(
    CompoundField[GeneralForceAttrOperator, GeneralForcePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GeneralForceAttrOperator
    PLUG_CLS = GeneralForcePlugOperator


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


class ConstraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslateX", "ctx"),
        ("constraintTranslateY", "cty"),
        ("constraintTranslateZ", "ctz"),
    )

    constraintTranslateX = DoubleLinearField(default_value=0.0)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0)
    ctz = constraintTranslateZ


class ConstraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0)
    ctz = constraintTranslateZ


class ConstraintTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTranslateAttrOperator
    PLUG_CLS = ConstraintTranslatePlugOperator


class ConstraintRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateX", "crx"),
        ("constraintRotateY", "cry"),
        ("constraintRotateZ", "crz"),
    )

    constraintRotateX = DoubleAngleField(default_value=0.0)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0)
    crz = constraintRotateZ


class ConstraintRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintRotatePlugOperator]
):
    __slots__ = ()

    constraintRotateX = DoubleAngleField(default_value=0.0)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0)
    crz = constraintRotateZ


class ConstraintRotateField(
    DoubleAngle3CompoundBaseField[ConstraintRotateAttrOperator, ConstraintRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateAttrOperator
    PLUG_CLS = ConstraintRotatePlugOperator
