# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class PositionPlugOperator(
    Double2CompoundBasePlugOperator["PositionAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positionX", "px"),
        ("positionY", "py"),
    )

    positionX = DoubleField()
    px = positionX

    positionY = DoubleField()
    py = positionY


class PositionAttrOperator(
    Double2CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleField()
    px = positionX

    positionY = DoubleField()
    py = positionY


class PositionField(
    Double2CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator

    positionX = DoubleField()
    px = positionX

    positionY = DoubleField()
    py = positionY


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
