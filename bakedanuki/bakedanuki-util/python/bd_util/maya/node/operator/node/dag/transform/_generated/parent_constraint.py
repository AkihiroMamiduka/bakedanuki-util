# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.parent_constraint import (
    ConstraintJointOrientField,
    ConstraintRotateField,
    ConstraintRotatePivotField,
    ConstraintRotateTranslateField,
    ConstraintTranslateField,
    LastTargetRotateField,
    RestRotateField,
    RestTranslateField,
    RotationDecompositionTargetField,
    TargetField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.dt.matrix import DataMatrixField


class ConstraintRotateOrderEnumPlugOperator(
    EnumPlugOperator["ConstraintRotateOrderEnumAttrOperator"]
):
    __slots__ = ()

    XYZ = 0
    YZX = 1
    ZXY = 2
    XZY = 3
    YXZ = 4
    ZYX = 5


class ConstraintRotateOrderEnumAttrOperator(
    EnumAttrOperator[ConstraintRotateOrderEnumPlugOperator]
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


class ConstraintRotateOrderEnumField(
    EnumField[
        ConstraintRotateOrderEnumAttrOperator,
        ConstraintRotateOrderEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConstraintRotateOrderEnumAttrOperator
    PLUG_CLS = ConstraintRotateOrderEnumPlugOperator


class InterpTypeEnumPlugOperator(
    EnumPlugOperator["InterpTypeEnumAttrOperator"]
):
    __slots__ = ()

    NO_FLIP = 0
    AVERAGE = 1
    SHORTEST = 2
    LONGEST = 3
    CACHE = 4


class InterpTypeEnumAttrOperator(EnumAttrOperator[InterpTypeEnumPlugOperator]):
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


class GeneratedParentConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "parentConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    lastTargetRotate = LastTargetRotateField(default_value=(0.0, 0.0, 0.0))
    lr = lastTargetRotate
    lastTargetRotateX = lastTargetRotate.lastTargetRotateX
    lrx = lastTargetRotateX
    lastTargetRotateY = lastTargetRotate.lastTargetRotateY
    lry = lastTargetRotateY
    lastTargetRotateZ = lastTargetRotate.lastTargetRotateZ
    lrz = lastTargetRotateZ

    constraintRotatePivot = ConstraintRotatePivotField(
        default_value=(0.0, 0.0, 0.0)
    )
    crp = constraintRotatePivot
    constraintRotatePivotX = constraintRotatePivot.constraintRotatePivotX
    crpx = constraintRotatePivotX
    constraintRotatePivotY = constraintRotatePivot.constraintRotatePivotY
    crpy = constraintRotatePivotY
    constraintRotatePivotZ = constraintRotatePivot.constraintRotatePivotZ
    crpz = constraintRotatePivotZ

    constraintRotateTranslate = ConstraintRotateTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    crt = constraintRotateTranslate
    constraintRotateTranslateX = (
        constraintRotateTranslate.constraintRotateTranslateX
    )
    crtx = constraintRotateTranslateX
    constraintRotateTranslateY = (
        constraintRotateTranslate.constraintRotateTranslateY
    )
    crty = constraintRotateTranslateY
    constraintRotateTranslateZ = (
        constraintRotateTranslate.constraintRotateTranslateZ
    )
    crtz = constraintRotateTranslateZ

    constraintTranslate = ConstraintTranslateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    ct = constraintTranslate
    constraintTranslateX = constraintTranslate.constraintTranslateX
    ctx = constraintTranslateX
    constraintTranslateY = constraintTranslate.constraintTranslateY
    cty = constraintTranslateY
    constraintTranslateZ = constraintTranslate.constraintTranslateZ
    ctz = constraintTranslateZ

    restTranslate = RestTranslateField(default_value=(0.0, 0.0, 0.0))
    rst = restTranslate
    restTranslateX = restTranslate.restTranslateX
    rtx = restTranslateX
    restTranslateY = restTranslate.restTranslateY
    rty = restTranslateY
    restTranslateZ = restTranslate.restTranslateZ
    rtz = restTranslateZ

    constraintRotateOrder = ConstraintRotateOrderEnumField(default_value=0)
    cro = constraintRotateOrder

    constraintJointOrient = ConstraintJointOrientField(
        default_value=(0.0, 0.0, 0.0)
    )
    cjo = constraintJointOrient
    constraintJointOrientX = constraintJointOrient.constraintJointOrientX
    cjox = constraintJointOrientX
    constraintJointOrientY = constraintJointOrient.constraintJointOrientY
    cjoy = constraintJointOrientY
    constraintJointOrientZ = constraintJointOrient.constraintJointOrientZ
    cjoz = constraintJointOrientZ

    constraintRotate = ConstraintRotateField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ

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

    rotationDecompositionTarget = RotationDecompositionTargetField(
        default_value=(0.0, 0.0, 0.0)
    )
    rdta = rotationDecompositionTarget
    rotationDecompositionTargetX = (
        rotationDecompositionTarget.rotationDecompositionTargetX
    )
    rdtx = rotationDecompositionTargetX
    rotationDecompositionTargetY = (
        rotationDecompositionTarget.rotationDecompositionTargetY
    )
    rdty = rotationDecompositionTargetY
    rotationDecompositionTargetZ = (
        rotationDecompositionTarget.rotationDecompositionTargetZ
    )
    rdtz = rotationDecompositionTargetZ

    useDecompositionTarget = BoolField(default_value=False)
    udt = useDecompositionTarget
