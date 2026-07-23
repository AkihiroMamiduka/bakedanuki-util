# coding: utf-8
from .._core import DG
from ....attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.numeric_scalar.bool import BoolField
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


class _GeneratedPolyUnite(DG):
    __slots__ = ()

    NODE_TYPE = "polyUnite"

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
