# coding: utf-8

# self
from ...std.dt.lattice import DataLatticeField


class ExtraDataLatticeField(DataLatticeField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
