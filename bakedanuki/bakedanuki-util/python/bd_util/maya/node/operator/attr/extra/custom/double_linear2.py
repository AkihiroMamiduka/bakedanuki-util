# coding: utf-8

# self
from ...define.custom import (
    DoubleLinear2Field,
)


class ExtraDoubleLinear2Field(DoubleLinear2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
