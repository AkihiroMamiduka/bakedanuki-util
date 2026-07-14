# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.double4 import (
    Double4Field,
)


class ExtraDouble4Field(Double4Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
