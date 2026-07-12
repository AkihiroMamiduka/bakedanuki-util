# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.dt.matrix import DataMatrixField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field
from ..custom.at.scalar_compound.unit_compound.angle_compound.double3._base import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
    )

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0)
    tw = targetWeight


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0)
    tw = targetWeight


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class AimVectorPlugOperator(
    Double3CompoundBasePlugOperator["AimVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("aimVectorX", "ax"),
        ("aimVectorY", "ay"),
        ("aimVectorZ", "az"),
    )

    aimVectorX = DoubleField(default_value=1.0)
    ax = aimVectorX

    aimVectorY = DoubleField(default_value=0.0)
    ay = aimVectorY

    aimVectorZ = DoubleField(default_value=0.0)
    az = aimVectorZ


class AimVectorAttrOperator(
    Double3CompoundBaseAttrOperator[AimVectorPlugOperator]
):
    __slots__ = ()

    aimVectorX = DoubleField(default_value=1.0)
    ax = aimVectorX

    aimVectorY = DoubleField(default_value=0.0)
    ay = aimVectorY

    aimVectorZ = DoubleField(default_value=0.0)
    az = aimVectorZ


class AimVectorField(
    Double3CompoundBaseField[AimVectorAttrOperator, AimVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AimVectorAttrOperator
    PLUG_CLS = AimVectorPlugOperator

    aimVectorX = DoubleField(default_value=1.0)
    ax = aimVectorX

    aimVectorY = DoubleField(default_value=0.0)
    ay = aimVectorY

    aimVectorZ = DoubleField(default_value=0.0)
    az = aimVectorZ


class UpVectorPlugOperator(
    Double3CompoundBasePlugOperator["UpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("upVectorX", "ux"),
        ("upVectorY", "uy"),
        ("upVectorZ", "uz"),
    )

    upVectorX = DoubleField(default_value=0.0)
    ux = upVectorX

    upVectorY = DoubleField(default_value=1.0)
    uy = upVectorY

    upVectorZ = DoubleField(default_value=0.0)
    uz = upVectorZ


class UpVectorAttrOperator(
    Double3CompoundBaseAttrOperator[UpVectorPlugOperator]
):
    __slots__ = ()

    upVectorX = DoubleField(default_value=0.0)
    ux = upVectorX

    upVectorY = DoubleField(default_value=1.0)
    uy = upVectorY

    upVectorZ = DoubleField(default_value=0.0)
    uz = upVectorZ


class UpVectorField(
    Double3CompoundBaseField[UpVectorAttrOperator, UpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UpVectorAttrOperator
    PLUG_CLS = UpVectorPlugOperator

    upVectorX = DoubleField(default_value=0.0)
    ux = upVectorX

    upVectorY = DoubleField(default_value=1.0)
    uy = upVectorY

    upVectorZ = DoubleField(default_value=0.0)
    uz = upVectorZ


class WorldUpVectorPlugOperator(
    Double3CompoundBasePlugOperator["WorldUpVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("worldUpVectorX", "wux"),
        ("worldUpVectorY", "wuy"),
        ("worldUpVectorZ", "wuz"),
    )

    worldUpVectorX = DoubleField(default_value=0.0)
    wux = worldUpVectorX

    worldUpVectorY = DoubleField(default_value=1.0)
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField(default_value=0.0)
    wuz = worldUpVectorZ


class WorldUpVectorAttrOperator(
    Double3CompoundBaseAttrOperator[WorldUpVectorPlugOperator]
):
    __slots__ = ()

    worldUpVectorX = DoubleField(default_value=0.0)
    wux = worldUpVectorX

    worldUpVectorY = DoubleField(default_value=1.0)
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField(default_value=0.0)
    wuz = worldUpVectorZ


class WorldUpVectorField(
    Double3CompoundBaseField[WorldUpVectorAttrOperator, WorldUpVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldUpVectorAttrOperator
    PLUG_CLS = WorldUpVectorPlugOperator

    worldUpVectorX = DoubleField(default_value=0.0)
    wux = worldUpVectorX

    worldUpVectorY = DoubleField(default_value=1.0)
    wuy = worldUpVectorY

    worldUpVectorZ = DoubleField(default_value=0.0)
    wuz = worldUpVectorZ


class ConstraintRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateX", "crx"),
        ("constraintRotateY", "cry"),
        ("constraintRotateZ", "crz"),
    )

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintRotatePlugOperator]
):
    __slots__ = ()

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ


class ConstraintRotateField(
    DoubleAngle3CompoundBaseField[ConstraintRotateAttrOperator, ConstraintRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateAttrOperator
    PLUG_CLS = ConstraintRotatePlugOperator

    constraintRotateX = DoubleAngleField(default_value=0.0, writable=False)
    crx = constraintRotateX

    constraintRotateY = DoubleAngleField(default_value=0.0, writable=False)
    cry = constraintRotateY

    constraintRotateZ = DoubleAngleField(default_value=0.0, writable=False)
    crz = constraintRotateZ
