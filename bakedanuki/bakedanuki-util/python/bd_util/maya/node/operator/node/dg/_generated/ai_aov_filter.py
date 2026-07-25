# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.float import FloatField
from ....attr.define.std.dt.string import DataStringField


class DomainEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    FIRST_HIT = 0
    ALL_HITS = 1


class DomainEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    FIRST_HIT = 0
    ALL_HITS = 1

    NAME_MAP = {
        FIRST_HIT: "first_hit",
        ALL_HITS: "all_hits",
    }


class DomainEnumField(
    EnumField[DomainEnumAttrOperator, DomainEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = DomainEnumAttrOperator
    PLUG_CLS = DomainEnumPlugOperator


class FilterWeightsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACKMAN_HARRIS = 0
    BOX = 1
    CATROM = 2
    GAUSSIAN = 3
    MITNET = 4
    SINC = 5
    TRIANGLE = 6


class FilterWeightsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLACKMAN_HARRIS = 0
    BOX = 1
    CATROM = 2
    GAUSSIAN = 3
    MITNET = 4
    SINC = 5
    TRIANGLE = 6

    NAME_MAP = {
        BLACKMAN_HARRIS: "blackman_harris",
        BOX: "box",
        CATROM: "catrom",
        GAUSSIAN: "gaussian",
        MITNET: "mitnet",
        SINC: "sinc",
        TRIANGLE: "triangle",
    }


class FilterWeightsEnumField(
    EnumField[FilterWeightsEnumAttrOperator, FilterWeightsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = FilterWeightsEnumAttrOperator
    PLUG_CLS = FilterWeightsEnumPlugOperator


class AiFilterWeightsEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    BLACKMAN_HARRIS = 0
    BOX = 1
    CATROM = 2
    GAUSSIAN = 3
    MITNET = 4
    SINC = 5
    TRIANGLE = 6


class AiFilterWeightsEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    BLACKMAN_HARRIS = 0
    BOX = 1
    CATROM = 2
    GAUSSIAN = 3
    MITNET = 4
    SINC = 5
    TRIANGLE = 6

    NAME_MAP = {
        BLACKMAN_HARRIS: "blackman_harris",
        BOX: "box",
        CATROM: "catrom",
        GAUSSIAN: "gaussian",
        MITNET: "mitnet",
        SINC: "sinc",
        TRIANGLE: "triangle",
    }


class AiFilterWeightsEnumField(
    EnumField[AiFilterWeightsEnumAttrOperator, AiFilterWeightsEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = AiFilterWeightsEnumAttrOperator
    PLUG_CLS = AiFilterWeightsEnumPlugOperator


class _GeneratedAiAOVFilter(DG):
    __slots__ = ()

    NODE_TYPE = "aiAOVFilter"

    aiTranslator = DataStringField()
    ai_translator = aiTranslator

    aiUserOptions = DataStringField(category="arnold")
    ai_user_options = aiUserOptions

    width = FloatField(default_value=2.0, category="arnold")

    domain = DomainEnumField(default_value=0, category="arnold")

    scalarMode = BoolField(default_value=False, category="arnold")
    scalar_mode = scalarMode

    filterWeights = FilterWeightsEnumField(default_value=1, category="arnold")
    filter_weights = filterWeights

    minimum = FloatField(default_value=0.0, category="arnold")

    maximum = FloatField(default_value=1.0, category="arnold")

    aiWidth = FloatField(default_value=2.0, category="arnold")
    ai_width = aiWidth

    aiFilterWeights = AiFilterWeightsEnumField(default_value=1, category="arnold")
    ai_filter_weights = aiFilterWeights
