# coding: utf-8
from .._core import Shape
from .....attr.define.std.at.generic import GenericField
from .....attr.define.std.at.scalar.numeric.range.double import DoubleField


class GeneratedArcLengthDimension(Shape):
    __slots__ = ()

    NODE_TYPE = "arcLengthDimension"

    uParamValue = DoubleField(default_value=0.0)
    upv = uParamValue

    vParamValue = DoubleField(default_value=0.0)
    vpv = vParamValue

    nurbsGeometry = GenericField()
    ng = nurbsGeometry

    arcLength = DoubleField(default_value=0.0, writable=False)
    al = arcLength

    arcLengthInV = DoubleField(default_value=0.0, writable=False)
    alv = arcLengthInV
