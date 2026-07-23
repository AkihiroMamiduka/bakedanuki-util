# coding: utf-8

from ..std.at.numeric_scalar_range.double import DoubleField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double2_compound._base import (
    Double2CompoundBaseAttrOperator,
    Double2CompoundBasePlugOperator,
    Double2CompoundBaseField,
)


class LatticePointPlugOperator(
    Double2CompoundBasePlugOperator["LatticePointAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("latticePointX", "lpx"),
        ("latticePointY", "lpy"),
    )

    latticePointX = DoubleField(default_value=0.0)
    lpx = latticePointX

    latticePointY = DoubleField(default_value=0.0)
    lpy = latticePointY


class LatticePointAttrOperator(
    Double2CompoundBaseAttrOperator[LatticePointPlugOperator]
):
    __slots__ = ()

    latticePointX = DoubleField(default_value=0.0)
    lpx = latticePointX

    latticePointY = DoubleField(default_value=0.0)
    lpy = latticePointY


class LatticePointField(
    Double2CompoundBaseField[LatticePointAttrOperator, LatticePointPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = LatticePointAttrOperator
    PLUG_CLS = LatticePointPlugOperator


class BoundingBoxInfPlugOperator(
    Double2CompoundBasePlugOperator["BoundingBoxInfAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxTop", "bbxt"),
        ("boundingBoxLeft", "bbxl"),
    )

    boundingBoxTop = DoubleField(default_value=0.0)
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField(default_value=0.0)
    bbxl = boundingBoxLeft


class BoundingBoxInfAttrOperator(
    Double2CompoundBaseAttrOperator[BoundingBoxInfPlugOperator]
):
    __slots__ = ()

    boundingBoxTop = DoubleField(default_value=0.0)
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField(default_value=0.0)
    bbxl = boundingBoxLeft


class BoundingBoxInfField(
    Double2CompoundBaseField[BoundingBoxInfAttrOperator, BoundingBoxInfPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxInfAttrOperator
    PLUG_CLS = BoundingBoxInfPlugOperator

    boundingBoxTop = DoubleField(default_value=0.0)
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField(default_value=0.0)
    bbxl = boundingBoxLeft


class BoundingBoxSupPlugOperator(
    Double2CompoundBasePlugOperator["BoundingBoxSupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxBottom", "bbxb"),
        ("boundingBoxRight", "bbxr"),
    )

    boundingBoxBottom = DoubleField(default_value=0.0)
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField(default_value=0.0)
    bbxr = boundingBoxRight


class BoundingBoxSupAttrOperator(
    Double2CompoundBaseAttrOperator[BoundingBoxSupPlugOperator]
):
    __slots__ = ()

    boundingBoxBottom = DoubleField(default_value=0.0)
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField(default_value=0.0)
    bbxr = boundingBoxRight


class BoundingBoxSupField(
    Double2CompoundBaseField[BoundingBoxSupAttrOperator, BoundingBoxSupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxSupAttrOperator
    PLUG_CLS = BoundingBoxSupPlugOperator

    boundingBoxBottom = DoubleField(default_value=0.0)
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField(default_value=0.0)
    bbxr = boundingBoxRight
