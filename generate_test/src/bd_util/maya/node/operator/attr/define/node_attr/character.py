# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..std.at.typed import TypedField
from ..std.dt.string import DataStringField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound._base import (
    Float3CompoundBaseAttrOperator,
    Float3CompoundBasePlugOperator,
    Float3CompoundBaseField,
)


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

    isHierarchicalNode = BoolField()
    ihn = isHierarchicalNode

    publishedNodeType = DataStringField()
    pntp = publishedNodeType


class PublishedNodeInfoAttrOperator(
    CompoundAttrOperator[PublishedNodeInfoPlugOperator]
):
    __slots__ = ()

    publishedNode = MessageField()
    pnod = publishedNode

    isHierarchicalNode = BoolField()
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

    channelSetColorR = FloatField()
    cscolr = channelSetColorR

    channelSetColorG = FloatField()
    cscolg = channelSetColorG

    channelSetColorB = FloatField()
    cscolb = channelSetColorB


class ChannelSetColorAttrOperator(
    Float3CompoundBaseAttrOperator[ChannelSetColorPlugOperator]
):
    __slots__ = ()

    channelSetColorR = FloatField()
    cscolr = channelSetColorR

    channelSetColorG = FloatField()
    cscolg = channelSetColorG

    channelSetColorB = FloatField()
    cscolb = channelSetColorB


class ChannelSetColorField(
    Float3CompoundBaseField[ChannelSetColorAttrOperator, ChannelSetColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ChannelSetColorAttrOperator
    PLUG_CLS = ChannelSetColorPlugOperator

    channelSetColorR = FloatField()
    cscolr = channelSetColorR

    channelSetColorG = FloatField()
    cscolg = channelSetColorG

    channelSetColorB = FloatField()
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

    clipEvaluate_Inmap = CompoundField()
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = CompoundField()
    ceo = clipEvaluate_Outmap


class ClipEvaluateAttrOperator(
    CompoundAttrOperator[ClipEvaluatePlugOperator]
):
    __slots__ = ()

    clipEvaluate_Hidden = TypedField()
    ceh = clipEvaluate_Hidden

    clipEvaluate_Raw = TypedField()
    cer = clipEvaluate_Raw

    clipEvaluate_Inmap = CompoundField()
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = CompoundField()
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

    clipEvaluate_Inmap = CompoundField()
    cei = clipEvaluate_Inmap

    clipEvaluate_Outmap = CompoundField()
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

    clipStatePercentEval_Inmap = CompoundField()
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = CompoundField()
    cspeo = clipStatePercentEval_Outmap


class ClipStatePercentEvalAttrOperator(
    CompoundAttrOperator[ClipStatePercentEvalPlugOperator]
):
    __slots__ = ()

    clipStatePercentEval_Hidden = TypedField()
    cspeh = clipStatePercentEval_Hidden

    clipStatePercentEval_Raw = TypedField()
    csper = clipStatePercentEval_Raw

    clipStatePercentEval_Inmap = CompoundField()
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = CompoundField()
    cspeo = clipStatePercentEval_Outmap


class ClipStatePercentEvalField(
    CompoundField[ClipStatePercentEvalAttrOperator, ClipStatePercentEvalPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ClipStatePercentEvalAttrOperator
    PLUG_CLS = ClipStatePercentEvalPlugOperator

    clipStatePercentEval_Hidden = TypedField()
    cspeh = clipStatePercentEval_Hidden

    clipStatePercentEval_Raw = TypedField()
    csper = clipStatePercentEval_Raw

    clipStatePercentEval_Inmap = CompoundField()
    cspei = clipStatePercentEval_Inmap

    clipStatePercentEval_Outmap = CompoundField()
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

    translationOffsetIndexX = LongField()
    tox = translationOffsetIndexX

    translationOffsetY = LongField()
    toy = translationOffsetY

    translationOffsetZ = LongField()
    toz = translationOffsetZ


class TranslationOffsetIndicesAttrOperator(
    CompoundAttrOperator[TranslationOffsetIndicesPlugOperator]
):
    __slots__ = ()

    translationOffsetIndexX = LongField()
    tox = translationOffsetIndexX

    translationOffsetY = LongField()
    toy = translationOffsetY

    translationOffsetZ = LongField()
    toz = translationOffsetZ


class TranslationOffsetIndicesField(
    CompoundField[TranslationOffsetIndicesAttrOperator, TranslationOffsetIndicesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslationOffsetIndicesAttrOperator
    PLUG_CLS = TranslationOffsetIndicesPlugOperator

    translationOffsetIndexX = LongField()
    tox = translationOffsetIndexX

    translationOffsetY = LongField()
    toy = translationOffsetY

    translationOffsetZ = LongField()
    toz = translationOffsetZ
