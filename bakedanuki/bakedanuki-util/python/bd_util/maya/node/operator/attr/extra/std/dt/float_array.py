# coding: utf-8

# self
from ....define.std.dt.float_array import DataFloatArrayField


class ExtraDataFloatArrayField(DataFloatArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
