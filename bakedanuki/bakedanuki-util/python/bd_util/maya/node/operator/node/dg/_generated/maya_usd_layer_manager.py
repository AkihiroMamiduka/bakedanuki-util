# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.maya_usd_layer_manager import LayersField
from ....attr.define.std.dt.string import DataStringField


class GeneratedMayaUsdLayerManager(DG):
    __slots__ = ()

    NODE_TYPE = "mayaUsdLayerManager"

    selectedStage = DataStringField()
    sst = selectedStage

    layers = LayersField(multi=True)
    lyr = layers
