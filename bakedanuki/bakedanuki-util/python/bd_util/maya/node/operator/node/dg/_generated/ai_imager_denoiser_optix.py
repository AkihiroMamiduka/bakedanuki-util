# coding: utf-8
from .._core import DG
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiImagerDenoiserOptix(DG):
    __slots__ = ()

    NODE_TYPE = "aiImagerDenoiserOptix"

    out = MessageField(writable=False)

    enable = BoolField(default_value=True)

    layerSelection = DataStringField()
    layer_selection = layerSelection

    outputSuffix = DataStringField()
    output_suffix = outputSuffix

    blend = FloatField(default_value=1.0, min_value=0.0, max_value=1.0, soft_min_value=0.0, soft_max_value=1.0)

    clamp = BoolField(default_value=False)

    clampMin = FloatField(default_value=0.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    clamp_min = clampMin

    clampMax = FloatField(default_value=1.0, min_value=0.0, soft_min_value=0.0, soft_max_value=1.0)
    clamp_max = clampMax

    useFeatureAovs = BoolField(default_value=True)
    use_feature_aovs = useFeatureAovs
