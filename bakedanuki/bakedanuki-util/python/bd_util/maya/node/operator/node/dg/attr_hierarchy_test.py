# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.attr_hierarchy_test import (
    CompoundValueField,
    MultiCompoundField,
)
from ...attr.define.std.at.compound import CompoundField
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class AttrHierarchyTest(DG):
    __slots__ = ()

    NODE_TYPE = "attrHierarchyTest"

    single = FloatField(default_value=0.0)
    s = single

    multi = FloatField(multi=True, default_value=0.0)
    m = multi

    compound = CompoundValueField()
    c = compound
    level1CC = compound.level1CC
    l1cc = level1CC
    level1CMC = compound.level1CMC
    cmc = level1CMC
    level1CM = compound.level1CM
    cm = level1CM
    level1CS = compound.level1CS
    cs = level1CS

    level3CCMCS1 = FloatField()
    ccm1 = level3CCMCS1

    level3CCMCS2 = FloatField()
    ccm2 = level3CCMCS2

    level2CMCC = CompoundField()
    cmcc = level2CMCC

    level3CMCCS1 = FloatField()
    cmc1 = level3CMCCS1

    level3CMCCS2 = FloatField()
    cmc2 = level3CMCCS2

    level2CMCMC = CompoundField()
    cmmc = level2CMCMC

    level3CMCMCS1 = FloatField()
    cmm1 = level3CMCMCS1

    level3CMCMCS2 = FloatField()
    cmm2 = level3CMCMCS2

    level2CMCM = FloatField()
    cmcm = level2CMCM

    level2CMCS = FloatField()
    cmcs = level2CMCS

    multiCompound = MultiCompoundField(multi=True)
    mc = multiCompound

    level2MCCC = CompoundField()
    mccc = level2MCCC

    level3MCCCS1 = FloatField()
    mcc1 = level3MCCCS1

    level3MCCCS2 = FloatField()
    mcc2 = level3MCCCS2

    level2MCCMC = CompoundField()
    mccm = level2MCCMC

    level3MCCMCS1 = FloatField()
    mcm1 = level3MCCMCS1

    level3MCCMCS2 = FloatField()
    mcm2 = level3MCCMCS2

    level2MCCM = FloatField()
    mcm = level2MCCM

    level2MCCS = FloatField()
    mccs = level2MCCS

    level3MCMCCS1 = FloatField()
    mmc1 = level3MCMCCS1

    level3MCMCCS2 = FloatField()
    mmc2 = level3MCMCCS2
