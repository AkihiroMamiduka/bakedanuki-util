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
from ...attr.define.std.at.unit_scalar_range.double_angle import DoubleAngleField
from ...attr.define.std.dt.mesh import DataMeshField


class SplitTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1


class SplitTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    ABSOLUTE = 0
    RELATIVE = 1

    NAME_MAP = {
        ABSOLUTE: "Absolute",
        RELATIVE: "Relative",
    }


class SplitTypeEnumField(
    EnumField[SplitTypeEnumAttrOperator, SplitTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SplitTypeEnumAttrOperator
    PLUG_CLS = SplitTypeEnumPlugOperator


class PolyDuplicateEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polyDuplicateEdge"

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

    offset = FloatField()
    of = offset

    startVertexOffset = FloatField()
    svo = startVertexOffset

    endVertexOffset = FloatField()
    evo = endVertexOffset

    deleteEdge = BoolField()
    de = deleteEdge

    smoothingAngle = DoubleAngleField()
    sma = smoothingAngle

    splitType = SplitTypeEnumField()
    stp = splitType

    insertWithEdgeFlow = BoolField()
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField()
    aef = adjustEdgeFlow
