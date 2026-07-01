# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiImagerExposure(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerExposure"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    exposure = FloatField()
