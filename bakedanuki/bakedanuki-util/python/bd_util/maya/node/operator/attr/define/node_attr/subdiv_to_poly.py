# coding: utf-8

from ..std.at.scalar.numeric.range.long import LongField
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

    outSubdCVIdLeft = LongField(default_value=0)
    osl = outSubdCVIdLeft

    outSubdCVIdRight = LongField(default_value=0)
    osr = outSubdCVIdRight


class OutSubdCVIdAttrOperator(
    Long2CompoundBaseAttrOperator[OutSubdCVIdPlugOperator]
):
    __slots__ = ()

    outSubdCVIdLeft = LongField(default_value=0)
    osl = outSubdCVIdLeft

    outSubdCVIdRight = LongField(default_value=0)
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

    inSubdCVIdLeft = LongField(default_value=0)
    isl = inSubdCVIdLeft

    inSubdCVIdRight = LongField(default_value=0)
    isr = inSubdCVIdRight


class InSubdCVIdAttrOperator(
    Long2CompoundBaseAttrOperator[InSubdCVIdPlugOperator]
):
    __slots__ = ()

    inSubdCVIdLeft = LongField(default_value=0)
    isl = inSubdCVIdLeft

    inSubdCVIdRight = LongField(default_value=0)
    isr = inSubdCVIdRight


class InSubdCVIdField(
    Long2CompoundBaseField[InSubdCVIdAttrOperator, InSubdCVIdPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = InSubdCVIdAttrOperator
    PLUG_CLS = InSubdCVIdPlugOperator
