# coding: utf-8

# self
from ....define.std.at.unit_scalar_range.double_linear import DoubleLinearField


class ExtraDoubleLinearField(DoubleLinearField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
