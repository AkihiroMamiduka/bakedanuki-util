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
        ("targetRotate", "tr"),
        ("targetRotateOrder", "tro"),
        ("targetJointOrient", "tjo"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
        ("targetRotateCached", "ctr"),
    )

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Double3Field(default_value=(0.0, 0.0, 0.0))
    ctr = targetRotateCached


class TargetAttrOperator(
    CompoundAttrOperator[TargetPlugOperator]
):
    __slots__ = ()

    targetRotate = Double3Field(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = TargetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Double3Field(default_value=(0.0, 0.0, 0.0))
    tjo = targetJointOrient

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Double3Field(default_value=(0.0, 0.0, 0.0))
    ctr = targetRotateCached


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
