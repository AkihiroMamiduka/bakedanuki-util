# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_light_mixer import LayerTintField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiImagerLightMixer(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerLightMixer"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerName = DataStringField(multi=True)
    layer_name = layerName

    layerEnable = BoolField(multi=True, default_value=False)
    layer_enable = layerEnable

    layerSolo = BoolField(multi=True, default_value=True)
    layer_solo = layerSolo

    layerTint = LayerTintField(multi=True, default_value=(2.246063752498668e+26, 6.305843089461677e-43, 1.0))
    layer_tint = layerTint

    layerIntensity = FloatField(multi=True, default_value=2.2460696554567714e+26)
    layer_intensity = layerIntensity

    layerExposure = FloatField(multi=True, default_value=2.246075558414875e+26)
    layer_exposure = layerExposure

    outputName = DataStringField()
    output_name = outputName
