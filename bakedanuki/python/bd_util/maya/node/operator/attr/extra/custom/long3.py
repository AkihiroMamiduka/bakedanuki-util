# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.long_compound.long3_compound.long3 import (
    Long3Field,
)


class ExtraLong3Field(Long3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
