# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.poly_split_ring import ProfileCurveField
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField


class SplitTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1
    MULTI = 2


class SplitTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1
    MULTI = 2

    NAME_MAP = {
        ABSOLUTE: "Absolute",
        RELATIVE: "Relative",
        MULTI: "Multi",
    }


class SplitTypeEnumField(
    EnumField[SplitTypeEnumAttrOperator, SplitTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SplitTypeEnumAttrOperator
    PLUG_CLS = SplitTypeEnumPlugOperator


class PolySplitRing(DG):
    __slots__ = ()

    NODE_TYPE = "polySplitRing"

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

    weight = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    wt = weight

    absoluteWeight = BoolField(default_value=False)
    ab = absoluteWeight

    direction = BoolField(default_value=True)
    dr = direction

    rootEdge = LongField(default_value=-1)
    re = rootEdge

    smoothingAngle = DoubleAngleField(default_value=180.0, soft_min_value=0.0, soft_max_value=180.0)
    sma = smoothingAngle

    splitType = SplitTypeEnumField(default_value=1)
    stp = splitType

    divisions = LongField(default_value=2, min_value=1, soft_max_value=25)
    div = divisions

    enableProfileCurve = BoolField(default_value=True)
    epc = enableProfileCurve

    profileCurve = ProfileCurveField(multi=True, default_value=(0.0, 0.0, 0.0))
    p = profileCurve

    profileCurveInputOffset = FloatField(default_value=0.0, soft_min_value=-20.0, soft_max_value=20.0)
    pio = profileCurveInputOffset

    profileCurveInputScale = FloatField(default_value=1.0, soft_min_value=-10.0, soft_max_value=10.0)
    pis = profileCurveInputScale

    useFaceNormalsAtEnds = BoolField(default_value=True)
    fne = useFaceNormalsAtEnds

    useEqualMultiplier = BoolField(default_value=True)
    uem = useEqualMultiplier

    fixQuads = BoolField(default_value=False)
    fq = fixQuads

    insertWithEdgeFlow = BoolField(default_value=False)
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    aef = adjustEdgeFlow
