# coding: utf-8
from ._generated.anim_layer import GeneratedAnimLayer
from ._anim_layer import AnimLayerOperations


class AnimLayer(GeneratedAnimLayer, AnimLayerOperations):
    __slots__ = ()

    NODE_TYPE = "animLayer"
