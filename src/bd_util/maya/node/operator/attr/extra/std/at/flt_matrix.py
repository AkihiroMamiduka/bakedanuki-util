# coding: utf-8

# self
from ...define.std.at.flt_matrix import FltMatrixField


class ExtraFltMatrixField(FltMatrixField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
