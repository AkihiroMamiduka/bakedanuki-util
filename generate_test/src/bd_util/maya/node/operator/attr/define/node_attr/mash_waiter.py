# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.dt.string import DataStringField
from ..std.dt.vector_array import DataVectorArrayField
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


class TranslateInPPPlugOperator(
    CompoundPlugOperator["TranslateInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inPositionPP", "inArray"),
        ("inScalePP", "inScPP"),
        ("inRotationPP", "inRotPP"),
        ("inIdPP", "inIdPP"),
        ("inVisibilityPP", "inVisPP"),
    )

    inPositionPP = DataVectorArrayField()
    inArray = inPositionPP

    inScalePP = DataVectorArrayField()
    inScPP = inScalePP

    inRotationPP = DataVectorArrayField()
    inRotPP = inRotationPP

    inIdPP = DataVectorArrayField()

    inVisibilityPP = DataVectorArrayField()
    inVisPP = inVisibilityPP


class TranslateInPPAttrOperator(
    CompoundAttrOperator[TranslateInPPPlugOperator]
):
    __slots__ = ()

    inPositionPP = DataVectorArrayField()
    inArray = inPositionPP

    inScalePP = DataVectorArrayField()
    inScPP = inScalePP

    inRotationPP = DataVectorArrayField()
    inRotPP = inRotationPP

    inIdPP = DataVectorArrayField()

    inVisibilityPP = DataVectorArrayField()
    inVisPP = inVisibilityPP


class TranslateInPPField(
    CompoundField[TranslateInPPAttrOperator, TranslateInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = TranslateInPPAttrOperator
    PLUG_CLS = TranslateInPPPlugOperator

    inPositionPP = DataVectorArrayField()
    inArray = inPositionPP

    inScalePP = DataVectorArrayField()
    inScPP = inScalePP

    inRotationPP = DataVectorArrayField()
    inRotPP = inRotationPP

    inIdPP = DataVectorArrayField()

    inVisibilityPP = DataVectorArrayField()
    inVisPP = inVisibilityPP


class CacheInPPPlugOperator(
    CompoundPlugOperator["CacheInPPAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("cacheInArrayPP", "cacheInArrayPP"),
        ("cacheRotationPP", "cacheRotationPP"),
        ("cacheScalePP", "cacheScalePP"),
        ("cacheIdPP", "cacheIdPP"),
        ("cacheVisibilityPP", "cacheVisibilityPP"),
    )

    cacheInArrayPP = DataVectorArrayField()

    cacheRotationPP = DataVectorArrayField()

    cacheScalePP = DataVectorArrayField()

    cacheIdPP = DataVectorArrayField()

    cacheVisibilityPP = DataVectorArrayField()


class CacheInPPAttrOperator(
    CompoundAttrOperator[CacheInPPPlugOperator]
):
    __slots__ = ()

    cacheInArrayPP = DataVectorArrayField()

    cacheRotationPP = DataVectorArrayField()

    cacheScalePP = DataVectorArrayField()

    cacheIdPP = DataVectorArrayField()

    cacheVisibilityPP = DataVectorArrayField()


class CacheInPPField(
    CompoundField[CacheInPPAttrOperator, CacheInPPPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CacheInPPAttrOperator
    PLUG_CLS = CacheInPPPlugOperator

    cacheInArrayPP = DataVectorArrayField()

    cacheRotationPP = DataVectorArrayField()

    cacheScalePP = DataVectorArrayField()

    cacheIdPP = DataVectorArrayField()

    cacheVisibilityPP = DataVectorArrayField()


class LabelColorPlugOperator(
    Float3CompoundBasePlugOperator["LabelColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("labelColorR", "labelColorr"),
        ("labelColorG", "labelColorg"),
        ("labelColorB", "labelColorb"),
    )

    labelColorR = FloatField()
    labelColorr = labelColorR

    labelColorG = FloatField()
    labelColorg = labelColorG

    labelColorB = FloatField()
    labelColorb = labelColorB


class LabelColorAttrOperator(
    Float3CompoundBaseAttrOperator[LabelColorPlugOperator]
):
    __slots__ = ()

    labelColorR = FloatField()
    labelColorr = labelColorR

    labelColorG = FloatField()
    labelColorg = labelColorG

    labelColorB = FloatField()
    labelColorb = labelColorB


class LabelColorField(
    Float3CompoundBaseField[LabelColorAttrOperator, LabelColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LabelColorAttrOperator
    PLUG_CLS = LabelColorPlugOperator

    labelColorR = FloatField()
    labelColorr = labelColorR

    labelColorG = FloatField()
    labelColorg = labelColorG

    labelColorB = FloatField()
    labelColorb = labelColorB
