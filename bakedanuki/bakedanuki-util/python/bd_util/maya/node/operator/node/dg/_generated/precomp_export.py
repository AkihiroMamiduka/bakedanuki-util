# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.precomp_export import (
    ExcludedExportItemListField,
)
from ....attr.define.std.dt.string import DataStringField


class GeneratedPrecompExport(DG):
    __slots__ = ()

    NODE_TYPE = "precompExport"

    excludedExportItemList = ExcludedExportItemListField(multi=True)
    eil = excludedExportItemList

    preCompositingAnchor = DataStringField()
    pca = preCompositingAnchor

    preCompositingNotes = DataStringField()
    pcn = preCompositingNotes
