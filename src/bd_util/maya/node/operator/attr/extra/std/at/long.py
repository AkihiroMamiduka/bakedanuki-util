# coding: utf-8

# self
from ...define.std.at.long import LongField


class ExtraLongField(LongField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
