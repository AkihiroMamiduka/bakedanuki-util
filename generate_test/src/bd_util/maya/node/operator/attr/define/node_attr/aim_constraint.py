# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
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
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
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

    constraintTranslateX = DoubleLinearField(default_value=0.0)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0)
    ctz = constraintTranslateZ


class ConstraintRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotatePivotAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotatePivotX", "crpx"),
        ("constraintRotatePivotY", "crpy"),
        ("constraintRotatePivotZ", "crpz"),
    )

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotatePivotField(
    DoubleLinear3CompoundBaseField[ConstraintRotatePivotAttrOperator, ConstraintRotatePivotPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotatePivotAttrOperator
    PLUG_CLS = ConstraintRotatePivotPlugOperator

    constraintRotatePivotX = DoubleLinearField(default_value=0.0)
    crpx = constraintRotatePivotX

    constraintRotatePivotY = DoubleLinearField(default_value=0.0)
    crpy = constraintRotatePivotY

    constraintRotatePivotZ = DoubleLinearField(default_value=0.0)
    crpz = constraintRotatePivotZ


class ConstraintRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintRotateTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintRotateTranslateX", "crtx"),
        ("constraintRotateTranslateY", "crty"),
        ("constraintRotateTranslateZ", "crtz"),
    )

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintRotateTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintRotateTranslateAttrOperator, ConstraintRotateTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateTranslateAttrOperator
    PLUG_CLS = ConstraintRotateTranslatePlugOperator

    constraintRotateTranslateX = DoubleLinearField(default_value=0.0)
    crtx = constraintRotateTranslateX

    constraintRotateTranslateY = DoubleLinearField(default_value=0.0)
    crty = constraintRotateTranslateY

    constraintRotateTranslateZ = DoubleLinearField(default_value=0.0)
    crtz = constraintRotateTranslateZ


class ConstraintJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["ConstraintJointOrientAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintJointOrientX", "cjox"),
        ("constraintJointOrientY", "cjoy"),
        ("constraintJointOrientZ", "cjoz"),
    )

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class ConstraintJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[ConstraintJointOrientPlugOperator]
):
    __slots__ = ()

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class ConstraintJointOrientField(
    DoubleAngle3CompoundBaseField[ConstraintJointOrientAttrOperator, ConstraintJointOrientPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintJointOrientAttrOperator
    PLUG_CLS = ConstraintJointOrientPlugOperator

    constraintJointOrientX = DoubleAngleField(default_value=0.0)
    cjox = constraintJointOrientX

    constraintJointOrientY = DoubleAngleField(default_value=0.0)
    cjoy = constraintJointOrientY

    constraintJointOrientZ = DoubleAngleField(default_value=0.0)
    cjoz = constraintJointOrientZ


class InverseScalePlugOperator(
    Double3CompoundBasePlugOperator["InverseScaleAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inverseScaleX", "isx"),
        ("inverseScaleY", "isy"),
        ("inverseScaleZ", "isz"),
    )

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


class InverseScaleAttrOperator(
    Double3CompoundBaseAttrOperator[InverseScalePlugOperator]
):
    __slots__ = ()

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


class InverseScaleField(
    Double3CompoundBaseField[InverseScaleAttrOperator, InverseScalePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InverseScaleAttrOperator
    PLUG_CLS = InverseScalePlugOperator

    inverseScaleX = DoubleField(default_value=1.0)
    isx = inverseScaleX

    inverseScaleY = DoubleField(default_value=1.0)
    isy = inverseScaleY

    inverseScaleZ = DoubleField(default_value=1.0)
    isz = inverseScaleZ


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


class ConstraintVectorPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintVectorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintVectorX", "cvx"),
        ("constraintVectorY", "cvy"),
        ("constraintVectorZ", "cvz"),
    )

    constraintVectorX = DoubleLinearField(default_value=0.0, writable=False)
    cvx = constraintVectorX

    constraintVectorY = DoubleLinearField(default_value=0.0, writable=False)
    cvy = constraintVectorY

    constraintVectorZ = DoubleLinearField(default_value=0.0, writable=False)
    cvz = constraintVectorZ


class ConstraintVectorAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintVectorPlugOperator]
):
    __slots__ = ()

    constraintVectorX = DoubleLinearField(default_value=0.0, writable=False)
    cvx = constraintVectorX

    constraintVectorY = DoubleLinearField(default_value=0.0, writable=False)
    cvy = constraintVectorY

    constraintVectorZ = DoubleLinearField(default_value=0.0, writable=False)
    cvz = constraintVectorZ


class ConstraintVectorField(
    DoubleLinear3CompoundBaseField[ConstraintVectorAttrOperator, ConstraintVectorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintVectorAttrOperator
    PLUG_CLS = ConstraintVectorPlugOperator

    constraintVectorX = DoubleLinearField(default_value=0.0, writable=False)
    cvx = constraintVectorX

    constraintVectorY = DoubleLinearField(default_value=0.0, writable=False)
    cvy = constraintVectorY

    constraintVectorZ = DoubleLinearField(default_value=0.0, writable=False)
    cvz = constraintVectorZ


class OffsetPlugOperator(
    DoubleAngle3CompoundBasePlugOperator["OffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("offsetX", "ox"),
        ("offsetY", "oy"),
        ("offsetZ", "oz"),
    )

    offsetX = DoubleAngleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleAngleField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleAngleField(default_value=0.0)
    oz = offsetZ


class OffsetAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[OffsetPlugOperator]
):
    __slots__ = ()

    offsetX = DoubleAngleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleAngleField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleAngleField(default_value=0.0)
    oz = offsetZ


class OffsetField(
    DoubleAngle3CompoundBaseField[OffsetAttrOperator, OffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OffsetAttrOperator
    PLUG_CLS = OffsetPlugOperator

    offsetX = DoubleAngleField(default_value=0.0)
    ox = offsetX

    offsetY = DoubleAngleField(default_value=0.0)
    oy = offsetY

    offsetZ = DoubleAngleField(default_value=0.0)
    oz = offsetZ


class RestRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["RestRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restRotateX", "rrx"),
        ("restRotateY", "rry"),
        ("restRotateZ", "rrz"),
    )

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[RestRotatePlugOperator]
):
    __slots__ = ()

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ


class RestRotateField(
    DoubleAngle3CompoundBaseField[RestRotateAttrOperator, RestRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestRotateAttrOperator
    PLUG_CLS = RestRotatePlugOperator

    restRotateX = DoubleAngleField(default_value=0.0)
    rrx = restRotateX

    restRotateY = DoubleAngleField(default_value=0.0)
    rry = restRotateY

    restRotateZ = DoubleAngleField(default_value=0.0)
    rrz = restRotateZ
