# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.ai_imager_lens_effects import BloomTintField
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiImagerLensEffects(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerLensEffects"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    vignetting = FloatField()

    bloomThreshold = FloatField()
    bloom_threshold = bloomThreshold

    bloomTint = BloomTintField()
    bloom_tint = bloomTint
    bloomTintR = bloomTint.bloomTintR
    bloom_tintr = bloomTintR
    bloomTintG = bloomTint.bloomTintG
    bloom_tintg = bloomTintG
    bloomTintB = bloomTint.bloomTintB
    bloom_tintb = bloomTintB

    bloomRadius = LongField()
    bloom_radius = bloomRadius

    bloomStrength = FloatField()
    bloom_strength = bloomStrength
