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

    weight = FloatField()
    wt = weight

    absoluteWeight = BoolField()
    ab = absoluteWeight

    direction = BoolField()
    dr = direction

    rootEdge = LongField()
    re = rootEdge

    smoothingAngle = DoubleAngleField()
    sma = smoothingAngle

    splitType = SplitTypeEnumField()
    stp = splitType

    divisions = LongField()
    div = divisions

    enableProfileCurve = BoolField()
    epc = enableProfileCurve

    profileCurve = ProfileCurveField(multi=True)
    p = profileCurve

    profileCurveInputOffset = FloatField()
    pio = profileCurveInputOffset

    profileCurveInputScale = FloatField()
    pis = profileCurveInputScale

    useFaceNormalsAtEnds = BoolField()
    fne = useFaceNormalsAtEnds

    useEqualMultiplier = BoolField()
    uem = useEqualMultiplier

    fixQuads = BoolField()
    fq = fixQuads

    insertWithEdgeFlow = BoolField()
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField()
    aef = adjustEdgeFlow
