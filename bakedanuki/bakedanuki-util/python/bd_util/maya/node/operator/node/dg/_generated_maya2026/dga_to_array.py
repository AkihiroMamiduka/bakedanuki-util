# coding: utf-8
from .._core import DG
from ....attr.define.std.at.generic import GenericField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.dt.double_array import DataDoubleArrayField


class GeneratedDgaToArray(DG):
    __slots__ = ()

    NODE_TYPE = "dgaToArray"

    inputDoubleValues = DoubleField(multi=True, default_value=0.0)
    idv = inputDoubleValues

    inputGeometry = GenericField()
    ig = inputGeometry

    outputDoubleArray = DataDoubleArrayField(writable=False)
    oda = outputDoubleArray

    defaultValue = DoubleField(default_value=0.0)
    dv = defaultValue
