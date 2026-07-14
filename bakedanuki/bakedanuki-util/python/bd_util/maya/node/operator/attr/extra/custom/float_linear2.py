# coding: utf-8

# self
from ...define.custom.at.scalar_compound.unit_compound.linear_compound.float2.float_linear2 import (
    FloatLinear2Field,
)


class ExtraFloatLinear2Field(FloatLinear2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
