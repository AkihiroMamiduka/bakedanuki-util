# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.numeric_scalar_range.long import LongField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
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

    positionX = FloatField()
    x = positionX

    positionY = FloatField()
    y = positionY

    isCollapsed = BoolField()
    isc = isCollapsed

    isFreeform = BoolField()
    isf = isFreeform

    nodeVisualState = LongField()
    nvs = nodeVisualState

    dependNode = MessageField()
    dn = dependNode


class HyperPositionAttrOperator(
    CompoundAttrOperator[HyperPositionPlugOperator]
):
    __slots__ = ()

    positionX = FloatField()
    x = positionX

    positionY = FloatField()
    y = positionY

    isCollapsed = BoolField()
    isc = isCollapsed

    isFreeform = BoolField()
    isf = isFreeform

    nodeVisualState = LongField()
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

    imagePositionX = DoubleField()
    ipx = imagePositionX

    imagePositionY = DoubleField()
    ipy = imagePositionY


class ImagePositionAttrOperator(
    Double2CompoundBaseAttrOperator[ImagePositionPlugOperator]
):
    __slots__ = ()

    imagePositionX = DoubleField()
    ipx = imagePositionX

    imagePositionY = DoubleField()
    ipy = imagePositionY


class ImagePositionField(
    Double2CompoundBaseField[ImagePositionAttrOperator, ImagePositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ImagePositionAttrOperator
    PLUG_CLS = ImagePositionPlugOperator

    imagePositionX = DoubleField()
    ipx = imagePositionX

    imagePositionY = DoubleField()
    ipy = imagePositionY
