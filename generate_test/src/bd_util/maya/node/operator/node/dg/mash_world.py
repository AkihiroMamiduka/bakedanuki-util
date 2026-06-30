# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_world import (
    AvoidanceRampField,
    IdMapField,
    MColourField,
    PoleDirectionField,
    PruningStrengthMapField,
    RandomRotateField,
    ScaleMapField,
    TerrainConditionsMapField,
    TimeRangeField,
    UpVectorField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.generic import GenericField
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class MapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class MapDirectionEnumField(
    EnumField[MapDirectionEnumAttrOperator, MapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MapDirectionEnumAttrOperator
    PLUG_CLS = MapDirectionEnumPlugOperator


class TransformationSpaceEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[TransformationSpaceEnumAttrOperator, TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class PrevousPointsModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    KEEP = 1
    KEEP_AND_AVOID = 2
    KILL_AND_AVOID = 3
    KILL = 4


class PrevousPointsModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    KEEP = 1
    KEEP_AND_AVOID = 2
    KILL_AND_AVOID = 3
    KILL = 4

    NAME_MAP = {
        KEEP: "Keep",
        KEEP_AND_AVOID: "Keep and Avoid",
        KILL_AND_AVOID: "Kill and Avoid",
        KILL: "Kill",
    }


class PrevousPointsModeEnumField(
    EnumField[PrevousPointsModeEnumAttrOperator, PrevousPointsModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PrevousPointsModeEnumAttrOperator
    PLUG_CLS = PrevousPointsModeEnumPlugOperator


class ClusterModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BALL = 1
    DISC = 2
    CIRCLE = 3
    FIBONACCI_SPIRAL = 4
    FIBONACCI_SPHERE = 5
    MAP_BASED = 6
    TERRESTRIAL_ECOSYSTEM = 7


class ClusterModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BALL = 1
    DISC = 2
    CIRCLE = 3
    FIBONACCI_SPIRAL = 4
    FIBONACCI_SPHERE = 5
    MAP_BASED = 6
    TERRESTRIAL_ECOSYSTEM = 7

    NAME_MAP = {
        BALL: "Ball",
        DISC: "Disc",
        CIRCLE: "Circle",
        FIBONACCI_SPIRAL: "Fibonacci Spiral",
        FIBONACCI_SPHERE: "Fibonacci Sphere",
        MAP_BASED: "Map Based",
        TERRESTRIAL_ECOSYSTEM: "Terrestrial Ecosystem",
    }


class ClusterModeEnumField(
    EnumField[ClusterModeEnumAttrOperator, ClusterModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClusterModeEnumAttrOperator
    PLUG_CLS = ClusterModeEnumPlugOperator


class IdModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIXED = 1
    STEPPED = 2
    RANDOM = 3
    CLUSTER_RANDOM = 4


class IdModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIXED = 1
    STEPPED = 2
    RANDOM = 3
    CLUSTER_RANDOM = 4

    NAME_MAP = {
        FIXED: "Fixed",
        STEPPED: "Stepped",
        RANDOM: "Random",
        CLUSTER_RANDOM: "Cluster Random",
    }


class IdModeEnumField(
    EnumField[IdModeEnumAttrOperator, IdModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdModeEnumAttrOperator
    PLUG_CLS = IdModeEnumPlugOperator


class ScaleModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    SCALE_MAP = 2
    EXPAND_TO_NEAREST = 3
    INHERIT = 4


class ScaleModeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NORMAL = 1
    SCALE_MAP = 2
    EXPAND_TO_NEAREST = 3
    INHERIT = 4

    NAME_MAP = {
        NORMAL: "Normal",
        SCALE_MAP: "Scale map",
        EXPAND_TO_NEAREST: "Expand to nearest",
        INHERIT: "Inherit",
    }


class ScaleModeEnumField(
    EnumField[ScaleModeEnumAttrOperator, ScaleModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ScaleModeEnumAttrOperator
    PLUG_CLS = ScaleModeEnumPlugOperator


class PruningMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class PruningMapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class PruningMapDirectionEnumField(
    EnumField[PruningMapDirectionEnumAttrOperator, PruningMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PruningMapDirectionEnumAttrOperator
    PLUG_CLS = PruningMapDirectionEnumPlugOperator


class ConditionMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class ConditionMapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class ConditionMapDirectionEnumField(
    EnumField[ConditionMapDirectionEnumAttrOperator, ConditionMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ConditionMapDirectionEnumAttrOperator
    PLUG_CLS = ConditionMapDirectionEnumPlugOperator


class IdMapDirectionEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class IdMapDirectionEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4

    NAME_MAP = {
        UV: "UV",
        Y: "Y",
        X: "X",
        Z: "Z",
    }


class IdMapDirectionEnumField(
    EnumField[IdMapDirectionEnumAttrOperator, IdMapDirectionEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = IdMapDirectionEnumAttrOperator
    PLUG_CLS = IdMapDirectionEnumPlugOperator


class MASH_World(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_World"

    savedData = TypedField()

    mColour = MColourField()
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField()

    Envelope = FloatField()

    randEnvelope = FloatField()

    StepEnvelope = FloatField()

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField()

    enableStrengthY = BoolField()

    enableStrengthZ = BoolField()

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField()

    outputPoints = TypedField()

    inputPoints = TypedField()

    enable = BoolField()

    prevousPointsMode = PrevousPointsModeEnumField()

    randomSeed = LongField()

    collisionIterations = LongField()

    minimumSeparation = FloatField()

    avoidanceRadius = FloatField()

    avoidanceRamp = AvoidanceRampField(multi=True)

    killSize = FloatField()

    radiusVariance = FloatField()

    randomRotate = RandomRotateField()
    randomRotateX = randomRotate.randomRotateX
    randomRotateY = randomRotate.randomRotateY
    randomRotateZ = randomRotate.randomRotateZ

    idValue = LongField()

    maxId = LongField()

    minId = LongField()

    clusterRadius = FloatField()

    radius = FloatField()

    pointsPerCluster = LongField()

    randomPointsPerCluster = LongField()

    clusterMode = ClusterModeEnumField()

    idMode = IdModeEnumField()

    scaleMode = ScaleModeEnumField()

    scaleMap = ScaleMapField()
    scaleMapR = scaleMap.scaleMapR
    scaleMapr = scaleMapR
    scaleMapG = scaleMap.scaleMapG
    scaleMapg = scaleMapG
    scaleMapB = scaleMap.scaleMapB
    scaleMapb = scaleMapB

    ignoreSlope = BoolField()

    upVector = UpVectorField()
    upVector0 = upVector.upVector0
    upVector1 = upVector.upVector1
    upVector2 = upVector.upVector2

    useUpVector = BoolField()

    avoidanceObjects = GenericField(multi=True)

    coreObjects = GenericField(multi=True)

    groundMesh = DataMeshField()

    pruningMapMatrix = MatrixField()

    pruningMapDirection = PruningMapDirectionEnumField()

    pruningStrengthMap = PruningStrengthMapField()
    pruningStrengthMapR = pruningStrengthMap.pruningStrengthMapR
    pruningStrengthMapr = pruningStrengthMapR
    pruningStrengthMapG = pruningStrengthMap.pruningStrengthMapG
    pruningStrengthMapg = pruningStrengthMapG
    pruningStrengthMapB = pruningStrengthMap.pruningStrengthMapB
    pruningStrengthMapb = pruningStrengthMapB

    ecosystemAge = LongField()

    scaleMultiplier = FloatField()

    conditionMapDirection = ConditionMapDirectionEnumField()

    useRChannel = BoolField()

    useGChannel = BoolField()

    useBChannel = BoolField()

    terrainConditionsMap = TerrainConditionsMapField()
    terrainConditionsMapR = terrainConditionsMap.terrainConditionsMapR
    terrainConditionsMapr = terrainConditionsMapR
    terrainConditionsMapG = terrainConditionsMap.terrainConditionsMapG
    terrainConditionsMapg = terrainConditionsMapG
    terrainConditionsMapB = terrainConditionsMap.terrainConditionsMapB
    terrainConditionsMapb = terrainConditionsMapB

    idMapDirection = IdMapDirectionEnumField()

    groundMatrix = MatrixField()

    useIdMap = BoolField()

    idMap = IdMapField()
    idMapR = idMap.idMapR
    idMapr = idMapR
    idMapG = idMap.idMapG
    idMapg = idMapG
    idMapB = idMap.idMapB
    idMapb = idMapB

    calculateShade = BoolField()

    shadeVariance = FloatField()

    poleBias = FloatField()

    poleDirection = PoleDirectionField()
    poleDirectionX = poleDirection.poleDirectionX
    poleDirectionx = poleDirectionX
    poleDirectionY = poleDirection.poleDirectionY
    poleDirectiony = poleDirectionY
    poleDirectionZ = poleDirection.poleDirectionZ
    poleDirectionz = poleDirectionZ

    highQualitySim = BoolField()

    sparsity = FloatField()

    seedMultiplier = FloatField()

    maxPlants = LongField()

    ageToTime = BoolField()

    timeRange = TimeRangeField()
    timeRange0 = timeRange.timeRange0
    timeRange1 = timeRange.timeRange1

    roundTime = BoolField()

    genotypeJSON = DataStringField()
