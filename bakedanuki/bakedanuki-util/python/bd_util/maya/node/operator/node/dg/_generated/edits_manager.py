# coding: utf-8
from .._core import DG
from ....attr.define.std.at.typed import TypedField


class GeneratedEditsManager(DG):
    __slots__ = ()

    NODE_TYPE = "editsManager"

    edits = TypedField()
    edt = edits
