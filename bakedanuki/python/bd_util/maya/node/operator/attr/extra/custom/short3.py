# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.short_compound.short3_compound.short3 import (
    Short3Field,
)


class ExtraShort3Field(Short3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
