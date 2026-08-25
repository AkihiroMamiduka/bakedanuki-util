# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.aim_constraint import (
    AimVectorField,
    ConstraintJointOrientField,
    ConstraintRotateField,
    ConstraintRotatePivotField,
    ConstraintRotateTranslateField,
    ConstraintTranslateField,
    ConstraintVectorField,
    InverseScaleField,
    OffsetField,
    RestRotateField,
    TargetField,
    UpVectorField,
    WorldUpVectorField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.dt.matrix import DataMatrixField


class WorldUpTypeEnumPlugOperator(
    EnumPlugOperator["WorldUpTypeEnumAttrOperator"]
):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_ROTATION_UP = 2
    VECTOR = 3
    NONE = 4


class WorldUpTypeEnumAttrOperator(
    EnumAttrOperator[WorldUpTypeEnumPlugOperator]
):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_ROTATION_UP = 2
    VECTOR = 3
    NONE = 4

    NAME_MAP = {
        SCENE_UP: "Scene Up",
        OBJECT_UP: "Object Up",
        OBJECT_ROTATION_UP: "Object Rotation Up",
        VECTOR: "Vector",
        NONE: "None",
    }


class WorldUpTypeEnumField(
    EnumField[WorldUpTypeEnumAttrOperator, WorldUpTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WorldUpTypeEnumAttrOperator
    PLUG_CLS = WorldUpTypeEnumPlugOperator


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


class GeneratedAimConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "aimConstraint"

    enableRestPosition = BoolField(default_value=False)
    erp = enableRestPosition

    lockOutput = BoolField(default_value=False)
    lo = lockOutput

    target = TargetField(multi=True)
    tg = target

    constraintParentInverseMatrix = DataMatrixField()
    cpim = constraintParentInverseMatrix

    aimVector = AimVectorField(default_value=(1.0, 0.0, 0.0))
    a = aimVector
    aimVectorX = aimVector.aimVectorX
    ax = aimVectorX
    aimVectorY = aimVector.aimVectorY
    ay = aimVectorY
    aimVectorZ = aimVector.aimVectorZ
    az = aimVectorZ

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    u = upVector
    upVectorX = upVector.upVectorX
    ux = upVectorX
    upVectorY = upVector.upVectorY
    uy = upVectorY
    upVectorZ = upVector.upVectorZ
    uz = upVectorZ

    worldUpVector = WorldUpVectorField(default_value=(0.0, 1.0, 0.0))
    wu = worldUpVector
    worldUpVectorX = worldUpVector.worldUpVectorX
    wux = worldUpVectorX
    worldUpVectorY = worldUpVector.worldUpVectorY
    wuy = worldUpVectorY
    worldUpVectorZ = worldUpVector.worldUpVectorZ
    wuz = worldUpVectorZ

    worldUpMatrix = DataMatrixField()
    wum = worldUpMatrix

    worldUpType = WorldUpTypeEnumField(default_value=3)
    wut = worldUpType

    constraintTranslate = ConstraintTranslateField(
        default_value=(0.0, 0.0, 0.0)
    )
    ct = constraintTranslate
    constraintTranslateX = constraintTranslate.constraintTranslateX
    ctx = constraintTranslateX
    constraintTranslateY = constraintTranslate.constraintTranslateY
    cty = constraintTranslateY
    constraintTranslateZ = constraintTranslate.constraintTranslateZ
    ctz = constraintTranslateZ

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

    constraintVector = ConstraintVectorField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cv = constraintVector
    constraintVectorX = constraintVector.constraintVectorX
    cvx = constraintVectorX
    constraintVectorY = constraintVector.constraintVectorY
    cvy = constraintVectorY
    constraintVectorZ = constraintVector.constraintVectorZ
    cvz = constraintVectorZ

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

    useOldOffsetCalculation = BoolField(default_value=False)
    uooc = useOldOffsetCalculation
