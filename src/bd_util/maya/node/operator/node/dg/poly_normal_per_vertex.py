# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_normal_per_vertex import NormalPerVertexField
from ...attr.define.custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field
from ...attr.define.std.at.compound import CompoundField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.mesh import DataMeshField


class PolyNormalPerVertex(DG):
    __slots__ = ()

    NODE_TYPE = "polyNormalPerVertex"

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

    normalDeform = BoolField()
    npvd = normalDeform

    normalAdd = BoolField()
    npva = normalAdd
