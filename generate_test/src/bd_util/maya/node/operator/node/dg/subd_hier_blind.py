# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.subd_hier_blind import (
    BdUserInfoField,
    BlindDataPresetsField,
)
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class SubdHierBlind(DG):
    __slots__ = ()

    NODE_TYPE = "subdHierBlind"

    typeId = LongField()
    tid = typeId

    blindDataPresets = BlindDataPresetsField(multi=True)
    bdps = blindDataPresets

    bdUserInfo = BdUserInfoField(multi=True)
    bdui = bdUserInfo

    whichOneIndex = LongField()
    woi = whichOneIndex
