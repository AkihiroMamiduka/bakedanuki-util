# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.mash_distribute import (
    BiasRampField,
    BiasRampXField,
    BiasRampYField,
    BiasRampZField,
    FalloffObjectField,
    ForwardVectorField,
    MColourField,
    PfxUpVectorField,
    RadialOffsetField,
    RotationRampField,
    ScaleRampField,
    TranslateInPPField,
    TranslateOutPPField,
    UpVectorField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.matrix import MatrixField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.time import TimeField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.vector_array import DataVectorArrayField


class MapDirectionEnumPlugOperator(EnumPlugOperator["MapDirectionEnumAttrOperator"]):
    __slots__ = ()

    UV = 1
    Y = 2
    X = 3
    Z = 4


class MapDirectionEnumAttrOperator(EnumAttrOperator[MapDirectionEnumPlugOperator]):
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


class TransformationSpaceEnumPlugOperator(EnumPlugOperator["TransformationSpaceEnumAttrOperator"]):
    __slots__ = ()

    WORLD = 1
    LOCAL = 2


class TransformationSpaceEnumAttrOperator(EnumAttrOperator[TransformationSpaceEnumPlugOperator]):
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


class ModelAxisEnumPlugOperator(EnumPlugOperator["ModelAxisEnumAttrOperator"]):
    __slots__ = ()

    XY = 1
    YZ = 2
    ZX = 3


class ModelAxisEnumAttrOperator(EnumAttrOperator[ModelAxisEnumPlugOperator]):
    __slots__ = ()

    XY = 1
    YZ = 2
    ZX = 3

    NAME_MAP = {
        XY: "XY",
        YZ: "YZ",
        ZX: "ZX",
    }


