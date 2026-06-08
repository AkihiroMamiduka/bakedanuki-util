# coding: utf-8

# self
from ...std.at.long_long_int import LongLongIntField


class ExtraLongLongIntField(LongLongIntField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
