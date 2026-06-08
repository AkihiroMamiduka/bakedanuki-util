# coding: utf-8

# self
from ....define.std.at.float_angle import FloatAngleField


class ExtraFloatAngleField(FloatAngleField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
