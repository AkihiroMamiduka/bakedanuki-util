# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_split import (
    SplitPointsField,
    VerticesField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.mesh import DataMeshField


class PolySplit(DG):
    __slots__ = ()

    NODE_TYPE = "polySplit"

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

    vertices = VerticesField(multi=True)
    v = vertices

    edge = FloatField(multi=True)
    e = edge

    desc = LongField(multi=True)
    d = desc

    subdivision = LongField()
    s = subdivision

    smoothingAngle = DoubleAngleField()
    sma = smoothingAngle

    maya70 = BoolField()
    m70 = maya70

    maya2015 = BoolField()
    m2015 = maya2015

    splitPoints = SplitPointsField(multi=True)
    sps = splitPoints

    # TODO: splitPoints.splitPoint.baryCoord1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: splitPoints.splitPoint.baryCoord2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: splitPoints.splitPoint.baryCoord3 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    detachEdges = BoolField()
    de = detachEdges

    projectedCurveTolerance = FloatField()
    pct = projectedCurveTolerance

    clean2Verts = BoolField()
    c2v = clean2Verts

    insertWithEdgeFlow = BoolField()
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField()
    aef = adjustEdgeFlow
