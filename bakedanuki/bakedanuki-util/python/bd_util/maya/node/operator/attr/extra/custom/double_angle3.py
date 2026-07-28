# coding: utf-8

# self
from ...define.custom import (
    DoubleAngle3Field,
)


class ExtraDoubleAngle3Field(DoubleAngle3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
