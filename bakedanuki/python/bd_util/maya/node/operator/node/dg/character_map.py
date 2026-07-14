# coding: utf-8
from ._core import DG
from ...attr.define.std.at.message import MessageField
from ...attr.define.std.at.typed import TypedField


class CharacterMap(DG):
    __slots__ = ()

    NODE_TYPE = "characterMap"

    member = MessageField(multi=True)
    m = member

    memberIndex = TypedField(multi=True)
    mi = memberIndex
