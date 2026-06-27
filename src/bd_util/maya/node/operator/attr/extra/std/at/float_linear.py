# coding: utf-8

# self
from ....define.std.at.float_linear import FloatLinearField


class ExtraFloatLinearField(FloatLinearField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
