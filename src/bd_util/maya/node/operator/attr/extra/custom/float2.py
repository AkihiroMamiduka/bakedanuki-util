# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.float_compound.float2 import (
    Float2Field,
)


class ExtraFloat2Field(Float2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
