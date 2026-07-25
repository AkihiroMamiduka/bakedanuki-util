# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.blind_data_template import (
    BdUserInfoField,
    BlindDataPresetsField,
)
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class _GeneratedBlindDataTemplate(DG):
    __slots__ = ()

    NODE_TYPE = "blindDataTemplate"

    typeId = LongField(default_value=0)
    tid = typeId

    blindDataPresets = BlindDataPresetsField(multi=True)
    bdps = blindDataPresets

    bdUserInfo = BdUserInfoField(multi=True)
    bdui = bdUserInfo
