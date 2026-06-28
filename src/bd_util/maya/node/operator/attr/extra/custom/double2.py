# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.double_compound.double2_compound.double2 import (
    Double2Field,
)


class ExtraDouble2Field(Double2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
