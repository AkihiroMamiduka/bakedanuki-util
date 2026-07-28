# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.scalar.unit.range.float_linear import (
    FloatLinearField,
)
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField


class InterpolationTypeEnumPlugOperator(
    EnumPlugOperator["InterpolationTypeEnumAttrOperator"]
):
    __slots__ = ()

    LINEAR = 0
    CUBIC = 1
    HYBRID = 2


class InterpolationTypeEnumAttrOperator(
    EnumAttrOperator[InterpolationTypeEnumPlugOperator]
):
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
    EnumField[
        InterpolationTypeEnumAttrOperator, InterpolationTypeEnumPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = InterpolationTypeEnumAttrOperator
    PLUG_CLS = InterpolationTypeEnumPlugOperator


class GeneratedPolyRemesh(DG):
    __slots__ = ()

    NODE_TYPE = "polyRemesh"

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

    maxEdgeLength = FloatLinearField(
        default_value=1.0,
        min_value=0.0,
        soft_min_value=0.1,
        soft_max_value=2.0,
    )
    mel = maxEdgeLength

    collapseThreshold = FloatField(
        default_value=20.0, min_value=0.0, max_value=100.0
    )
    cot = collapseThreshold

    smoothStrength = FloatField(
        default_value=0.0, min_value=0.0, soft_max_value=100.0
    )
    smt = smoothStrength

    tessellateBorders = BoolField(default_value=True)
    tsb = tessellateBorders

    interpolationType = InterpolationTypeEnumField(default_value=2)
    ipt = interpolationType

    maxTriangleCount = LongField(
        default_value=5000000, min_value=0, soft_max_value=5000000
    )
    mtc = maxTriangleCount
