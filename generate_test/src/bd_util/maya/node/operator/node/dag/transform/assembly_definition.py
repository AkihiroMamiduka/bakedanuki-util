# coding: utf-8
from ._core import Transform
from ....attr.define.std.at.typed import TypedField


class AssemblyDefinition(Transform):
    __slots__ = ()

    NODE_TYPE = "assemblyDefinition"

    assemblyEdits = TypedField(writable=False)
    aed = assemblyEdits
