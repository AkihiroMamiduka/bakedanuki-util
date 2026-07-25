# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.subd_hier_blind import (
    BdUserInfoField,
    BlindDataPresetsField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedSubdHierBlind(DG):
    __slots__ = ()

    NODE_TYPE = "subdHierBlind"

    typeId = LongField(default_value=0)
    tid = typeId

    blindDataPresets = BlindDataPresetsField(multi=True)
    bdps = blindDataPresets

    bdUserInfo = BdUserInfoField(multi=True)
    bdui = bdUserInfo

    whichOneIndex = LongField(default_value=-1)
    woi = whichOneIndex
