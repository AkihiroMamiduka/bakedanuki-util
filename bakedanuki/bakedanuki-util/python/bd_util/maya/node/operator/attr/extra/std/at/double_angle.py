# coding: utf-8

# self
from ....define.std.at.scalar.unit.range.double_angle import DoubleAngleField


class ExtraDoubleAngleField(DoubleAngleField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
