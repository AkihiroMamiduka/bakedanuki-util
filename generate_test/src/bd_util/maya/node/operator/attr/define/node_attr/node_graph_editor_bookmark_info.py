# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
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

    viewXL = DoubleField()
    xl = viewXL

    viewYL = DoubleField()
    yl = viewYL


class ViewRectLowAttrOperator(
    Double2CompoundBaseAttrOperator[ViewRectLowPlugOperator]
):
    __slots__ = ()

    viewXL = DoubleField()
    xl = viewXL

    viewYL = DoubleField()
    yl = viewYL


class ViewRectLowField(
    Double2CompoundBaseField[ViewRectLowAttrOperator, ViewRectLowPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewRectLowAttrOperator
    PLUG_CLS = ViewRectLowPlugOperator

    viewXL = DoubleField()
    xl = viewXL

    viewYL = DoubleField()
    yl = viewYL


class ViewRectHighPlugOperator(
    Double2CompoundBasePlugOperator["ViewRectHighAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("viewXH", "xh"),
        ("viewYH", "yh"),
    )

    viewXH = DoubleField()
    xh = viewXH

    viewYH = DoubleField()
    yh = viewYH


class ViewRectHighAttrOperator(
    Double2CompoundBaseAttrOperator[ViewRectHighPlugOperator]
):
    __slots__ = ()

    viewXH = DoubleField()
    xh = viewXH

    viewYH = DoubleField()
    yh = viewYH


class ViewRectHighField(
    Double2CompoundBaseField[ViewRectHighAttrOperator, ViewRectHighPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewRectHighAttrOperator
    PLUG_CLS = ViewRectHighPlugOperator

    viewXH = DoubleField()
    xh = viewXH

    viewYH = DoubleField()
    yh = viewYH


class NodeInfoPlugOperator(
    CompoundPlugOperator["NodeInfoAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "x"),
        ("positionY", "y"),
        ("nodeVisualState", "nvs"),
        ("dependNode", "dn"),
    )

    positionX = FloatField()
    x = positionX

    positionY = FloatField()
    y = positionY

    nodeVisualState = LongField()
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class NodeInfoAttrOperator(
    CompoundAttrOperator[NodeInfoPlugOperator]
):
    __slots__ = ()

    positionX = FloatField()
    x = positionX

    positionY = FloatField()
    y = positionY

    nodeVisualState = LongField()
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class NodeInfoField(
    CompoundField[NodeInfoAttrOperator, NodeInfoPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NodeInfoAttrOperator
    PLUG_CLS = NodeInfoPlugOperator
