# coding: utf-8
from ._core import Shape
from ....attr.define.node_attr.n_particle import (
    BounceScaleField,
    BoundingBoxField,
    CachedWorldCentroidField,
    CenterField,
    CentroidField,
    CollideStrengthScaleField,
    CollisionDataField,
    ColorField,
    CompInstObjGroupsField,
    ComponentTagsField,
    DisplayColorField,
    DrawOverrideField,
    EmitterDataField,
    EventRandStateField,
    FieldDataField,
    FieldScaleField,
    FrictionScaleField,
    GhostColorPostField,
    GhostColorPreField,
    GhostCustomStepsField,
    GhostOpacityRangeField,
    IdMappingField,
    IncandescenceField,
    InstObjGroupsField,
    InstanceDataField,
    LocalForceField,
    LocalWindField,
    MassScaleField,
    ObjectColorRGBField,
    OpacityScaleField,
    OutlinerColorField,
    PointFieldDropoffField,
    PointFieldScaleField,
    PublishedNodeInfoField,
    RadiusScaleField,
    RandStateField,
    RenderInfoField,
    RenderLayerInfoField,
    StickinessScaleField,
    SurfaceTensionScaleField,
    ViscosityScaleField,
    WireColorRGBField,
    WorldCentroidField,
)
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.double import DoubleField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
from ....attr.define.std.at.numeric_scalar_range.long import LongField
from ....attr.define.std.at.numeric_scalar_range.short import ShortField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.unit_scalar.time import TimeField
from ....attr.define.std.dt.double_array import DataDoubleArrayField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class ViewModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2


class ViewModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FLAT = 0
    USE_TEMPLATE = 1
    GROUP_BY_NODE = 2

    NAME_MAP = {
        FLAT: "Flat",
        USE_TEMPLATE: "Use Template",
        GROUP_BY_NODE: "Group By Node",
    }


