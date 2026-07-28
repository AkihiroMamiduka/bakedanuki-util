# coding: utf-8

# self
from ...define.custom import (
    FloatLinear3Field,
)


class ExtraFloatLinear3Field(FloatLinear3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
