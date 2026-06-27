# coding: utf-8

# self
from ....define.std.at.numeric_scalar_range.float import FloatField


class ExtraFloatField(FloatField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
