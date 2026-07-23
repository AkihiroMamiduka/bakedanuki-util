# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.short_compound.short2_compound.short2 import (
    Short2Field,
)


class ExtraShort2Field(Short2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
