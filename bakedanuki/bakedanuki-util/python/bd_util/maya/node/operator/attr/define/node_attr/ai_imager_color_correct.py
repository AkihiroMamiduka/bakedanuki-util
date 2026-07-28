# coding: utf-8

from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import (
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

    mainGainR = FloatField(default_value=1.0)
    main_gainr = mainGainR

    mainGainG = FloatField(default_value=1.0)
    main_gaing = mainGainG

    mainGainB = FloatField(default_value=1.0)
    main_gainb = mainGainB


class MainGainAttrOperator(
    Float3CompoundBaseAttrOperator[MainGainPlugOperator]
):
    __slots__ = ()

    mainGainR = FloatField(default_value=1.0)
    main_gainr = mainGainR

    mainGainG = FloatField(default_value=1.0)
    main_gaing = mainGainG

    mainGainB = FloatField(default_value=1.0)
    main_gainb = mainGainB


class MainGainField(
    Float3CompoundBaseField[MainGainAttrOperator, MainGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MainGainAttrOperator
    PLUG_CLS = MainGainPlugOperator

    mainGainR = FloatField(default_value=1.0)
    main_gainr = mainGainR

    mainGainG = FloatField(default_value=1.0)
    main_gaing = mainGainG

    mainGainB = FloatField(default_value=1.0)
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

    mainOffsetR = FloatField(default_value=0.0)
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField(default_value=0.0)
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField(default_value=0.0)
    main_offsetb = mainOffsetB


class MainOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[MainOffsetPlugOperator]
):
    __slots__ = ()

    mainOffsetR = FloatField(default_value=0.0)
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField(default_value=0.0)
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField(default_value=0.0)
    main_offsetb = mainOffsetB


class MainOffsetField(
    Float3CompoundBaseField[MainOffsetAttrOperator, MainOffsetPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MainOffsetAttrOperator
    PLUG_CLS = MainOffsetPlugOperator

    mainOffsetR = FloatField(default_value=0.0)
    main_offsetr = mainOffsetR

    mainOffsetG = FloatField(default_value=0.0)
    main_offsetg = mainOffsetG

    mainOffsetB = FloatField(default_value=0.0)
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

    shadowsGainR = FloatField(default_value=1.0)
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField(default_value=1.0)
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField(default_value=1.0)
    shadows_gainb = shadowsGainB


class ShadowsGainAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowsGainPlugOperator]
):
    __slots__ = ()

    shadowsGainR = FloatField(default_value=1.0)
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField(default_value=1.0)
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField(default_value=1.0)
    shadows_gainb = shadowsGainB


class ShadowsGainField(
    Float3CompoundBaseField[ShadowsGainAttrOperator, ShadowsGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ShadowsGainAttrOperator
    PLUG_CLS = ShadowsGainPlugOperator

    shadowsGainR = FloatField(default_value=1.0)
    shadows_gainr = shadowsGainR

    shadowsGainG = FloatField(default_value=1.0)
    shadows_gaing = shadowsGainG

    shadowsGainB = FloatField(default_value=1.0)
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

    shadowsOffsetR = FloatField(default_value=0.0)
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField(default_value=0.0)
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField(default_value=0.0)
    shadows_offsetb = shadowsOffsetB


class ShadowsOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[ShadowsOffsetPlugOperator]
):
    __slots__ = ()

    shadowsOffsetR = FloatField(default_value=0.0)
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField(default_value=0.0)
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField(default_value=0.0)
    shadows_offsetb = shadowsOffsetB


class ShadowsOffsetField(
    Float3CompoundBaseField[
        ShadowsOffsetAttrOperator, ShadowsOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ShadowsOffsetAttrOperator
    PLUG_CLS = ShadowsOffsetPlugOperator

    shadowsOffsetR = FloatField(default_value=0.0)
    shadows_offsetr = shadowsOffsetR

    shadowsOffsetG = FloatField(default_value=0.0)
    shadows_offsetg = shadowsOffsetG

    shadowsOffsetB = FloatField(default_value=0.0)
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

    midtonesGainR = FloatField(default_value=1.0)
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField(default_value=1.0)
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField(default_value=1.0)
    midtones_gainb = midtonesGainB


class MidtonesGainAttrOperator(
    Float3CompoundBaseAttrOperator[MidtonesGainPlugOperator]
):
    __slots__ = ()

    midtonesGainR = FloatField(default_value=1.0)
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField(default_value=1.0)
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField(default_value=1.0)
    midtones_gainb = midtonesGainB


class MidtonesGainField(
    Float3CompoundBaseField[MidtonesGainAttrOperator, MidtonesGainPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MidtonesGainAttrOperator
    PLUG_CLS = MidtonesGainPlugOperator

    midtonesGainR = FloatField(default_value=1.0)
    midtones_gainr = midtonesGainR

    midtonesGainG = FloatField(default_value=1.0)
    midtones_gaing = midtonesGainG

    midtonesGainB = FloatField(default_value=1.0)
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

    midtonesOffsetR = FloatField(default_value=0.0)
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField(default_value=0.0)
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField(default_value=0.0)
    midtones_offsetb = midtonesOffsetB


class MidtonesOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[MidtonesOffsetPlugOperator]
):
    __slots__ = ()

    midtonesOffsetR = FloatField(default_value=0.0)
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField(default_value=0.0)
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField(default_value=0.0)
    midtones_offsetb = midtonesOffsetB


class MidtonesOffsetField(
    Float3CompoundBaseField[
        MidtonesOffsetAttrOperator, MidtonesOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = MidtonesOffsetAttrOperator
    PLUG_CLS = MidtonesOffsetPlugOperator

    midtonesOffsetR = FloatField(default_value=0.0)
    midtones_offsetr = midtonesOffsetR

    midtonesOffsetG = FloatField(default_value=0.0)
    midtones_offsetg = midtonesOffsetG

    midtonesOffsetB = FloatField(default_value=0.0)
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

    highlightsGainR = FloatField(default_value=1.0)
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField(default_value=1.0)
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField(default_value=1.0)
    highlights_gainb = highlightsGainB


class HighlightsGainAttrOperator(
    Float3CompoundBaseAttrOperator[HighlightsGainPlugOperator]
):
    __slots__ = ()

    highlightsGainR = FloatField(default_value=1.0)
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField(default_value=1.0)
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField(default_value=1.0)
    highlights_gainb = highlightsGainB


class HighlightsGainField(
    Float3CompoundBaseField[
        HighlightsGainAttrOperator, HighlightsGainPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HighlightsGainAttrOperator
    PLUG_CLS = HighlightsGainPlugOperator

    highlightsGainR = FloatField(default_value=1.0)
    highlights_gainr = highlightsGainR

    highlightsGainG = FloatField(default_value=1.0)
    highlights_gaing = highlightsGainG

    highlightsGainB = FloatField(default_value=1.0)
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

    highlightsOffsetR = FloatField(default_value=0.0)
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField(default_value=0.0)
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField(default_value=0.0)
    highlights_offsetb = highlightsOffsetB


class HighlightsOffsetAttrOperator(
    Float3CompoundBaseAttrOperator[HighlightsOffsetPlugOperator]
):
    __slots__ = ()

    highlightsOffsetR = FloatField(default_value=0.0)
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField(default_value=0.0)
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField(default_value=0.0)
    highlights_offsetb = highlightsOffsetB


class HighlightsOffsetField(
    Float3CompoundBaseField[
        HighlightsOffsetAttrOperator, HighlightsOffsetPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = HighlightsOffsetAttrOperator
    PLUG_CLS = HighlightsOffsetPlugOperator

    highlightsOffsetR = FloatField(default_value=0.0)
    highlights_offsetr = highlightsOffsetR

    highlightsOffsetG = FloatField(default_value=0.0)
    highlights_offsetg = highlightsOffsetG

    highlightsOffsetB = FloatField(default_value=0.0)
    highlights_offsetb = highlightsOffsetB
