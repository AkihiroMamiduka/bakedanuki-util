# coding: utf-8

from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class MainGainPlugOperator(
    Float3CompoundBasePlugOperator["MainGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mainGainR", "main_gainr"),
        ("mainGainG", "main_gaing"),
        ("mainGainB", "main_gainb"),
    )

    mainGainR = FloatField()
    main_gainr = mainGainR

    mainGainG = FloatField()
    main_gaing = mainGainG

    mainGainB = FloatField()
    main_gainb = mainGainB


class MainGainAttrOperator(
    Float3CompoundBaseAttrOperator[MainGainPlugOperator]
):
    __slots__ = ()

    mainGainR = FloatField()
    main_gainr = mainGainR

    mainGainG = FloatField()
    main_gaing = mainGainG

    mainGainB = FloatField()
    main_gainb = mainGainB


class MainGainField(
    Float3CompoundBaseField[MainGainAttrOperator, MainGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MainGainAttrOperator
    PLUG_CLS = MainGainPlugOperator

    mainGainR = FloatField()
    main_gainr = mainGainR

    mainGainG = FloatField()
    main_gaing = mainGainG

    mainGainB = FloatField()
    main_gainb = mainGainB


class MainOffsetPlugOperator(
    Float3CompoundBasePlugOperator["MainOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("mainOffsetR", "main_offsetr"),
        ("mainOffsetG", "main_offsetg"),
        ("mainOffsetB", "main_offsetb"),
    )

    mainOffsetR = FloatField()
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField()
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField()
    main_offsetb = mainOffsetB


class MainOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[MainOffsetPlugOperator]
):
    __slots__ = ()

    mainOffsetR = FloatField()
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField()
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField()
    main_offsetb = mainOffsetB


class MainOffsetField(
    Float3CompoundBaseField[MainOffsetAttrOperator, MainOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MainOffsetAttrOperator
    PLUG_CLS = MainOffsetPlugOperator

    mainOffsetR = FloatField()
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField()
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField()
    main_offsetb = mainOffsetB


class ShadowsGainPlugOperator(
    Float3CompoundBasePlugOperator["ShadowsGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowsGainR", "shadows_gainr"),
        ("shadowsGainG", "shadows_gaing"),
        ("shadowsGainB", "shadows_gainb"),
    )

    shadowsGainR = FloatField()
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField()
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField()
    shadows_gainb = shadowsGainB


class ShadowsGainAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowsGainPlugOperator]
):
    __slots__ = ()

    shadowsGainR = FloatField()
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField()
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField()
    shadows_gainb = shadowsGainB


class ShadowsGainField(
    Float3CompoundBaseField[ShadowsGainAttrOperator, ShadowsGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowsGainAttrOperator
    PLUG_CLS = ShadowsGainPlugOperator

    shadowsGainR = FloatField()
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField()
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField()
    shadows_gainb = shadowsGainB


class ShadowsOffsetPlugOperator(
    Float3CompoundBasePlugOperator["ShadowsOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("shadowsOffsetR", "shadows_offsetr"),
        ("shadowsOffsetG", "shadows_offsetg"),
        ("shadowsOffsetB", "shadows_offsetb"),
    )

    shadowsOffsetR = FloatField()
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField()
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField()
    shadows_offsetb = shadowsOffsetB


class ShadowsOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowsOffsetPlugOperator]
):
    __slots__ = ()

    shadowsOffsetR = FloatField()
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField()
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField()
    shadows_offsetb = shadowsOffsetB


class ShadowsOffsetField(
    Float3CompoundBaseField[ShadowsOffsetAttrOperator, ShadowsOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowsOffsetAttrOperator
    PLUG_CLS = ShadowsOffsetPlugOperator

    shadowsOffsetR = FloatField()
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField()
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField()
    shadows_offsetb = shadowsOffsetB


class MidtonesGainPlugOperator(
    Float3CompoundBasePlugOperator["MidtonesGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("midtonesGainR", "midtones_gainr"),
        ("midtonesGainG", "midtones_gaing"),
        ("midtonesGainB", "midtones_gainb"),
    )

    midtonesGainR = FloatField()
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField()
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField()
    midtones_gainb = midtonesGainB


class MidtonesGainAttrOperator(
    Float3CompoundBaseAttrOperator[MidtonesGainPlugOperator]
):
    __slots__ = ()

    midtonesGainR = FloatField()
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField()
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField()
    midtones_gainb = midtonesGainB


class MidtonesGainField(
    Float3CompoundBaseField[MidtonesGainAttrOperator, MidtonesGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MidtonesGainAttrOperator
    PLUG_CLS = MidtonesGainPlugOperator

    midtonesGainR = FloatField()
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField()
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField()
    midtones_gainb = midtonesGainB


class MidtonesOffsetPlugOperator(
    Float3CompoundBasePlugOperator["MidtonesOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("midtonesOffsetR", "midtones_offsetr"),
        ("midtonesOffsetG", "midtones_offsetg"),
        ("midtonesOffsetB", "midtones_offsetb"),
    )

    midtonesOffsetR = FloatField()
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField()
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField()
    midtones_offsetb = midtonesOffsetB


class MidtonesOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[MidtonesOffsetPlugOperator]
):
    __slots__ = ()

    midtonesOffsetR = FloatField()
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField()
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField()
    midtones_offsetb = midtonesOffsetB


class MidtonesOffsetField(
    Float3CompoundBaseField[MidtonesOffsetAttrOperator, MidtonesOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MidtonesOffsetAttrOperator
    PLUG_CLS = MidtonesOffsetPlugOperator

    midtonesOffsetR = FloatField()
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField()
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField()
    midtones_offsetb = midtonesOffsetB


class HighlightsGainPlugOperator(
    Float3CompoundBasePlugOperator["HighlightsGainAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("highlightsGainR", "highlights_gainr"),
        ("highlightsGainG", "highlights_gaing"),
        ("highlightsGainB", "highlights_gainb"),
    )

    highlightsGainR = FloatField()
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField()
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField()
    highlights_gainb = highlightsGainB


class HighlightsGainAttrOperator(
    Float3CompoundBaseAttrOperator[HighlightsGainPlugOperator]
):
    __slots__ = ()

    highlightsGainR = FloatField()
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField()
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField()
    highlights_gainb = highlightsGainB


class HighlightsGainField(
    Float3CompoundBaseField[HighlightsGainAttrOperator, HighlightsGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HighlightsGainAttrOperator
    PLUG_CLS = HighlightsGainPlugOperator

    highlightsGainR = FloatField()
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField()
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField()
    highlights_gainb = highlightsGainB


class HighlightsOffsetPlugOperator(
    Float3CompoundBasePlugOperator["HighlightsOffsetAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("highlightsOffsetR", "highlights_offsetr"),
        ("highlightsOffsetG", "highlights_offsetg"),
        ("highlightsOffsetB", "highlights_offsetb"),
    )

    highlightsOffsetR = FloatField()
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField()
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField()
    highlights_offsetb = highlightsOffsetB


class HighlightsOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[HighlightsOffsetPlugOperator]
):
    __slots__ = ()

    highlightsOffsetR = FloatField()
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField()
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField()
    highlights_offsetb = highlightsOffsetB


class HighlightsOffsetField(
    Float3CompoundBaseField[HighlightsOffsetAttrOperator, HighlightsOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HighlightsOffsetAttrOperator
    PLUG_CLS = HighlightsOffsetPlugOperator

    highlightsOffsetR = FloatField()
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField()
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField()
    highlights_offsetb = highlightsOffsetB
