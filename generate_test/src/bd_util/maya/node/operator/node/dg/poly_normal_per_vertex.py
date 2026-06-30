# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_normal_per_vertex import NormalPerVertexField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
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

    # TODO: vertexNormal.vertexNormalXYZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexNormalX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexNormalY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexNormalZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexFaceNormal (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexFaceNormal.vertexFaceNormalXYZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexFaceNormal.vertexFaceNormalX (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexFaceNormal.vertexFaceNormalY (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: vertexNormal.vertexFaceNormal.vertexFaceNormalZ (attributeType=None, dataType=None) は未対応のため手動で追加してください

    normalDeform = BoolField()
    npvd = normalDeform

    normalAdd = BoolField()
    npva = normalAdd
