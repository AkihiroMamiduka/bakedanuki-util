# coding: utf-8

# self
from ....define.std.dt.vector_array import DataVectorArrayField


class ExtraDataVectorArrayField(DataVectorArrayField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
