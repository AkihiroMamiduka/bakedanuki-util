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


class PntsPlugOperator(
    Double3CompoundBasePlugOperator["PntsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("px", ".pt.x"),
        ("py", ".pt.y"),
        ("pz", ".pt.z"),
    )

    px = DoubleField(default_value=1.0)

    py = DoubleField(default_value=1.0)

    pz = DoubleField(default_value=1.0)


class PntsAttrOperator(
    Double3CompoundBaseAttrOperator[PntsPlugOperator]
):
    __slots__ = ()

    px = DoubleField(default_value=1.0)

    py = DoubleField(default_value=1.0)

    pz = DoubleField(default_value=1.0)


class PntsField(
    Double3CompoundBaseField[PntsAttrOperator, PntsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PntsAttrOperator
    PLUG_CLS = PntsPlugOperator


class KitAPlugOperator(
    CompoundPlugOperator["KitAAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelope", "ka.env"),
        ("pnts", "ka.pt"),
    )

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))


class KitAAttrOperator(
    CompoundAttrOperator[KitAPlugOperator]
):
    __slots__ = ()

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))


class KitAField(
    CompoundField[KitAAttrOperator, KitAPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KitAAttrOperator
    PLUG_CLS = KitAPlugOperator

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))


class KitBPlugOperator(
    CompoundPlugOperator["KitBAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("envelope", "kb.env"),
        ("pnts", "kb.pt"),
    )

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))


class KitBAttrOperator(
    CompoundAttrOperator[KitBPlugOperator]
):
    __slots__ = ()

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))


class KitBField(
    CompoundField[KitBAttrOperator, KitBPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = KitBAttrOperator
    PLUG_CLS = KitBPlugOperator

    envelope = FloatField(default_value=0.0)

    pnts = Double3Field(multi=True, default_value=(1.0, 1.0, 1.0))
