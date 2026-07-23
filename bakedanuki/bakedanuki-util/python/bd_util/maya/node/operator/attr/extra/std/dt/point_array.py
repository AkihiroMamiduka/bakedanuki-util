# coding: utf-8

# self
from ....define.std.dt.point_array import DataPointArrayField


class ExtraDataPointArrayField(DataPointArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
