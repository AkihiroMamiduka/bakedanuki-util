# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.scalar.numeric.bool import BoolField
from ..std.at.scalar.numeric.range.double import DoubleField
from ..std.at.scalar.numeric.range.float import FloatField
from ..std.at.scalar.numeric.range.long import LongField
from ..custom import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class HyperPositionPlugOperator(
    CompoundPlugOperator["HyperPositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "x"),
        ("positionY", "y"),
        ("isCollapsed", "isc"),
        ("isFreeform", "isf"),
        ("nodeVisualState", "nvs"),
        ("dependNode", "dn"),
    )

    positionX = FloatField(default_value=0.0)
    x = positionX

    positionY = FloatField(default_value=0.0)
    y = positionY

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    isFreeform = BoolField(default_value=False)
    isf = isFreeform

    nodeVisualState = LongField(default_value=0)
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class HyperPositionAttrOperator(
    CompoundAttrOperator[HyperPositionPlugOperator]
):
    __slots__ = ()

    positionX = FloatField(default_value=0.0)
    x = positionX

    positionY = FloatField(default_value=0.0)
    y = positionY

    isCollapsed = BoolField(default_value=False)
    isc = isCollapsed

    isFreeform = BoolField(default_value=False)
    isf = isFreeform

    nodeVisualState = LongField(default_value=0)
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class HyperPositionField(
    CompoundField[HyperPositionAttrOperator, HyperPositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = HyperPositionAttrOperator
    PLUG_CLS = HyperPositionPlugOperator


class ImagePositionPlugOperator(
    Double2CompoundBasePlugOperator["ImagePositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("imagePositionX", "ipx"),
        ("imagePositionY", "ipy"),
    )

    imagePositionX = DoubleField(default_value=0.0)
    ipx = imagePositionX

    imagePositionY = DoubleField(default_value=0.0)
    ipy = imagePositionY


class ImagePositionAttrOperator(
    Double2CompoundBaseAttrOperator[ImagePositionPlugOperator]
):
    __slots__ = ()

    imagePositionX = DoubleField(default_value=0.0)
    ipx = imagePositionX

    imagePositionY = DoubleField(default_value=0.0)
    ipy = imagePositionY


class ImagePositionField(
    Double2CompoundBaseField[
        ImagePositionAttrOperator, ImagePositionPlugOperator
    ]
):
    __slots__ = ()

    ATTR_CLS = ImagePositionAttrOperator
    PLUG_CLS = ImagePositionPlugOperator

    imagePositionX = DoubleField(default_value=0.0)
    ipx = imagePositionX

    imagePositionY = DoubleField(default_value=0.0)
    ipy = imagePositionY
