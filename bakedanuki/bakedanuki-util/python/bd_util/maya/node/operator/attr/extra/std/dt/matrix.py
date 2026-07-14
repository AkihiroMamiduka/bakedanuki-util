# coding: utf-8

# self
from ....define.std.dt.matrix import DataMatrixField


class ExtraDataMatrixField(DataMatrixField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
