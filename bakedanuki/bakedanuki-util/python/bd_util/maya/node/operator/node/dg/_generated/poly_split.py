# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_split import (
    SplitPointsField,
    VerticesField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.mesh import DataMeshField


class _GeneratedPolySplit(DG):
    __slots__ = ()

    NODE_TYPE = "polySplit"

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

    vertices = VerticesField(multi=True, default_value=(0.0, 0.0, 0.0))
    v = vertices

    edge = FloatField(multi=True, default_value=0.0, min_value=0.0, max_value=1.0)
    e = edge

    desc = LongField(multi=True, default_value=0)
    d = desc

    subdivision = LongField(default_value=1, min_value=1, max_value=100, soft_max_value=10)
    s = subdivision

    smoothingAngle = DoubleAngleField(default_value=0.0, soft_min_value=0.0, soft_max_value=180.0)
    sma = smoothingAngle

    maya70 = BoolField(default_value=True)
    m70 = maya70

    maya2015 = BoolField(default_value=False)
    m2015 = maya2015

    splitPoints = SplitPointsField(multi=True)
    sps = splitPoints

    baryCoord1 = DoubleLinearField()
    bc1 = baryCoord1

    baryCoord2 = DoubleLinearField()
    bc2 = baryCoord2

    baryCoord3 = DoubleLinearField()
    bc3 = baryCoord3

    detachEdges = BoolField(default_value=False)
    de = detachEdges

    projectedCurveTolerance = FloatField(default_value=9.999999747378752e-05, min_value=0.0)
    pct = projectedCurveTolerance

    clean2Verts = BoolField(default_value=False)
    c2v = clean2Verts

    insertWithEdgeFlow = BoolField(default_value=False)
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    aef = adjustEdgeFlow
