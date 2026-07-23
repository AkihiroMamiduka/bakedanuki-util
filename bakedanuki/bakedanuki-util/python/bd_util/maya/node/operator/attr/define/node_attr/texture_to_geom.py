# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField
from ..custom.at.scalar_compound.numeric_compound.float_compound.float3_compound.float3 import Float3Field


class OutColorDataPlugOperator(
    CompoundPlugOperator["OutColorDataAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("outColor", "oc"),
        ("outAlpha", "oa"),
    )

    outColor = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha


class OutColorDataAttrOperator(
    CompoundAttrOperator[OutColorDataPlugOperator]
):
    __slots__ = ()

    outColor = Float3Field(default_value=(0.0, 0.0, 0.0), writable=False)
    oc = outColor

    outAlpha = FloatField(default_value=0.0, writable=False)
    oa = outAlpha


class OutColorDataField(
    CompoundField[OutColorDataAttrOperator, OutColorDataPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = OutColorDataAttrOperator
    PLUG_CLS = OutColorDataPlugOperator
