# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_light_mixer import LayerTintField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField
from ....attr.define.std.at.numeric_scalar_range.float import FloatField
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

    layerTint = LayerTintField(multi=True, default_value=(5.872863084732671e-09, 5.885453550164232e-43, 1.0))
    layer_tint = layerTint

    layerIntensity = FloatField(multi=True, default_value=5.8728772955873865e-09)
    layer_intensity = layerIntensity

    layerExposure = FloatField(multi=True, default_value=5.872891506442102e-09)
    layer_exposure = layerExposure

    outputName = DataStringField()
    output_name = outputName
