# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.long_compound.long2_compound.long2 import (
    Long2Field,
)


class ExtraLong2Field(Long2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
