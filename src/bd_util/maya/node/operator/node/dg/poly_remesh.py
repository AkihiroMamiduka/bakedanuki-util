# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.float_linear import FloatLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class InterpolationTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    LINEAR = 0
    CUBIC = 1
    HYBRID = 2


class InterpolationTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    LINEAR = 0
    CUBIC = 1
    HYBRID = 2

    NAME_MAP = {
        LINEAR: "Linear",
        CUBIC: "Cubic",
        HYBRID: "Hybrid",
    }


class InterpolationTypeEnumField(
    EnumField[InterpolationTypeEnumAttrOperator, InterpolationTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InterpolationTypeEnumAttrOperator
    PLUG_CLS = InterpolationTypeEnumPlugOperator


class PolyRemesh(DG):
    __slots__ = ()

    NODE_TYPE = "polyRemesh"

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

    maxEdgeLength = FloatLinearField()
    mel = maxEdgeLength

    collapseThreshold = FloatField()
    cot = collapseThreshold

    smoothStrength = FloatField()
    smt = smoothStrength

    tessellateBorders = BoolField()
    tsb = tessellateBorders

    interpolationType = InterpolationTypeEnumField()
    ipt = interpolationType

    maxTriangleCount = LongField()
    mtc = maxTriangleCount
