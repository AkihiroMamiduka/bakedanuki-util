# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..custom import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class ViewRectLowPlugOperator(
    Double2CompoundBasePlugOperator["ViewRectLowAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("viewXL", "xl"),
        ("viewYL", "yl"),
    )

    viewXL = DoubleField(default_value=0.0)
    xl = viewXL

    viewYL = DoubleField(default_value=0.0)
    yl = viewYL


class ViewRectLowAttrOperator(
    Double2CompoundBaseAttrOperator[ViewRectLowPlugOperator]
):
    __slots__ = ()

    viewXL = DoubleField(default_value=0.0)
    xl = viewXL

    viewYL = DoubleField(default_value=0.0)
    yl = viewYL


class ViewRectLowField(
    Double2CompoundBaseField[ViewRectLowAttrOperator, ViewRectLowPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewRectLowAttrOperator
    PLUG_CLS = ViewRectLowPlugOperator

    viewXL = DoubleField(default_value=0.0)
    xl = viewXL

    viewYL = DoubleField(default_value=0.0)
    yl = viewYL


class ViewRectHighPlugOperator(
    Double2CompoundBasePlugOperator["ViewRectHighAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("viewXH", "xh"),
        ("viewYH", "yh"),
    )

    viewXH = DoubleField(default_value=0.0)
    xh = viewXH

    viewYH = DoubleField(default_value=0.0)
    yh = viewYH


class ViewRectHighAttrOperator(
    Double2CompoundBaseAttrOperator[ViewRectHighPlugOperator]
):
    __slots__ = ()

    viewXH = DoubleField(default_value=0.0)
    xh = viewXH

    viewYH = DoubleField(default_value=0.0)
    yh = viewYH


class ViewRectHighField(
    Double2CompoundBaseField[
        ViewRectHighAttrOperator, ViewRectHighPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ViewRectHighAttrOperator
    PLUG_CLS = ViewRectHighPlugOperator

    viewXH = DoubleField(default_value=0.0)
    xh = viewXH

    viewYH = DoubleField(default_value=0.0)
    yh = viewYH


class NodeInfoPlugOperator(CompoundPlugOperator["NodeInfoAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "x"),
        ("positionY", "y"),
        ("nodeVisualState", "nvs"),
        ("dependNode", "dn"),
    )

    positionX = FloatField(default_value=0.0)
    x = positionX

    positionY = FloatField(default_value=0.0)
    y = positionY

    nodeVisualState = LongField(default_value=0)
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class NodeInfoAttrOperator(CompoundAttrOperator[NodeInfoPlugOperator]):
    __slots__ = ()

    positionX = FloatField(default_value=0.0)
    x = positionX

    positionY = FloatField(default_value=0.0)
    y = positionY

    nodeVisualState = LongField(default_value=0)
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class NodeInfoField(CompoundField[NodeInfoAttrOperator, NodeInfoPlugOperator]):
    __slots__ = ()

    ATTR_CLS = NodeInfoAttrOperator
    PLUG_CLS = NodeInfoPlugOperator
