# coding: utf-8
from ._core import DG
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.matrix import DataMatrixField
from ...attr.define.std.dt.mesh import DataMeshField
from ...attr.define.std.dt.string import DataStringField


class MergeUVSetsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NO_MERGE = 0
    MERGE_BY_NAME = 1
    MERGE_BY_UV_LINKS = 2


class MergeUVSetsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NO_MERGE = 0
    MERGE_BY_NAME = 1
    MERGE_BY_UV_LINKS = 2

    NAME_MAP = {
        NO_MERGE: "No Merge",
        MERGE_BY_NAME: "Merge By Name",
        MERGE_BY_UV_LINKS: "Merge By UV Links",
    }


class MergeUVSetsEnumField(
    EnumField[MergeUVSetsEnumAttrOperator, MergeUVSetsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MergeUVSetsEnumAttrOperator
    PLUG_CLS = MergeUVSetsEnumPlugOperator


class OperationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    UNION = 1
    DIFFERENCE = 2
    INTERSECTION = 3


class OperationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    UNION = 1
    DIFFERENCE = 2
    INTERSECTION = 3

    NAME_MAP = {
        UNION: "union",
        DIFFERENCE: "difference",
        INTERSECTION: "intersection",
    }


class OperationEnumField(
    EnumField[OperationEnumAttrOperator, OperationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OperationEnumAttrOperator
    PLUG_CLS = OperationEnumPlugOperator


class ClassificationEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    EDGE = 1
    NORMAL = 2


class ClassificationEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    EDGE = 1
    NORMAL = 2

    NAME_MAP = {
        EDGE: "Edge",
        NORMAL: "Normal",
    }


class ClassificationEnumField(
    EnumField[ClassificationEnumAttrOperator, ClassificationEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClassificationEnumAttrOperator
    PLUG_CLS = ClassificationEnumPlugOperator


class PolyBoolOp(DG):
    __slots__ = ()

    NODE_TYPE = "polyBoolOp"

    output = DataMeshField()
    out = output

    useOldPolyArchitecture = BoolField()
    uopa = useOldPolyArchitecture

    inputPoly = DataMeshField(multi=True)
    ip = inputPoly

    inputMat = DataMatrixField(multi=True)
    im = inputMat

    componentTagName = DataStringField(multi=True)
    ctg = componentTagName

    mergeUVSets = MergeUVSetsEnumField()
    muv = mergeUVSets

    outputUVSetName = DataStringField(multi=True)
    ouv = outputUVSetName

    operation = OperationEnumField()
    op = operation

    classification = ClassificationEnumField()
    cls = classification

    useThresholds = BoolField()
    uth = useThresholds

    vertexDistanceThreshold = DoubleLinearField()
    vdt = vertexDistanceThreshold

    faceAreaThreshold = DoubleLinearField()
    fat = faceAreaThreshold

    preserveColor = BoolField()
    pcr = preserveColor
