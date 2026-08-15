# coding: utf-8
from .._core import Shape
from .....attr.define.node_attr.pfx_hair import CameraPointField
from .....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from .....attr.define.std.at.generic import GenericField
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


class GeneratedPfxHair(Shape):
    __slots__ = ()

    NODE_TYPE = "pfxHair"

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

    renderHairs = TypedField()
    rhs = renderHairs

    receiveShadows = BoolField(default_value=True)
    rcsh = receiveShadows

    visibleInReflections = BoolField(default_value=False)
    vir = visibleInReflections

    visibleInRefractions = BoolField(default_value=False)
    vif = visibleInRefractions
