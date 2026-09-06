# coding: utf-8
from .._core import DG
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.typed import TypedField


class GeneratedBifrostClosureConverter(DG):
    __slots__ = ()

    NODE_TYPE = "bifrostClosureConverter"

    inputClosure = TypedField(readable=False)
    ic = inputClosure

    asyncComputeDone = BoolField(default_value=False, readable=False)
