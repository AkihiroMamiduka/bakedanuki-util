# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.unit.range.double_angle import DoubleAngleField
from ..std.dt.matrix import DataMatrixField
from ..custom import (
    DoubleAngle3CompoundBaseAttrOperator,
    DoubleAngle3CompoundBasePlugOperator,
    DoubleAngle3CompoundBaseField,
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)


class Target_targetRotateOrderEnumPlugOperator(
    EnumPlugOperator["Target_targetRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class Target_targetRotateOrderEnumAttrOperator(
    EnumAttrOperator[Target_targetRotateOrderEnumPlugOperator]
):
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


class Target_targetRotateOrderEnumField(
    EnumField[
        Target_targetRotateOrderEnumAttrOperator,
        Target_targetRotateOrderEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateOrderEnumAttrOperator
    PLUG_CLS = Target_targetRotateOrderEnumPlugOperator


class Target_targetRotatePlugOperator(
    DoubleAngle3CompoundBasePlugOperator["Target_targetRotateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateX", "trx"),
        ("targetRotateY", "try"),
        ("targetRotateZ", "trz"),
    )

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetRotateAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetRotatePlugOperator]
):
    __slots__ = ()

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetRotateField(
    DoubleAngle3CompoundBaseField[
        Target_targetRotateAttrOperator, Target_targetRotatePlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateAttrOperator
    PLUG_CLS = Target_targetRotatePlugOperator

    targetRotateX = DoubleAngleField(default_value=0.0)
    trx = targetRotateX

    targetRotateY = DoubleAngleField(default_value=0.0)
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField(default_value=0.0)
    trz = targetRotateZ


class Target_targetJointOrientPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetJointOrientAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetJointOrientX", "tjox"),
        ("targetJointOrientY", "tjoy"),
        ("targetJointOrientZ", "tjoz"),
    )

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetJointOrientAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetJointOrientPlugOperator]
):
    __slots__ = ()

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetJointOrientField(
    DoubleAngle3CompoundBaseField[
        Target_targetJointOrientAttrOperator,
        Target_targetJointOrientPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetJointOrientAttrOperator
    PLUG_CLS = Target_targetJointOrientPlugOperator

    targetJointOrientX = DoubleAngleField(default_value=0.0)
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField(default_value=0.0)
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField(default_value=0.0)
    tjoz = targetJointOrientZ


class Target_targetRotateCachedPlugOperator(
    DoubleAngle3CompoundBasePlugOperator[
        "Target_targetRotateCachedAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotateCachedX", "ctrx"),
        ("targetRotateCachedY", "ctry"),
        ("targetRotateCachedZ", "ctrz"),
    )

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class Target_targetRotateCachedAttrOperator(
    DoubleAngle3CompoundBaseAttrOperator[Target_targetRotateCachedPlugOperator]
):
    __slots__ = ()

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class Target_targetRotateCachedField(
    DoubleAngle3CompoundBaseField[
        Target_targetRotateCachedAttrOperator,
        Target_targetRotateCachedPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = Target_targetRotateCachedAttrOperator
    PLUG_CLS = Target_targetRotateCachedPlugOperator

    targetRotateCachedX = DoubleAngleField(default_value=0.0)
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField(default_value=0.0)
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField(default_value=0.0)
    ctrz = targetRotateCachedZ


class TargetPlugOperator(CompoundPlugOperator["TargetAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("targetRotate", "tr"),
        ("targetRotateOrder", "tro"),
        ("targetJointOrient", "tjo"),
        ("targetParentMatrix", "tpm"),
        ("targetWeight", "tw"),
        ("targetRotateCached", "ctr"),
    )

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Target_targetRotateCachedField(
        default_value=(0.0, 0.0, 0.0)
    )
    ctr = targetRotateCached


class TargetAttrOperator(CompoundAttrOperator[TargetPlugOperator]):
    __slots__ = ()

    targetRotate = Target_targetRotateField(default_value=(0.0, 0.0, 0.0))
    tr = targetRotate

    targetRotateOrder = Target_targetRotateOrderEnumField(default_value=0)
    tro = targetRotateOrder

    targetJointOrient = Target_targetJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    tjo = targetJointOrient

    targetParentMatrix = DataMatrixField()
    tpm = targetParentMatrix

    targetWeight = DoubleField(default_value=1.0, min_value=0.0)
    tw = targetWeight

    targetRotateCached = Target_targetRotateCachedField(
        default_value=(0.0, 0.0, 0.0)
    )
    ctr = targetRotateCached


class TargetField(CompoundField[TargetAttrOperator, TargetPlugOperator]):
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
    DoubleAngle3CompoundBaseField[
        LastTargetRotateAttrOperator, LastTargetRotatePlugOperator
    ]
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
    DoubleAngle3CompoundBaseField[
        ConstraintJointOrientAttrOperator, ConstraintJointOrientPlugOperator
    ]
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
    Double3CompoundBaseField[
        InverseScaleAttrOperator, InverseScalePlugOperator
    ]
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
    DoubleAngle3CompoundBaseField[
        RestRotateAttrOperator, RestRotatePlugOperator
    ]
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
