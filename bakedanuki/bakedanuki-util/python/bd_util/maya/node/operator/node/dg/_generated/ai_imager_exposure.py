# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class GeneratedAiImagerExposure(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerExposure"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    exposure = FloatField(default_value=0.0, soft_min_value=-10.0, soft_max_value=10.0)
