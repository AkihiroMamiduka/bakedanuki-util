# coding: utf-8

# self
from ...std.dt.specrtrum_rgb import DataSpectrumRGBField


class ExtraDataSpectrumRGBField(DataSpectrumRGBField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
