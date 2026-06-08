# coding: utf-8

# self
from ...std.dt.mesh import DataMeshField


class ExtraDataMeshField(DataMeshField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
