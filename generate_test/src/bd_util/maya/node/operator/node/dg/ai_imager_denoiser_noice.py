# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.dt.string import DataStringField


class AiImagerDenoiserNoice(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerDenoiserNoice"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    patchRadius = LongField()
    patch_radius = patchRadius

    searchRadius = LongField()
    search_radius = searchRadius

    variance = FloatField()

    outputSuffix = DataStringField()
    output_suffix = outputSuffix
