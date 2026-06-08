# coding: utf-8

# self
from ...std.dt.string import DataStringField


class ExtraDataStringField(DataStringField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
