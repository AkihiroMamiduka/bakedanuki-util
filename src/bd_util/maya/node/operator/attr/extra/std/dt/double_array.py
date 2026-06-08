# coding: utf-8

# self
from ...define.std.dt.double_array import DataDoubleArrayField


class ExtraDataDoubleArrayField(DataDoubleArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
