# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.n_cloth import (
    CachedWorldCentroidField,
    CentroidField,
    CollisionDataField,
    CompInstObjGroupsField,
    ComponentTagsField,
    DisplayColorField,
    EmitterDataField,
    EventRandStateField,
    FieldDataField,
    FieldScaleField,
    IdMappingField,
    InstanceDataField,
    LocalForceField,
    LocalWindField,
    PointFieldDropoffField,
    RandStateField,
    WorldCentroidField,
)
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.message import MessageField
from .....attr.define.std.at.scalar.numeric.bool import BoolField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField
from .....attr.define.std.at.scalar.numeric.range.float import FloatField
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.scalar.numeric.range.short import ShortField
from .....attr.define.std.at.scalar.unit.range.float_angle import (
    FloatAngleField,
)
from .....attr.define.std.at.scalar.unit.time import TimeField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.double_array import DataDoubleArrayField
from .....attr.define.std.dt.matrix import DataMatrixField
from .....attr.define.std.dt.string import DataStringField
from .....attr.define.std.dt.vector_array import DataVectorArrayField


class LifespanModeEnumPlugOperator(
    EnumPlugOperator["LifespanModeEnumAttrOperator"]
):
    __slots__ = ()

    LIVE_FOREVER = 0
    CONSTANT = 1
    RANDOM_RANGE = 2
    LIFESPANPP_ONLY = 3


class LifespanModeEnumAttrOperator(
    EnumAttrOperator[LifespanModeEnumPlugOperator]
):
    __slots__ = ()

    LIVE_FOREVER = 0
    CONSTANT = 1
    RANDOM_RANGE = 2
    LIFESPANPP_ONLY = 3

    NAME_MAP = {
        LIVE_FOREVER: "Live forever",
        CONSTANT: "Constant",
        RANDOM_RANGE: "Random range",
        LIFESPANPP_ONLY: "lifespanPP only",
    }


