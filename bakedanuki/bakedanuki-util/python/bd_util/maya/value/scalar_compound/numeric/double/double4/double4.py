# coding: utf-8
from ....scalar4 import Scalar4
from ..._floating_arithmetic import FloatingNumericArithmeticMixin


class Double4(FloatingNumericArithmeticMixin, Scalar4[float]):
    __slots__ = ()
