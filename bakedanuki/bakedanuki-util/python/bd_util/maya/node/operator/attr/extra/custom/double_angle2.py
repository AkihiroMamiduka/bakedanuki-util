# coding: utf-8

# self
from ...define.custom import (
    DoubleAngle2Field,
)


class ExtraDoubleAngle2Field(DoubleAngle2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
