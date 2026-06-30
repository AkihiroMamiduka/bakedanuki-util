# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.dt.string import DataStringField


class AiUserDataBool(DG):
    __slots__ = ()

    NODE_TYPE = "aiUserDataBool"

    outValue = BoolField()
    out = outValue

    defaultValue = BoolField()

    boolAttrName = DataStringField()
