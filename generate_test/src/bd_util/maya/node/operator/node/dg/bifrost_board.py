# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class BifrostBoard(DG):
    __slots__ = ()

    NODE_TYPE = "bifrostBoard"

    saveContainerToJSON = DataStringField()
    sc = saveContainerToJSON

    runOnDemand = BoolField()
    rod = runOnDemand

    resumableAfterEsc = BoolField()
    rae = resumableAfterEsc

    dirtyFlag = BoolField()
