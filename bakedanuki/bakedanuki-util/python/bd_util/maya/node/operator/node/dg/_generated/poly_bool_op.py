# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.matrix import DataMatrixField
from ....attr.define.std.dt.mesh import DataMeshField
from ....attr.define.std.dt.string import DataStringField


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


class _GeneratedPolyBoolOp(DG):
    __slots__ = ()

    NODE_TYPE = "polyBoolOp"

    output = DataMeshField(writable=False)
    out = output

    useOldPolyArchitecture = BoolField(default_value=False)
    uopa = useOldPolyArchitecture

    inputPoly = DataMeshField(multi=True)
    ip = inputPoly

    inputMat = DataMatrixField(multi=True)
    im = inputMat

    componentTagName = DataStringField(multi=True)
    ctg = componentTagName

    mergeUVSets = MergeUVSetsEnumField(default_value=1)
    muv = mergeUVSets

    outputUVSetName = DataStringField(multi=True, writable=False)
    ouv = outputUVSetName

    operation = OperationEnumField(default_value=1)
    op = operation

    classification = ClassificationEnumField(default_value=2)
    cls = classification

    useThresholds = BoolField(default_value=False)
    uth = useThresholds

    vertexDistanceThreshold = DoubleLinearField(default_value=0.001, min_value=0.0, soft_max_value=1.0)
    vdt = vertexDistanceThreshold

    faceAreaThreshold = DoubleLinearField(default_value=0.0001, min_value=0.0, soft_max_value=1.0)
    fat = faceAreaThreshold

    preserveColor = BoolField(default_value=False)
    pcr = preserveColor
