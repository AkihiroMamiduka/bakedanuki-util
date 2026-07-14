# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.float_linear import FloatLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class PolyBevelCutback(DG):
    __slots__ = ()

    NODE_TYPE = "polyBevelCutback"

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

    offset = FloatLinearField(default_value=0.20000000298023224, min_value=0.0, soft_max_value=5.0)
    o = offset

    selectedEdgeGroup = TypedField(writable=False)
    seg = selectedEdgeGroup

    selectedFaceGroup = TypedField(writable=False)
    sfg = selectedFaceGroup
