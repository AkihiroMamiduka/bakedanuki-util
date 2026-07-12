# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.orient_constraint import (
    ConstraintJointOrientField,
    ConstraintRotateField,
    InverseScaleField,
    LastTargetRotateField,
    OffsetField,
    RestRotateField,
    TargetField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ....attr.define.std.dt.matrix import DataMatrixField


class ConstraintRotateOrderEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class ConstraintRotateOrderEnumAttrOperator(EnumAttrOperator):
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


class ConstraintRotateOrderEnumField(
    EnumField[ConstraintRotateOrderEnumAttrOperator, ConstraintRotateOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateOrderEnumAttrOperator
    PLUG_CLS = ConstraintRotateOrderEnumPlugOperator


class InterpTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_FLIP = 0
    AVERAGE = 1
    SHORTEST = 2
    LONGEST = 3
    CACHE = 4


class InterpTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_FLIP = 0
    AVERAGE = 1
    SHORTEST = 2
    LONGEST = 3
    CACHE = 4

    NAME_MAP = {
        NO_FLIP: "No Flip",
        AVERAGE: "Average",
        SHORTEST: "Shortest",
        LONGEST: "Longest",
        CACHE: "Cache",
    }


class InterpTypeEnumField(
    EnumField[InterpTypeEnumAttrOperator, InterpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpTypeEnumAttrOperator
    PLUG_CLS = InterpTypeEnumPlugOperator


class OrientConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "orientConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    targetRotateX = DoubleAngleField()
    trx = targetRotateX

    targetRotateY = DoubleAngleField()
    try_ = targetRotateY

    targetRotateZ = DoubleAngleField()
    trz = targetRotateZ

    targetJointOrientX = DoubleAngleField()
    tjox = targetJointOrientX

    targetJointOrientY = DoubleAngleField()
    tjoy = targetJointOrientY

    targetJointOrientZ = DoubleAngleField()
    tjoz = targetJointOrientZ

    targetRotateCachedX = DoubleAngleField()
    ctrx = targetRotateCachedX

    targetRotateCachedY = DoubleAngleField()
    ctry = targetRotateCachedY

    targetRotateCachedZ = DoubleAngleField()
    ctrz = targetRotateCachedZ

    lastTargetRotate = LastTargetRotateField(default_value=(0.0, 0.0, 0.0))
    lr = lastTargetRotate
    lastTargetRotateX = lastTargetRotate.lastTargetRotateX
    lrx = lastTargetRotateX
    lastTargetRotateY = lastTargetRotate.lastTargetRotateY
    lry = lastTargetRotateY
    lastTargetRotateZ = lastTargetRotate.lastTargetRotateZ
    lrz = lastTargetRotateZ

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0)
    cro = constraintRotateOrder

    constraintJointOrient = ConstraintJointOrientField(default_value=(0.0, 0.0, 0.0))
    cjo = constraintJointOrient
    constraintJointOrientX = constraintJointOrient.constraintJointOrientX
    cjox = constraintJointOrientX
    constraintJointOrientY = constraintJointOrient.constraintJointOrientY
    cjoy = constraintJointOrientY
    constraintJointOrientZ = constraintJointOrient.constraintJointOrientZ
    cjoz = constraintJointOrientZ

    scaleCompensate = BoolField(default_value=True)
    ssc = scaleCompensate

    inverseScale = InverseScaleField(default_value=(1.0, 1.0, 1.0))
    is_ = inverseScale
    inverseScaleX = inverseScale.inverseScaleX
    isx = inverseScaleX
    inverseScaleY = inverseScale.inverseScaleY
    isy = inverseScaleY
    inverseScaleZ = inverseScale.inverseScaleZ
    isz = inverseScaleZ

    constraintRotate = ConstraintRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ

    offset = OffsetField(default_value=(0.0, 0.0, 0.0))
    o = offset
    offsetX = offset.offsetX
    ox = offsetX
    offsetY = offset.offsetY
    oy = offsetY
    offsetZ = offset.offsetZ
    oz = offsetZ

    restRotate = RestRotateField(default_value=(0.0, 0.0, 0.0))
    rsrr = restRotate
    restRotateX = restRotate.restRotateX
    rrx = restRotateX
    restRotateY = restRotate.restRotateY
    rry = restRotateY
    restRotateZ = restRotate.restRotateZ
    rrz = restRotateZ

    interpType = InterpTypeEnumField(default_value=1)
    int = interpType

    interpCache = LongField(default_value=0)
    inc = interpCache

    useOldOffsetCalculation = BoolField(default_value=False)
    uooc = useOldOffsetCalculation
