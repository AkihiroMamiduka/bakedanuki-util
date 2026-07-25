# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.dt.string import DataStringField


class _GeneratedAiUserDataBool(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataBool"

    outValue = BoolField(default_value=False, writable=False)
    out = outValue

    defaultValue = BoolField(default_value=False)

    boolAttrName = DataStringField()
