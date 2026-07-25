# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.float import FloatField
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
    Float3CompoundBaseField[ChannelSetColorAttrOperator, ChannelSetColorPlugOperator]
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


class MinColorPlugOperator(
    Float3CompoundBasePlugOperator["MinColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("minColorR", "lr"),
        ("minColorG", "lg"),
        ("minColorB", "lb"),
    )

    minColorR = FloatField(default_value=0.0)
    lr = minColorR

    minColorG = FloatField(default_value=0.0)
    lg = minColorG

    minColorB = FloatField(default_value=0.0)
    lb = minColorB


class MinColorAttrOperator(
    Float3CompoundBaseAttrOperator[MinColorPlugOperator]
):
    __slots__ = ()

    minColorR = FloatField(default_value=0.0)
    lr = minColorR

    minColorG = FloatField(default_value=0.0)
    lg = minColorG

    minColorB = FloatField(default_value=0.0)
    lb = minColorB


class MinColorField(
    Float3CompoundBaseField[MinColorAttrOperator, MinColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MinColorAttrOperator
    PLUG_CLS = MinColorPlugOperator

    minColorR = FloatField(default_value=0.0)
    lr = minColorR

    minColorG = FloatField(default_value=0.0)
    lg = minColorG

    minColorB = FloatField(default_value=0.0)
    lb = minColorB


class MaxColorPlugOperator(
    Float3CompoundBasePlugOperator["MaxColorAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("maxColorR", "hr"),
        ("maxColorG", "hg"),
        ("maxColorB", "hb"),
    )

    maxColorR = FloatField(default_value=0.0)
    hr = maxColorR

    maxColorG = FloatField(default_value=0.0)
    hg = maxColorG

    maxColorB = FloatField(default_value=0.0)
    hb = maxColorB


class MaxColorAttrOperator(
    Float3CompoundBaseAttrOperator[MaxColorPlugOperator]
):
    __slots__ = ()

    maxColorR = FloatField(default_value=0.0)
    hr = maxColorR

    maxColorG = FloatField(default_value=0.0)
    hg = maxColorG

    maxColorB = FloatField(default_value=0.0)
    hb = maxColorB


class MaxColorField(
    Float3CompoundBaseField[MaxColorAttrOperator, MaxColorPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MaxColorAttrOperator
    PLUG_CLS = MaxColorPlugOperator

    maxColorR = FloatField(default_value=0.0)
    hr = maxColorR

    maxColorG = FloatField(default_value=0.0)
    hg = maxColorG

    maxColorB = FloatField(default_value=0.0)
    hb = maxColorB
