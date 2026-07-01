# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.mash_distribute import (
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
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.matrix import MatrixField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar.time import TimeField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField
from ...attr.define.std.dt.vector_array import DataVectorArrayField


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


class ModelAxisEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    XY = 1
    YZ = 2
    ZX = 3


class ModelAxisEnumAttrOperator(EnumAttrOperator):
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


class MeshTypeEnumPlugOperator(EnumPlugOperator):
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


class MeshTypeEnumAttrOperator(EnumAttrOperator):
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


class EdgeAlignmentEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    CENTRE = 1
    START = 2
    END = 3


class EdgeAlignmentEnumAttrOperator(EnumAttrOperator):
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


class VoxelModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    SHELL_ONLY = 1
    FILL_AND_SHELL = 2
    FILL_ONLY = 3


class VoxelModeEnumAttrOperator(EnumAttrOperator):
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


class PfxModeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NORMAL = 1
    SKIP_LAST_POINT = 2
    EDGE_MODE = 3
    LEAF_MODE = 4


class PfxModeEnumAttrOperator(EnumAttrOperator):
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


class VolumeShapeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    POINT = 1
    CUBE = 2
    SPHERE = 3


class VolumeShapeEnumAttrOperator(EnumAttrOperator):
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


class ArrangementEnumPlugOperator(EnumPlugOperator):
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


class ArrangementEnumAttrOperator(EnumAttrOperator):
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


class MASH_Distribute(DG):
    __slots__ = ()

    NODE_TYPE = "MASH_Distribute"

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

    pointCount = LongField()

    fallPosArray = DataVectorArrayField()
    fArray = fallPosArray

    voxelObjMatrix = MatrixField()

    initialStateMatrix = MatrixField(multi=True)

    inPositionPP = DataVectorArrayField()
    inPPP = inPositionPP

    time = TimeField()
    ti = time

    inIterations = LongField()
    inIter = inIterations

    batchRenderMultiplier = LongField()

    enable = BoolField()
    en = enable

    centerLinearDistribution = BoolField()

    strengthPosition = BoolField()

    strengthRotation = BoolField()

    strengthScale = BoolField()

    ignoreRamps = BoolField()

    radialOffset = RadialOffsetField()
    radialOffset0 = radialOffset.radialOffset0
    radialOffset1 = radialOffset.radialOffset1
    radialOffset2 = radialOffset.radialOffset2

    upVector = UpVectorField()
    uVec = upVector
    upVector0 = upVector.upVector0
    uVec0 = upVector0
    upVector1 = upVector.upVector1
    uVec1 = upVector1
    upVector2 = upVector.upVector2
    uVec2 = upVector2

    pfxUpVector = PfxUpVectorField()
    pfxUpVector0 = pfxUpVector.pfxUpVector0
    pfxUpVector1 = pfxUpVector.pfxUpVector1
    pfxUpVector2 = pfxUpVector.pfxUpVector2

    forwardVector = ForwardVectorField()
    forwardVector0 = forwardVector.forwardVector0
    forwardVector1 = forwardVector.forwardVector1
    forwardVector2 = forwardVector.forwardVector2

    falloffInfo = TypedField()

    falloffObject = FalloffObjectField()
    fallObj = falloffObject
    falloffObjectX = falloffObject.falloffObjectX
    fallObjx = falloffObjectX
    falloffObjectY = falloffObject.falloffObjectY
    fallObjy = falloffObjectY
    falloffObjectZ = falloffObject.falloffObjectZ
    fallObjz = falloffObjectZ

    falloffX = BoolField()
    fax = falloffX

    falloffY = BoolField()
    fay = falloffY

    falloffZ = BoolField()
    faz = falloffZ

    falloffMessage = MessageField()
    fmsg = falloffMessage

    selectionSetMessage = MessageField()

    waiterMessage = MessageField()

    scaleRamp = ScaleRampField(multi=True)

    rotationRamp = RotationRampField(multi=True)

    biasRamp = BiasRampField(multi=True)
    bRmp = biasRamp

    biasRampX = BiasRampXField(multi=True)
    bRmpX = biasRampX

    biasRampY = BiasRampYField(multi=True)
    bRmpY = biasRampY

    biasRampZ = BiasRampZField(multi=True)
    bRmpZ = biasRampZ

    animationTime = FloatField()

    seed = LongField()
    see = seed

    amplitudeX = FloatField()
    ampX = amplitudeX

    amplitudeY = FloatField()
    ampY = amplitudeY

    amplitudeZ = FloatField()
    ampZ = amplitudeZ

    scaleX = FloatField()

    scaleY = FloatField()

    scaleZ = FloatField()

    rotateX = FloatField()

    rotateY = FloatField()

    rotateZ = FloatField()

    voxPatternOffsetX = FloatField()

    voxPatternOffsetY = FloatField()

    voxPatternOffsetZ = FloatField()

    areaBasedScatter = BoolField()

    scatterEvenly = BoolField()

    useFaceScale = BoolField()

    floodMesh = BoolField()

    faceScaleMultiplier = FloatField()

    offset = LongField()

    gridAmplitudeX = FloatField()

    gridAmplitudeY = FloatField()

    gridAmplitudeZ = FloatField()

    sphericalAngleX = FloatField()

    sphericalAngleY = FloatField()

    radialRadius = FloatField()

    radialAngle = FloatField()

    distanceAlongNormal = FloatField()

    inputMesh = DataMeshField()
    inM = inputMesh

    voxelBoundingBox = DataMeshField()

    gridx = LongField()
    grx = gridx

    gridy = LongField()
    gry = gridy

    gridz = LongField()
    grz = gridz

    noiseFrequency = FloatField()
    noFre = noiseFrequency

    modelAxis = ModelAxisEnumField()

    meshType = MeshTypeEnumField()

    edgeAlignment = EdgeAlignmentEnumField()

    voxelMode = VoxelModeEnumField()

    legacy2017 = BoolField()

    legacy2018 = BoolField()

    calcRotation = BoolField()

    zeroScale = BoolField()

    voxelDensity = FloatField()

    maxVoxels = LongField()

    voxelBorder = FloatField()

    inPaintEffects = DataMeshField(multi=True)

    pfxMode = PfxModeEnumField()

    enableMain = BoolField()

    enableLeaf = BoolField()

    enableFlowers = BoolField()

    enablePfxRotation = BoolField()

    useUpVector = BoolField()

    volumeSize = FloatField()

    sphericalBias = FloatField()

    volumeShape = VolumeShapeEnumField()

    arrangement = ArrangementEnumField()
    rt = arrangement
