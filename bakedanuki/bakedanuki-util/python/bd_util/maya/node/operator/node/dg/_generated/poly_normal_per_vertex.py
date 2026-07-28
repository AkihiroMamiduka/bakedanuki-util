# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.poly_normal_per_vertex import (
    NormalPerVertexField,
)
from ....attr.define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import (
    Float3Field,
)
from ....attr.define.std.at.compound import CompoundField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


class GeneratedPolyNormalPerVertex(DG):
    __slots__ = ()

    NODE_TYPE = "polyNormalPerVertex"

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

    normalPerVertex = NormalPerVertexField()
    npvx = normalPerVertex
    vertexNormal = normalPerVertex.vertexNormal
    vn = vertexNormal

    vertexNormalXYZ = Float3Field()
    nxyz = vertexNormalXYZ

    vertexNormalX = FloatField()
    vxnx = vertexNormalX

    vertexNormalY = FloatField()
    vxny = vertexNormalY

    vertexNormalZ = FloatField()
    vxnz = vertexNormalZ

    vertexFaceNormal = CompoundField()
    vfnl = vertexFaceNormal

    vertexFaceNormalXYZ = Float3Field()
    fnxy = vertexFaceNormalXYZ

    vertexFaceNormalX = FloatField()
    vfnx = vertexFaceNormalX

    vertexFaceNormalY = FloatField()
    vfny = vertexFaceNormalY

    vertexFaceNormalZ = FloatField()
    vfnz = vertexFaceNormalZ

    normalDeform = BoolField(default_value=True)
    npvd = normalDeform

    normalAdd = BoolField(default_value=False)
    npva = normalAdd
