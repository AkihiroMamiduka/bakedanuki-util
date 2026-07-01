# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_cut import (
    CutPlaneCenterField,
    CutPlaneRotateField,
    CutPlaneSizeField,
    ExtractOffsetField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class PolyCut(DG):
    __slots__ = ()

    NODE_TYPE = "polyCut"

    output = DataMeshField()
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField()
    cin = cacheInput

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField()
    vmap = vertexIdMap

    edgeIdMap = BoolField()
    emap = edgeIdMap

    faceIdMap = BoolField()
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField()
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField()
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    cutPlaneCenter = CutPlaneCenterField()
    pc = cutPlaneCenter
    cutPlaneCenterX = cutPlaneCenter.cutPlaneCenterX
    pcx = cutPlaneCenterX
    cutPlaneCenterY = cutPlaneCenter.cutPlaneCenterY
    pcy = cutPlaneCenterY
    cutPlaneCenterZ = cutPlaneCenter.cutPlaneCenterZ
    pcz = cutPlaneCenterZ

    cutPlaneRotate = CutPlaneRotateField()
    ro = cutPlaneRotate
    cutPlaneRotateX = cutPlaneRotate.cutPlaneRotateX
    rx = cutPlaneRotateX
    cutPlaneRotateY = cutPlaneRotate.cutPlaneRotateY
    ry = cutPlaneRotateY
    cutPlaneRotateZ = cutPlaneRotate.cutPlaneRotateZ
    rz = cutPlaneRotateZ

    cutPlaneSize = CutPlaneSizeField()
    ps = cutPlaneSize
    cutPlaneWidth = cutPlaneSize.cutPlaneWidth
    pw = cutPlaneWidth
    cutPlaneHeight = cutPlaneSize.cutPlaneHeight
    ph = cutPlaneHeight

    extractFaces = BoolField()
    ef = extractFaces

    extractOffset = ExtractOffsetField()
    eo = extractOffset
    extractOffsetX = extractOffset.extractOffsetX
    eox = extractOffsetX
    extractOffsetY = extractOffset.extractOffsetY
    eoy = extractOffsetY
    extractOffsetZ = extractOffset.extractOffsetZ
    eoz = extractOffsetZ

    deleteFaces = BoolField()
    df = deleteFaces

    onObject = BoolField()
    oo = onObject

    compId = LongField()
    cid = compId

    cutEdges = TypedField()
    cec = cutEdges
