# coding: utf-8

# self
from ...define.custom.at.scalar_compound.unit_compound.linear_compound.double_linear3 import (
    DoubleLinear3Field,
)


class ExtraDoubleLinear3Field(DoubleLinear3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
