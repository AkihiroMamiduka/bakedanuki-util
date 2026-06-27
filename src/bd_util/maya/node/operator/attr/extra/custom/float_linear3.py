# coding: utf-8

# self
from ...define.custom.at.scalar_compound.float_linear3 import (
    FloatLinear3Field,
)


class ExtraFloatLinear3Field(FloatLinear3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
