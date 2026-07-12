# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.typed import TypedField
from ....attr.define.std.dt.string import DataStringField


class AssemblyReference(Transform):
    __slots__ = ()

    NODE_TYPE = "assemblyReference"

    assemblyEdits = TypedField(writable=False)
    aed = assemblyEdits

    definition = DataStringField()
    def_ = definition

    repNamespace = DataStringField()
    rns = repNamespace

    initialRep = DataStringField()
    irp = initialRep
