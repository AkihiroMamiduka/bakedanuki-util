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

    latticePointX = DoubleField()
    lpx = latticePointX

    latticePointY = DoubleField()
    lpy = latticePointY


class LatticePointAttrOperator(
    Double2CompoundBaseAttrOperator[LatticePointPlugOperator]
):
    __slots__ = ()

    latticePointX = DoubleField()
    lpx = latticePointX

    latticePointY = DoubleField()
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

    boundingBoxTop = DoubleField()
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField()
    bbxl = boundingBoxLeft


class BoundingBoxInfAttrOperator(
    Double2CompoundBaseAttrOperator[BoundingBoxInfPlugOperator]
):
    __slots__ = ()

    boundingBoxTop = DoubleField()
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField()
    bbxl = boundingBoxLeft


class BoundingBoxInfField(
    Double2CompoundBaseField[BoundingBoxInfAttrOperator, BoundingBoxInfPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxInfAttrOperator
    PLUG_CLS = BoundingBoxInfPlugOperator

    boundingBoxTop = DoubleField()
    bbxt = boundingBoxTop

    boundingBoxLeft = DoubleField()
    bbxl = boundingBoxLeft


class BoundingBoxSupPlugOperator(
    Double2CompoundBasePlugOperator["BoundingBoxSupAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("boundingBoxBottom", "bbxb"),
        ("boundingBoxRight", "bbxr"),
    )

    boundingBoxBottom = DoubleField()
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField()
    bbxr = boundingBoxRight


class BoundingBoxSupAttrOperator(
    Double2CompoundBaseAttrOperator[BoundingBoxSupPlugOperator]
):
    __slots__ = ()

    boundingBoxBottom = DoubleField()
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField()
    bbxr = boundingBoxRight


class BoundingBoxSupField(
    Double2CompoundBaseField[BoundingBoxSupAttrOperator, BoundingBoxSupPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = BoundingBoxSupAttrOperator
    PLUG_CLS = BoundingBoxSupPlugOperator

    boundingBoxBottom = DoubleField()
    bbxb = boundingBoxBottom

    boundingBoxRight = DoubleField()
    bbxr = boundingBoxRight
