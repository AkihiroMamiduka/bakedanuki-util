# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.at.scalar.unit.range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
)


class Target_targetTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["Target_targetTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslateX", "ttx"),
        ("targetTranslateY", "tty"),
        ("targetTranslateZ", "ttz"),
    )

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetTranslatePlugOperator]
):
    __slots__ = ()

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetTranslateAttrOperator, Target_targetTranslatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetTranslateAttrOperator
    PLUG_CLS = Target_targetTranslatePlugOperator

    targetTranslateX = DoubleLinearField(default_value=0.0)
    ttx = targetTranslateX

    targetTranslateY = DoubleLinearField(default_value=0.0)
    tty = targetTranslateY

    targetTranslateZ = DoubleLinearField(default_value=0.0)
    ttz = targetTranslateZ


class Target_targetRotatePivotPlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotatePivotAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotatePivotX", "trpx"),
        ("targetRotatePivotY", "trpy"),
        ("targetRotatePivotZ", "trpz"),
    )

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[Target_targetRotatePivotPlugOperator]
):
    __slots__ = ()

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotatePivotField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotatePivotAttrOperator,
        Target_targetRotatePivotPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotatePivotAttrOperator
    PLUG_CLS = Target_targetRotatePivotPlugOperator

    targetRotatePivotX = DoubleLinearField(default_value=0.0)
    trpx = targetRotatePivotX

    targetRotatePivotY = DoubleLinearField(default_value=0.0)
    trpy = targetRotatePivotY

    targetRotatePivotZ = DoubleLinearField(default_value=0.0)
    trpz = targetRotatePivotZ


class Target_targetRotateTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator[
        "Target_targetRotateTranslateAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateTranslateX", "trtx"),
        ("targetRotateTranslateY", "trty"),
        ("targetRotateTranslateZ", "trtz"),
    )

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[
        Target_targetRotateTranslatePlugOperator
    ]
):
    __slots__ = ()

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class Target_targetRotateTranslateField(
    DoubleLinear3CompoundBaseField[
        Target_targetRotateTranslateAttrOperator,
        Target_targetRotateTranslatePlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateTranslateAttrOperator
    PLUG_CLS = Target_targetRotateTranslatePlugOperator

    targetRotateTranslateX = DoubleLinearField(default_value=0.0)
    trtx = targetRotateTranslateX

    targetRotateTranslateY = DoubleLinearField(default_value=0.0)
    trty = targetRotateTranslateY

    targetRotateTranslateZ = DoubleLinearField(default_value=0.0)
    trtz = targetRotateTranslateZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
    )

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0)
    tw = targetWeight


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetTranslate = Target_targetTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    tt = targetTranslate

    targetRotatePivot = Target_targetRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    trp = targetRotatePivot

    targetRotateTranslate = Target_targetRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    trt = targetRotateTranslate

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0)
    tw = targetWeight


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
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
    Double3CompoundBaseField[
        WorldUpVectorAttrOperator, WorldUpVectorPlugOperator
    ]
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
    DoubleAngle3CompoundBaseField[
        ConstraintRotateAttrOperator, ConstraintRotatePlugOperator
    ]
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
