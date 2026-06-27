# coding: utf-8

# self
from ...define.custom.at.scalar_compound.unit_compound.angle_compound.float_angle3 import (
    FloatAngle3Field,
)


class ExtraFloatAngle3Field(FloatAngle3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
