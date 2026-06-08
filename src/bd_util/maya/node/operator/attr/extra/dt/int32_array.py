# coding: utf-8

# self
from ...std.dt.int32_array import DataInt32ArrayField


class ExtraDataInt32ArrayField(DataInt32ArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
