# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.stroke import (
    CameraPointField,
    NormalField,
    OutNormalField,
    OutPointField,
    PathCurveField,
    PressureScaleField,
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
from .....attr.define.std.at.scalar.numeric.range.long import LongField
from .....attr.define.std.at.typed import TypedField
from .....attr.define.std.dt.mesh import DataMeshField
from .....attr.define.std.dt.nurbs_curve import DataNurbsCurveField


class MeshVertexColorModeEnumPlugOperator(
    EnumPlugOperator["MeshVertexColorModeEnumAttrOperator"]
):
    __slots__ = ()

    NONE = 0
    COLOR = 1
    ILLUMINATED = 2


class MeshVertexColorModeEnumAttrOperator(
    EnumAttrOperator[MeshVertexColorModeEnumPlugOperator]
):
    __slots__ = ()

    NONE = 0
    COLOR = 1
    ILLUMINATED = 2

    NAME_MAP = {
        NONE: "None",
        COLOR: "Color",
        ILLUMINATED: "Illuminated",
    }


class MeshVertexColorModeEnumField(
    EnumField[
        MeshVertexColorModeEnumAttrOperator,
        MeshVertexColorModeEnumPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = MeshVertexColorModeEnumAttrOperator
    PLUG_CLS = MeshVertexColorModeEnumPlugOperator


class PressureMap1EnumPlugOperator(
    EnumPlugOperator["PressureMap1EnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap1EnumAttrOperator(
    EnumAttrOperator[PressureMap1EnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap1EnumField(
    EnumField[PressureMap1EnumAttrOperator, PressureMap1EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap1EnumAttrOperator
    PLUG_CLS = PressureMap1EnumPlugOperator


class PressureMap2EnumPlugOperator(
    EnumPlugOperator["PressureMap2EnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap2EnumAttrOperator(
    EnumAttrOperator[PressureMap2EnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap2EnumField(
    EnumField[PressureMap2EnumAttrOperator, PressureMap2EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap2EnumAttrOperator
    PLUG_CLS = PressureMap2EnumPlugOperator


class PressureMap3EnumPlugOperator(
    EnumPlugOperator["PressureMap3EnumAttrOperator"]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23


class PressureMap3EnumAttrOperator(
    EnumAttrOperator[PressureMap3EnumPlugOperator]
):
    __slots__ = ()

    OFF = 0
    SCALE = 1
    WIDTH = 2
    SOFTNESS = 3
    COLOR = 4
    TRANSPARENCY = 5
    TUBE_WIDTH = 6
    TUBE_LENGTH = 7
    INCANDESCENCE = 8
    GLOW_SPREAD = 9
    TUBES_PER_STEP = 10
    ELEVATION = 11
    AZIMUTH = 12
    PATH_FOLLOW = 13
    PATH_ATTRACT = 14
    RANDOM = 15
    WIGGLE = 16
    CURL = 17
    NOISE = 18
    TURBULENCE = 19
    NUM_TWIGS = 20
    NUM_LEAVES = 21
    NUM_PETALS = 22
    SURFACEOFFSET = 23

    NAME_MAP = {
        OFF: "Off",
        SCALE: "Scale",
        WIDTH: "Width",
        SOFTNESS: "Softness",
        COLOR: "Color",
        TRANSPARENCY: "Transparency",
        TUBE_WIDTH: "Tube Width",
        TUBE_LENGTH: "Tube Length",
        INCANDESCENCE: "Incandescence",
        GLOW_SPREAD: "Glow Spread",
        TUBES_PER_STEP: "Tubes Per Step",
        ELEVATION: "Elevation",
        AZIMUTH: "Azimuth",
        PATH_FOLLOW: "Path Follow",
        PATH_ATTRACT: "Path Attract",
        RANDOM: "Random",
        WIGGLE: "Wiggle",
        CURL: "Curl",
        NOISE: "Noise",
        TURBULENCE: "Turbulence",
        NUM_TWIGS: "Num Twigs",
        NUM_LEAVES: "Num Leaves",
        NUM_PETALS: "Num Petals",
        SURFACEOFFSET: "surfaceOffset",
    }


class PressureMap3EnumField(
    EnumField[PressureMap3EnumAttrOperator, PressureMap3EnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PressureMap3EnumAttrOperator
    PLUG_CLS = PressureMap3EnumPlugOperator


class GeneratedStroke(Shape):
    __slots__ = ()

    NODE_TYPE = "stroke"

    displayPercent = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=100.0
    )
    dpc = displayPercent

    drawAsMesh = BoolField(default_value=True)
    dam = drawAsMesh

    seed = LongField(default_value=0, soft_min_value=0, soft_max_value=1000)
    sed = seed

    drawOrder = LongField(
        default_value=0, soft_min_value=-10, soft_max_value=10
    )
    dro = drawOrder

    surfaceOffset = DoubleField(
        default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0
    )
    sof = surfaceOffset

    brush = TypedField()
    brs = brush

    motionBlurred = BoolField(default_value=True)
    mblr = motionBlurred

    primaryVisibility = BoolField(default_value=True)
    pvs = primaryVisibility

    controlCurve = GenericField(multi=True)
    clc = controlCurve

    outMainMesh = DataMeshField(writable=False)
    omm = outMainMesh

    outFlowerMesh = DataMeshField(writable=False)
    ofm = outFlowerMesh

    outLeafMesh = DataMeshField(writable=False)
    olm = outLeafMesh

    worldMainMesh = DataMeshField(multi=True, writable=False)
    wmm = worldMainMesh

    worldLeafMesh = DataMeshField(multi=True, writable=False)
    wlm = worldLeafMesh

    worldFlowerMesh = DataMeshField(multi=True, writable=False)
    wfm = worldFlowerMesh

    mainVertBufSize = LongField(default_value=0)
    mvbs = mainVertBufSize

    flowerVertBufSize = LongField(default_value=0)
    fvbs = flowerVertBufSize

    leafVertBufSize = LongField(default_value=0)
    lvbs = leafVertBufSize

    meshPolyLimit = LongField(default_value=0)
    mpl = meshPolyLimit

    meshVertexColorMode = MeshVertexColorModeEnumField(default_value=0)
    mvc = meshVertexColorMode

    meshHardEdges = BoolField(default_value=False)
    mhe = meshHardEdges

    meshQuadOutput = BoolField(default_value=False)
    mqo = meshQuadOutput

    cameraPoint = CameraPointField(default_value=(0.0, 0.0, 0.0))
    cpt = cameraPoint
    cameraPointX = cameraPoint.cameraPointX
    cpx = cameraPointX
    cameraPointY = cameraPoint.cameraPointY
    cpy = cameraPointY
    cameraPointZ = cameraPoint.cameraPointZ
    cpz = cameraPointZ

    lineModifier = TypedField(multi=True)
    lmd = lineModifier

    maxDrawSegments = LongField(default_value=1000000)
    mdsg = maxDrawSegments

    curveMode = LongField(default_value=0, min_value=0, max_value=2)
    cmd = curveMode

    leafCurveMode = LongField(default_value=0, min_value=0, max_value=2)
    lcm = leafCurveMode

    flowerCurveMode = LongField(default_value=0, min_value=0, max_value=2)
    fcm = flowerCurveMode

    degree = LongField(default_value=2, min_value=1, max_value=7)
    dgr = degree

    curveAlign = BoolField(default_value=False)
    cva = curveAlign

    outMainCurveCount = LongField(default_value=0, writable=False)
    omcc = outMainCurveCount

    outLeafCurveCount = LongField(default_value=0, writable=False)
    olcc = outLeafCurveCount

    outFlowerCurveCount = LongField(default_value=0, writable=False)
    ofcc = outFlowerCurveCount

    outMainCurves = DataNurbsCurveField(multi=True, writable=False)
    omc = outMainCurves

    outLeafCurves = DataNurbsCurveField(multi=True, writable=False)
    olc = outLeafCurves

    outFlowerCurves = DataNurbsCurveField(multi=True, writable=False)
    ofc = outFlowerCurves

    sampleDensity = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=2.0
    )
    sdn = sampleDensity

    smoothing = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=10.0
    )
    smo = smoothing

    perspective = BoolField(default_value=True)
    per = perspective

    useNormal = BoolField(default_value=False)
    usn = useNormal

    minimalTwist = BoolField(default_value=False)
    mnt = minimalTwist

    normal = NormalField(
        default_value=(0.0, 0.0, 1.0),
        soft_min_value=(-1.0, -1.0, -1.0),
        soft_max_value=(1.0, 1.0, 1.0),
    )
    nml = normal
    normalX = normal.normalX
    nmx = normalX
    normalY = normal.normalY
    nmy = normalY
    normalZ = normal.normalZ
    nmz = normalZ

    minClip = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    mnc = minClip

    maxClip = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    mxc = maxClip

    pathCurve = PathCurveField(multi=True)
    pcv = pathCurve

    collisionObject = GenericField(multi=True)
    clob = collisionObject

    outPoint = OutPointField(multi=True, default_value=(0.0, 0.0, 0.0))
    opt = outPoint

    outNormal = OutNormalField(
        multi=True, default_value=(0.0, 0.0, 0.0), writable=False
    )
    onm = outNormal

    pressureMap1 = PressureMap1EnumField(default_value=0)
    spm1 = pressureMap1

    pressureMin1 = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ps1 = pressureMin1

    pressureMax1 = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    px1 = pressureMax1

    pressureMap2 = PressureMap2EnumField(default_value=0)
    spm2 = pressureMap2

    pressureMin2 = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ps2 = pressureMin2

    pressureMax2 = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    px2 = pressureMax2

    pressureMap3 = PressureMap3EnumField(default_value=0)
    spm3 = pressureMap3

    pressureMin3 = DoubleField(
        default_value=0.0, soft_min_value=0.0, soft_max_value=1.0
    )
    ps3 = pressureMin3

    pressureMax3 = DoubleField(
        default_value=1.0, soft_min_value=0.0, soft_max_value=1.0
    )
    px3 = pressureMax3

    pressureScale = PressureScaleField(multi=True, default_value=(0.0, 0.0, 0))
    psc = pressureScale

    pressure = DoubleField(multi=True, default_value=0.0)
    psr = pressure

    uvSetName = MessageField(multi=True)
    uvsetn = uvSetName
