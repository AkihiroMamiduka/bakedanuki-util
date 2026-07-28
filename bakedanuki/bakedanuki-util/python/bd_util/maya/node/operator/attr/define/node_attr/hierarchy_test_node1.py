# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.scalar.numeric.range.float import FloatField


class N1compoundPlugOperator(CompoundPlugOperator["N1compoundAttrOperator"]):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("n1level1M", "n1m1"),
        ("n1level1S", "n1s1"),
        ("n1level1C", "n1c1"),
    )

    n1level1M = FloatField(multi=True, default_value=0.0)
    n1m1 = n1level1M

    n1level1S = FloatField(default_value=0.0)
    n1s1 = n1level1S

    n1level1C = CompoundField(default_value=(0.0, 0.0))
    n1c1 = n1level1C


class N1compoundAttrOperator(CompoundAttrOperator[N1compoundPlugOperator]):
    __slots__ = ()

    n1level1M = FloatField(multi=True, default_value=0.0)
    n1m1 = n1level1M

    n1level1S = FloatField(default_value=0.0)
    n1s1 = n1level1S

    n1level1C = CompoundField(default_value=(0.0, 0.0))
    n1c1 = n1level1C


class N1compoundField(
    CompoundField[N1compoundAttrOperator, N1compoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = N1compoundAttrOperator
    PLUG_CLS = N1compoundPlugOperator

    n1level1M = FloatField(multi=True, default_value=0.0)
    n1m1 = n1level1M

    n1level1S = FloatField(default_value=0.0)
    n1s1 = n1level1S

    n1level1C = CompoundField(default_value=(0.0, 0.0))
    n1c1 = n1level1C
