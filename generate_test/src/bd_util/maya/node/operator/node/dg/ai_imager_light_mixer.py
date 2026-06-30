# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_imager_light_mixer import LayerTintField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiImagerLightMixer(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerLightMixer"

    out = MessageField()

    enable = BoolField()

    layerName = DataStringField(multi=True)
    layer_name = layerName

    layerEnable = BoolField(multi=True)
    layer_enable = layerEnable

    layerSolo = BoolField(multi=True)
    layer_solo = layerSolo

    layerTint = LayerTintField(multi=True)
    layer_tint = layerTint

    layerIntensity = FloatField(multi=True)
    layer_intensity = layerIntensity

    layerExposure = FloatField(multi=True)
    layer_exposure = layerExposure

    outputName = DataStringField()
    output_name = outputName
