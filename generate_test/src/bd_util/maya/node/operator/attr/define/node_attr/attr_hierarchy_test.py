# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class CompoundPlugOperator(
    CompoundPlugOperator["CompoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("level1CC", "l1cc"),
        ("level1CMC", "cmc"),
        ("level1CM", "cm"),
        ("level1CS", "cs"),
    )

    level1CC = CompoundField()
    l1cc = level1CC

    level1CMC = CompoundField()
    cmc = level1CMC

    level1CM = FloatField()
    cm = level1CM

    level1CS = FloatField()
    cs = level1CS


class CompoundAttrOperator(
    CompoundAttrOperator[CompoundPlugOperator]
):
    __slots__ = ()

    level1CC = CompoundField()
    l1cc = level1CC

    level1CMC = CompoundField()
    cmc = level1CMC

    level1CM = FloatField()
    cm = level1CM

    level1CS = FloatField()
    cs = level1CS


class CompoundField(
    CompoundField[CompoundAttrOperator, CompoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompoundAttrOperator
    PLUG_CLS = CompoundPlugOperator

    level1CC = CompoundField()
    l1cc = level1CC

    level1CMC = CompoundField()
    cmc = level1CMC

    level1CM = FloatField()
    cm = level1CM

    level1CS = FloatField()
    cs = level1CS


class MultiCompoundPlugOperator(
    CompoundPlugOperator["MultiCompoundAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("level1MCC", "mcc"),
        ("level1MCMC", "mcmc"),
        ("level1MCM", "mm"),
        ("level1MCS", "mcs"),
    )

    level1MCC = CompoundField()
    mcc = level1MCC

    level1MCMC = CompoundField()
    mcmc = level1MCMC

    level1MCM = FloatField()
    mm = level1MCM

    level1MCS = FloatField()
    mcs = level1MCS


class MultiCompoundAttrOperator(
    CompoundAttrOperator[MultiCompoundPlugOperator]
):
    __slots__ = ()

    level1MCC = CompoundField()
    mcc = level1MCC

    level1MCMC = CompoundField()
    mcmc = level1MCMC

    level1MCM = FloatField()
    mm = level1MCM

    level1MCS = FloatField()
    mcs = level1MCS


class MultiCompoundField(
    CompoundField[MultiCompoundAttrOperator, MultiCompoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiCompoundAttrOperator
    PLUG_CLS = MultiCompoundPlugOperator
