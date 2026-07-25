# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_cut import (
    CutPlaneCenterField,
    CutPlaneRotateField,
    CutPlaneSizeField,
    ExtractOffsetField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolyCut(DG):
    __slots__ = ()

    NODE_TYPE = "polyCut"

    output = DataMeshField(writable=False)
    out = output

    inputPolymesh = DataMeshField()
    ip = inputPolymesh

    inMeshCache = DataMeshField()
    imc = inMeshCache

    cacheInput = LongField(default_value=0)
    cin = cacheInput

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    vertexIdMap = BoolField(default_value=False)
    vmap = vertexIdMap

    edgeIdMap = BoolField(default_value=False)
    emap = edgeIdMap

    faceIdMap = BoolField(default_value=False)
    fmap = faceIdMap

    inputComponents = TypedField()
    ics = inputComponents

    useInputComp = BoolField(default_value=True)
    uic = useInputComp

    inputMatrix = DataMatrixField()
    ix = inputMatrix

    worldSpace = BoolField(default_value=False)
    ws = worldSpace

    manipMatrix = DataMatrixField()
    mp = manipMatrix

    cutPlaneCenter = CutPlaneCenterField(default_value=(0.0, 0.0, 0.0))
    pc = cutPlaneCenter
    cutPlaneCenterX = cutPlaneCenter.cutPlaneCenterX
    pcx = cutPlaneCenterX
    cutPlaneCenterY = cutPlaneCenter.cutPlaneCenterY
    pcy = cutPlaneCenterY
    cutPlaneCenterZ = cutPlaneCenter.cutPlaneCenterZ
    pcz = cutPlaneCenterZ

    cutPlaneRotate = CutPlaneRotateField(default_value=(0.0, 0.0, 0.0))
    ro = cutPlaneRotate
    cutPlaneRotateX = cutPlaneRotate.cutPlaneRotateX
    rx = cutPlaneRotateX
    cutPlaneRotateY = cutPlaneRotate.cutPlaneRotateY
    ry = cutPlaneRotateY
    cutPlaneRotateZ = cutPlaneRotate.cutPlaneRotateZ
    rz = cutPlaneRotateZ

    cutPlaneSize = CutPlaneSizeField(default_value=(1.0, 1.0), min_value=(0.0, 0.0), soft_max_value=(2.0, 2.0))
    ps = cutPlaneSize
    cutPlaneWidth = cutPlaneSize.cutPlaneWidth
    pw = cutPlaneWidth
    cutPlaneHeight = cutPlaneSize.cutPlaneHeight
    ph = cutPlaneHeight

    extractFaces = BoolField(default_value=False)
    ef = extractFaces

    extractOffset = ExtractOffsetField(default_value=(0.5, 0.5, 0.5))
    eo = extractOffset
    extractOffsetX = extractOffset.extractOffsetX
    eox = extractOffsetX
    extractOffsetY = extractOffset.extractOffsetY
    eoy = extractOffsetY
    extractOffsetZ = extractOffset.extractOffsetZ
    eoz = extractOffsetZ

    deleteFaces = BoolField(default_value=False)
    df = deleteFaces

    onObject = BoolField(default_value=True)
    oo = onObject

    compId = LongField(default_value=0, writable=False)
    cid = compId

    cutEdges = TypedField(writable=False)
    cec = cutEdges
