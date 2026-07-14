# coding: utf-8
from ._core import DG
from ...attr.define.std.at.typed import TypedField
from ...attr.define.std.dt.string import DataStringField


class PxrUsdStageNode(DG):
    __slots__ = ()

    NODE_TYPE = "pxrUsdStageNode"

    filePath = DataStringField()
    fp = filePath

    outUsdStage = TypedField(writable=False)
    os = outUsdStage
