# coding: utf-8

# self
from ...std.dt.float_array import DataFloatArrayField


class ExtraDataFloatArrayField(DataFloatArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
