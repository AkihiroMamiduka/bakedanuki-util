# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_dynamics import (
    InitialRotationalVelocityField,
    InitialVelocityField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedMASH_Dynamics(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Dynamics"

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    time = TimeField(default_value=0.0)

    enable = BoolField(default_value=True)

    autoFit = BoolField(default_value=True)

    initiallySleeping = BoolField(default_value=False)

    bounce = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)

    friction = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)

    damping = FloatField(default_value=0.05000000074505806, min_value=0.0, max_value=1.0)

    rollingFriction = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)

    rollingDamping = FloatField(default_value=0.009999999776482582, min_value=0.0, max_value=1.0)

    mass = FloatField(default_value=1.0, min_value=0.0, soft_max_value=100.0)

    useDensity = BoolField(default_value=False)

    positionStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    rotationalStrength = FloatField(default_value=0.0, min_value=0.0, soft_max_value=100.0)

    collisionObjectScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    maxVelocity = FloatField(default_value=100.0, min_value=0.0, soft_max_value=100.0)

    maxAngularVelocity = FloatField(default_value=100.0, min_value=0.0, soft_max_value=2.0)

    dynamicsPP = TypedField(multi=True)

    constraintsPP = TypedField(multi=True)

    ignoreInvisible = BoolField(default_value=True)

    emitFromCollisions = BoolField(default_value=False)

    collisionDistanceThreshold = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)

    contactMaskLayers = DataStringField()

    collisionMaskLayers = DataStringField()

    collisionGroupLayers = DataStringField()

    hierarchyMode = HierarchyModeEnumField(default_value=1)

    initialVelocitySpace = InitialVelocitySpaceEnumField(default_value=1)

    initialVelocity = InitialVelocityField(default_value=(0.0, 0.0, 0.0))
    initialVelocity0 = initialVelocity.initialVelocity0
    initialVelocity1 = initialVelocity.initialVelocity1
    initialVelocity2 = initialVelocity.initialVelocity2

    initialRotationalVelocity = InitialRotationalVelocityField(default_value=(0.0, 0.0, 0.0))
    initialRotationalVelocity0 = initialRotationalVelocity.initialRotationalVelocity0
    initialRotationalVelocity1 = initialRotationalVelocity.initialRotationalVelocity1
    initialRotationalVelocity2 = initialRotationalVelocity.initialRotationalVelocity2

    linearVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    angularVelocityThreshold = FloatField(default_value=0.0, min_value=0.0, soft_max_value=10.0)

    collisionJitter = FloatField(default_value=0.009999999776482582, min_value=0.0, soft_max_value=1.0)

    collisionShapeLength = FloatField(default_value=5.0, min_value=0.0, soft_max_value=10.0)

    initialStateJSON = DataStringField()

    collisionShapeAxis = CollisionShapeAxisEnumField(default_value=1)

    collisionShape = CollisionShapeEnumField(default_value=0)
