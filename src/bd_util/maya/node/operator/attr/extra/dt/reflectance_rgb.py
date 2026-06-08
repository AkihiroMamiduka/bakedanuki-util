# coding: utf-8

# self
from ...std.dt.reflectance_rgb import DataReflectanceRGBField


class ExtraDataReflectanceRGBField(DataReflectanceRGBField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
