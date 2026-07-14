# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.sampler import FunctionField
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.numeric_scalar_range.short import ShortField


class Sampler(DG):
    __slots__ = ()

    NODE_TYPE = "sampler"

    minimum = DoubleField(default_value=0.0)
    min = minimum

    maximum = DoubleField(default_value=0.0)
    max = maximum

    step = DoubleField(default_value=0.0)
    s = step

    invert = BoolField(default_value=False)
    i = invert

    value = DoubleField(multi=True, default_value=0.0, writable=False)
    v = value

    function = FunctionField()
    f = function
    function_Hidden = function.function_Hidden
    fh = function_Hidden
    function_Raw = function.function_Raw
    fr = function_Raw
    function_Inmap = function.function_Inmap
    fi = function_Inmap
    function_Outmap = function.function_Outmap
    fo = function_Outmap
    function_Default = function.function_Default
    fd = function_Default

    function_InmapTo = ShortField()
    fit = function_InmapTo

    function_InmapFrom = ShortField()
    fif = function_InmapFrom

    function_OutmapTo = ShortField()
    fot = function_OutmapTo

    function_OutmapFrom = ShortField()
    fof = function_OutmapFrom
