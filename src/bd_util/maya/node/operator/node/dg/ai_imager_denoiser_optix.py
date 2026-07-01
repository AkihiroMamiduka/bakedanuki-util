# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField
from ...attr.define.std.dt.string import DataStringField


class AiImagerDenoiserOptix(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerDenoiserOptix"

    out = MessageField()

    enable = BoolField()

    layerSelection = DataStringField()
    layer_selection = layerSelection

    outputSuffix = DataStringField()
    output_suffix = outputSuffix

    blend = FloatField()

    clamp = BoolField()

    clampMin = FloatField()
    clamp_min = clampMin

    clampMax = FloatField()
    clamp_max = clampMax

    useFeatureAovs = BoolField()
    use_feature_aovs = useFeatureAovs
