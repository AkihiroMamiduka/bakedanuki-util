# coding: utf-8
from ....scalar2 import Scalar2
from ..._floating_arithmetic import FloatingNumericArithmeticMixin


class Double2(FloatingNumericArithmeticMixin, Scalar2[float]):
    __slots__ = ()
