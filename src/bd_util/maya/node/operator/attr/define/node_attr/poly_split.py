# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.unit_scalar_range.float_linear import FloatLinearField
from ..custom.at.scalar_compound.unit_compound.linear_compound.float3._base import (
    FloatLinear3CompoundBaseAttrOperator,
    FloatLinear3CompoundBasePlugOperator,
    FloatLinear3CompoundBaseField,
)


class VerticesPlugOperator(
    FloatLinear3CompoundBasePlugOperator["VerticesAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("vtxx", "vx"),
        ("vtxy", "vy"),
        ("vtxz", "vz"),
    )

    vtxx = FloatLinearField(default_value=0.0)
    vx = vtxx

    vtxy = FloatLinearField(default_value=0.0)
    vy = vtxy

    vtxz = FloatLinearField(default_value=0.0)
    vz = vtxz


class VerticesAttrOperator(
    FloatLinear3CompoundBaseAttrOperator[VerticesPlugOperator]
):
    __slots__ = ()

    vtxx = FloatLinearField(default_value=0.0)
    vx = vtxx

    vtxy = FloatLinearField(default_value=0.0)
    vy = vtxy

    vtxz = FloatLinearField(default_value=0.0)
    vz = vtxz


class VerticesField(
    FloatLinear3CompoundBaseField[VerticesAttrOperator, VerticesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VerticesAttrOperator
    PLUG_CLS = VerticesPlugOperator


class SplitPointsPlugOperator(
    CompoundPlugOperator["SplitPointsAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("splitPoint", "sp"),
    )

    splitPoint = CompoundField(multi=True)
    sp = splitPoint


class SplitPointsAttrOperator(
    CompoundAttrOperator[SplitPointsPlugOperator]
):
    __slots__ = ()

    splitPoint = CompoundField(multi=True)
    sp = splitPoint


class SplitPointsField(
    CompoundField[SplitPointsAttrOperator, SplitPointsPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = SplitPointsAttrOperator
    PLUG_CLS = SplitPointsPlugOperator
