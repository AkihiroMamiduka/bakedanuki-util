# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.double import DoubleField
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound._base import (
    Double3CompoundBaseAttrOperator,
    Double3CompoundBasePlugOperator,
    Double3CompoundBaseField,
)
from ..custom.at.scalar_compound.numeric_compound.double_compound.double3_compound.double3 import Double3Field


class .pntsPlugOperator(
    Double3CompoundBasePlugOperator[".pntsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("px", ".pt.x"),
        ("py", ".pt.y"),
        ("pz", ".pt.z"),
    )

    px = DoubleField()
    .pt.x = px

    py = DoubleField()
    .pt.y = py

    pz = DoubleField()
    .pt.z = pz


class .pntsAttrOperator(
    Double3CompoundBaseAttrOperator[.pntsPlugOperator]
):
    __slots__ = ()

    px = DoubleField()
    .pt.x = px

    py = DoubleField()
    .pt.y = py

    pz = DoubleField()
    .pt.z = pz


class .pntsField(
    Double3CompoundBaseField[.pntsAttrOperator, .pntsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = .pntsAttrOperator
    PLUG_CLS = .pntsPlugOperator


class KitAPlugOperator(
    CompoundPlugOperator["KitAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelope", "ka.env"),
        ("pnts", "ka.pt"),
    )

    envelope = FloatField()
    ka.env = envelope

    pnts = Double3Field()
    ka.pt = pnts


class KitAAttrOperator(
    CompoundAttrOperator[KitAPlugOperator]
):
    __slots__ = ()

    envelope = FloatField()
    ka.env = envelope

    pnts = Double3Field()
    ka.pt = pnts


class KitAField(
    CompoundField[KitAAttrOperator, KitAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KitAAttrOperator
    PLUG_CLS = KitAPlugOperator

    envelope = FloatField()
    ka.env = envelope

    pnts = Double3Field()
    ka.pt = pnts


class KitBPlugOperator(
    CompoundPlugOperator["KitBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelope", "kb.env"),
        ("pnts", "kb.pt"),
    )

    envelope = FloatField()
    kb.env = envelope

    pnts = Double3Field()
    kb.pt = pnts


class KitBAttrOperator(
    CompoundAttrOperator[KitBPlugOperator]
):
    __slots__ = ()

    envelope = FloatField()
    kb.env = envelope

    pnts = Double3Field()
    kb.pt = pnts


class KitBField(
    CompoundField[KitBAttrOperator, KitBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KitBAttrOperator
    PLUG_CLS = KitBPlugOperator

    envelope = FloatField()
    kb.env = envelope

    pnts = Double3Field()
    kb.pt = pnts
