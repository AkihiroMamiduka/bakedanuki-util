# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField
from ..custom import Float3Field


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


class OutColorDataAttrOperator(CompoundAttrOperator[OutColorDataPlugOperator]):
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
