# coding: utf-8

# self
from ...define.custom.at.scalar_compound.unit_compound.angle_compound.float2.float_angle2 import (
    FloatAngle2Field,
)


class ExtraFloatAngle2Field(FloatAngle2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
