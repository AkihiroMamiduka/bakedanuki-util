# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.ai_imager_lens_effects import BloomTintField
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiImagerLensEffects(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerLensEffects"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    vignetting = FloatField(
        default_value=0.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=100.0,
    )

    bloomThreshold = FloatField(
        default_value=0.8999999761581421,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    bloom_threshold = bloomThreshold

    bloomTint = BloomTintField(default_value=(1.0, 1.0, 1.0))
    bloom_tint = bloomTint
    bloomTintR = bloomTint.bloomTintR
    bloom_tintr = bloomTintR
    bloomTintG = bloomTint.bloomTintG
    bloom_tintg = bloomTintG
    bloomTintB = bloomTint.bloomTintB
    bloom_tintb = bloomTintB

    bloomRadius = LongField(
        default_value=4, min_value=1, soft_min_value=1, soft_max_value=12
    )
    bloom_radius = bloomRadius

    bloomStrength = FloatField(
        default_value=0.0,
        min_value=0.0,
        soft_min_value=0.0,
        soft_max_value=10.0,
    )
    bloom_strength = bloomStrength
