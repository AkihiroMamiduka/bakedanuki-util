# coding: utf-8
from ....scalar3 import Scalar3
from ..._floating_arithmetic import FloatingNumericArithmeticMixin


class Double3(FloatingNumericArithmeticMixin, Scalar3[float]):
    __slots__ = ()
