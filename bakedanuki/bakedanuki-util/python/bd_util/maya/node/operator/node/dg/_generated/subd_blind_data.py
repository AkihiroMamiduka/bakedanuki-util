# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.long import LongField
from ....attr.define.std.at.typed import TypedField


class GeneratedSubdBlindData(DG):
    __slots__ = ()

    NODE_TYPE = "subdBlindData"

    typeId = LongField(default_value=0)
    tid = typeId

    inMesh = TypedField()
    i = inMesh

    outMesh = TypedField()
    o = outMesh

    blindDataEntriesAreNew = BoolField(default_value=False)
    bdn = blindDataEntriesAreNew
