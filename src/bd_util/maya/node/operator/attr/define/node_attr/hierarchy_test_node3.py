# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class N1compoundPlugOperator(
    CompoundPlugOperator["N1compoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("n1level1M", "n1m1"),
        ("n1level1S", "n1s1"),
        ("n1level1C", "n1c1"),
    )

    n1level1M = FloatField()
    n1m1 = n1level1M

    n1level1S = FloatField()
    n1s1 = n1level1S

    n1level1C = CompoundField()
    n1c1 = n1level1C


class N1compoundAttrOperator(
    CompoundAttrOperator[N1compoundPlugOperator]
):
    __slots__ = ()

    n1level1M = FloatField()
    n1m1 = n1level1M

    n1level1S = FloatField()
    n1s1 = n1level1S

    n1level1C = CompoundField()
    n1c1 = n1level1C


class N1compoundField(
    CompoundField[N1compoundAttrOperator, N1compoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = N1compoundAttrOperator
    PLUG_CLS = N1compoundPlugOperator

    n1level1M = FloatField()
    n1m1 = n1level1M

    n1level1S = FloatField()
    n1s1 = n1level1S

    n1level1C = CompoundField()
    n1c1 = n1level1C


class N2compoundPlugOperator(
    CompoundPlugOperator["N2compoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("n2level1M", "n2m1"),
        ("n2level1S", "n2s1"),
        ("n2level1C", "n2c1"),
    )

    n2level1M = FloatField()
    n2m1 = n2level1M

    n2level1S = FloatField()
    n2s1 = n2level1S

    n2level1C = CompoundField()
    n2c1 = n2level1C


class N2compoundAttrOperator(
    CompoundAttrOperator[N2compoundPlugOperator]
):
    __slots__ = ()

    n2level1M = FloatField()
    n2m1 = n2level1M

    n2level1S = FloatField()
    n2s1 = n2level1S

    n2level1C = CompoundField()
    n2c1 = n2level1C


class N2compoundField(
    CompoundField[N2compoundAttrOperator, N2compoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = N2compoundAttrOperator
    PLUG_CLS = N2compoundPlugOperator

    n2level1M = FloatField()
    n2m1 = n2level1M

    n2level1S = FloatField()
    n2s1 = n2level1S

    n2level1C = CompoundField()
    n2c1 = n2level1C


class N3compoundPlugOperator(
    CompoundPlugOperator["N3compoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("n3level1M", "n3m1"),
        ("n3level1S", "n3s1"),
        ("n3level1C", "n3c1"),
    )

    n3level1M = FloatField()
    n3m1 = n3level1M

    n3level1S = FloatField()
    n3s1 = n3level1S

    n3level1C = CompoundField()
    n3c1 = n3level1C


class N3compoundAttrOperator(
    CompoundAttrOperator[N3compoundPlugOperator]
):
    __slots__ = ()

    n3level1M = FloatField()
    n3m1 = n3level1M

    n3level1S = FloatField()
    n3s1 = n3level1S

    n3level1C = CompoundField()
    n3c1 = n3level1C


class N3compoundField(
    CompoundField[N3compoundAttrOperator, N3compoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = N3compoundAttrOperator
    PLUG_CLS = N3compoundPlugOperator

    n3level1M = FloatField()
    n3m1 = n3level1M

    n3level1S = FloatField()
    n3s1 = n3level1S

    n3level1C = CompoundField()
    n3c1 = n3level1C
