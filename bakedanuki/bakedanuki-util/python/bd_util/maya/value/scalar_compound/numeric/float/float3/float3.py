# coding: utf-8
from ....scalar3 import Scalar3
from ..._floating_arithmetic import FloatingNumericArithmeticMixin


class Float3(FloatingNumericArithmeticMixin, Scalar3[float]):
    """3 成分の float 数値。"""

    __slots__ = ()
