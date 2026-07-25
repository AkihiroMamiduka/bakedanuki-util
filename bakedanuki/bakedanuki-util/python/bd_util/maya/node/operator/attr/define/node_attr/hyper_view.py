# coding: utf-8

from ..std.at.scalar.numeric.range.double import DoubleField
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

    positionX = DoubleField(default_value=0.0)
    px = positionX

    positionY = DoubleField(default_value=0.0)
    py = positionY


class PositionAttrOperator(
    Double2CompoundBaseAttrOperator[PositionPlugOperator]
):
    __slots__ = ()

    positionX = DoubleField(default_value=0.0)
    px = positionX

    positionY = DoubleField(default_value=0.0)
    py = positionY


class PositionField(
    Double2CompoundBaseField[PositionAttrOperator, PositionPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositionAttrOperator
    PLUG_CLS = PositionPlugOperator

    positionX = DoubleField(default_value=0.0)
    px = positionX

    positionY = DoubleField(default_value=0.0)
    py = positionY


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
    Double2CompoundBaseField[ViewRectHighAttrOperator, ViewRectHighPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewRectHighAttrOperator
    PLUG_CLS = ViewRectHighPlugOperator

    viewXH = DoubleField(default_value=0.0)
    xh = viewXH

    viewYH = DoubleField(default_value=0.0)
    yh = viewYH
