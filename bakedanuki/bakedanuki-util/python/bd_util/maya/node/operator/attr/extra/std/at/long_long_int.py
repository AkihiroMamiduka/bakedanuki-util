# coding: utf-8

# self
from ....define.std.at.scalar.numeric.range.long_long_int import (
    LongLongIntField,
)


class ExtraLongLongIntField(LongLongIntField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
