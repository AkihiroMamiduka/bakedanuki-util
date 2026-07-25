# coding: utf-8

# self
from ....define.std.at.scalar.numeric.bool import BoolField


class ExtraBoolField(BoolField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
