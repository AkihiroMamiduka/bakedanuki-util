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
from ....attr.define.std.at.scalar.unit.range.double_angle import DoubleAngleField
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.mesh import DataMeshField


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


class _GeneratedPolyDuplicateEdge(DG):
    __slots__ = ()

    NODE_TYPE = "polyDuplicateEdge"

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

    offset = FloatField(default_value=0.5, min_value=0.0, max_value=1.0)
    of = offset

    startVertexOffset = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    svo = startVertexOffset

    endVertexOffset = FloatField(default_value=0.0, min_value=-1.0, max_value=1.0)
    evo = endVertexOffset

    deleteEdge = BoolField(default_value=True)
    de = deleteEdge

    smoothingAngle = DoubleAngleField(default_value=180.0, soft_min_value=0.0, soft_max_value=180.0)
    sma = smoothingAngle

    splitType = SplitTypeEnumField(default_value=1)
    stp = splitType

    insertWithEdgeFlow = BoolField(default_value=False)
    ief = insertWithEdgeFlow

    adjustEdgeFlow = FloatField(default_value=1.0, soft_min_value=0.0, soft_max_value=1.0)
    aef = adjustEdgeFlow
