# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_dynamics import (
    InitialRotationalVelocityField,
    InitialVelocityField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.string import DataStringField


class HierarchyModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 4


class HierarchyModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 4

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class HierarchyModeEnumField(
    EnumField[HierarchyModeEnumAttrOperator, HierarchyModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HierarchyModeEnumAttrOperator
    PLUG_CLS = HierarchyModeEnumPlugOperator


class InitialVelocitySpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class InitialVelocitySpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class InitialVelocitySpaceEnumField(
    EnumField[InitialVelocitySpaceEnumAttrOperator, InitialVelocitySpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InitialVelocitySpaceEnumAttrOperator
    PLUG_CLS = InitialVelocitySpaceEnumPlugOperator


class CollisionShapeAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2


class CollisionShapeAxisEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    X = 0
    Y = 1
    Z = 2

    NAME_MAP = {
        X: "X",
        Y: "Y",
        Z: "Z",
    }


class CollisionShapeAxisEnumField(
    EnumField[CollisionShapeAxisEnumAttrOperator, CollisionShapeAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionShapeAxisEnumAttrOperator
    PLUG_CLS = CollisionShapeAxisEnumPlugOperator


class CollisionShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    AUTOMATIC = 0
    BOX = 1
    SPHERE = 2
    CAPSULE = 3
    CONVEX_HULL = 4
    CYLINDER = 7
    MESH = 8


class CollisionShapeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    AUTOMATIC = 0
    BOX = 1
    SPHERE = 2
    CAPSULE = 3
    CONVEX_HULL = 4
    CYLINDER = 7
    MESH = 8

    NAME_MAP = {
        AUTOMATIC: "Automatic",
        BOX: "Box",
        SPHERE: "Sphere",
        CAPSULE: "Capsule",
        CONVEX_HULL: "Convex Hull",
        CYLINDER: "Cylinder",
        MESH: "Mesh",
    }


class CollisionShapeEnumField(
    EnumField[CollisionShapeEnumAttrOperator, CollisionShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionShapeEnumAttrOperator
    PLUG_CLS = CollisionShapeEnumPlugOperator


class MASH_Dynamics(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Dynamics"

    outputPoints = TypedField()

    inputPoints = TypedField()

    time = TimeField()

    enable = BoolField()

    autoFit = BoolField()

    initiallySleeping = BoolField()

    bounce = FloatField()

    friction = FloatField()

    damping = FloatField()

    rollingFriction = FloatField()

    rollingDamping = FloatField()

    mass = FloatField()

    useDensity = BoolField()

    positionStrength = FloatField()

    rotationalStrength = FloatField()

    collisionObjectScale = FloatField()

    maxVelocity = FloatField()

    maxAngularVelocity = FloatField()

    dynamicsPP = TypedField(multi=True)

    constraintsPP = TypedField(multi=True)

    ignoreInvisible = BoolField()

    emitFromCollisions = BoolField()

    collisionDistanceThreshold = FloatField()

    contactMaskLayers = DataStringField()

    collisionMaskLayers = DataStringField()

    collisionGroupLayers = DataStringField()

    hierarchyMode = HierarchyModeEnumField()

    initialVelocitySpace = InitialVelocitySpaceEnumField()

    initialVelocity = InitialVelocityField()
    initialVelocity0 = initialVelocity.initialVelocity0
    initialVelocity1 = initialVelocity.initialVelocity1
    initialVelocity2 = initialVelocity.initialVelocity2

    initialRotationalVelocity = InitialRotationalVelocityField()
    initialRotationalVelocity0 = initialRotationalVelocity.initialRotationalVelocity0
    initialRotationalVelocity1 = initialRotationalVelocity.initialRotationalVelocity1
    initialRotationalVelocity2 = initialRotationalVelocity.initialRotationalVelocity2

    linearVelocityThreshold = FloatField()

    angularVelocityThreshold = FloatField()

    collisionJitter = FloatField()

    collisionShapeLength = FloatField()

    initialStateJSON = DataStringField()

    collisionShapeAxis = CollisionShapeAxisEnumField()

    collisionShape = CollisionShapeEnumField()
