# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.message import MessageField
from ....attr.define.std.at.numeric_scalar.bool import BoolField


class IkEffector(Transform):
    __slots__ = ()

    NODE_TYPE = "ikEffector"

    hideDisplay = BoolField(default_value=False)
    hd = hideDisplay

    handlePath = MessageField(multi=True)
    hp = handlePath
