# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiImagerDenoiserNoice(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerDenoiserNoice"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    patchRadius = LongField(default_value=3, min_value=0, soft_max_value=6)
    patch_radius = patchRadius

    searchRadius = LongField(default_value=9, min_value=0, soft_min_value=6, soft_max_value=21)
    search_radius = searchRadius

    variance = FloatField(default_value=0.25, min_value=0.0, max_value=1.0)

    outputSuffix = DataStringField()
    output_suffix = outputSuffix
