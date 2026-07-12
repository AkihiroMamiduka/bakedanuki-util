# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..std.at.unit_scalar_range.double_linear import DoubleLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.double3._base import (
    DoubleLinear3CompoundBaseAttrOperator,
    DoubleLinear3CompoundBasePlugOperator,
    DoubleLinear3CompoundBaseField,
)


class Ramp_InterpEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3


class Ramp_InterpEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    NONE = 0
    LINEAR = 1
    SMOOTH = 2
    SPLINE = 3

    NAME_MAP = {
        NONE: "None",
        LINEAR: "Linear",
        SMOOTH: "Smooth",
        SPLINE: "Spline",
    }


class Ramp_InterpEnumField(
    EnumField[Ramp_InterpEnumAttrOperator, Ramp_InterpEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = Ramp_InterpEnumAttrOperator
    PLUG_CLS = Ramp_InterpEnumPlugOperator


class PositiveSizePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["PositiveSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("positiveSizeX", "psx"),
        ("positiveSizeY", "psy"),
        ("positiveSizeZ", "psz"),
    )

    positiveSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    psx = positiveSizeX

    positiveSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    psy = positiveSizeY

    positiveSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    psz = positiveSizeZ


class PositiveSizeAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[PositiveSizePlugOperator]
):
    __slots__ = ()

    positiveSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    psx = positiveSizeX

    positiveSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    psy = positiveSizeY

    positiveSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    psz = positiveSizeZ


class PositiveSizeField(
    DoubleLinear3CompoundBaseField[PositiveSizeAttrOperator, PositiveSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = PositiveSizeAttrOperator
    PLUG_CLS = PositiveSizePlugOperator

    positiveSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    psx = positiveSizeX

    positiveSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    psy = positiveSizeY

    positiveSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    psz = positiveSizeZ


class NegativeSizePlugOperator(
    DoubleLinear3CompoundBasePlugOperator["NegativeSizeAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("negativeSizeX", "nsx"),
        ("negativeSizeY", "nsy"),
        ("negativeSizeZ", "nsz"),
    )

    negativeSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsx = negativeSizeX

    negativeSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsy = negativeSizeY

    negativeSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsz = negativeSizeZ


class NegativeSizeAttrOperator(
    DoubleLinear3CompoundBaseAttrOperator[NegativeSizePlugOperator]
):
    __slots__ = ()

    negativeSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsx = negativeSizeX

    negativeSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsy = negativeSizeY

    negativeSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsz = negativeSizeZ


class NegativeSizeField(
    DoubleLinear3CompoundBaseField[NegativeSizeAttrOperator, NegativeSizePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = NegativeSizeAttrOperator
    PLUG_CLS = NegativeSizePlugOperator

    negativeSizeX = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsx = negativeSizeX

    negativeSizeY = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsy = negativeSizeY

    negativeSizeZ = DoubleLinearField(default_value=1.0, min_value=0.0)
    nsz = negativeSizeZ


class RampPlugOperator(
    CompoundPlugOperator["RampAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("ramp_Position", "rmpp"),
        ("ramp_FloatValue", "rmpfv"),
        ("ramp_Interp", "rmpi"),
    )

    ramp_Position = FloatField(default_value=0.0)
    rmpp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    rmpfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=0)
    rmpi = ramp_Interp


class RampAttrOperator(
    CompoundAttrOperator[RampPlugOperator]
):
    __slots__ = ()

    ramp_Position = FloatField(default_value=0.0)
    rmpp = ramp_Position

    ramp_FloatValue = FloatField(default_value=0.0)
    rmpfv = ramp_FloatValue

    ramp_Interp = Ramp_InterpEnumField(default_value=0)
    rmpi = ramp_Interp


class RampField(
    CompoundField[RampAttrOperator, RampPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = RampAttrOperator
    PLUG_CLS = RampPlugOperator