class LifespanModeEnumField(
    EnumField[LifespanModeEnumAttrOperator, LifespanModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LifespanModeEnumAttrOperator
    PLUG_CLS = LifespanModeEnumPlugOperator


class InputGeometrySpaceEnumPlugOperator(
    EnumPlugOperator["InputGeometrySpaceEnumAttrOperator"]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class InputGeometrySpaceEnumAttrOperator(
    EnumAttrOperator[InputGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2

    NAME_MAP = {
        GEOMETRY_LOCAL: "Geometry Local",
        WORLD: "World",
        PARTICLE_LOCAL: "Particle Local",
    }


class InputGeometrySpaceEnumField(
    EnumField[
        InputGeometrySpaceEnumAttrOperator, InputGeometrySpaceEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputGeometrySpaceEnumAttrOperator
    PLUG_CLS = InputGeometrySpaceEnumPlugOperator


class TargetGeometrySpaceEnumPlugOperator(
    EnumPlugOperator["TargetGeometrySpaceEnumAttrOperator"]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class TargetGeometrySpaceEnumAttrOperator(
    EnumAttrOperator[TargetGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2

    NAME_MAP = {
        GEOMETRY_LOCAL: "Geometry Local",
        WORLD: "World",
        PARTICLE_LOCAL: "Particle Local",
    }


class TargetGeometrySpaceEnumField(
    EnumField[
        TargetGeometrySpaceEnumAttrOperator,
        TargetGeometrySpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TargetGeometrySpaceEnumAttrOperator
    PLUG_CLS = TargetGeometrySpaceEnumPlugOperator


class ParticleRenderTypeEnumPlugOperator(
    EnumPlugOperator["ParticleRenderTypeEnumAttrOperator"]
):
    __slots__ = ()

    MULTIPOINT = 0
    MULTISTREAK = 1
    NUMERIC = 2
    POINTS = 3
    SPHERES = 4
    SPRITES = 5
    STREAK = 6
    BLOBBY_SURFACE_S_SLASH_W = 7
    CLOUD_S_SLASH_W = 8
    TUBE_S_SLASH_W = 9


class ParticleRenderTypeEnumAttrOperator(
    EnumAttrOperator[ParticleRenderTypeEnumPlugOperator]
):
    __slots__ = ()

    MULTIPOINT = 0
    MULTISTREAK = 1
    NUMERIC = 2
    POINTS = 3
    SPHERES = 4
    SPRITES = 5
    STREAK = 6
    BLOBBY_SURFACE_S_SLASH_W = 7
    CLOUD_S_SLASH_W = 8
    TUBE_S_SLASH_W = 9

    NAME_MAP = {
        MULTIPOINT: "MultiPoint",
        MULTISTREAK: "MultiStreak",
        NUMERIC: "Numeric",
        POINTS: "Points",
        SPHERES: "Spheres",
        SPRITES: "Sprites",
        STREAK: "Streak",
        BLOBBY_SURFACE_S_SLASH_W: "Blobby Surface (s/w)",
        CLOUD_S_SLASH_W: "Cloud (s/w)",
        TUBE_S_SLASH_W: "Tube (s/w)",
    }


class ParticleRenderTypeEnumField(
    EnumField[
        ParticleRenderTypeEnumAttrOperator, ParticleRenderTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ParticleRenderTypeEnumAttrOperator
    PLUG_CLS = ParticleRenderTypeEnumPlugOperator


class CollisionFlagEnumPlugOperator(
    EnumPlugOperator["CollisionFlagEnumAttrOperator"]
):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2
    FACE = 3


class CollisionFlagEnumAttrOperator(
    EnumAttrOperator[CollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2
    FACE = 3

    NAME_MAP = {
        VERTEX: "Vertex",
        EDGE: "Edge",
        FACE: "Face",
    }


class CollisionFlagEnumField(
    EnumField[CollisionFlagEnumAttrOperator, CollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollisionFlagEnumAttrOperator
    PLUG_CLS = CollisionFlagEnumPlugOperator


class SelfCollisionFlagEnumPlugOperator(
    EnumPlugOperator["SelfCollisionFlagEnumAttrOperator"]
):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4


class SelfCollisionFlagEnumAttrOperator(
    EnumAttrOperator[SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4

    NAME_MAP = {
        VERTEX: "Vertex",
        VERTEXEDGE: "VertexEdge",
        VERTEXFACE: "VertexFace",
        FULL_SURFACE: "Full Surface",
    }


class SelfCollisionFlagEnumField(
    EnumField[
        SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class ForceFieldEnumPlugOperator(
    EnumPlugOperator["ForceFieldEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    ALONGNORMAL = 1
    SINGLE_SIDED = 2
    DOUBLE_SIDED = 3


class ForceFieldEnumAttrOperator(EnumAttrOperator[ForceFieldEnumPlugOperator]):
    __slots__ = ()

    OFF = 0
    ALONGNORMAL = 1
    SINGLE_SIDED = 2
    DOUBLE_SIDED = 3

    NAME_MAP = {
        OFF: "Off",
        ALONGNORMAL: "AlongNormal",
        SINGLE_SIDED: "Single Sided",
        DOUBLE_SIDED: "Double Sided",
    }


class ForceFieldEnumField(
    EnumField[ForceFieldEnumAttrOperator, ForceFieldEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ForceFieldEnumAttrOperator
    PLUG_CLS = ForceFieldEnumPlugOperator


class PointForceFieldEnumPlugOperator(
    EnumPlugOperator["PointForceFieldEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    THICKNESSRELATIVE = 1
    WORLDSPACE = 2


class PointForceFieldEnumAttrOperator(
    EnumAttrOperator[PointForceFieldEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    THICKNESSRELATIVE = 1
    WORLDSPACE = 2

    NAME_MAP = {
        OFF: "Off",
        THICKNESSRELATIVE: "ThicknessRelative",
        WORLDSPACE: "Worldspace",
    }


class PointForceFieldEnumField(
    EnumField[PointForceFieldEnumAttrOperator, PointForceFieldEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointForceFieldEnumAttrOperator
    PLUG_CLS = PointForceFieldEnumPlugOperator


class ThicknessMapTypeEnumPlugOperator(
    EnumPlugOperator["ThicknessMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class ThicknessMapTypeEnumAttrOperator(
    EnumAttrOperator[ThicknessMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class ThicknessMapTypeEnumField(
    EnumField[
        ThicknessMapTypeEnumAttrOperator, ThicknessMapTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ThicknessMapTypeEnumAttrOperator
    PLUG_CLS = ThicknessMapTypeEnumPlugOperator


class BounceMapTypeEnumPlugOperator(
    EnumPlugOperator["BounceMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class BounceMapTypeEnumAttrOperator(
    EnumAttrOperator[BounceMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class BounceMapTypeEnumField(
    EnumField[BounceMapTypeEnumAttrOperator, BounceMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BounceMapTypeEnumAttrOperator
    PLUG_CLS = BounceMapTypeEnumPlugOperator


class FrictionMapTypeEnumPlugOperator(
    EnumPlugOperator["FrictionMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class FrictionMapTypeEnumAttrOperator(
    EnumAttrOperator[FrictionMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class FrictionMapTypeEnumField(
    EnumField[FrictionMapTypeEnumAttrOperator, FrictionMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrictionMapTypeEnumAttrOperator
    PLUG_CLS = FrictionMapTypeEnumPlugOperator


class StickinessMapTypeEnumPlugOperator(
    EnumPlugOperator["StickinessMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class StickinessMapTypeEnumAttrOperator(
    EnumAttrOperator[StickinessMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class StickinessMapTypeEnumField(
    EnumField[
        StickinessMapTypeEnumAttrOperator, StickinessMapTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = StickinessMapTypeEnumAttrOperator
    PLUG_CLS = StickinessMapTypeEnumPlugOperator


class CollideStrengthMapTypeEnumPlugOperator(
    EnumPlugOperator["CollideStrengthMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class CollideStrengthMapTypeEnumAttrOperator(
    EnumAttrOperator[CollideStrengthMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class CollideStrengthMapTypeEnumField(
    EnumField[
        CollideStrengthMapTypeEnumAttrOperator,
        CollideStrengthMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthMapTypeEnumAttrOperator
    PLUG_CLS = CollideStrengthMapTypeEnumPlugOperator


class DampMapTypeEnumPlugOperator(
    EnumPlugOperator["DampMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class DampMapTypeEnumAttrOperator(
    EnumAttrOperator[DampMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class DampMapTypeEnumField(
    EnumField[DampMapTypeEnumAttrOperator, DampMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DampMapTypeEnumAttrOperator
    PLUG_CLS = DampMapTypeEnumPlugOperator


class MassMapTypeEnumPlugOperator(
    EnumPlugOperator["MassMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class MassMapTypeEnumAttrOperator(
    EnumAttrOperator[MassMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class MassMapTypeEnumField(
    EnumField[MassMapTypeEnumAttrOperator, MassMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassMapTypeEnumAttrOperator
    PLUG_CLS = MassMapTypeEnumPlugOperator


class FieldMagnitudeMapTypeEnumPlugOperator(
    EnumPlugOperator["FieldMagnitudeMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class FieldMagnitudeMapTypeEnumAttrOperator(
    EnumAttrOperator[FieldMagnitudeMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class FieldMagnitudeMapTypeEnumField(
    EnumField[
        FieldMagnitudeMapTypeEnumAttrOperator,
        FieldMagnitudeMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = FieldMagnitudeMapTypeEnumAttrOperator
    PLUG_CLS = FieldMagnitudeMapTypeEnumPlugOperator


class ScalingRelationEnumPlugOperator(
    EnumPlugOperator["ScalingRelationEnumAttrOperator"]
):
    __slots__ = ()

    LINK = 0
    OBJECT_SPACE = 1
    WORLD_SPACE = 2


class ScalingRelationEnumAttrOperator(
    EnumAttrOperator[ScalingRelationEnumPlugOperator]
):
    __slots__ = ()

    LINK = 0
    OBJECT_SPACE = 1
    WORLD_SPACE = 2

    NAME_MAP = {
        LINK: "Link",
        OBJECT_SPACE: "Object Space",
        WORLD_SPACE: "World Space",
    }


class ScalingRelationEnumField(
    EnumField[ScalingRelationEnumAttrOperator, ScalingRelationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScalingRelationEnumAttrOperator
    PLUG_CLS = ScalingRelationEnumPlugOperator


class BendSolverEnumPlugOperator(
    EnumPlugOperator["BendSolverEnumAttrOperator"]
):
    __slots__ = ()

    SIMPLE = 0
    HIGH_QUALITY = 1
    FLIP_TRACKING = 2


class BendSolverEnumAttrOperator(EnumAttrOperator[BendSolverEnumPlugOperator]):
    __slots__ = ()

    SIMPLE = 0
    HIGH_QUALITY = 1
    FLIP_TRACKING = 2

    NAME_MAP = {
        SIMPLE: "Simple",
        HIGH_QUALITY: "High Quality",
        FLIP_TRACKING: "Flip Tracking",
    }


class BendSolverEnumField(
    EnumField[BendSolverEnumAttrOperator, BendSolverEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BendSolverEnumAttrOperator
    PLUG_CLS = BendSolverEnumPlugOperator


class InputAttractMethodEnumPlugOperator(
    EnumPlugOperator["InputAttractMethodEnumAttrOperator"]
):
    __slots__ = ()

    NON_LOCKING = 0
    LOCK_VALUES_OF_1_0_OR_GREATER = 1


class InputAttractMethodEnumAttrOperator(
    EnumAttrOperator[InputAttractMethodEnumPlugOperator]
):
    __slots__ = ()

    NON_LOCKING = 0
    LOCK_VALUES_OF_1_0_OR_GREATER = 1

    NAME_MAP = {
        NON_LOCKING: "Non locking",
        LOCK_VALUES_OF_1_0_OR_GREATER: "Lock values of 1.0 or greater",
    }


class InputAttractMethodEnumField(
    EnumField[
        InputAttractMethodEnumAttrOperator, InputAttractMethodEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InputAttractMethodEnumAttrOperator
    PLUG_CLS = InputAttractMethodEnumPlugOperator


class EvaluationOrderEnumPlugOperator(
    EnumPlugOperator["EvaluationOrderEnumAttrOperator"]
):
    __slots__ = ()

    SEQUENTIAL = 0
    PARALLEL = 1


class EvaluationOrderEnumAttrOperator(
    EnumAttrOperator[EvaluationOrderEnumPlugOperator]
):
    __slots__ = ()

    SEQUENTIAL = 0
    PARALLEL = 1

    NAME_MAP = {
        SEQUENTIAL: "Sequential",
        PARALLEL: "Parallel",
    }


class EvaluationOrderEnumField(
    EnumField[EvaluationOrderEnumAttrOperator, EvaluationOrderEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EvaluationOrderEnumAttrOperator
    PLUG_CLS = EvaluationOrderEnumPlugOperator


class PressureMethodEnumPlugOperator(
    EnumPlugOperator["PressureMethodEnumAttrOperator"]
):
    __slots__ = ()

    MANUAL_PRESSURE_SETTING = 0
    VOLUME_TRACKING_MODEL = 1


class PressureMethodEnumAttrOperator(
    EnumAttrOperator[PressureMethodEnumPlugOperator]
):
    __slots__ = ()

    MANUAL_PRESSURE_SETTING = 0
    VOLUME_TRACKING_MODEL = 1

    NAME_MAP = {
        MANUAL_PRESSURE_SETTING: "Manual Pressure Setting",
        VOLUME_TRACKING_MODEL: "Volume Tracking Model",
    }


class PressureMethodEnumField(
    EnumField[PressureMethodEnumAttrOperator, PressureMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMethodEnumAttrOperator
    PLUG_CLS = PressureMethodEnumPlugOperator


class SolverDisplayEnumPlugOperator(
    EnumPlugOperator["SolverDisplayEnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2
    STRETCH_LINKS = 5
    BEND_LINKS = 6
    WEIGHTING = 7


class SolverDisplayEnumAttrOperator(
    EnumAttrOperator[SolverDisplayEnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2
    STRETCH_LINKS = 5
    BEND_LINKS = 6
    WEIGHTING = 7

    NAME_MAP = {
        OFF: "Off",
        COLLISION_THICKNESS: "Collision Thickness",
        SELF_COLLISION_THICKNESS: "Self Collision Thickness",
        STRETCH_LINKS: "Stretch Links",
        BEND_LINKS: "Bend Links",
        WEIGHTING: "Weighting",
    }


class SolverDisplayEnumField(
    EnumField[SolverDisplayEnumAttrOperator, SolverDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverDisplayEnumAttrOperator
    PLUG_CLS = SolverDisplayEnumPlugOperator


class StretchMapTypeEnumPlugOperator(
    EnumPlugOperator["StretchMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class StretchMapTypeEnumAttrOperator(
    EnumAttrOperator[StretchMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class StretchMapTypeEnumField(
    EnumField[StretchMapTypeEnumAttrOperator, StretchMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StretchMapTypeEnumAttrOperator
    PLUG_CLS = StretchMapTypeEnumPlugOperator


class CompressionMapTypeEnumPlugOperator(
    EnumPlugOperator["CompressionMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class CompressionMapTypeEnumAttrOperator(
    EnumAttrOperator[CompressionMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class CompressionMapTypeEnumField(
    EnumField[
        CompressionMapTypeEnumAttrOperator, CompressionMapTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = CompressionMapTypeEnumAttrOperator
    PLUG_CLS = CompressionMapTypeEnumPlugOperator


class BendMapTypeEnumPlugOperator(
    EnumPlugOperator["BendMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class BendMapTypeEnumAttrOperator(
    EnumAttrOperator[BendMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class BendMapTypeEnumField(
    EnumField[BendMapTypeEnumAttrOperator, BendMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BendMapTypeEnumAttrOperator
    PLUG_CLS = BendMapTypeEnumPlugOperator


class BendAngleDropoffMapTypeEnumPlugOperator(
    EnumPlugOperator["BendAngleDropoffMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class BendAngleDropoffMapTypeEnumAttrOperator(
    EnumAttrOperator[BendAngleDropoffMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class BendAngleDropoffMapTypeEnumField(
    EnumField[
        BendAngleDropoffMapTypeEnumAttrOperator,
        BendAngleDropoffMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = BendAngleDropoffMapTypeEnumAttrOperator
    PLUG_CLS = BendAngleDropoffMapTypeEnumPlugOperator


class RestitutionAngleMapTypeEnumPlugOperator(
    EnumPlugOperator["RestitutionAngleMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class RestitutionAngleMapTypeEnumAttrOperator(
    EnumAttrOperator[RestitutionAngleMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class RestitutionAngleMapTypeEnumField(
    EnumField[
        RestitutionAngleMapTypeEnumAttrOperator,
        RestitutionAngleMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RestitutionAngleMapTypeEnumAttrOperator
    PLUG_CLS = RestitutionAngleMapTypeEnumPlugOperator


class RigidityMapTypeEnumPlugOperator(
    EnumPlugOperator["RigidityMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class RigidityMapTypeEnumAttrOperator(
    EnumAttrOperator[RigidityMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class RigidityMapTypeEnumField(
    EnumField[RigidityMapTypeEnumAttrOperator, RigidityMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RigidityMapTypeEnumAttrOperator
    PLUG_CLS = RigidityMapTypeEnumPlugOperator


class DeformMapTypeEnumPlugOperator(
    EnumPlugOperator["DeformMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class DeformMapTypeEnumAttrOperator(
    EnumAttrOperator[DeformMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class DeformMapTypeEnumField(
    EnumField[DeformMapTypeEnumAttrOperator, DeformMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DeformMapTypeEnumAttrOperator
    PLUG_CLS = DeformMapTypeEnumPlugOperator


class InputAttractMapTypeEnumPlugOperator(
    EnumPlugOperator["InputAttractMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class InputAttractMapTypeEnumAttrOperator(
    EnumAttrOperator[InputAttractMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class InputAttractMapTypeEnumField(
    EnumField[
        InputAttractMapTypeEnumAttrOperator,
        InputAttractMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = InputAttractMapTypeEnumAttrOperator
    PLUG_CLS = InputAttractMapTypeEnumPlugOperator


class RestLengthScaleMapTypeEnumPlugOperator(
    EnumPlugOperator["RestLengthScaleMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class RestLengthScaleMapTypeEnumAttrOperator(
    EnumAttrOperator[RestLengthScaleMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class RestLengthScaleMapTypeEnumField(
    EnumField[
        RestLengthScaleMapTypeEnumAttrOperator,
        RestLengthScaleMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = RestLengthScaleMapTypeEnumAttrOperator
    PLUG_CLS = RestLengthScaleMapTypeEnumPlugOperator


class LiftMapTypeEnumPlugOperator(
    EnumPlugOperator["LiftMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class LiftMapTypeEnumAttrOperator(
    EnumAttrOperator[LiftMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class LiftMapTypeEnumField(
    EnumField[LiftMapTypeEnumAttrOperator, LiftMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LiftMapTypeEnumAttrOperator
    PLUG_CLS = LiftMapTypeEnumPlugOperator


class DragMapTypeEnumPlugOperator(
    EnumPlugOperator["DragMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class DragMapTypeEnumAttrOperator(
    EnumAttrOperator[DragMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class DragMapTypeEnumField(
    EnumField[DragMapTypeEnumAttrOperator, DragMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DragMapTypeEnumAttrOperator
    PLUG_CLS = DragMapTypeEnumPlugOperator


class TangentialDragMapTypeEnumPlugOperator(
    EnumPlugOperator["TangentialDragMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class TangentialDragMapTypeEnumAttrOperator(
    EnumAttrOperator[TangentialDragMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class TangentialDragMapTypeEnumField(
    EnumField[
        TangentialDragMapTypeEnumAttrOperator,
        TangentialDragMapTypeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TangentialDragMapTypeEnumAttrOperator
    PLUG_CLS = TangentialDragMapTypeEnumPlugOperator


class WrinkleMapTypeEnumPlugOperator(
    EnumPlugOperator["WrinkleMapTypeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class WrinkleMapTypeEnumAttrOperator(
    EnumAttrOperator[WrinkleMapTypeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2

    NAME_MAP = {
        NONE: "None",
        PER_MINUS_VERTEX: "Per-vertex",
        TEXTURE: "Texture",
    }


class WrinkleMapTypeEnumField(
    EnumField[WrinkleMapTypeEnumAttrOperator, WrinkleMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = WrinkleMapTypeEnumAttrOperator
    PLUG_CLS = WrinkleMapTypeEnumPlugOperator


class CacheableAttributesEnumPlugOperator(
    EnumPlugOperator["CacheableAttributesEnumAttrOperator"]
):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMIC_STATE = 2


class CacheableAttributesEnumAttrOperator(
    EnumAttrOperator[CacheableAttributesEnumPlugOperator]
):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMIC_STATE = 2

    NAME_MAP = {
        POSITION: "Position",
        POSITION_AND_VELOCITY: "Position And Velocity",
        DYNAMIC_STATE: "Dynamic State",
    }


class CacheableAttributesEnumField(
    EnumField[
        CacheableAttributesEnumAttrOperator,
        CacheableAttributesEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = CacheableAttributesEnumAttrOperator
    PLUG_CLS = CacheableAttributesEnumPlugOperator


class CacheUsageEnumPlugOperator(
    EnumPlugOperator["CacheUsageEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    CACHE_SLASH_SIMULATION = 1
    CACHE_FILE_INFO = 2


class CacheUsageEnumAttrOperator(EnumAttrOperator[CacheUsageEnumPlugOperator]):
    __slots__ = ()

    NONE = 0
    CACHE_SLASH_SIMULATION = 1
    CACHE_FILE_INFO = 2

    NAME_MAP = {
        NONE: "None",
        CACHE_SLASH_SIMULATION: "Cache/Simulation",
        CACHE_FILE_INFO: "Cache File Info",
    }


class CacheUsageEnumField(
    EnumField[CacheUsageEnumAttrOperator, CacheUsageEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheUsageEnumAttrOperator
    PLUG_CLS = CacheUsageEnumPlugOperator


class AiRenderPointsAsEnumPlugOperator(
    EnumPlugOperator["AiRenderPointsAsEnumAttrOperator"]
):
    __slots__ = ()

    POINTS = 0
    SPHERES = 1
    QUADS = 2


class AiRenderPointsAsEnumAttrOperator(
    EnumAttrOperator[AiRenderPointsAsEnumPlugOperator]
):
    __slots__ = ()

    POINTS = 0
    SPHERES = 1
    QUADS = 2

    NAME_MAP = {
        POINTS: "points",
        SPHERES: "spheres",
        QUADS: "quads",
    }


class AiRenderPointsAsEnumField(
    EnumField[
        AiRenderPointsAsEnumAttrOperator, AiRenderPointsAsEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = AiRenderPointsAsEnumAttrOperator
    PLUG_CLS = AiRenderPointsAsEnumPlugOperator


class GeneratedNCloth(Shape):
    __slots__ = ()

    NODE_TYPE = "nCloth"

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    hfm = hardwareFogMultiplier

    motionBlur = BoolField(default_value=True)
    mb = motionBlur

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions

    castsShadows = BoolField(default_value=True)
    csh = castsShadows

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    asBackground = BoolField(default_value=False)
    asbg = asBackground

    maxVisibilitySamplesOverride = BoolField(default_value=False)
    vbo = maxVisibilitySamplesOverride

    maxVisibilitySamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(
        default_value=1, min_value=1, max_value=5, soft_max_value=5
    )
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(
        default_value=1, min_value=1, max_value=32, soft_max_value=20
    )
    msa = maxShadingSamples

    volumeSamplesOverride = BoolField(default_value=False)
    vso = volumeSamplesOverride

    volumeSamples = LongField(default_value=1, soft_max_value=20)
    vss = volumeSamples

    depthJitter = BoolField(default_value=False)
    dej = depthJitter

    ignoreSelfShadowing = BoolField(default_value=False)
    iss = ignoreSelfShadowing

    primaryVisibility = BoolField(default_value=True)
    vis = primaryVisibility

    referenceObject = MessageField()
    rob = referenceObject

    compInstObjGroups = CompInstObjGroupsField(multi=True)
    ciog = compInstObjGroups

    componentTags = ComponentTagsField(multi=True)
    gtag = componentTags

    instMaterialAssign = MessageField(multi=True)
    imtla = instMaterialAssign

    pickTexture = MessageField()
    pte = pickTexture

    position = DataVectorArrayField()
    pos = position

    rampPosition = DataVectorArrayField()
    rps = rampPosition

    centroid = CentroidField(default_value=(0.0, 0.0, 0.0), writable=False)
    ctd = centroid
    centroidX = centroid.centroidX
    ctdx = centroidX
    centroidY = centroid.centroidY
    ctdy = centroidY
    centroidZ = centroid.centroidZ
    ctdz = centroidZ

    lastPosition = DataVectorArrayField(writable=False)
    lpos = lastPosition

    velocity = DataVectorArrayField()
    vel = velocity

    rampVelocity = DataVectorArrayField()
    rvl = rampVelocity

    lastVelocity = DataVectorArrayField(writable=False)
    lvel = lastVelocity

    acceleration = DataVectorArrayField()
    acc = acceleration

    rampAcceleration = DataVectorArrayField()
    rac = rampAcceleration

    force = DataVectorArrayField(writable=False)
    frc = force

    inputForce = DataVectorArrayField(multi=True)
    ifc = inputForce

    worldPosition = DataVectorArrayField(writable=False)
    wps = worldPosition

    worldCentroid = WorldCentroidField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    wctn = worldCentroid
    worldCentroidX = worldCentroid.worldCentroidX
    wctx = worldCentroidX
    worldCentroidY = worldCentroid.worldCentroidY
    wcty = worldCentroidY
    worldCentroidZ = worldCentroid.worldCentroidZ
    wctz = worldCentroidZ

    lastWorldPosition = DataVectorArrayField(writable=False)
    lwps = lastWorldPosition

    worldVelocity = DataVectorArrayField(writable=False)
    wvl = worldVelocity

    worldVelocityInObjectSpace = DataVectorArrayField()
    wvo = worldVelocityInObjectSpace

    lastWorldVelocity = DataVectorArrayField(writable=False)
    lwvl = lastWorldVelocity

    lastWorldMatrix = DataMatrixField(writable=False)
    lwm = lastWorldMatrix

    position0 = DataVectorArrayField()
    pos0 = position0

    velocity0 = DataVectorArrayField()
    vel0 = velocity0

    acceleration0 = DataVectorArrayField()
    acc0 = acceleration0

    emitterId0 = DataDoubleArrayField(writable=False)
    eid0 = emitterId0

    useStartupCache = BoolField(default_value=False)
    usc = useStartupCache

    startupCachePath = DataStringField()
    scp = startupCachePath

    startupCacheFrame = LongField(default_value=0)
    scf = startupCacheFrame

    cachedPosition = DataVectorArrayField(writable=False)
    cpos = cachedPosition

    lastCachedPosition = DataVectorArrayField(writable=False)
    lcps = lastCachedPosition

    cachedWorldPosition = DataVectorArrayField(writable=False)
    cwps = cachedWorldPosition

    cachedWorldCentroid = CachedWorldCentroidField(
        default_value=(0.0, 0.0, 0.0), writable=False
    )
    cwcn = cachedWorldCentroid
    cachedWorldCentroidX = cachedWorldCentroid.cachedWorldCentroidX
    cwcx = cachedWorldCentroidX
    cachedWorldCentroidY = cachedWorldCentroid.cachedWorldCentroidY
    cwcy = cachedWorldCentroidY
    cachedWorldCentroidZ = cachedWorldCentroid.cachedWorldCentroidZ
    cwcz = cachedWorldCentroidZ

    cachedVelocity = DataVectorArrayField(writable=False)
    cvel = cachedVelocity

    cachedWorldVelocity = DataVectorArrayField(writable=False)
    cwvl = cachedWorldVelocity

    count = LongField(default_value=0, writable=False)
    cnt = count

    computingCount = BoolField(default_value=False)
    cmp = computingCount

    mass = DataDoubleArrayField()
    mas = mass

    mass0 = DataDoubleArrayField()
    mas0 = mass0

    massCache = DataDoubleArrayField(writable=False)
    masc = massCache

    particleId = DataDoubleArrayField(writable=False)
    id = particleId

    particleId0 = DataDoubleArrayField()
    id0 = particleId0

    idCache = DataDoubleArrayField(writable=False)
    idc = idCache

    idMapping = IdMappingField(writable=False)
    idm = idMapping
    sortedId = idMapping.sortedId
    sid = sortedId
    idIndex = idMapping.idIndex
    idix = idIndex

    nextId = LongField(default_value=0)
    nid = nextId

    nextId0 = LongField(default_value=0)
    nid0 = nextId0

    birthTime = DataDoubleArrayField(writable=False)
    bt = birthTime

    birthTime0 = DataDoubleArrayField()
    bt0 = birthTime0

    birthTimeCache = DataDoubleArrayField()
    btc = birthTimeCache

    age = DataDoubleArrayField(writable=False)
    ag = age

    age0 = DataDoubleArrayField()
    ag0 = age0

    ageCache = DataDoubleArrayField(writable=False)
    agc = ageCache

    emission = TypedField(writable=False)
    emt = emission

    emitterId = DataDoubleArrayField(writable=False)
    eid = emitterId

    dieOnEmissionVolumeExit = BoolField(default_value=False)
    dve = dieOnEmissionVolumeExit

    isFull = BoolField(default_value=False, writable=False)
    ifl = isFull

    newParticles = TypedField(multi=True, readable=False)
    npt = newParticles

    collisionEvents = BoolField(
        default_value=False, readable=False, writable=False
    )
    cev = collisionEvents

    death = BoolField(default_value=False, readable=False, writable=False)
    dth = death

    lifespanMode = LifespanModeEnumField(default_value=0)
    lfm = lifespanMode

    lifespanRandom = DoubleField(default_value=0.0)
    lfr = lifespanRandom

    finalLifespanPP = DataDoubleArrayField(writable=False)
    flp = finalLifespanPP

    generalSeed = LongField(default_value=0)
    gsd = generalSeed

    randState = RandStateField(default_value=(0, 0, 0))
    rnst = randState
    randStateX = randState.randStateX
    rstx = randStateX
    randStateY = randState.randStateY
    rsty = randStateY
    randStateZ = randState.randStateZ
    rstz = randStateZ

    expressionsAfterDynamics = BoolField(default_value=False)
    ead = expressionsAfterDynamics

    executeCreationExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    ece = executeCreationExpression

    executeRuntimeBeforeDynamicsExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    erbe = executeRuntimeBeforeDynamicsExpression

    executeRuntimeAfterDynamicsExpression = BoolField(
        default_value=False, readable=False, writable=False
    )
    erae = executeRuntimeAfterDynamicsExpression

    input = GenericField(multi=True)
    xi = input

    output = GenericField(multi=True, writable=False)
    xo = output

    time = TimeField(default_value=0.0, readable=False)
    tim = time

    frame = TimeField(default_value=0.0, readable=False)
    frm = frame

    internalRuntimeExpression = DataStringField()
    irx = internalRuntimeExpression

    internalRuntimeBeforeDynamicsExpression = DataStringField()
    irbx = internalRuntimeBeforeDynamicsExpression

    internalRuntimeAfterDynamicsExpression = DataStringField()
    irax = internalRuntimeAfterDynamicsExpression

    internalCreationExpression = DataStringField()
    icx = internalCreationExpression

    currentParticle = LongField(
        default_value=0, readable=False, writable=False
    )
    xcp = currentParticle

    diedLastTime = LongField(default_value=0)
    dlt = diedLastTime

    netEmittedLastTime = LongField(default_value=0)
    nlt = netEmittedLastTime

    startEmittedIndex = LongField(default_value=-1)
    sei = startEmittedIndex

    isDynamic = BoolField(default_value=True)
    isd = isDynamic

    dynamicsWeight = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    dw = dynamicsWeight

    forcesInWorld = BoolField(default_value=True)
    fiw = forcesInWorld

    conserve = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    con = conserve

    emissionInWorld = BoolField(default_value=True)
    eiw = emissionInWorld

    maxCount = LongField(default_value=-1)
    mxc = maxCount

    levelOfDetail = DoubleField(
        default_value=1.0, min_value=0.0, max_value=1.0
    )
    lod = levelOfDetail

    inheritFactor = DoubleField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    inh = inheritFactor

    seed = LongField(multi=True, default_value=1)
    sd = seed

    fieldData = FieldDataField(writable=False)
    fd = fieldData
    fieldDataPosition = fieldData.fieldDataPosition
    fdp = fieldDataPosition
    fieldDataVelocity = fieldData.fieldDataVelocity
    fdv = fieldDataVelocity
    fieldDataMass = fieldData.fieldDataMass
    fdm = fieldDataMass
    fieldDataDeltaTime = fieldData.fieldDataDeltaTime
    fdt = fieldDataDeltaTime

    emitterData = EmitterDataField(writable=False)
    ed = emitterData
    emitterDataPosition = emitterData.emitterDataPosition
    edp = emitterDataPosition
    emitterDataVelocity = emitterData.emitterDataVelocity
    edv = emitterDataVelocity
    emitterDataDeltaTime = emitterData.emitterDataDeltaTime
    edt = emitterDataDeltaTime

    forceDynamics = BoolField(
        default_value=False, readable=False, writable=False
    )
    fdn = forceDynamics

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    currentTimeSave = TimeField(default_value=0.0)
    cts = currentTimeSave

    evaluationTime = TimeField(default_value=0.0)
    eti = evaluationTime

    currentSceneTime = TimeField(default_value=1.0)
    cst = currentSceneTime

    lastTimeEvaluated = TimeField(default_value=0.0, writable=False)
    lti = lastTimeEvaluated

    lastSceneTime = TimeField(default_value=0.0)
    lst = lastSceneTime

    cachedTime = TimeField(default_value=0.0, writable=False)
    chti = cachedTime

    timeStepSize = TimeField(default_value=0.0, writable=False)
    tss = timeStepSize

    sceneTimeStepSize = TimeField(default_value=0.0, writable=False)
    sts = sceneTimeStepSize

    startFrame = DoubleField(default_value=1.0)
    stf = startFrame

    startTime = TimeField(default_value=0.0, writable=False)
    stt = startTime

    inputGeometry = GenericField()
    igeo = inputGeometry

    inputGeometryPoints = DataVectorArrayField(writable=False)
    igpt = inputGeometryPoints

    inputGeometrySpace = InputGeometrySpaceEnumField(default_value=0)
    igs = inputGeometrySpace

    enforceCountFromHistory = BoolField(default_value=True)
    ecfh = enforceCountFromHistory

    targetGeometry = GenericField(writable=False)
    tgeo = targetGeometry

    targetGeometryWorldMatrix = DataMatrixField()
    tgm = targetGeometryWorldMatrix

    targetGeometrySpace = TargetGeometrySpaceEnumField(default_value=2)
    tgs = targetGeometrySpace

    goalSmoothness = DoubleField(
        default_value=3.0, min_value=0.0, soft_max_value=10.0
    )
    gsm = goalSmoothness

    goalGeometry = GenericField(multi=True)
    ggeo = goalGeometry

    goalWeight = DoubleField(
        multi=True,
        default_value=0.0,
        min_value=0.0,
        max_value=1.0,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    gw = goalWeight

    goalActive = BoolField(multi=True, default_value=True)
    ga = goalActive

    goalUvSetName = DataStringField(multi=True)
    guv = goalUvSetName

    cacheData = BoolField(default_value=False)
    chd = cacheData

    cacheWidth = LongField(default_value=1)
    chw = cacheWidth

    collisions = BoolField(default_value=False, readable=False, writable=False)
    col = collisions

    traceDepth = LongField(default_value=10, min_value=0)
    trd = traceDepth

    collisionData = CollisionDataField()
    cda = collisionData
    collisionGeometry = collisionData.collisionGeometry
    cge = collisionGeometry
    collisionResilience = collisionData.collisionResilience
    crs = collisionResilience
    collisionFriction = collisionData.collisionFriction
    cfr = collisionFriction
    collisionOffset = collisionData.collisionOffset
    cof = collisionOffset

    collisionRecords = TypedField(writable=False)
    crc = collisionRecords

    totalEventCount = LongField(default_value=0, writable=False)
    tec = totalEventCount

    eventTest = BoolField(default_value=False, writable=False)
    evt = eventTest

    lastTotalEventCount = LongField(default_value=0)
    ltec = lastTotalEventCount

    eventSeed = LongField(default_value=0)
    esd = eventSeed

    eventRandState = EventRandStateField(default_value=(0, 0, 0))
    erst = eventRandState
    eventRandStateX = eventRandState.eventRandStateX
    ersx = eventRandStateX
    eventRandStateY = eventRandState.eventRandStateY
    ersy = eventRandStateY
    eventRandStateZ = eventRandState.eventRandStateZ
    ersz = eventRandStateZ

    eventTarget = MessageField(multi=True)
    etg = eventTarget

    eventName = DataStringField(multi=True)
    evn = eventName

    eventValid = LongField(multi=True, default_value=-1)
    evv = eventValid

    eventCount = ShortField(multi=True, default_value=-1)
    ecp = eventCount

    eventEmit = ShortField(multi=True, default_value=-1)
    eve = eventEmit

    eventSplit = ShortField(multi=True, default_value=-1)
    evs = eventSplit

    eventDie = ShortField(multi=True, default_value=-1)
    evd = eventDie

    eventRandom = ShortField(multi=True, default_value=-1)
    evr = eventRandom

    eventSpread = DoubleField(multi=True, default_value=-1.0)
    esp = eventSpread

    eventProc = DataStringField(multi=True)
    epr = eventProc

    instanceData = InstanceDataField(multi=True)
    idt = instanceData

    debugDraw = ShortField(default_value=0)
    dbd = debugDraw

    numberOfEvents = ShortField(default_value=0)
    nev = numberOfEvents

    eventNameCount = ShortField(default_value=0)
    enc = eventNameCount

    fieldConnections = MessageField(multi=True)
    fc = fieldConnections

    collisionConnections = MessageField(multi=True)
    cc = collisionConnections

    connectionsToMe = MessageField(multi=True)
    ct = connectionsToMe

    auxiliariesOwned = MessageField()
    ao = auxiliariesOwned

    emitterConnections = MessageField(multi=True)
    ec = emitterConnections

    inheritColor = BoolField(default_value=False)
    inc = inheritColor

    shapeNameMsg = MessageField()
    snmg = shapeNameMsg

    doDynamics = BoolField(default_value=False)
    ddy = doDynamics

    doEmission = BoolField(default_value=False)
    dem = doEmission

    forceEmission = BoolField(default_value=False)
    fem = forceEmission

    doAge = BoolField(default_value=False)
    dag = doAge

    agesLastDone = DoubleField(default_value=0.0)
    agld = agesLastDone

    timeLastComputed = DoubleField(default_value=0.0)
    tlc = timeLastComputed

    parentMatrixDirty = BoolField(default_value=False)
    pmd = parentMatrixDirty

    newFileFormat = ShortField(default_value=0)
    nff = newFileFormat

    depthSort = BoolField(default_value=False)
    ds = depthSort

    particleRenderType = ParticleRenderTypeEnumField(default_value=3)
    prt = particleRenderType

    disableCloudAxis = BoolField(default_value=False)
    dca = disableCloudAxis

    normalizeVelocity = BoolField(default_value=False)
    nvl = normalizeVelocity

    samplerPerParticleData = TypedField(writable=False)
    spd = samplerPerParticleData

    ppFieldData = TypedField(multi=True, writable=False)
    ppfd = ppFieldData

    ownerPPFieldData = TypedField(multi=True, writable=False)
    opfd = ownerPPFieldData

    deformedPosition = GenericField()
    dpos = deformedPosition

    useCustomCache = BoolField(default_value=False)
    ucc = useCustomCache

    inputMesh = GenericField()
    imsh = inputMesh

    positions = GenericField()
    poss = positions

    velocities = GenericField()
    vels = velocities

    internalState = GenericField()
    inst = internalState

    playFromCache = BoolField(default_value=False)
    pfc = playFromCache

    cacheArrayData = TypedField()
    chad = cacheArrayData

    startPositions = DataVectorArrayField()
    spns = startPositions

    startVelocities = DataVectorArrayField()
    sves = startVelocities

    thickness = FloatField(
        default_value=0.10000000149011612,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    thss = thickness

    thicknessMap = FloatField(default_value=0.10000000149011612)
    thmp = thicknessMap

    thicknessPerVertex = DataDoubleArrayField()
    thpv = thicknessPerVertex

    bounce = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    boce = bounce

    bounceMap = FloatField(default_value=0.0)
    bomp = bounceMap

    bouncePerVertex = DataDoubleArrayField()
    bpv = bouncePerVertex

    friction = FloatField(
        default_value=0.10000000149011612,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    fron = friction

    frictionMap = FloatField(default_value=0.0)
    frmp = frictionMap

    frictionPerVertex = DataDoubleArrayField()
    fpv = frictionPerVertex

    damp = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    adng = damp

    dampMap = FloatField(default_value=0.0)
    admp = dampMap

    dampPerVertex = DataDoubleArrayField()
    dpv = dampPerVertex

    stickiness = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=2.0
    )
    stck = stickiness

    stickinessMap = FloatField(default_value=0.0)
    skmp = stickinessMap

    stickinessPerVertex = DataDoubleArrayField()
    skpv = stickinessPerVertex

    collideStrength = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    clst = collideStrength

    collideStrengthMap = FloatField(default_value=0.0)
    csmp = collideStrengthMap

    collideStrengthPerVertex = DataDoubleArrayField()
    cspv = collideStrengthPerVertex

    collisionFlag = CollisionFlagEnumField(default_value=3)
    cofl = collisionFlag

    selfCollisionFlag = SelfCollisionFlagEnumField(default_value=1)
    scfl = selfCollisionFlag

    maxSelfCollisionIterations = LongField(
        default_value=4, soft_min_value=0, soft_max_value=100
    )
    msci = maxSelfCollisionIterations

    maxIterations = LongField(
        default_value=10000, soft_min_value=0, soft_max_value=20000
    )
    mxit = maxIterations

    pointMass = FloatField(
        default_value=1.0, soft_min_value=0.001, soft_max_value=10.0
    )
    pmss = pointMass

    massMap = FloatField(default_value=1.0)
    mamp = massMap

    massPerVertex = DataDoubleArrayField()
    mpv = massPerVertex

    restLengthScale = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    rlsc = restLengthScale

    localForce = LocalForceField(default_value=(0.0, 0.0, 0.0))
    lfcr = localForce
    localForceX = localForce.localForceX
    lfcx = localForceX
    localForceY = localForce.localForceY
    lfcy = localForceY
    localForceZ = localForce.localForceZ
    lfcz = localForceZ

    localWind = LocalWindField(default_value=(0.0, 0.0, 0.0))
    lwnr = localWind
    localWindX = localWind.localWindX
    lwnx = localWindX
    localWindY = localWind.localWindY
    lwny = localWindY
    localWindZ = localWind.localWindZ
    lwnz = localWindZ

    active = BoolField(default_value=True)
    actv = active

    collide = BoolField(default_value=True)
    cold = collide

    selfCollide = BoolField(default_value=True)
    scld = selfCollide

    collisionLayer = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    cll = collisionLayer

    windShadowDiffusion = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    wsdi = windShadowDiffusion

    windShadowDistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=50.0
    )
    wsds = windShadowDistance

    airPushDistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=50.0
    )
    apds = airPushDistance

    airPushVorticity = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    apvy = airPushVorticity

    pushOut = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    pou = pushOut

    pushOutRadius = FloatField(
        default_value=10.0, min_value=0.0, soft_max_value=100.0
    )
    por = pushOutRadius

    crossoverPush = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    cop = crossoverPush

    trappedCheck = BoolField(default_value=False)
    tpc = trappedCheck

    forceField = ForceFieldEnumField(default_value=0)
    ffd = forceField

    fieldMagnitude = FloatField(
        default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    fma = fieldMagnitude

    fieldMagnitudeMap = FloatField(default_value=0.0)
    fmmp = fieldMagnitudeMap

    fieldMagnitudePerVertex = DataDoubleArrayField()
    fmpv = fieldMagnitudePerVertex

    fieldDistance = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=100.0
    )
    fdi = fieldDistance

    fieldScale = FieldScaleField(multi=True, default_value=(0.0, 0.0, 0))
    fsc = fieldScale

    pointForceField = PointForceFieldEnumField(default_value=0)
    pff = pointForceField

    pointFieldMagnitude = FloatField(
        default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    pfma = pointFieldMagnitude

    selfAttract = FloatField(
        default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0
    )
    sfat = selfAttract

    pointFieldDistance = FloatField(
        default_value=2.0, min_value=0.0, soft_max_value=100.0
    )
    pfdi = pointFieldDistance

    pointFieldDropoff = PointFieldDropoffField(
        multi=True, default_value=(0.0, 0.0, 0)
    )
    pfdo = pointFieldDropoff

    thicknessMapType = ThicknessMapTypeEnumField(default_value=2)
    tmt = thicknessMapType

    bounceMapType = BounceMapTypeEnumField(default_value=2)
    bmt = bounceMapType

    frictionMapType = FrictionMapTypeEnumField(default_value=2)
    fmt = frictionMapType

    stickinessMapType = StickinessMapTypeEnumField(default_value=2)
    skmt = stickinessMapType

    collideStrengthMapType = CollideStrengthMapTypeEnumField(default_value=2)
    csmt = collideStrengthMapType

    dampMapType = DampMapTypeEnumField(default_value=2)
    dmt = dampMapType

    massMapType = MassMapTypeEnumField(default_value=2)
    mmt = massMapType

    fieldMagnitudeMapType = FieldMagnitudeMapTypeEnumField(default_value=2)
    fmmt = fieldMagnitudeMapType

    nextState = GenericField(readable=False)
    nxst = nextState

    currentState = GenericField(writable=False)
    cust = currentState

    startState = GenericField(writable=False)
    stst = startState

    nucleusId = GenericField(writable=False)
    nuid = nucleusId

    lastNBaseTime = TimeField(default_value=-1568600686539.928)
    lnbt = lastNBaseTime

    localSpaceOutput = BoolField(default_value=False)
    lsou = localSpaceOutput

    displayColor = DisplayColorField(
        default_value=(1.0, 0.800000011920929, 0.0)
    )
    dcl = displayColor
    displayColorR = displayColor.displayColorR
    dcr = displayColorR
    displayColorG = displayColor.displayColorG
    dcg = displayColorG
    displayColorB = displayColor.displayColorB
    dcb = displayColorB

    outputMesh = GenericField()
    omsh = outputMesh

    outputStartMesh = GenericField()
    otms = outputStartMesh

    restShapeMesh = GenericField()
    rsmh = restShapeMesh

    numSubdivisions = LongField(default_value=2)
    nsub = numSubdivisions

    scalingRelation = ScalingRelationEnumField(default_value=0)
    srl = scalingRelation

    stretchResistance = FloatField(
        default_value=20.0, soft_min_value=0.0, soft_max_value=200.0
    )
    stch = stretchResistance

    compressionResistance = FloatField(
        default_value=10.0, soft_min_value=0.0, soft_max_value=200.0
    )
    comr = compressionResistance

    stretchMap = FloatField(default_value=1.0)
    stmp = stretchMap

    stretchPerVertex = DataDoubleArrayField()
    spv = stretchPerVertex

    compressionMap = FloatField(default_value=1.0)
    cmmp = compressionMap

    compressionPerVertex = DataDoubleArrayField()
    cmpv = compressionPerVertex

    bendSolver = BendSolverEnumField(default_value=1)
    bnsl = bendSolver

    bendResistance = FloatField(
        default_value=0.10000000149011612,
        soft_min_value=0.0,
        soft_max_value=200.0,
    )
    bnd = bendResistance

    bendMap = FloatField(default_value=0.0)
    bemp = bendMap

    bendPerVertex = DataDoubleArrayField()
    bdpv = bendPerVertex

    bendAngleDropoff = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    bnad = bendAngleDropoff

    bendAngleDropoffMap = FloatField(default_value=0.0)
    badm = bendAngleDropoffMap

    bendAngleDropoffPerVertex = DataDoubleArrayField()
    badv = bendAngleDropoffPerVertex

    restitutionTension = FloatField(
        default_value=1000.0, soft_min_value=0.0, soft_max_value=1000.0
    )
    retn = restitutionTension

    restitutionAngle = FloatAngleField(
        default_value=360.00001001791264,
        soft_min_value=0.0,
        soft_max_value=360.0,
    )
    reae = restitutionAngle

    restitutionAngleMap = FloatField(default_value=0.0)
    ranm = restitutionAngleMap

    restitutionAnglePerVertex = DataDoubleArrayField()
    rapv = restitutionAnglePerVertex

    shearResistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=200.0
    )
    shr = shearResistance

    rigidity = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    rity = rigidity

    rigidityMap = FloatField(default_value=0.0)
    rimp = rigidityMap

    rigidityPerVertex = DataDoubleArrayField()
    rpv = rigidityPerVertex

    usePolygonShells = BoolField(default_value=False)
    ussh = usePolygonShells

    deformResistance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    dety = deformResistance

    deformMap = FloatField(default_value=0.0)
    demp = deformMap

    deformPerVertex = DataDoubleArrayField()
    dfpv = deformPerVertex

    inputMeshAttract = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    imat = inputMeshAttract

    inputAttractMethod = InputAttractMethodEnumField(default_value=0)
    iatm = inputAttractMethod

    collideLastThreshold = FloatField(
        default_value=0.20000000298023224,
        soft_min_value=0.0,
        soft_max_value=1.0,
    )
    clth = collideLastThreshold

    inputAttractMap = FloatField(default_value=0.0)
    iamp = inputAttractMap

    inputAttractPerVertex = DataDoubleArrayField()
    iapv = inputAttractPerVertex

    inputAttractDamp = FloatField(
        default_value=0.5, soft_min_value=0.0, soft_max_value=1.0
    )
    iadm = inputAttractDamp

    inputMotionDrag = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    imdr = inputMotionDrag

    restLengthScaleMap = FloatField(default_value=1.0)
    rlmp = restLengthScaleMap

    restLengthScalePerVertex = DataDoubleArrayField()
    rlpv = restLengthScalePerVertex

    liftMap = FloatField(default_value=1.0)
    lfmp = liftMap

    liftPerVertex = DataDoubleArrayField()
    lfpv = liftPerVertex

    dragMap = FloatField(default_value=1.0)
    drmp = dragMap

    dragPerVertex = DataDoubleArrayField()
    drpv = dragPerVertex

    tangentialDragMap = FloatField(default_value=1.0)
    tdmp = tangentialDragMap

    tangentialDragPerVertex = DataDoubleArrayField()
    tdpv = tangentialDragPerVertex

    wrinkleMap = FloatField(default_value=0.0)
    wkmp = wrinkleMap

    wrinklePerVertex = DataDoubleArrayField()
    wpv = wrinklePerVertex

    wrinkleMapScale = FloatField(
        default_value=1.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    wms = wrinkleMapScale

    bendAngleScale = FloatField(
        default_value=1.0, soft_min_value=-2.0, soft_max_value=2.0
    )
    basc = bendAngleScale

    sortLinks = BoolField(default_value=False)
    stlk = sortLinks

    evaluationOrder = EvaluationOrderEnumField(default_value=0)
    evo = evaluationOrder

    addCrossLinks = BoolField(default_value=True)
    aclk = addCrossLinks

    stretchDamp = FloatField(
        default_value=0.10000000149011612,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    sdmp = stretchDamp

    minimalStretch = BoolField(default_value=False)
    msso = minimalStretch

    minimalBend = BoolField(default_value=False)
    mbso = minimalBend

    minimalShear = BoolField(default_value=False)
    mshs = minimalShear

    stretchHierarchyLevels = LongField(
        default_value=0, min_value=0, soft_max_value=10
    )
    shlv = stretchHierarchyLevels

    stretchHierarchyPercent = FloatField(
        default_value=25.0, soft_min_value=0.0, soft_max_value=100.0
    )
    shpe = stretchHierarchyPercent

    selfCollideWidthScale = FloatField(
        default_value=1.0, soft_min_value=0.001, soft_max_value=2.0
    )
    scws = selfCollideWidthScale

    selfCollisionSoftness = FloatField(
        default_value=0.0, min_value=0.0, max_value=1.0
    )
    scsf = selfCollisionSoftness

    selfCrossoverPush = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=1.0
    )
    scpu = selfCrossoverPush

    selfTrappedCheck = BoolField(default_value=False)
    stpc = selfTrappedCheck

    pressureMethod = PressureMethodEnumField(default_value=0)
    pmth = pressureMethod

    pressure = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    pres = pressure

    startPressure = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    stpe = startPressure

    incompressibility = FloatField(
        default_value=5.0, soft_min_value=0.0, soft_max_value=200.0
    )
    incm = incompressibility

    pressureDamping = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    prdg = pressureDamping

    pumpRate = FloatField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    pure = pumpRate

    airTightness = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    aits = airTightness

    sealHoles = BoolField(default_value=True)
    shol = sealHoles

    ignoreSolverGravity = BoolField(default_value=False)
    igsg = ignoreSolverGravity

    ignoreSolverWind = BoolField(default_value=False)
    igsw = ignoreSolverWind

    windSelfShadow = BoolField(default_value=False)
    wssh = windSelfShadow

    lift = FloatField(
        default_value=0.05000000074505806,
        soft_min_value=0.0,
        soft_max_value=2.0,
    )
    lft = lift

    drag = FloatField(
        default_value=0.05000000074505806,
        soft_min_value=0.0,
        soft_max_value=2.0,
    )
    drg = drag

    tangentialDrag = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    tdrg = tangentialDrag

    solverDisplay = SolverDisplayEnumField(default_value=0)
    svds = solverDisplay

    stretchMapType = StretchMapTypeEnumField(default_value=2)
    smt = stretchMapType

    compressionMapType = CompressionMapTypeEnumField(default_value=2)
    cmmt = compressionMapType

    bendMapType = BendMapTypeEnumField(default_value=2)
    bdmt = bendMapType

    bendAngleDropoffMapType = BendAngleDropoffMapTypeEnumField(default_value=2)
    bamt = bendAngleDropoffMapType

    restitutionAngleMapType = RestitutionAngleMapTypeEnumField(default_value=2)
    ramt = restitutionAngleMapType

    rigidityMapType = RigidityMapTypeEnumField(default_value=2)
    rmt = rigidityMapType

    deformMapType = DeformMapTypeEnumField(default_value=2)
    dmmt = deformMapType

    inputAttractMapType = InputAttractMapTypeEnumField(default_value=2)
    iamt = inputAttractMapType

    restLengthScaleMapType = RestLengthScaleMapTypeEnumField(default_value=2)
    rlmt = restLengthScaleMapType

    liftMapType = LiftMapTypeEnumField(default_value=2)
    lfmt = liftMapType

    dragMapType = DragMapTypeEnumField(default_value=2)
    drmt = dragMapType

    tangentialDragMapType = TangentialDragMapTypeEnumField(default_value=2)
    tdmt = tangentialDragMapType

    wrinkleMapType = WrinkleMapTypeEnumField(default_value=2)
    wmt = wrinkleMapType

    cacheableAttributes = CacheableAttributesEnumField(default_value=0)
    caat = cacheableAttributes

    cacheUsage = CacheUsageEnumField(default_value=0)
    cu = cacheUsage

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    aiSelfShadows = BoolField(default_value=True, category="arnold")
    ai_self_shadows = aiSelfShadows

    aiOpaque = BoolField(default_value=True, category="arnold")
    ai_opaque = aiOpaque

    aiMatte = BoolField(default_value=False, category="arnold")
    ai_matte = aiMatte

    aiTraceSets = DataStringField(category="arnold")
    trace_sets = aiTraceSets

    aiSssSetname = DataStringField(category="arnold")
    ai_sss_setname = aiSssSetname

    aiToonId = DataStringField(category="arnold")
    ai_toon_id = aiToonId

    aiVisibleInDiffuseReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(
        default_value=True, category="arnold"
    )
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(
        default_value=True, category="arnold"
    )
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    aiExportParticleIDs = BoolField(default_value=False, category="arnold")
    ai_export_particle_ids = aiExportParticleIDs

    aiExportAttributes = DataStringField(category="arnold")
    ai_export_attributes = aiExportAttributes

    aiRenderPointsAs = AiRenderPointsAsEnumField(
        default_value=0, category="arnold"
    )
    ai_render_points_as = aiRenderPointsAs

    aiMinParticleRadius = FloatField(default_value=0.0, category="arnold")
    ai_min_particle_radius = aiMinParticleRadius

    aiRadiusMultiplier = FloatField(default_value=1.0, category="arnold")
    ai_radius_multiplier = aiRadiusMultiplier

    aiMaxParticleRadius = FloatField(
        default_value=1000000.0, category="arnold"
    )
    ai_max_particle_radius = aiMaxParticleRadius

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiFalloffExponent = FloatField(default_value=0.0, category="arnold")
    ai_falloff_exponent = aiFalloffExponent

    aiSmoothStepFalloff = BoolField(default_value=True, category="arnold")
    ai_smooth_step_falloff = aiSmoothStepFalloff

    aiImplicitSamples = LongField(
        default_value=10, min_value=1, category="arnold"
    )
    ai_implicit_samples = aiImplicitSamples

    aiStepSize = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=2.0, category="arnold"
    )
    ai_step_size = aiStepSize

    aiStepScale = FloatField(
        default_value=1.0,
        min_value=0.0,
        soft_max_value=10.0,
        category="arnold",
    )
    ai_step_scale = aiStepScale

    aiDeleteDeadParticles = BoolField(default_value=False, category="arnold")
    ai_delete_dead_particles = aiDeleteDeadParticles

    aiInterpolateBlur = BoolField(default_value=True, category="arnold")
    ai_interpolate_blur = aiInterpolateBlur

    aiEvaluateEvery = FloatField(
        default_value=1.0,
        min_value=9.999999747378752e-05,
        soft_min_value=0.10000000149011612,
        soft_max_value=2.0,
        category="arnold",
    )
    ai_evaluate_every = aiEvaluateEvery
