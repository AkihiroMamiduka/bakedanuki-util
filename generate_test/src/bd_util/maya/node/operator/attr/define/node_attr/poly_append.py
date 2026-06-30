# coding: utf-8

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

    vtxx = FloatLinearField()
    vx = vtxx

    vtxy = FloatLinearField()
    vy = vtxy

    vtxz = FloatLinearField()
    vz = vtxz


class VerticesAttrOperator(
    FloatLinear3CompoundBaseAttrOperator[VerticesPlugOperator]
):
    __slots__ = ()

    vtxx = FloatLinearField()
    vx = vtxx

    vtxy = FloatLinearField()
    vy = vtxy

    vtxz = FloatLinearField()
    vz = vtxz


class VerticesField(
    FloatLinear3CompoundBaseField[VerticesAttrOperator, VerticesPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = VerticesAttrOperator
    PLUG_CLS = VerticesPlugOperator