class ModelAxisEnumField(
    EnumField[ModelAxisEnumAttrOperator, ModelAxisEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ModelAxisEnumAttrOperator
    PLUG_CLS = ModelAxisEnumPlugOperator


class MeshTypeEnumPlugOperator(EnumPlugOperator["MeshTypeEnumAttrOperator"]):
    __slots__ = ()

    SCATTER = 1
    VERTEX = 2
    RANDOM_VERTEX = 3
    FACE_CENTRE = 4
    RANDOM_FACE_CENTRE = 5
    VOXEL = 6
    COMPONENT_SELECTION_SET = 7
    EDGE = 8
    RANDOM_EDGE = 9
    UV_SPACE = 10


class MeshTypeEnumAttrOperator(EnumAttrOperator[MeshTypeEnumPlugOperator]):
    __slots__ = ()

    SCATTER = 1
    VERTEX = 2
    RANDOM_VERTEX = 3
    FACE_CENTRE = 4
    RANDOM_FACE_CENTRE = 5
    VOXEL = 6
    COMPONENT_SELECTION_SET = 7
    EDGE = 8
    RANDOM_EDGE = 9
    UV_SPACE = 10

    NAME_MAP = {
        SCATTER: "Scatter",
        VERTEX: "Vertex",
        RANDOM_VERTEX: "Random Vertex",
        FACE_CENTRE: "Face Centre",
        RANDOM_FACE_CENTRE: "Random Face Centre",
        VOXEL: "Voxel",
        COMPONENT_SELECTION_SET: "Component Selection Set",
        EDGE: "Edge",
        RANDOM_EDGE: "Random Edge",
        UV_SPACE: "UV Space",
    }


class MeshTypeEnumField(
    EnumField[MeshTypeEnumAttrOperator, MeshTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MeshTypeEnumAttrOperator
    PLUG_CLS = MeshTypeEnumPlugOperator


class EdgeAlignmentEnumPlugOperator(EnumPlugOperator["EdgeAlignmentEnumAttrOperator"]):
    __slots__ = ()

    CENTRE = 1
    START = 2
    END = 3


class EdgeAlignmentEnumAttrOperator(EnumAttrOperator[EdgeAlignmentEnumPlugOperator]):
    __slots__ = ()

    CENTRE = 1
    START = 2
    END = 3

    NAME_MAP = {
        CENTRE: "Centre",
        START: "Start",
        END: "End",
    }


class EdgeAlignmentEnumField(
    EnumField[EdgeAlignmentEnumAttrOperator, EdgeAlignmentEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = EdgeAlignmentEnumAttrOperator
    PLUG_CLS = EdgeAlignmentEnumPlugOperator


class VoxelModeEnumPlugOperator(EnumPlugOperator["VoxelModeEnumAttrOperator"]):
    __slots__ = ()

    SHELL_ONLY = 1
    FILL_AND_SHELL = 2
    FILL_ONLY = 3


class VoxelModeEnumAttrOperator(EnumAttrOperator[VoxelModeEnumPlugOperator]):
    __slots__ = ()

    SHELL_ONLY = 1
    FILL_AND_SHELL = 2
    FILL_ONLY = 3

    NAME_MAP = {
        SHELL_ONLY: "Shell Only",
        FILL_AND_SHELL: "Fill and Shell",
        FILL_ONLY: "Fill Only",
    }


class VoxelModeEnumField(
    EnumField[VoxelModeEnumAttrOperator, VoxelModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VoxelModeEnumAttrOperator
    PLUG_CLS = VoxelModeEnumPlugOperator


class PfxModeEnumPlugOperator(EnumPlugOperator["PfxModeEnumAttrOperator"]):
    __slots__ = ()

    NORMAL = 1
    SKIP_LAST_POINT = 2
    EDGE_MODE = 3
    LEAF_MODE = 4


class PfxModeEnumAttrOperator(EnumAttrOperator[PfxModeEnumPlugOperator]):
    __slots__ = ()

    NORMAL = 1
    SKIP_LAST_POINT = 2
    EDGE_MODE = 3
    LEAF_MODE = 4

    NAME_MAP = {
        NORMAL: "Normal",
        SKIP_LAST_POINT: "Skip Last Point",
        EDGE_MODE: "Edge Mode",
        LEAF_MODE: "Leaf Mode",
    }


class PfxModeEnumField(
    EnumField[PfxModeEnumAttrOperator, PfxModeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PfxModeEnumAttrOperator
    PLUG_CLS = PfxModeEnumPlugOperator


class VolumeShapeEnumPlugOperator(EnumPlugOperator["VolumeShapeEnumAttrOperator"]):
    __slots__ = ()

    POINT = 1
    CUBE = 2
    SPHERE = 3


class VolumeShapeEnumAttrOperator(EnumAttrOperator[VolumeShapeEnumPlugOperator]):
    __slots__ = ()

    POINT = 1
    CUBE = 2
    SPHERE = 3

    NAME_MAP = {
        POINT: "Point",
        CUBE: "Cube",
        SPHERE: "Sphere",
    }


class VolumeShapeEnumField(
    EnumField[VolumeShapeEnumAttrOperator, VolumeShapeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VolumeShapeEnumAttrOperator
    PLUG_CLS = VolumeShapeEnumPlugOperator


class ArrangementEnumPlugOperator(EnumPlugOperator["ArrangementEnumAttrOperator"]):
    __slots__ = ()

    LINEAR = 1
    RADIAL = 2
    SPHERICAL = 3
    MESH = 4
    INPOSITIONPP = 5
    GRID = 6
    INITIAL_STATE = 7
    PAINT_EFFECTS = 8
    VOLUME = 9


class ArrangementEnumAttrOperator(EnumAttrOperator[ArrangementEnumPlugOperator]):
    __slots__ = ()

    LINEAR = 1
    RADIAL = 2
    SPHERICAL = 3
    MESH = 4
    INPOSITIONPP = 5
    GRID = 6
    INITIAL_STATE = 7
    PAINT_EFFECTS = 8
    VOLUME = 9

    NAME_MAP = {
        LINEAR: "Linear",
        RADIAL: "Radial",
        SPHERICAL: "Spherical",
        MESH: "Mesh",
        INPOSITIONPP: "inPositionPP",
        GRID: "Grid",
        INITIAL_STATE: "Initial State",
        PAINT_EFFECTS: "Paint Effects",
        VOLUME: "Volume",
    }


class ArrangementEnumField(
    EnumField[ArrangementEnumAttrOperator, ArrangementEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ArrangementEnumAttrOperator
    PLUG_CLS = ArrangementEnumPlugOperator


class GeneratedMASH_Distribute(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Distribute"

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

    Envelope = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

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

    inputArray = DataVectorArrayField()
    inArray = inputArray

    outputArray = DataVectorArrayField()
    outArray = outputArray

    translateInPP = TranslateInPPField()
    positionInPP = translateInPP.positionInPP
    scaleInPP = translateInPP.scaleInPP
    rotationInPP = translateInPP.rotationInPP
    idInPP = translateInPP.idInPP
    visibilityInPP = translateInPP.visibilityInPP

    translateOutPP = TranslateOutPPField()
    positionOutPP = translateOutPP.positionOutPP
    scaleOutPP = translateOutPP.scaleOutPP
    rotationOutPP = translateOutPP.rotationOutPP
    idOutPP = translateOutPP.idOutPP
    visibilityOutPP = translateOutPP.visibilityOutPP

    pointCount = LongField(default_value=10, min_value=0, soft_max_value=100)

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    voxelObjMatrix = MatrixField()

    initialStateMatrix = MatrixField(multi=True)

    inPositionPP = DataVectorArrayField()
    inPPP = inPositionPP

    time = TimeField(default_value=1.0)
    ti = time

    inIterations = LongField(default_value=0)
    inIter = inIterations

    batchRenderMultiplier = LongField(default_value=1, min_value=1, soft_max_value=100)

    enable = BoolField(default_value=True)
    en = enable

    centerLinearDistribution = BoolField(default_value=False)

    strengthPosition = BoolField(default_value=True)

    strengthRotation = BoolField(default_value=True)

    strengthScale = BoolField(default_value=True)

    ignoreRamps = BoolField(default_value=True)

    radialOffset = RadialOffsetField(default_value=(0.0, 0.0, 0.0))
    radialOffset0 = radialOffset.radialOffset0
    radialOffset1 = radialOffset.radialOffset1
    radialOffset2 = radialOffset.radialOffset2

    upVector = UpVectorField(default_value=(0.0, 1.0, 0.0))
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    pfxUpVector = PfxUpVectorField(default_value=(0.0, 1.0, 0.0))
    pfxUpVector0 = pfxUpVector.pfxUpVector0
    pfxUpVector1 = pfxUpVector.pfxUpVector1
    pfxUpVector2 = pfxUpVector.pfxUpVector2

    forwardVector = ForwardVectorField(default_value=(0.0, 0.0, 0.0))
    forwardVector0 = forwardVector.forwardVector0
    forwardVector1 = forwardVector.forwardVector1
    forwardVector2 = forwardVector.forwardVector2

    falloffInfo = TypedField()

    falloffObject = FalloffObjectField(default_value=(0.0, 0.0, 0.0))
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField(default_value=True)
    fax = falloffX

    falloffY = BoolField(default_value=True)
    fay = falloffY

    falloffZ = BoolField(default_value=True)
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    selectionSetMessage = MessageField()

    waiterMessage = MessageField()

    scaleRamp = ScaleRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    rotationRamp = RotationRampField(multi=True, default_value=(0.0, 0.0, 1.0))

    biasRamp = BiasRampField(multi=True, default_value=(0.0, 0.0, 1.0))
    bRmp = biasRamp

    biasRampX = BiasRampXField(multi=True, default_value=(0.0, 0.0, 1.0))
    bRmpX = biasRampX

    biasRampY = BiasRampYField(multi=True, default_value=(0.0, 0.0, 1.0))
    bRmpY = biasRampY

    biasRampZ = BiasRampZField(multi=True, default_value=(0.0, 0.0, 1.0))
    bRmpZ = biasRampZ

    animationTime = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=100.0)

    seed = LongField(default_value=1, min_value=1, soft_max_value=100)
    see = seed

    amplitudeX = FloatField(default_value=20.0, soft_min_value=0.0, soft_max_value=60.0)
    ampX = amplitudeX

    amplitudeY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=60.0)
    ampY = amplitudeY

    amplitudeZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=60.0)
    ampZ = amplitudeZ

    scaleX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    scaleY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    scaleZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    rotateX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)

    rotateY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)

    rotateZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=360.0)

    voxPatternOffsetX = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    voxPatternOffsetY = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    voxPatternOffsetZ = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=10.0)

    areaBasedScatter = BoolField(default_value=False)

    scatterEvenly = BoolField(default_value=False)

    useFaceScale = BoolField(default_value=False)

    floodMesh = BoolField(default_value=False)

    faceScaleMultiplier = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    offset = LongField(default_value=0, min_value=0, soft_max_value=30)

    gridAmplitudeX = FloatField(default_value=5.0, soft_min_value=0.0, soft_max_value=30.0)

    gridAmplitudeY = FloatField(default_value=5.0, soft_min_value=0.0, soft_max_value=30.0)

    gridAmplitudeZ = FloatField(default_value=5.0, soft_min_value=0.0, soft_max_value=30.0)

    sphericalAngleX = FloatField(default_value=360.0, soft_min_value=0.0, soft_max_value=360.0)

    sphericalAngleY = FloatField(default_value=360.0, soft_min_value=0.0, soft_max_value=360.0)

    radialRadius = FloatField(default_value=10.0, soft_min_value=0.0, soft_max_value=20.0)

    radialAngle = FloatField(default_value=360.0, soft_min_value=-360.0, soft_max_value=360.0)

    distanceAlongNormal = FloatField(default_value=0.0, soft_min_value=0.0, soft_max_value=2.0)

    inputMesh = DataMeshField()
    inM = inputMesh

    voxelBoundingBox = DataMeshField()

    gridx = LongField(default_value=3, min_value=1, soft_max_value=25)
    grx = gridx

    gridy = LongField(default_value=1, min_value=1, soft_max_value=25)
    gry = gridy

    gridz = LongField(default_value=3, min_value=1, soft_max_value=25)
    grz = gridz

    noiseFrequency = FloatField(default_value=1.0, min_value=0.0, soft_max_value=3.0)
    noFre = noiseFrequency

    modelAxis = ModelAxisEnumField(default_value=1)

    meshType = MeshTypeEnumField(default_value=1)

    edgeAlignment = EdgeAlignmentEnumField(default_value=1)

    voxelMode = VoxelModeEnumField(default_value=1)

    legacy2017 = BoolField(default_value=False)

    legacy2018 = BoolField(default_value=False)

    calcRotation = BoolField(default_value=True)

    zeroScale = BoolField(default_value=False)

    voxelDensity = FloatField(default_value=1.5, min_value=0.1, soft_min_value=0.2, soft_max_value=3.0)

    maxVoxels = LongField(default_value=100000)

    voxelBorder = FloatField(default_value=0.0010000000474974513, min_value=0.001, soft_max_value=1.0)

    inPaintEffects = DataMeshField(multi=True)

    pfxMode = PfxModeEnumField(default_value=1)

    enableMain = BoolField(default_value=True)

    enableLeaf = BoolField(default_value=False)

    enableFlowers = BoolField(default_value=False)

    enablePfxRotation = BoolField(default_value=False)

    useUpVector = BoolField(default_value=False)

    volumeSize = FloatField(default_value=5.0, min_value=0.0, soft_max_value=20.0)

    sphericalBias = FloatField(default_value=0.5, min_value=0.0, soft_max_value=2.0)

    volumeShape = VolumeShapeEnumField(default_value=2)

    arrangement = ArrangementEnumField(default_value=1)
    rt = arrangement
