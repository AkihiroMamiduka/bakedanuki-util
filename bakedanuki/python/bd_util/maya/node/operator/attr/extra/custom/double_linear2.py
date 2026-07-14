# coding: utf-8

# self
from ...define.custom.at.scalar_compound.unit_compound.linear_compound.double2.double_linear2 import (
    DoubleLinear2Field,
)


class ExtraDoubleLinear2Field(DoubleLinear2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
