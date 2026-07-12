# coding: utf-8
from ._core import Transform
from ....attr.define.node_attr.tangent_constraint import (
    AimVectorField,
    ConstraintJointOrientField,
    ConstraintRotateField,
    ConstraintRotatePivotField,
    ConstraintRotateTranslateField,
    ConstraintTranslateField,
    ConstraintVectorField,
    RestRotateField,
    TargetField,
    UpVectorField,
    WorldUpVectorField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.dt.matrix import DataMatrixField


class WorldUpTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SCENE_UP = 0
    OBJECT_UP = 1
    OBJECT_ROTATION_UP = 2
    VECTOR = 3
    NONE = 4


class WorldUpTypeEnumAttrOperator(EnumAttrOperator):
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


class TangentConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "tangentConstraint"

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

    constraintTranslate = ConstraintTranslateField(default_value=(0.0, 0.0, 0.0))
    ct = constraintTranslate
    constraintTranslateX = constraintTranslate.constraintTranslateX
    ctx = constraintTranslateX
    constraintTranslateY = constraintTranslate.constraintTranslateY
    cty = constraintTranslateY
    constraintTranslateZ = constraintTranslate.constraintTranslateZ
    ctz = constraintTranslateZ

    constraintRotatePivot = ConstraintRotatePivotField(default_value=(0.0, 0.0, 0.0))
    crp = constraintRotatePivot
    constraintRotatePivotX = constraintRotatePivot.constraintRotatePivotX
    crpx = constraintRotatePivotX
    constraintRotatePivotY = constraintRotatePivot.constraintRotatePivotY
    crpy = constraintRotatePivotY
    constraintRotatePivotZ = constraintRotatePivot.constraintRotatePivotZ
    crpz = constraintRotatePivotZ

    constraintRotateTranslate = ConstraintRotateTranslateField(default_value=(0.0, 0.0, 0.0))
    crt = constraintRotateTranslate
    constraintRotateTranslateX = constraintRotateTranslate.constraintRotateTranslateX
    crtx = constraintRotateTranslateX
    constraintRotateTranslateY = constraintRotateTranslate.constraintRotateTranslateY
    crty = constraintRotateTranslateY
    constraintRotateTranslateZ = constraintRotateTranslate.constraintRotateTranslateZ
    crtz = constraintRotateTranslateZ

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

    constraintRotate = ConstraintRotateField(default_value=(0.0, 0.0, 0.0), writable=False)
    cr = constraintRotate
    constraintRotateX = constraintRotate.constraintRotateX
    crx = constraintRotateX
    constraintRotateY = constraintRotate.constraintRotateY
    cry = constraintRotateY
    constraintRotateZ = constraintRotate.constraintRotateZ
    crz = constraintRotateZ

    constraintVector = ConstraintVectorField(default_value=(0.0, 0.0, 0.0), writable=False)
    cv = constraintVector
    constraintVectorX = constraintVector.constraintVectorX
    cvx = constraintVectorX
    constraintVectorY = constraintVector.constraintVectorY
    cvy = constraintVectorY
    constraintVectorZ = constraintVector.constraintVectorZ
    cvz = constraintVectorZ

    restRotate = RestRotateField(default_value=(0.0, 0.0, 0.0))
    rsrr = restRotate
    restRotateX = restRotate.restRotateX
    rrx = restRotateX
    restRotateY = restRotate.restRotateY
    rry = restRotateY
    restRotateZ = restRotate.restRotateZ
    rrz = restRotateZ
