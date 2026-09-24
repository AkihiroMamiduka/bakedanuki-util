# coding: utf-8
from ....scalar2 import Scalar2
from ..._floating_arithmetic import FloatingNumericArithmeticMixin


class Double2(FloatingNumericArithmeticMixin, Scalar2[float]):
    """2 成分の double 数値。"""

    __slots__ = ()
