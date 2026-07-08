# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.numeric_scalar_range.float import FloatField


class CompoundValuePlugOperator(
    CompoundPlugOperator["CompoundValueAttrOperator"]
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

    level1CMC = CompoundField(multi=True)
    cmc = level1CMC

    level1CM = FloatField(multi=True, default_value=0.0)
    cm = level1CM

    level1CS = FloatField(default_value=0.0)
    cs = level1CS


class CompoundValueAttrOperator(
    CompoundAttrOperator[CompoundValuePlugOperator]
):
    __slots__ = ()

    level1CC = CompoundField()
    l1cc = level1CC

    level1CMC = CompoundField(multi=True)
    cmc = level1CMC

    level1CM = FloatField(multi=True, default_value=0.0)
    cm = level1CM

    level1CS = FloatField(default_value=0.0)
    cs = level1CS


class CompoundValueField(
    CompoundField[CompoundValueAttrOperator, CompoundValuePlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CompoundValueAttrOperator
    PLUG_CLS = CompoundValuePlugOperator

    level1CC = CompoundField()
    l1cc = level1CC

    level1CMC = CompoundField(multi=True)
    cmc = level1CMC

    level1CM = FloatField(multi=True, default_value=0.0)
    cm = level1CM

    level1CS = FloatField(default_value=0.0)
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

    level1MCMC = CompoundField(multi=True)
    mcmc = level1MCMC

    level1MCM = FloatField(multi=True, default_value=0.0)
    mm = level1MCM

    level1MCS = FloatField(default_value=0.0)
    mcs = level1MCS


class MultiCompoundAttrOperator(
    CompoundAttrOperator[MultiCompoundPlugOperator]
):
    __slots__ = ()

    level1MCC = CompoundField()
    mcc = level1MCC

    level1MCMC = CompoundField(multi=True)
    mcmc = level1MCMC

    level1MCM = FloatField(multi=True, default_value=0.0)
    mm = level1MCM

    level1MCS = FloatField(default_value=0.0)
    mcs = level1MCS


class MultiCompoundField(
    CompoundField[MultiCompoundAttrOperator, MultiCompoundPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = MultiCompoundAttrOperator
    PLUG_CLS = MultiCompoundPlugOperator
