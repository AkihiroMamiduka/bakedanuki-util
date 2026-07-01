# coding: utf-8
from ._core import DG
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.long import LongField
from ...attr.define.std.at.typed import TypedField


class PolyBlindData(DG):
    __slots__ = ()

    NODE_TYPE = "polyBlindData"

    typeId = LongField()
    tid = typeId

    inMesh = TypedField()
    i = inMesh

    outMesh = TypedField()
    o = outMesh

    blindDataEntriesAreNew = BoolField()
    bdn = blindDataEntriesAreNew
