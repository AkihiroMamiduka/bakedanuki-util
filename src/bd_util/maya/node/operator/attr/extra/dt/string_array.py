# coding: utf-8

# self
from ...std.dt.string_array import DataStringArrayField


class ExtraDataStringArrayField(DataStringArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
