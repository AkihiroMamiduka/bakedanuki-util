# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.unit_scalar_range.double_angle import DoubleAngleField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..std.dt.matrix import DataMatrixField
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


class TargetRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class TargetRotateOrderEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5

    NAME_MAP = {
        XYZ: "xyz",
        YZX: "yzx",
        ZXY: "zxy",
        XZY: "xzy",
        YXZ: "yxz",
        ZYX: "zyx",
    }


class TargetRotateOrderEnumField(
    EnumField[TargetRotateOrderEnumAttrOperator, TargetRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetRotateOrderEnumAttrOperator
    PLUG_CLS = TargetRotateOrderEnumPlugOperator


class TargetPlugOperator(
    CompoundPlugOperator["TargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
        ("targetRotateCached", "ctr"),
        ("targetTranslate", "tt"),
        ("targetRotatePivot", "trp"),
        ("targetRotateTranslate", "trt"),
        ("targetOffsetTranslate", "tot"),
        ("targetRotate", "tr"),
        ("targetRotateOrder", "tro"),
        ("targetJointOrient", "tjo"),
        ("targetOffsetRotate", "tor"),
        ("targetScaleCompensate", "tsc"),
        ("targetInverseScale", "tis"),
        ("targetScale", "ts"),
    )

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Double3Field(default_value=(0.0, 0.0, 0.0))
    ctr = targetRotateCached

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetOffsetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tot = targetOffsetTranslate

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetOffsetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tor = targetOffsetRotate

    targetScaleCompensate = BoolField(default_value=True)
    tsc = targetScaleCompensate

    targetInverseScale = Double3Field(default_value=(1.0, 1.0, 1.0))
    tis = targetInverseScale

    targetScale = Double3Field(default_value=(1.0, 1.0, 1.0))
    ts = targetScale


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Double3Field(default_value=(0.0, 0.0, 0.0))
    ctr = targetRotateCached

    targetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tt = targetTranslate

    targetRotatePivot = Double3Field(default_value=(0.0, 0.0, 0.0))
    trp = targetRotatePivot

    targetRotateTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    trt = targetRotateTranslate

    targetOffsetTranslate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tot = targetOffsetTranslate

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetOffsetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tor = targetOffsetRotate

    targetScaleCompensate = BoolField(default_value=True)
    tsc = targetScaleCompensate

    targetInverseScale = Double3Field(default_value=(1.0, 1.0, 1.0))
    tis = targetInverseScale

    targetScale = Double3Field(default_value=(1.0, 1.0, 1.0))
    ts = targetScale


class TargetField(
    CompoundField[TargetAttrOperator, TargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetAttrOperator
    PLUG_CLS = TargetPlugOperator


class LastTargetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["LastTargetRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("lastTargetRotateX", "lrx"),
        ("lastTargetRotateY", "lry"),
        ("lastTargetRotateZ", "lrz"),
    )

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


class LastTargetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[LastTargetRotatePlugOperator]
):
    __slots__ = ()

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


class LastTargetRotateField(
    DoubleAngle3CompoundBaseField[LastTargetRotateAttrOperator, LastTargetRotatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LastTargetRotateAttrOperator
    PLUG_CLS = LastTargetRotatePlugOperator

    lastTargetRotateX = DoubleAngleField(default_value=0.0)
    lrx = lastTargetRotateX

    lastTargetRotateY = DoubleAngleField(default_value=0.0)
    lry = lastTargetRotateY

    lastTargetRotateZ = DoubleAngleField(default_value=0.0)
    lrz = lastTargetRotateZ


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


class ConstraintTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["ConstraintTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("constraintTranslateX", "ctx"),
        ("constraintTranslateY", "cty"),
        ("constraintTranslateZ", "ctz"),
    )

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class ConstraintTranslateField(
    DoubleLinear3CompoundBaseField[ConstraintTranslateAttrOperator, ConstraintTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTranslateAttrOperator
    PLUG_CLS = ConstraintTranslatePlugOperator

    constraintTranslateX = DoubleLinearField(default_value=0.0, writable=False)
    ctx = constraintTranslateX

    constraintTranslateY = DoubleLinearField(default_value=0.0, writable=False)
    cty = constraintTranslateY

    constraintTranslateZ = DoubleLinearField(default_value=0.0, writable=False)
    ctz = constraintTranslateZ


class RestTranslatePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RestTranslateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("restTranslateX", "rtx"),
        ("restTranslateY", "rty"),
        ("restTranslateZ", "rtz"),
    )

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RestTranslatePlugOperator]
):
    __slots__ = ()

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


class RestTranslateField(
    DoubleLinear3CompoundBaseField[RestTranslateAttrOperator, RestTranslatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RestTranslateAttrOperator
    PLUG_CLS = RestTranslatePlugOperator

    restTranslateX = DoubleLinearField(default_value=0.0)
    rtx = restTranslateX

    restTranslateY = DoubleLinearField(default_value=0.0)
    rty = restTranslateY

    restTranslateZ = DoubleLinearField(default_value=0.0)
    rtz = restTranslateZ


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


class RotationDecompositionTargetPlugOperator(
    DoubleLinear3CompoundBasePlugOperator["RotationDecompositionTargetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("rotationDecompositionTargetX", "rdtx"),
        ("rotationDecompositionTargetY", "rdty"),
        ("rotationDecompositionTargetZ", "rdtz"),
    )

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ


class RotationDecompositionTargetAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[RotationDecompositionTargetPlugOperator]
):
    __slots__ = ()

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ


class RotationDecompositionTargetField(
    DoubleLinear3CompoundBaseField[RotationDecompositionTargetAttrOperator, RotationDecompositionTargetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RotationDecompositionTargetAttrOperator
    PLUG_CLS = RotationDecompositionTargetPlugOperator

    rotationDecompositionTargetX = DoubleLinearField(default_value=0.0)
    rdtx = rotationDecompositionTargetX

    rotationDecompositionTargetY = DoubleLinearField(default_value=0.0)
    rdty = rotationDecompositionTargetY

    rotationDecompositionTargetZ = DoubleLinearField(default_value=0.0)
    rdtz = rotationDecompositionTargetZ
