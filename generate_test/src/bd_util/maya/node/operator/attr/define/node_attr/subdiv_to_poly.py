# coding: utf-8

from ..std.at.numeric_scalar_range.long import LongField
from ..custom.at.scalar_compound.numeric_compound.long_compound.long2_compound._base import (
    Long2CompoundBaseAttrOperator,
    Long2CompoundBasePlugOperator,
    Long2CompoundBaseField,
)


class OutSubdCVIdPlugOperator(
    Long2CompoundBasePlugOperator["OutSubdCVIdAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outSubdCVIdLeft", "osl"),
        ("outSubdCVIdRight", "osr"),
    )

    outSubdCVIdLeft = LongField()
    osl = outSubdCVIdLeft

    outSubdCVIdRight = LongField()
    osr = outSubdCVIdRight


class OutSubdCVIdAttrOperator(
    Long2CompoundBaseAttrOperator[OutSubdCVIdPlugOperator]
):
    __slots__ = ()

    outSubdCVIdLeft = LongField()
    osl = outSubdCVIdLeft

    outSubdCVIdRight = LongField()
    osr = outSubdCVIdRight


class OutSubdCVIdField(
    Long2CompoundBaseField[OutSubdCVIdAttrOperator, OutSubdCVIdPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutSubdCVIdAttrOperator
    PLUG_CLS = OutSubdCVIdPlugOperator


class InSubdCVIdPlugOperator(
    Long2CompoundBasePlugOperator["InSubdCVIdAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("inSubdCVIdLeft", "isl"),
        ("inSubdCVIdRight", "isr"),
    )

    inSubdCVIdLeft = LongField()
    isl = inSubdCVIdLeft

    inSubdCVIdRight = LongField()
    isr = inSubdCVIdRight


class InSubdCVIdAttrOperator(
    Long2CompoundBaseAttrOperator[InSubdCVIdPlugOperator]
):
    __slots__ = ()

    inSubdCVIdLeft = LongField()
    isl = inSubdCVIdLeft

    inSubdCVIdRight = LongField()
    isr = inSubdCVIdRight


class InSubdCVIdField(
    Long2CompoundBaseField[InSubdCVIdAttrOperator, InSubdCVIdPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InSubdCVIdAttrOperator
    PLUG_CLS = InSubdCVIdPlugOperator