class ViewModeEnumField(
    EnumField[ViewModeEnumAttrOperator, ViewModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewModeEnumAttrOperator
    PLUG_CLS = ViewModeEnumPlugOperator


class UiTreatmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000


class UiTreatmentEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    STANDARD = 0
    SHADER = 1
    CUSTOM = 1000

    NAME_MAP = {
        STANDARD: "Standard",
        SHADER: "Shader",
        CUSTOM: "Custom",
    }


class UiTreatmentEnumField(
    EnumField[UiTreatmentEnumAttrOperator, UiTreatmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UiTreatmentEnumAttrOperator
    PLUG_CLS = UiTreatmentEnumPlugOperator


class UseObjectColorEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2


class UseObjectColorEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    DEFAULT = 0
    INDEXED = 1
    RGB = 2

    NAME_MAP = {
        DEFAULT: "Default",
        INDEXED: "Indexed",
        RGB: "RGB",
    }


class UseObjectColorEnumField(
    EnumField[UseObjectColorEnumAttrOperator, UseObjectColorEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = UseObjectColorEnumAttrOperator
    PLUG_CLS = UseObjectColorEnumPlugOperator


class GhostingModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5


class GhostingModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    PRE_AND_POST_FRAMES = 0
    PRE_FRAMES = 1
    POST_FRAMES = 2
    CUSTOM_FRAMES = 3
    PRE_AND_POST_KEYFRAMES = 4
    ALL_KEYFRAMES = 5

    NAME_MAP = {
        PRE_AND_POST_FRAMES: "Pre And Post Frames",
        PRE_FRAMES: "Pre Frames",
        POST_FRAMES: "Post Frames",
        CUSTOM_FRAMES: "Custom Frames",
        PRE_AND_POST_KEYFRAMES: "Pre And Post Keyframes",
        ALL_KEYFRAMES: "All Keyframes",
    }


class GhostingModeEnumField(
    EnumField[GhostingModeEnumAttrOperator, GhostingModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = GhostingModeEnumAttrOperator
    PLUG_CLS = GhostingModeEnumPlugOperator


class LifespanModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LIVE_FOREVER = 0
    CONSTANT = 1
    RANDOM_RANGE = 2
    LIFESPANPP_ONLY = 3


class LifespanModeEnumAttrOperator(EnumAttrOperator):
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


class InputGeometrySpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class InputGeometrySpaceEnumAttrOperator(EnumAttrOperator):
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
    EnumField[InputGeometrySpaceEnumAttrOperator, InputGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InputGeometrySpaceEnumAttrOperator
    PLUG_CLS = InputGeometrySpaceEnumPlugOperator


class TargetGeometrySpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    GEOMETRY_LOCAL = 0
    WORLD = 1
    PARTICLE_LOCAL = 2


class TargetGeometrySpaceEnumAttrOperator(EnumAttrOperator):
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
    EnumField[TargetGeometrySpaceEnumAttrOperator, TargetGeometrySpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TargetGeometrySpaceEnumAttrOperator
    PLUG_CLS = TargetGeometrySpaceEnumPlugOperator


class ParticleRenderTypeEnumPlugOperator(EnumPlugOperator):
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


class ParticleRenderTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[ParticleRenderTypeEnumAttrOperator, ParticleRenderTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ParticleRenderTypeEnumAttrOperator
    PLUG_CLS = ParticleRenderTypeEnumPlugOperator


class AiRenderPointsAsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINTS = 0
    SPHERES = 1
    QUADS = 2


class AiRenderPointsAsEnumAttrOperator(EnumAttrOperator):
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
    EnumField[AiRenderPointsAsEnumAttrOperator, AiRenderPointsAsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiRenderPointsAsEnumAttrOperator
    PLUG_CLS = AiRenderPointsAsEnumPlugOperator


class CollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    EDGE = 2
    FACE = 3


class CollisionFlagEnumAttrOperator(EnumAttrOperator):
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


class SelfCollisionFlagEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    VERTEX = 1
    VERTEXEDGE = 2
    VERTEXFACE = 3
    FULL_SURFACE = 4


class SelfCollisionFlagEnumAttrOperator(EnumAttrOperator):
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
    EnumField[SelfCollisionFlagEnumAttrOperator, SelfCollisionFlagEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SelfCollisionFlagEnumAttrOperator
    PLUG_CLS = SelfCollisionFlagEnumPlugOperator


class ForceFieldEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    ALONGNORMAL = 1
    SINGLE_SIDED = 2
    DOUBLE_SIDED = 3


class ForceFieldEnumAttrOperator(EnumAttrOperator):
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


class PointForceFieldEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    THICKNESSRELATIVE = 1
    WORLDSPACE = 2


class PointForceFieldEnumAttrOperator(EnumAttrOperator):
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


class ThicknessMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class ThicknessMapTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[ThicknessMapTypeEnumAttrOperator, ThicknessMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ThicknessMapTypeEnumAttrOperator
    PLUG_CLS = ThicknessMapTypeEnumPlugOperator


class BounceMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class BounceMapTypeEnumAttrOperator(EnumAttrOperator):
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


class FrictionMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class FrictionMapTypeEnumAttrOperator(EnumAttrOperator):
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


class StickinessMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class StickinessMapTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[StickinessMapTypeEnumAttrOperator, StickinessMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessMapTypeEnumAttrOperator
    PLUG_CLS = StickinessMapTypeEnumPlugOperator


class CollideStrengthMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class CollideStrengthMapTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[CollideStrengthMapTypeEnumAttrOperator, CollideStrengthMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthMapTypeEnumAttrOperator
    PLUG_CLS = CollideStrengthMapTypeEnumPlugOperator


class DampMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class DampMapTypeEnumAttrOperator(EnumAttrOperator):
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


class MassMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class MassMapTypeEnumAttrOperator(EnumAttrOperator):
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


class FieldMagnitudeMapTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    PER_MINUS_VERTEX = 1
    TEXTURE = 2


class FieldMagnitudeMapTypeEnumAttrOperator(EnumAttrOperator):
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
    EnumField[FieldMagnitudeMapTypeEnumAttrOperator, FieldMagnitudeMapTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FieldMagnitudeMapTypeEnumAttrOperator
    PLUG_CLS = FieldMagnitudeMapTypeEnumPlugOperator


class ScalingRelationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINK = 0
    OBJECT_SPACE = 1
    WORLD_SPACE = 2


class ScalingRelationEnumAttrOperator(EnumAttrOperator):
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


class SolverDisplayEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2


class SolverDisplayEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    COLLISION_THICKNESS = 1
    SELF_COLLISION_THICKNESS = 2

    NAME_MAP = {
        OFF: "Off",
        COLLISION_THICKNESS: "Collision Thickness",
        SELF_COLLISION_THICKNESS: "Self Collision Thickness",
    }


class SolverDisplayEnumField(
    EnumField[SolverDisplayEnumAttrOperator, SolverDisplayEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SolverDisplayEnumAttrOperator
    PLUG_CLS = SolverDisplayEnumPlugOperator


class ViscosityScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class ViscosityScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class ViscosityScaleInputEnumField(
    EnumField[ViscosityScaleInputEnumAttrOperator, ViscosityScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViscosityScaleInputEnumAttrOperator
    PLUG_CLS = ViscosityScaleInputEnumPlugOperator


class SurfaceTensionScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class SurfaceTensionScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class SurfaceTensionScaleInputEnumField(
    EnumField[SurfaceTensionScaleInputEnumAttrOperator, SurfaceTensionScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SurfaceTensionScaleInputEnumAttrOperator
    PLUG_CLS = SurfaceTensionScaleInputEnumPlugOperator


class RadiusScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6


class RadiusScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
    }


class RadiusScaleInputEnumField(
    EnumField[RadiusScaleInputEnumAttrOperator, RadiusScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RadiusScaleInputEnumAttrOperator
    PLUG_CLS = RadiusScaleInputEnumPlugOperator


class MassScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class MassScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class MassScaleInputEnumField(
    EnumField[MassScaleInputEnumAttrOperator, MassScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MassScaleInputEnumAttrOperator
    PLUG_CLS = MassScaleInputEnumPlugOperator


class PointFieldScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class PointFieldScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class PointFieldScaleInputEnumField(
    EnumField[PointFieldScaleInputEnumAttrOperator, PointFieldScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PointFieldScaleInputEnumAttrOperator
    PLUG_CLS = PointFieldScaleInputEnumPlugOperator


class FrictionScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class FrictionScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class FrictionScaleInputEnumField(
    EnumField[FrictionScaleInputEnumAttrOperator, FrictionScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FrictionScaleInputEnumAttrOperator
    PLUG_CLS = FrictionScaleInputEnumPlugOperator


class StickinessScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class StickinessScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class StickinessScaleInputEnumField(
    EnumField[StickinessScaleInputEnumAttrOperator, StickinessScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = StickinessScaleInputEnumAttrOperator
    PLUG_CLS = StickinessScaleInputEnumPlugOperator


class CollideStrengthScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class CollideStrengthScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class CollideStrengthScaleInputEnumField(
    EnumField[CollideStrengthScaleInputEnumAttrOperator, CollideStrengthScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CollideStrengthScaleInputEnumAttrOperator
    PLUG_CLS = CollideStrengthScaleInputEnumPlugOperator


class BounceScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class BounceScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class BounceScaleInputEnumField(
    EnumField[BounceScaleInputEnumAttrOperator, BounceScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BounceScaleInputEnumAttrOperator
    PLUG_CLS = BounceScaleInputEnumPlugOperator


class OpacityScaleInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class OpacityScaleInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    OFF = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        OFF: "Off",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class OpacityScaleInputEnumField(
    EnumField[OpacityScaleInputEnumAttrOperator, OpacityScaleInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OpacityScaleInputEnumAttrOperator
    PLUG_CLS = OpacityScaleInputEnumPlugOperator


class ColorInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class ColorInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        CONSTANT: "Constant",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class ColorInputEnumField(
    EnumField[ColorInputEnumAttrOperator, ColorInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ColorInputEnumAttrOperator
    PLUG_CLS = ColorInputEnumPlugOperator


class IncandescenceInputEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CONSTANT = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7


class IncandescenceInputEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    CONSTANT = 0
    AGE = 1
    NORMALIZED_AGE = 2
    SPEED = 3
    ACCELERATION = 4
    PARTICLE_ID = 5
    RANDOMIZED_ID = 6
    RADIUS = 7

    NAME_MAP = {
        CONSTANT: "Constant",
        AGE: "Age",
        NORMALIZED_AGE: "Normalized Age",
        SPEED: "Speed",
        ACCELERATION: "Acceleration",
        PARTICLE_ID: "Particle ID",
        RANDOMIZED_ID: "Randomized ID",
        RADIUS: "Radius",
    }


class IncandescenceInputEnumField(
    EnumField[IncandescenceInputEnumAttrOperator, IncandescenceInputEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IncandescenceInputEnumAttrOperator
    PLUG_CLS = IncandescenceInputEnumPlugOperator


class CacheableAttributesEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMICS_AND_RENDERING = 2
    ALL = 3


class CacheableAttributesEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    POSITION = 0
    POSITION_AND_VELOCITY = 1
    DYNAMICS_AND_RENDERING = 2
    ALL = 3

    NAME_MAP = {
        POSITION: "Position",
        POSITION_AND_VELOCITY: "Position And Velocity",
        DYNAMICS_AND_RENDERING: "Dynamics and Rendering",
        ALL: "All",
    }


class CacheableAttributesEnumField(
    EnumField[CacheableAttributesEnumAttrOperator, CacheableAttributesEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheableAttributesEnumAttrOperator
    PLUG_CLS = CacheableAttributesEnumPlugOperator


class MeshMethodEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    TRIANGLE_MESH = 0
    TETRAHEDRA = 1
    ACUTE_TETRAHEDRA = 2
    QUAD_MESH = 3


class MeshMethodEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    TRIANGLE_MESH = 0
    TETRAHEDRA = 1
    ACUTE_TETRAHEDRA = 2
    QUAD_MESH = 3

    NAME_MAP = {
        TRIANGLE_MESH: "Triangle Mesh",
        TETRAHEDRA: "Tetrahedra",
        ACUTE_TETRAHEDRA: "Acute Tetrahedra",
        QUAD_MESH: "Quad Mesh",
    }


class MeshMethodEnumField(
    EnumField[MeshMethodEnumAttrOperator, MeshMethodEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MeshMethodEnumAttrOperator
    PLUG_CLS = MeshMethodEnumPlugOperator


class NParticle(Shape):
    __slots__ = ()

    NODE_TYPE = "nParticle"

    hyperLayout = MessageField()
    hl = hyperLayout

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    blackBox = BoolField(default_value=False)
    bbx = blackBox

    borderConnections = MessageField(multi=True)
    boc = borderConnections

    isHierarchicalConnection = BoolField(multi=True, default_value=False)
    ish = isHierarchicalConnection

    publishedNodeInfo = PublishedNodeInfoField(multi=True)
    pni = publishedNodeInfo

    rmbCommand = DataStringField()
    rmc = rmbCommand

    templateName = DataStringField()
    tna = templateName

    templatePath = DataStringField()
    tpt = templatePath

    viewName = DataStringField()
    vwn = viewName

    iconName = DataStringField()
    icn = iconName

    viewMode = ViewModeEnumField(default_value=2)
    vwm = viewMode

    templateVersion = LongField(default_value=0)
    tpv = templateVersion

    uiTreatment = UiTreatmentEnumField(default_value=0)
    uit = uiTreatment

    customTreatment = DataStringField()
    ctrt = customTreatment

    creator = DataStringField()
    ctor = creator

    creationDate = DataStringField()
    cdat = creationDate

    containerType = DataStringField()
    ctyp = containerType

    boundingBox = BoundingBoxField(writable=False)
    bb = boundingBox
    boundingBoxMin = boundingBox.boundingBoxMin
    bbmn = boundingBoxMin
    boundingBoxMax = boundingBox.boundingBoxMax
    bbmx = boundingBoxMax
    boundingBoxSize = boundingBox.boundingBoxSize
    bbsi = boundingBoxSize

    center = CenterField(default_value=(0.0, 0.0, 0.0), writable=False)
    c = center
    boundingBoxCenterX = center.boundingBoxCenterX
    bcx = boundingBoxCenterX
    boundingBoxCenterY = center.boundingBoxCenterY
    bcy = boundingBoxCenterY
    boundingBoxCenterZ = center.boundingBoxCenterZ
    bcz = boundingBoxCenterZ

    matrix = DataMatrixField(writable=False)
    m = matrix

    inverseMatrix = DataMatrixField(writable=False)
    im = inverseMatrix

    worldMatrix = DataMatrixField(multi=True, writable=False)
    wm = worldMatrix

    worldInverseMatrix = DataMatrixField(multi=True, writable=False)
    wim = worldInverseMatrix

    parentMatrix = DataMatrixField(multi=True, writable=False)
    pm = parentMatrix

    parentInverseMatrix = DataMatrixField(multi=True, writable=False)
    pim = parentInverseMatrix

    visibility = BoolField(default_value=True)
    v = visibility

    intermediateObject = BoolField(default_value=False)
    io = intermediateObject

    template = BoolField(default_value=False)
    tmp = template

    instObjGroups = InstObjGroupsField(multi=True)
    iog = instObjGroups

    objectColorRGB = ObjectColorRGBField(default_value=(0.0, 0.0, 0.0))
    obcc = objectColorRGB
    objectColorR = objectColorRGB.objectColorR
    obcr = objectColorR
    objectColorG = objectColorRGB.objectColorG
    obcg = objectColorG
    objectColorB = objectColorRGB.objectColorB
    obcb = objectColorB

    wireColorRGB = WireColorRGBField(default_value=(0.0, 0.0, 0.0))
    wfcc = wireColorRGB
    wireColorR = wireColorRGB.wireColorR
    wfcr = wireColorR
    wireColorG = wireColorRGB.wireColorG
    wfcg = wireColorG
    wireColorB = wireColorRGB.wireColorB
    wfcb = wireColorB

    useObjectColor = UseObjectColorEnumField(default_value=0)
    uoc = useObjectColor

    objectColor = ShortField(default_value=0, min_value=0, max_value=7)
    oc = objectColor

    drawOverride = DrawOverrideField()
    do = drawOverride
    overrideDisplayType = drawOverride.overrideDisplayType
    ovdt = overrideDisplayType
    overrideLevelOfDetail = drawOverride.overrideLevelOfDetail
    ovlod = overrideLevelOfDetail
    overrideShading = drawOverride.overrideShading
    ovs = overrideShading
    overrideTexturing = drawOverride.overrideTexturing
    ovt = overrideTexturing
    overridePlayback = drawOverride.overridePlayback
    ovp = overridePlayback
    overrideEnabled = drawOverride.overrideEnabled
    ove = overrideEnabled
    overrideVisibility = drawOverride.overrideVisibility
    ovv = overrideVisibility
    hideOnPlayback = drawOverride.hideOnPlayback
    hpb = hideOnPlayback
    overrideRGBColors = drawOverride.overrideRGBColors
    ovrgbf = overrideRGBColors
    overrideColor = drawOverride.overrideColor
    ovc = overrideColor
    overrideColorRGB = drawOverride.overrideColorRGB
    ovrgb = overrideColorRGB
    overrideColorA = drawOverride.overrideColorA
    ovca = overrideColorA

    lodVisibility = BoolField(default_value=True)
    lodv = lodVisibility

    selectionChildHighlighting = BoolField(default_value=True)
    sech = selectionChildHighlighting

    renderInfo = RenderInfoField(default_value=(0.0, 1.0, 0.0))
    ri = renderInfo
    identification = renderInfo.identification
    rlid = identification
    layerRenderable = renderInfo.layerRenderable
    rndr = layerRenderable
    layerOverrideColor = renderInfo.layerOverrideColor
    lovc = layerOverrideColor

    renderLayerInfo = RenderLayerInfoField(multi=True, default_value=(0.0, 1.0, 0.0))
    rlio = renderLayerInfo

    ghosting = BoolField(default_value=False)
    gh = ghosting

    ghostingMode = GhostingModeEnumField(default_value=0)
    gm = ghostingMode

    ghostCustomSteps = GhostCustomStepsField(default_value=(3.0, 3.0, 1.0))
    gcs = ghostCustomSteps
    ghostPreFrames = ghostCustomSteps.ghostPreFrames
    gprf = ghostPreFrames
    ghostPostFrames = ghostCustomSteps.ghostPostFrames
    gpof = ghostPostFrames
    ghostsStep = ghostCustomSteps.ghostsStep
    gstp = ghostsStep

    ghostFrames = TypedField()
    gf = ghostFrames

    ghostOpacityRange = GhostOpacityRangeField(default_value=(0.15000000596046448, 0.5), min_value=(0.0, 0.0), max_value=(1.0, 1.0))
    golr = ghostOpacityRange
    ghostFarOpacity = ghostOpacityRange.ghostFarOpacity
    gfro = ghostFarOpacity
    ghostNearOpacity = ghostOpacityRange.ghostNearOpacity
    gnro = ghostNearOpacity

    ghostColorPre = GhostColorPreField(default_value=(0.44699999690055847, 1.0, 1.0), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gcp = ghostColorPre
    ghostColorPreR = ghostColorPre.ghostColorPreR
    grr = ghostColorPreR
    ghostColorPreG = ghostColorPre.ghostColorPreG
    gpg = ghostColorPreG
    ghostColorPreB = ghostColorPre.ghostColorPreB
    gpb = ghostColorPreB

    ghostColorPost = GhostColorPostField(default_value=(0.878000020980835, 0.6779999732971191, 0.6629999876022339), min_value=(0.0, 0.0, 0.0), max_value=(1.0, 1.0, 1.0))
    gac = ghostColorPost
    ghostColorPostR = ghostColorPost.ghostColorPostR
    gar = ghostColorPostR
    ghostColorPostG = ghostColorPost.ghostColorPostG
    gag = ghostColorPostG
    ghostColorPostB = ghostColorPost.ghostColorPostB
    gab = ghostColorPostB

    ghostDriver = MessageField()
    gdr = ghostDriver

    ghostUseDriver = BoolField(default_value=False)
    gud = ghostUseDriver

    hiddenInOutliner = BoolField(default_value=False)
    hio = hiddenInOutliner

    useOutlinerColor = BoolField(default_value=False)
    uocol = useOutlinerColor

    outlinerColor = OutlinerColorField(default_value=(0.0, 0.0, 0.0))
    oclr = outlinerColor
    outlinerColorR = outlinerColor.outlinerColorR
    oclrr = outlinerColorR
    outlinerColorG = outlinerColor.outlinerColorG
    oclrg = outlinerColorG
    outlinerColorB = outlinerColor.outlinerColorB
    oclrb = outlinerColorB

    renderType = ShortField(default_value=0)
    rt = renderType

    renderVolume = BoolField(default_value=False)
    rv = renderVolume

    visibleFraction = FloatField(default_value=1.0)
    vf = visibleFraction

    hardwareFogMultiplier = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
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

    maxVisibilitySamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
    mvs = maxVisibilitySamples

    geometryAntialiasingOverride = BoolField(default_value=False)
    gao = geometryAntialiasingOverride

    antialiasingLevel = LongField(default_value=1, min_value=1, max_value=5, soft_max_value=5)
    gal = antialiasingLevel

    shadingSamplesOverride = BoolField(default_value=False)
    sso = shadingSamplesOverride

    shadingSamples = LongField(default_value=1, min_value=1, max_value=32)
    ssa = shadingSamples

    maxShadingSamples = LongField(default_value=1, min_value=1, max_value=32, soft_max_value=20)
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

    worldCentroid = WorldCentroidField(default_value=(0.0, 0.0, 0.0), writable=False)
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

    cachedWorldCentroid = CachedWorldCentroidField(default_value=(0.0, 0.0, 0.0), writable=False)
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

    collisionEvents = BoolField(default_value=False, readable=False, writable=False)
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

    executeCreationExpression = BoolField(default_value=False, readable=False, writable=False)
    ece = executeCreationExpression

    executeRuntimeBeforeDynamicsExpression = BoolField(default_value=False, readable=False, writable=False)
    erbe = executeRuntimeBeforeDynamicsExpression

    executeRuntimeAfterDynamicsExpression = BoolField(default_value=False, readable=False, writable=False)
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

    currentParticle = LongField(default_value=0, readable=False, writable=False)
    xcp = currentParticle

    diedLastTime = LongField(default_value=0)
    dlt = diedLastTime

    netEmittedLastTime = LongField(default_value=0)
    nlt = netEmittedLastTime

    startEmittedIndex = LongField(default_value=-1)
    sei = startEmittedIndex

    isDynamic = BoolField(default_value=True)
    isd = isDynamic

    dynamicsWeight = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    dw = dynamicsWeight

    forcesInWorld = BoolField(default_value=True)
    fiw = forcesInWorld

    conserve = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    con = conserve

    emissionInWorld = BoolField(default_value=True)
    eiw = emissionInWorld

    maxCount = LongField(default_value=-1)
    mxc = maxCount

    levelOfDetail = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    lod = levelOfDetail

    inheritFactor = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
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

    forceDynamics = BoolField(default_value=False, readable=False, writable=False)
    fdn = forceDynamics

    currentTime = TimeField(default_value=0.0)
    cti = currentTime

    currentTimeSave = TimeField(default_value=0.0)
    cts = currentTimeSave

    evaluationTime = TimeField(default_value=0.0)
    eti = evaluationTime

    currentSceneTime = TimeField(default_value=2.5)
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

    goalSmoothness = DoubleField(default_value=3.0, min_value=0.0, soft_max_value=10.0)
    gsm = goalSmoothness

    goalGeometry = GenericField(multi=True)
    ggeo = goalGeometry

    goalWeight = DoubleField(multi=True, default_value=0.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
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

    aiVisibleInDiffuseReflection = BoolField(default_value=True, category="arnold")
    ai_vidr = aiVisibleInDiffuseReflection

    aiVisibleInSpecularReflection = BoolField(default_value=True, category="arnold")
    ai_visr = aiVisibleInSpecularReflection

    aiVisibleInDiffuseTransmission = BoolField(default_value=True, category="arnold")
    ai_vidt = aiVisibleInDiffuseTransmission

    aiVisibleInSpecularTransmission = BoolField(default_value=True, category="arnold")
    ai_vist = aiVisibleInSpecularTransmission

    aiVisibleInVolume = BoolField(default_value=True, category="arnold")
    ai_viv = aiVisibleInVolume

    aiExportParticleIDs = BoolField(default_value=False, category="arnold")
    ai_export_particle_ids = aiExportParticleIDs

    aiExportAttributes = DataStringField(category="arnold")
    ai_export_attributes = aiExportAttributes

    aiRenderPointsAs = AiRenderPointsAsEnumField(default_value=0, category="arnold")
    ai_render_points_as = aiRenderPointsAs

    aiMinParticleRadius = FloatField(default_value=0.0, category="arnold")
    ai_min_particle_radius = aiMinParticleRadius

    aiRadiusMultiplier = FloatField(default_value=1.0, category="arnold")
    ai_radius_multiplier = aiRadiusMultiplier

    aiMaxParticleRadius = FloatField(default_value=1000000.0, category="arnold")
    ai_max_particle_radius = aiMaxParticleRadius

    aiMinPixelWidth = FloatField(default_value=0.0, category="arnold")
    ai_min_pixel_width = aiMinPixelWidth

    aiFalloffExponent = FloatField(default_value=0.0, category="arnold")
    ai_falloff_exponent = aiFalloffExponent

    aiSmoothStepFalloff = BoolField(default_value=True, category="arnold")
    ai_smooth_step_falloff = aiSmoothStepFalloff

    aiImplicitSamples = LongField(default_value=10, min_value=1, category="arnold")
    ai_implicit_samples = aiImplicitSamples

    aiStepSize = FloatField(default_value=0.0, min_value=0.0, soft_max_value=2.0, category="arnold")
    ai_step_size = aiStepSize

    aiStepScale = FloatField(default_value=1.0, min_value=0.0, soft_max_value=10.0, category="arnold")
    ai_step_scale = aiStepScale

    aiDeleteDeadParticles = BoolField(default_value=False, category="arnold")
    ai_delete_dead_particles = aiDeleteDeadParticles

    aiInterpolateBlur = BoolField(default_value=True, category="arnold")
    ai_interpolate_blur = aiInterpolateBlur

    aiEvaluateEvery = FloatField(default_value=1.0, min_value=9.999999747378752e-05, soft_min_value=0.10000000149011612, soft_max_value=2.0, category="arnold")
    ai_evaluate_every = aiEvaluateEvery

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

    thickness = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    thss = thickness

    thicknessMap = FloatField(default_value=0.10000000149011612)
    thmp = thicknessMap

    thicknessPerVertex = DataDoubleArrayField()
    thpv = thicknessPerVertex

    bounce = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    boce = bounce

    bounceMap = FloatField(default_value=0.0)
    bomp = bounceMap

    bouncePerVertex = DataDoubleArrayField()
    bpv = bouncePerVertex

    friction = FloatField(default_value=0.10000000149011612, soft_min_value=0.0, soft_max_value=1.0)
    fron = friction

    frictionMap = FloatField(default_value=0.0)
    frmp = frictionMap

    frictionPerVertex = DataDoubleArrayField()
    fpv = frictionPerVertex

    damp = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    adng = damp

    dampMap = FloatField(default_value=0.0)
    admp = dampMap

    dampPerVertex = DataDoubleArrayField()
    dpv = dampPerVertex

    stickiness = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)
    stck = stickiness

    stickinessMap = FloatField(default_value=0.0)
    skmp = stickinessMap

    stickinessPerVertex = DataDoubleArrayField()
    skpv = stickinessPerVertex

    collideStrength = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    clst = collideStrength

    collideStrengthMap = FloatField(default_value=0.0)
    csmp = collideStrengthMap

    collideStrengthPerVertex = DataDoubleArrayField()
    cspv = collideStrengthPerVertex

    collisionFlag = CollisionFlagEnumField(default_value=3)
    cofl = collisionFlag

    selfCollisionFlag = SelfCollisionFlagEnumField(default_value=1)
    scfl = selfCollisionFlag

    maxSelfCollisionIterations = LongField(default_value=4, soft_min_value=0, soft_max_value=100)
    msci = maxSelfCollisionIterations

    maxIterations = LongField(default_value=10000, soft_min_value=0, soft_max_value=20000)
    mxit = maxIterations

    pointMass = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=10.0)
    pmss = pointMass

    massMap = FloatField(default_value=1.0)
    mamp = massMap

    massPerVertex = DataDoubleArrayField()
    mpv = massPerVertex

    restLengthScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
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

    collisionLayer = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    cll = collisionLayer

    windShadowDiffusion = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    wsdi = windShadowDiffusion

    windShadowDistance = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)
    wsds = windShadowDistance

    airPushDistance = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=50.0)
    apds = airPushDistance

    airPushVorticity = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    apvy = airPushVorticity

    pushOut = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    pou = pushOut

    pushOutRadius = FloatField(default_value=10.0, min_value=0.0, soft_max_value=100.0)
    por = pushOutRadius

    crossoverPush = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    cop = crossoverPush

    trappedCheck = BoolField(default_value=False)
    tpc = trappedCheck

    forceField = ForceFieldEnumField(default_value=0)
    ffd = forceField

    fieldMagnitude = FloatField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    fma = fieldMagnitude

    fieldMagnitudeMap = FloatField(default_value=0.0)
    fmmp = fieldMagnitudeMap

    fieldMagnitudePerVertex = DataDoubleArrayField()
    fmpv = fieldMagnitudePerVertex

    fieldDistance = FloatField(default_value=1.0, min_value=0.0, soft_max_value=100.0)
    fdi = fieldDistance

    fieldScale = FieldScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    fsc = fieldScale

    pointForceField = PointForceFieldEnumField(default_value=0)
    pff = pointForceField

    pointFieldMagnitude = FloatField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    pfma = pointFieldMagnitude

    selfAttract = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
    sfat = selfAttract

    pointFieldDistance = FloatField(default_value=2.0, min_value=0.0, soft_max_value=100.0)
    pfdi = pointFieldDistance

    pointFieldDropoff = PointFieldDropoffField(multi=True, default_value=(0.0, 0.0, 0.0))
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

    lastNBaseTime = TimeField(default_value=-3921501716349.82)
    lnbt = lastNBaseTime

    localSpaceOutput = BoolField(default_value=False)
    lsou = localSpaceOutput

    displayColor = DisplayColorField(default_value=(1.0, 0.800000011920929, 0.0))
    dcl = displayColor
    displayColorR = displayColor.displayColorR
    dcr = displayColorR
    displayColorG = displayColor.displayColorG
    dcg = displayColorG
    displayColorB = displayColor.displayColorB
    dcb = displayColorB

    numSubdivisions = LongField(default_value=2)
    nsub = numSubdivisions

    scalingRelation = ScalingRelationEnumField(default_value=0)
    srl = scalingRelation

    inputAttract = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    iatt = inputAttract

    inputAttractDamp = FloatField(default_value=0.5, soft_min_value=0.0, soft_max_value=1.0)
    iadm = inputAttractDamp

    ignoreSolverGravity = BoolField(default_value=False)
    igsg = ignoreSolverGravity

    ignoreSolverWind = BoolField(default_value=False)
    igsw = ignoreSolverWind

    windSelfShadow = BoolField(default_value=False)
    wssh = windSelfShadow

    drag = FloatField(default_value=0.009999999776482582, soft_min_value=0.0, soft_max_value=2.0)
    drg = drag

    solverDisplay = SolverDisplayEnumField(default_value=0)
    svds = solverDisplay

    collideWidthScale = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=2.0)
    cwds = collideWidthScale

    selfCollideWidthScale = FloatField(default_value=1.0, soft_min_value=0.001, soft_max_value=2.0)
    scws = selfCollideWidthScale

    emissionOverlapPruning = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    eopr = emissionOverlapPruning

    computeRotation = BoolField(default_value=False)
    cprt = computeRotation

    rotationFriction = FloatField(default_value=0.8999999761581421, soft_min_value=0.0, soft_max_value=1.0)
    rtfr = rotationFriction

    rotationDamp = FloatField(default_value=0.0010000000474974513, soft_min_value=0.0, soft_max_value=1.0)
    rtdp = rotationDamp

    enableSPH = BoolField(default_value=False)
    esph = enableSPH

    parallelSPH = BoolField(default_value=False)
    psph = parallelSPH

    recomputePairsSPH = BoolField(default_value=False)
    rpsp = recomputePairsSPH

    incompressibility = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    incp = incompressibility

    viscosity = FloatField(default_value=0.10000000149011612, min_value=0.0, soft_max_value=1.0)
    visc = viscosity

    viscosityScale = ViscosityScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    vssc = viscosityScale

    viscosityScaleInput = ViscosityScaleInputEnumField(default_value=0)
    vsli = viscosityScaleInput

    viscosityScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    vsix = viscosityScaleInputMax

    surfaceTension = FloatField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    suft = surfaceTension

    surfaceTensionScale = SurfaceTensionScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    stns = surfaceTensionScale

    surfaceTensionScaleInput = SurfaceTensionScaleInputEnumField(default_value=0)
    stli = surfaceTensionScaleInput

    surfaceTensionScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    stix = surfaceTensionScaleInputMax

    restDensity = FloatField(default_value=2.0, min_value=1.0, soft_max_value=2.0)
    rdns = restDensity

    radiusScaleSPH = FloatField(default_value=1.0, min_value=0.0, soft_max_value=2.0)
    rsph = radiusScaleSPH

    threshold = DoubleField(default_value=0.1, min_value=0.0, soft_max_value=2.0)
    thr = threshold

    radius = FloatField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=20.0)
    ra = radius

    radiusScale = RadiusScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    rdc = radiusScale

    radiusScaleInput = RadiusScaleInputEnumField(default_value=0)
    rci = radiusScaleInput

    radiusScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    rcix = radiusScaleInputMax

    radiusScaleRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    rsr = radiusScaleRandomize

    massScale = MassScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    mssc = massScale

    massScaleInput = MassScaleInputEnumField(default_value=0)
    msli = massScaleInput

    massScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    msix = massScaleInputMax

    massScaleRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    msr = massScaleRandomize

    pointFieldScale = PointFieldScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    pfsc = pointFieldScale

    pointFieldScaleInput = PointFieldScaleInputEnumField(default_value=0)
    psli = pointFieldScaleInput

    pointFieldScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    psix = pointFieldScaleInputMax

    frictionScale = FrictionScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    frsc = frictionScale

    frictionScaleInput = FrictionScaleInputEnumField(default_value=0)
    fsli = frictionScaleInput

    frictionScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    fsix = frictionScaleInputMax

    frictionRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    fcr = frictionRandomize

    stickinessScale = StickinessScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    stsc = stickinessScale

    stickinessScaleInput = StickinessScaleInputEnumField(default_value=0)
    ssli = stickinessScaleInput

    stickinessScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    ssix = stickinessScaleInputMax

    stickinessRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    stra = stickinessRandomize

    collideStrengthScale = CollideStrengthScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    clsc = collideStrengthScale

    collideStrengthScaleInput = CollideStrengthScaleInputEnumField(default_value=0)
    csli = collideStrengthScaleInput

    collideStrengthScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    csix = collideStrengthScaleInputMax

    bounceScale = BounceScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    bosc = bounceScale

    bounceScaleInput = BounceScaleInputEnumField(default_value=0)
    bsli = bounceScaleInput

    bounceScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    bsix = bounceScaleInputMax

    bounceRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    bora = bounceRandomize

    opacity = DoubleField(default_value=1.0, min_value=0.0, max_value=1.0)
    op = opacity

    opacityScale = OpacityScaleField(multi=True, default_value=(0.0, 0.0, 0.0))
    opc = opacityScale

    opacityScaleInput = OpacityScaleInputEnumField(default_value=0)
    oci = opacityScaleInput

    opacityScaleInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    osis = opacityScaleInputMax

    opacityScaleRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    osr = opacityScaleRandomize

    colorRed = DoubleField(default_value=0.0, writable=False)
    clr = colorRed

    colorGreen = DoubleField(default_value=0.0, writable=False)
    clg = colorGreen

    colorBlue = DoubleField(default_value=0.0, writable=False)
    clb = colorBlue

    color = ColorField(multi=True)
    cl = color

    color_ColorR = FloatField()
    clcr = color_ColorR

    color_ColorG = FloatField()
    clcg = color_ColorG

    color_ColorB = FloatField()
    clcb = color_ColorB

    colorInput = ColorInputEnumField(default_value=0)
    coi = colorInput

    colorInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    cimx = colorInputMax

    colorRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    colr = colorRandomize

    incandescence = IncandescenceField(multi=True)
    inca = incandescence

    incandescence_ColorR = FloatField()
    incacr = incandescence_ColorR

    incandescence_ColorG = FloatField()
    incacg = incandescence_ColorG

    incandescence_ColorB = FloatField()
    incacb = incandescence_ColorB

    incandescenceInput = IncandescenceInputEnumField(default_value=0)
    ini = incandescenceInput

    incandescenceInputMax = FloatField(default_value=1.0, min_value=0.0, soft_max_value=50.0)
    iimx = incandescenceInputMax

    incandescenceRandomize = DoubleField(default_value=0.0, min_value=0.0, soft_max_value=1.0)
    icar = incandescenceRandomize

    internalRadiusRamp = DataDoubleArrayField(writable=False)
    inrr = internalRadiusRamp

    internalMassRamp = DataDoubleArrayField(writable=False)
    inmr = internalMassRamp

    internalFieldScaleRamp = DataDoubleArrayField(writable=False)
    infs = internalFieldScaleRamp

    internalFrictionRamp = DataDoubleArrayField(writable=False)
    infr = internalFrictionRamp

    internalStickinessRamp = DataDoubleArrayField(writable=False)
    insr = internalStickinessRamp

    internalCollideStrengthRamp = DataDoubleArrayField(writable=False)
    iclr = internalCollideStrengthRamp

    internalBounceRamp = DataDoubleArrayField(writable=False)
    inbr = internalBounceRamp

    internalViscosityRamp = DataDoubleArrayField(writable=False)
    invr = internalViscosityRamp

    internalSurfaceTensionRamp = DataDoubleArrayField(writable=False)
    istr = internalSurfaceTensionRamp

    internalOpacityRamp = DataDoubleArrayField(writable=False)
    inor = internalOpacityRamp

    internalColorRamp = DataVectorArrayField(writable=False)
    incr = internalColorRamp

    internalIncandescenceRamp = DataVectorArrayField(writable=False)
    inir = internalIncandescenceRamp

    cacheableAttributes = CacheableAttributesEnumField(default_value=3)
    caat = cacheableAttributes

    postCacheRampEval = BoolField(default_value=False)
    pcre = postCacheRampEval

    blobbyRadiusScale = DoubleField(default_value=1.0, min_value=0.0, soft_max_value=10.0)
    brs = blobbyRadiusScale

    motionStreak = DoubleField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)
    mstr = motionStreak

    colorPerVertex = BoolField(default_value=False)
    cpvx = colorPerVertex

    opacityPerVertex = BoolField(default_value=False)
    opvx = opacityPerVertex

    incandescencePerVertex = BoolField(default_value=False)
    ipvx = incandescencePerVertex

    velocityPerVertex = BoolField(default_value=True)
    vpvx = velocityPerVertex

    uvwPerVertex = BoolField(default_value=False)
    upvx = uvwPerVertex

    useGradientNormals = BoolField(default_value=False)
    ugn = useGradientNormals

    meshTriangleSize = DoubleField(default_value=0.5, min_value=0.0, soft_max_value=10.0)
    mts = meshTriangleSize

    maxTriangleResolution = LongField(default_value=100)
    mtrr = maxTriangleResolution

    meshSmoothingIterations = LongField(default_value=0, min_value=0, soft_max_value=10)
    msit = meshSmoothingIterations

    meshMethod = MeshMethodEnumField(default_value=0)
    mmd = meshMethod

    outMesh = DataMeshField(writable=False)
    oms = outMesh
