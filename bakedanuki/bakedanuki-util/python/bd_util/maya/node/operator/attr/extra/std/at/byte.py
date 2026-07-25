# coding: utf-8

# self
from ....define.std.at.scalar.numeric.range.byte import ByteField


class ExtraByteField(ByteField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
