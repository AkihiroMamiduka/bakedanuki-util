# coding: utf-8
from .._core import Transform
from .....attr.define.node_attr.rigid_constraint import (
    AngularVelocityField,
    ForceField,
    InitialOrientationField,
    InitialPositionField,
    UserDefinedPositionField,
    VelocityField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.long import LongField


class ConstraintTypeEnumPlugOperator(
    EnumPlugOperator["ConstraintTypeEnumAttrOperator"]
):
    __slots__ = ()

    PIN = 1
    NAIL = 2
    DIRECTIONALHINGE = 4
    BARRIER = 5
    SPRING = 7
    HINGE = 8


class ConstraintTypeEnumAttrOperator(
    EnumAttrOperator[ConstraintTypeEnumPlugOperator]
):
    __slots__ = ()

    PIN = 1
    NAIL = 2
    DIRECTIONALHINGE = 4
    BARRIER = 5
    SPRING = 7
    HINGE = 8

    NAME_MAP = {
        PIN: "pin",
        NAIL: "nail",
        DIRECTIONALHINGE: "directionalHinge",
        BARRIER: "barrier",
        SPRING: "spring",
        HINGE: "hinge",
    }


class ConstraintTypeEnumField(
    EnumField[ConstraintTypeEnumAttrOperator, ConstraintTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConstraintTypeEnumAttrOperator
    PLUG_CLS = ConstraintTypeEnumPlugOperator


class RelativeToEnumPlugOperator(
    EnumPlugOperator["RelativeToEnumAttrOperator"]
):
    __slots__ = ()

    BODY_1 = 0
    BODY_2 = 1
    MID_POINT = 2
    USER_DEFINED = 3


class RelativeToEnumAttrOperator(EnumAttrOperator[RelativeToEnumPlugOperator]):
    __slots__ = ()

    BODY_1 = 0
    BODY_2 = 1
    MID_POINT = 2
    USER_DEFINED = 3

    NAME_MAP = {
        BODY_1: "Body 1",
        BODY_2: "Body 2",
        MID_POINT: "Mid Point",
        USER_DEFINED: "User Defined",
    }


class RelativeToEnumField(
    EnumField[RelativeToEnumAttrOperator, RelativeToEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RelativeToEnumAttrOperator
    PLUG_CLS = RelativeToEnumPlugOperator


class GeneratedRigidConstraint(Transform):
    __slots__ = ()

    NODE_TYPE = "rigidConstraint"

    rigidBody1 = MessageField()
    rb1 = rigidBody1

    rigidBody2 = MessageField()
    rb2 = rigidBody2

    constraintType = ConstraintTypeEnumField(default_value=2)
    typ = constraintType

    initialPosition = InitialPositionField(default_value=(0.0, 0.0, 0.0))
    ip = initialPosition
    initialPositionX = initialPosition.initialPositionX
    ipx = initialPositionX
    initialPositionY = initialPosition.initialPositionY
    ipy = initialPositionY
    initialPositionZ = initialPosition.initialPositionZ
    ipz = initialPositionZ

    velocity = VelocityField(default_value=(0.0, 0.0, 0.0), writable=False)
    vel = velocity
    velocityX = velocity.velocityX
    vlx = velocityX
    velocityY = velocity.velocityY
    vly = velocityY
    velocityZ = velocity.velocityZ
    vlz = velocityZ

    angularVelocity = AngularVelocityField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    avl = angularVelocity
    angularVelocityX = angularVelocity.angularVelocityX
    avx = angularVelocityX
    angularVelocityY = angularVelocity.angularVelocityY
    avy = angularVelocityY
    angularVelocityZ = angularVelocity.angularVelocityZ
    avz = angularVelocityZ

    initialOrientation = InitialOrientationField(default_value=(0.0, 0.0, 0.0))
    ino = initialOrientation
    initialOrientationX = initialOrientation.initialOrientationX
    iox = initialOrientationX
    initialOrientationY = initialOrientation.initialOrientationY
    ioy = initialOrientationY
    initialOrientationZ = initialOrientation.initialOrientationZ
    ioz = initialOrientationZ

    force = ForceField(default_value=(0.0, 0.0, 0.0), writable=False)
    for_ = force
    forceX = force.forceX
    frx = forceX
    forceY = force.forceY
    fry = forceY
    forceZ = force.forceZ
    frz = forceZ

    springStiffness = DoubleField(
        default_value=5.0, min_value=0.0, soft_max_value=5.0
    )
    sst = springStiffness

    springDamping = DoubleField(
        default_value=0.1,
        min_value=-100.0,
        max_value=100.0,
        soft_min_value=-10.0,
        soft_max_value=10.0,
    )
    dmp = springDamping

    springRestLength = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=100.0
    )
    srl = springRestLength

    interpenetrate = BoolField(default_value=False)
    int = interpenetrate

    isParented = BoolField(default_value=False)
    par = isParented

    isBounded = BoolField(default_value=False, writable=False)
    bon = isBounded

    solverId = LongField(default_value=-1)
    sid = solverId

    constrain = BoolField(default_value=True)
    con = constrain

    relativeTo = RelativeToEnumField(default_value=0)
    rlt = relativeTo

    userDefinedPosition = UserDefinedPositionField(
        default_value=(0.0, 0.0, 0.0)
    )
    udp = userDefinedPosition
    userDefinedPositionX = userDefinedPosition.userDefinedPositionX
    upx = userDefinedPositionX
    userDefinedPositionY = userDefinedPosition.userDefinedPositionY
    upy = userDefinedPositionY
    userDefinedPositionZ = userDefinedPosition.userDefinedPositionZ
    upz = userDefinedPositionZ
