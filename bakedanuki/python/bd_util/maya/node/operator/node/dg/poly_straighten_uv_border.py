# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class PolyStraightenUVBorder(DG):
    __slots__ = ()

    NODE_TYPE = "polyStraightenUVBorder"

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

    uvSetName = DataStringField()
    uvs = uvSetName

    curvature = FloatField(default_value=0.0, soft_min_value=-1.0, soft_max_value=1.0)
    c = curvature

    preserveLength = FloatField(default_value=1.0, min_value=0.0, max_value=1.0)
    pl = preserveLength

    blendOriginal = FloatField(default_value=0.0, min_value=0.0, max_value=1.0)
    bo = blendOriginal

    gapTolerance = LongField(default_value=5, min_value=0, soft_min_value=0, soft_max_value=10)
    gt = gapTolerance
