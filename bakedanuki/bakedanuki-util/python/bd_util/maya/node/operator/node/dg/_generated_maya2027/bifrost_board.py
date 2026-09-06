# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField
from ....attr.define.std.dt.string_array import DataStringArrayField


class GeneratedBifrostBoard(DG):
    __slots__ = ()

    NODE_TYPE = "bifrostBoard"

    saveContainerToJSON = DataStringField()
    sc = saveContainerToJSON

    referencedGraph = DataStringField()
    rfg = referencedGraph

    runOnDemand = BoolField(default_value=False, readable=False)
    rod = runOnDemand

    resumableAfterEsc = BoolField(default_value=False, readable=False)
    rae = resumableAfterEsc

    enableAsync = BoolField(default_value=False, readable=False)
    eas = enableAsync

    isSimulation = BoolField(default_value=False, readable=False)
    ism = isSimulation

    dirtyFlag = BoolField(default_value=False, readable=False)

    asyncComputeDone = BoolField(default_value=False, readable=False)

    bifrostPinnedNode = DataStringField()
    pinnedNode = bifrostPinnedNode

    bifrostNodeList = DataStringArrayField()
    bfNodeList = bifrostNodeList

    bifrostSavedVersion = DataStringField()
