# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..std.at.scalar.numeric.range.short import ShortField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


class ClipEvaluate_clipEvaluate_InmapPlugOperator(
    CompoundPlugOperator["ClipEvaluate_clipEvaluate_InmapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipEvaluate_InmapTo", "ceit"),
        ("clipEvaluate_InmapFrom", "ceif"),
    )

    clipEvaluate_InmapTo = ShortField()
    ceit = clipEvaluate_InmapTo

    clipEvaluate_InmapFrom = ShortField()
    ceif = clipEvaluate_InmapFrom


class ClipEvaluate_clipEvaluate_InmapAttrOperator(
    CompoundAttrOperator[ClipEvaluate_clipEvaluate_InmapPlugOperator]
):
    __slots__ = ()

    clipEvaluate_InmapTo = ShortField()
    ceit = clipEvaluate_InmapTo

    clipEvaluate_InmapFrom = ShortField()
    ceif = clipEvaluate_InmapFrom


class ClipEvaluate_clipEvaluate_InmapField(
    CompoundField[
        ClipEvaluate_clipEvaluate_InmapAttrOperator,
        ClipEvaluate_clipEvaluate_InmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipEvaluate_clipEvaluate_InmapAttrOperator
    PLUG_CLS = ClipEvaluate_clipEvaluate_InmapPlugOperator


class ClipEvaluate_clipEvaluate_OutmapPlugOperator(
    CompoundPlugOperator["ClipEvaluate_clipEvaluate_OutmapAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipEvaluate_OutmapTo", "ceot"),
        ("clipEvaluate_OutmapFrom", "ceof"),
    )

    clipEvaluate_OutmapTo = ShortField()
    ceot = clipEvaluate_OutmapTo

    clipEvaluate_OutmapFrom = ShortField()
    ceof = clipEvaluate_OutmapFrom


class ClipEvaluate_clipEvaluate_OutmapAttrOperator(
    CompoundAttrOperator[ClipEvaluate_clipEvaluate_OutmapPlugOperator]
):
    __slots__ = ()

    clipEvaluate_OutmapTo = ShortField()
    ceot = clipEvaluate_OutmapTo

    clipEvaluate_OutmapFrom = ShortField()
    ceof = clipEvaluate_OutmapFrom


class ClipEvaluate_clipEvaluate_OutmapField(
    CompoundField[
        ClipEvaluate_clipEvaluate_OutmapAttrOperator,
        ClipEvaluate_clipEvaluate_OutmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipEvaluate_clipEvaluate_OutmapAttrOperator
    PLUG_CLS = ClipEvaluate_clipEvaluate_OutmapPlugOperator


class ClipStatePercentEval_clipStatePercentEval_InmapPlugOperator(
    CompoundPlugOperator[
        "ClipStatePercentEval_clipStatePercentEval_InmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipStatePercentEval_InmapTo", "cspeit"),
        ("clipStatePercentEval_InmapFrom", "cspeif"),
    )

    clipStatePercentEval_InmapTo = ShortField()
    cspeit = clipStatePercentEval_InmapTo

    clipStatePercentEval_InmapFrom = ShortField()
    cspeif = clipStatePercentEval_InmapFrom


class ClipStatePercentEval_clipStatePercentEval_InmapAttrOperator(
    CompoundAttrOperator[
        ClipStatePercentEval_clipStatePercentEval_InmapPlugOperator
    ]
):
    __slots__ = ()

    clipStatePercentEval_InmapTo = ShortField()
    cspeit = clipStatePercentEval_InmapTo

    clipStatePercentEval_InmapFrom = ShortField()
    cspeif = clipStatePercentEval_InmapFrom


class ClipStatePercentEval_clipStatePercentEval_InmapField(
    CompoundField[
        ClipStatePercentEval_clipStatePercentEval_InmapAttrOperator,
        ClipStatePercentEval_clipStatePercentEval_InmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipStatePercentEval_clipStatePercentEval_InmapAttrOperator
    PLUG_CLS = ClipStatePercentEval_clipStatePercentEval_InmapPlugOperator


class ClipStatePercentEval_clipStatePercentEval_OutmapPlugOperator(
    CompoundPlugOperator[
        "ClipStatePercentEval_clipStatePercentEval_OutmapAttrOperator"
    ]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipStatePercentEval_OutmapTo", "cspeot"),
        ("clipStatePercentEval_OutmapFrom", "cspeof"),
    )

    clipStatePercentEval_OutmapTo = ShortField()
    cspeot = clipStatePercentEval_OutmapTo

    clipStatePercentEval_OutmapFrom = ShortField()
    cspeof = clipStatePercentEval_OutmapFrom


class ClipStatePercentEval_clipStatePercentEval_OutmapAttrOperator(
    CompoundAttrOperator[
        ClipStatePercentEval_clipStatePercentEval_OutmapPlugOperator
    ]
):
    __slots__ = ()

    clipStatePercentEval_OutmapTo = ShortField()
    cspeot = clipStatePercentEval_OutmapTo

    clipStatePercentEval_OutmapFrom = ShortField()
    cspeof = clipStatePercentEval_OutmapFrom


class ClipStatePercentEval_clipStatePercentEval_OutmapField(
    CompoundField[
        ClipStatePercentEval_clipStatePercentEval_OutmapAttrOperator,
        ClipStatePercentEval_clipStatePercentEval_OutmapPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipStatePercentEval_clipStatePercentEval_OutmapAttrOperator
    PLUG_CLS = ClipStatePercentEval_clipStatePercentEval_OutmapPlugOperator


class PublishedNodeInfoPlugOperator(
    CompoundPlugOperator["PublishedNodeInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("publishedNode", "pnod"),
        ("isHierarchicalNode", "ihn"),
        ("publishedNodeType", "pntp"),
    )

    publishedNode = MessageField()
    pnod = publishedNode

    isHierarchicalNode = BoolField(default_value=False)
    ihn = isHierarchicalNode

    publishedNodeType = DataStringField()
    pntp = publishedNodeType


class PublishedNodeInfoAttrOperator(
    CompoundAttrOperator[PublishedNodeInfoPlugOperator]
):
    __slots__ = ()

    publishedNode = MessageField()
    pnod = publishedNode

    isHierarchicalNode = BoolField(default_value=False)
    ihn = isHierarchicalNode

    publishedNodeType = DataStringField()
    pntp = publishedNodeType


class PublishedNodeInfoField(
    CompoundField[PublishedNodeInfoAttrOperator, PublishedNodeInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PublishedNodeInfoAttrOperator
    PLUG_CLS = PublishedNodeInfoPlugOperator


class ChannelSetColorPlugOperator(
    Float3CompoundBasePlugOperator["ChannelSetColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("channelSetColorR", "cscolr"),
        ("channelSetColorG", "cscolg"),
        ("channelSetColorB", "cscolb"),
    )

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class ChannelSetColorAttrOperator(
    Float3CompoundBaseAttrOperator[ChannelSetColorPlugOperator]
):
    __slots__ = ()

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class ChannelSetColorField(
    Float3CompoundBaseField[
        ChannelSetColorAttrOperator, ChannelSetColorPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ChannelSetColorAttrOperator
    PLUG_CLS = ChannelSetColorPlugOperator

    channelSetColorR = FloatField(default_value=0.5)
    cscolr = channelSetColorR

    channelSetColorG = FloatField(default_value=0.5)
    cscolg = channelSetColorG

    channelSetColorB = FloatField(default_value=0.5)
    cscolb = channelSetColorB


class ClipEvaluatePlugOperator(
    CompoundPlugOperator["ClipEvaluateAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipEvaluate_Hidden", "ceh"),
        ("clipEvaluate_Raw", "cer"),
        ("clipEvaluate_Inmap", "cei"),
        ("clipEvaluate_Outmap", "ceo"),
    )

    clipEvaluate_Hidden = TypedField()
    ceh = clipEvaluate_Hidden

    clipEvaluate_Raw = TypedField()
    cer = clipEvaluate_Raw

    clipEvaluate_Inmap = ClipEvaluate_clipEvaluate_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = ClipEvaluate_clipEvaluate_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    ceo = clipEvaluate_Outmap


class ClipEvaluateAttrOperator(CompoundAttrOperator[ClipEvaluatePlugOperator]):
    __slots__ = ()

    clipEvaluate_Hidden = TypedField()
    ceh = clipEvaluate_Hidden

    clipEvaluate_Raw = TypedField()
    cer = clipEvaluate_Raw

    clipEvaluate_Inmap = ClipEvaluate_clipEvaluate_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = ClipEvaluate_clipEvaluate_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    ceo = clipEvaluate_Outmap


class ClipEvaluateField(
    CompoundField[ClipEvaluateAttrOperator, ClipEvaluatePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipEvaluateAttrOperator
    PLUG_CLS = ClipEvaluatePlugOperator

    clipEvaluate_Hidden = TypedField()
    ceh = clipEvaluate_Hidden

    clipEvaluate_Raw = TypedField()
    cer = clipEvaluate_Raw

    clipEvaluate_Inmap = ClipEvaluate_clipEvaluate_InmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = ClipEvaluate_clipEvaluate_OutmapField(
        multi=True, default_value=(0.0, 0.0)
    )
    ceo = clipEvaluate_Outmap


class ClipStatePercentEvalPlugOperator(
    CompoundPlugOperator["ClipStatePercentEvalAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("clipStatePercentEval_Hidden", "cspeh"),
        ("clipStatePercentEval_Raw", "csper"),
        ("clipStatePercentEval_Inmap", "cspei"),
        ("clipStatePercentEval_Outmap", "cspeo"),
    )

    clipStatePercentEval_Hidden = TypedField()
    cspeh = clipStatePercentEval_Hidden

    clipStatePercentEval_Raw = TypedField()
    csper = clipStatePercentEval_Raw

    clipStatePercentEval_Inmap = (
        ClipStatePercentEval_clipStatePercentEval_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = (
        ClipStatePercentEval_clipStatePercentEval_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspeo = clipStatePercentEval_Outmap


class ClipStatePercentEvalAttrOperator(
    CompoundAttrOperator[ClipStatePercentEvalPlugOperator]
):
    __slots__ = ()

    clipStatePercentEval_Hidden = TypedField()
    cspeh = clipStatePercentEval_Hidden

    clipStatePercentEval_Raw = TypedField()
    csper = clipStatePercentEval_Raw

    clipStatePercentEval_Inmap = (
        ClipStatePercentEval_clipStatePercentEval_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = (
        ClipStatePercentEval_clipStatePercentEval_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspeo = clipStatePercentEval_Outmap


class ClipStatePercentEvalField(
    CompoundField[
        ClipStatePercentEvalAttrOperator, ClipStatePercentEvalPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ClipStatePercentEvalAttrOperator
    PLUG_CLS = ClipStatePercentEvalPlugOperator

    clipStatePercentEval_Hidden = TypedField()
    cspeh = clipStatePercentEval_Hidden

    clipStatePercentEval_Raw = TypedField()
    csper = clipStatePercentEval_Raw

    clipStatePercentEval_Inmap = (
        ClipStatePercentEval_clipStatePercentEval_InmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = (
        ClipStatePercentEval_clipStatePercentEval_OutmapField(
            multi=True, default_value=(0.0, 0.0)
        )
    )
    cspeo = clipStatePercentEval_Outmap


class TranslationOffsetIndicesPlugOperator(
    CompoundPlugOperator["TranslationOffsetIndicesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("translationOffsetIndexX", "tox"),
        ("translationOffsetY", "toy"),
        ("translationOffsetZ", "toz"),
    )

    translationOffsetIndexX = LongField(default_value=-1)
    tox = translationOffsetIndexX

    translationOffsetY = LongField(default_value=-1)
    toy = translationOffsetY

    translationOffsetZ = LongField(default_value=-1)
    toz = translationOffsetZ


class TranslationOffsetIndicesAttrOperator(
    CompoundAttrOperator[TranslationOffsetIndicesPlugOperator]
):
    __slots__ = ()

    translationOffsetIndexX = LongField(default_value=-1)
    tox = translationOffsetIndexX

    translationOffsetY = LongField(default_value=-1)
    toy = translationOffsetY

    translationOffsetZ = LongField(default_value=-1)
    toz = translationOffsetZ


class TranslationOffsetIndicesField(
    CompoundField[
        TranslationOffsetIndicesAttrOperator,
        TranslationOffsetIndicesPlugOperator,
    ]
):
    __slots__ = ()

    ATTR_CLS = TranslationOffsetIndicesAttrOperator
    PLUG_CLS = TranslationOffsetIndicesPlugOperator

    translationOffsetIndexX = LongField(default_value=-1)
    tox = translationOffsetIndexX

    translationOffsetY = LongField(default_value=-1)
    toy = translationOffsetY

    translationOffsetZ = LongField(default_value=-1)
    toz = translationOffsetZ
