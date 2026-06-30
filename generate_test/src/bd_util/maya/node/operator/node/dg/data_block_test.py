# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.data_block_test import (
    CompoundField,
    MultiCompoundField,
)
from ...attr.define.std.at.numeric_scalar_range.float import FloatField


class DataBlockTest(DG):
    __slots__ = ()

    NODE_TYPE = "dataBlockTest"

    single = FloatField()
    s = single

    multi = FloatField(multi=True)
    m = multi

    compound = CompoundField()
    c = compound
    level1CC = compound.level1CC
    l1cc = level1CC
    level1CMC = compound.level1CMC
    cmc = level1CMC
    level1CM = compound.level1CM
    cm = level1CM
    level1CS = compound.level1CS
    cs = level1CS

    # TODO: level2CCMC.level3CCMCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level2CCMC.level3CCMCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCC (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level3CMCCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level3CMCCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCMC (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCMC.level3CMCMCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCMC.level3CMCMCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCM (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: level1CMC.level2CMCS (attributeType=None, dataType=None) は未対応のため手動で追加してください

    multiCompound = MultiCompoundField(multi=True)
    mc = multiCompound

    # TODO: multiCompound.level2MCCC (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level3MCCCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level3MCCCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level2MCCMC (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level2MCCMC.level3MCCMCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level2MCCMC.level3MCCMCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level2MCCM (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level2MCCS (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level1MCMC.level3MCMCCS1 (attributeType=None, dataType=None) は未対応のため手動で追加してください

    # TODO: multiCompound.level1MCMC.level3MCMCCS2 (attributeType=None, dataType=None) は未対応のため手動で追加してください
