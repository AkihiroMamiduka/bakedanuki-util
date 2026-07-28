# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_world import (
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
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


class MapDirectionEnumPlugOperator(
    EnumPlugOperator["MapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(
    EnumAttrOperator[MapDirectionEnumPlugOperator]
):
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


class TransformationSpaceEnumPlugOperator(
    EnumPlugOperator["TransformationSpaceEnumAttrOperator"]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(
    EnumAttrOperator[TransformationSpaceEnumPlugOperator]
):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2

    NAME_MAP = {
        WORLD: "World",
        LOCAL: "Local",
    }


class TransformationSpaceEnumField(
    EnumField[
        TransformationSpaceEnumAttrOperator,
        TransformationSpaceEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TransformationSpaceEnumAttrOperator
    PLUG_CLS = TransformationSpaceEnumPlugOperator


class PrevousPointsModeEnumPlugOperator(
    EnumPlugOperator["PrevousPointsModeEnumAttrOperator"]
):
    __slots__ = ()

    KEEP = 1
    KEEP_AND_AVOID = 2
    KILL_AND_AVOID = 3
    KILL = 4


class PrevousPointsModeEnumAttrOperator(
    EnumAttrOperator[PrevousPointsModeEnumPlugOperator]
):
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
    EnumField[
        PrevousPointsModeEnumAttrOperator, PrevousPointsModeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = PrevousPointsModeEnumAttrOperator
    PLUG_CLS = PrevousPointsModeEnumPlugOperator


class ClusterModeEnumPlugOperator(
    EnumPlugOperator["ClusterModeEnumAttrOperator"]
):
    __slots__ = ()

    BALL = 1
    DISC = 2
    CIRCLE = 3
    FIBONACCI_SPIRAL = 4
    FIBONACCI_SPHERE = 5
    MAP_BASED = 6
    TERRESTRIAL_ECOSYSTEM = 7


class ClusterModeEnumAttrOperator(
    EnumAttrOperator[ClusterModeEnumPlugOperator]
):
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


class IdModeEnumPlugOperator(EnumPlugOperator["IdModeEnumAttrOperator"]):
    __slots__ = ()

    FIXED = 1
    STEPPED = 2
    RANDOM = 3
    CLUSTER_RANDOM = 4


class IdModeEnumAttrOperator(EnumAttrOperator[IdModeEnumPlugOperator]):
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


class ScaleModeEnumPlugOperator(EnumPlugOperator["ScaleModeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 1
    SCALE_MAP = 2
    EXPAND_TO_NEAREST = 3
    INHERIT = 4


class ScaleModeEnumAttrOperator(EnumAttrOperator[ScaleModeEnumPlugOperator]):
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


class PruningMapDirectionEnumPlugOperator(
    EnumPlugOperator["PruningMapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class PruningMapDirectionEnumAttrOperator(
    EnumAttrOperator[PruningMapDirectionEnumPlugOperator]
):
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
    EnumField[
        PruningMapDirectionEnumAttrOperator,
        PruningMapDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = PruningMapDirectionEnumAttrOperator
    PLUG_CLS = PruningMapDirectionEnumPlugOperator


class ConditionMapDirectionEnumPlugOperator(
    EnumPlugOperator["ConditionMapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class ConditionMapDirectionEnumAttrOperator(
    EnumAttrOperator[ConditionMapDirectionEnumPlugOperator]
):
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
    EnumField[
        ConditionMapDirectionEnumAttrOperator,
        ConditionMapDirectionEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ConditionMapDirectionEnumAttrOperator
    PLUG_CLS = ConditionMapDirectionEnumPlugOperator


class IdMapDirectionEnumPlugOperator(
    EnumPlugOperator["IdMapDirectionEnumAttrOperator"]
):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class IdMapDirectionEnumAttrOperator(
    EnumAttrOperator[IdMapDirectionEnumPlugOperator]
):
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


class GeneratedMASH_World(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_World"

    savedData = TypedField()

    mColour = MColourField(default_value=(1.0, 1.0, 1.0))
    mc = mColour
    mColourR = mColour.mColourR
    mcr = mColourR
    mColourG = mColour.mColourG
    mcg = mColourG
    mColourB = mColour.mColourB
    mcb = mColourB

    inMapMatrix = MatrixField()

    mapDirection = MapDirectionEnumField(default_value=2)

    Envelope = FloatField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )

    randEnvelope = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)

    StepEnvelope = FloatField(default_value=1.0, min_value=-1.0, max_value=1.0)

    mFalloffInfo = TypedField(multi=True)

    enableStrengthX = BoolField(default_value=True)

    enableStrengthY = BoolField(default_value=True)

    enableStrengthZ = BoolField(default_value=True)

    stringOn = DataStringField()

    stringOff = DataStringField()

    strengthPP = TypedField(multi=True)

    transformationSpace = TransformationSpaceEnumField(default_value=1)

    outputPoints = TypedField(writable=False)

    inputPoints = TypedField()

    enable = BoolField(default_value=True)

    prevousPointsMode = PrevousPointsModeEnumField(default_value=1)

    randomSeed = LongField(default_value=1, min_value=1, soft_max_value=100)

    collisionIterations = LongField(
        default_value=6, min_value=0, soft_max_value=50
    )

    minimumSeparation = FloatField(
        default_value=0.10000000149011612, min_value=0.001, soft_max_value=10.0
    )

    avoidanceRadius = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )

    avoidanceRamp = AvoidanceRampField(
        multi=True, default_value=(0.0, 0.0, 1.0)
    )

    killSize = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=10.0
    )

    radiusVariance = FloatField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )

    randomRotate = RandomRotateField(default_value=(0.0, 6.28319, 0.0))
    randomRotateX = randomRotate.randomRotateX
    randomRotateY = randomRotate.randomRotateY
    randomRotateZ = randomRotate.randomRotateZ

    idValue = LongField(default_value=0, min_value=0, soft_max_value=20)

    maxId = LongField(default_value=0, min_value=1, soft_max_value=20)

    minId = LongField(default_value=0, min_value=1, soft_max_value=20)

    clusterRadius = FloatField(
        default_value=3.0, min_value=0.0, soft_max_value=50.0
    )

    radius = FloatField(default_value=2.0, min_value=0.01, soft_max_value=10.0)

    pointsPerCluster = LongField(
        default_value=10, min_value=0, soft_max_value=50
    )

    randomPointsPerCluster = LongField(
        default_value=0, min_value=0, soft_max_value=50
    )

    clusterMode = ClusterModeEnumField(default_value=1)

    idMode = IdModeEnumField(default_value=1)

    scaleMode = ScaleModeEnumField(default_value=1)

    scaleMap = ScaleMapField(default_value=(1.0, 1.0, 1.0))
    scaleMapR = scaleMap.scaleMapR
    scaleMapr = scaleMapR
    scaleMapG = scaleMap.scaleMapG
    scaleMapg = scaleMapG
    scaleMapB = scaleMap.scaleMapB
    scaleMapb = scaleMapB

    ignoreSlope = BoolField(default_value=False)

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    upVector0 = upVector.upVector0
    upVector1 = upVector.upVector1
    upVector2 = upVector.upVector2

    useUpVector = BoolField(default_value=False)

    avoidanceObjects = GenericField(multi=True)

    coreObjects = GenericField(multi=True)

    groundMesh = DataMeshField()

    pruningMapMatrix = MatrixField()

    pruningMapDirection = PruningMapDirectionEnumField(default_value=2)

    pruningStrengthMap = PruningStrengthMapField(default_value=(1.0, 1.0, 1.0))
    pruningStrengthMapR = pruningStrengthMap.pruningStrengthMapR
    pruningStrengthMapr = pruningStrengthMapR
    pruningStrengthMapG = pruningStrengthMap.pruningStrengthMapG
    pruningStrengthMapg = pruningStrengthMapG
    pruningStrengthMapB = pruningStrengthMap.pruningStrengthMapB
    pruningStrengthMapb = pruningStrengthMapB

    ecosystemAge = LongField(default_value=40, min_value=0, soft_max_value=120)

    scaleMultiplier = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=10.0
    )

    conditionMapDirection = ConditionMapDirectionEnumField(default_value=2)

    useRChannel = BoolField(default_value=False)

    useGChannel = BoolField(default_value=False)

    useBChannel = BoolField(default_value=False)

    terrainConditionsMap = TerrainConditionsMapField(
        default_value=(0.5, 0.5, 0.5)
    )
    terrainConditionsMapR = terrainConditionsMap.terrainConditionsMapR
    terrainConditionsMapr = terrainConditionsMapR
    terrainConditionsMapG = terrainConditionsMap.terrainConditionsMapG
    terrainConditionsMapg = terrainConditionsMapG
    terrainConditionsMapB = terrainConditionsMap.terrainConditionsMapB
    terrainConditionsMapb = terrainConditionsMapB

    idMapDirection = IdMapDirectionEnumField(default_value=2)

    groundMatrix = MatrixField()

    useIdMap = BoolField(default_value=False)

    idMap = IdMapField(default_value=(0.5, 0.5, 0.5))
    idMapR = idMap.idMapR
    idMapr = idMapR
    idMapG = idMap.idMapG
    idMapg = idMapG
    idMapB = idMap.idMapB
    idMapb = idMapB

    calculateShade = BoolField(default_value=False)

    shadeVariance = FloatField(
        default_value=30.0, min_value=0.0, max_value=90.0
    )

    poleBias = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)

    poleDirection = PoleDirectionField(default_value=(0.0, 0.0, 0.0))
    poleDirectionX = poleDirection.poleDirectionX
    poleDirectionx = poleDirectionX
    poleDirectionY = poleDirection.poleDirectionY
    poleDirectiony = poleDirectionY
    poleDirectionZ = poleDirection.poleDirectionZ
    poleDirectionz = poleDirectionZ

    highQualitySim = BoolField(default_value=False)

    sparsity = FloatField(
        default_value=1.0, min_value=0.001, soft_max_value=5.0
    )

    seedMultiplier = FloatField(
        default_value=1.0, min_value=0.0, soft_max_value=2.0
    )

    maxPlants = LongField(
        default_value=15000, min_value=0, soft_max_value=2000
    )

    ageToTime = BoolField(default_value=False)

    timeRange = TimeRangeField(
        default_value=(0.0, 120.0), min_value=(0.0, 0.0)
    )
    timeRange0 = timeRange.timeRange0
    timeRange1 = timeRange.timeRange1

    roundTime = BoolField(default_value=False)

    genotypeJSON = DataStringField()
