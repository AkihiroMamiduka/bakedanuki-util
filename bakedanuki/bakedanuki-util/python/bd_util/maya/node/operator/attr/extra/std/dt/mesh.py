# coding: utf-8
from typing import Any

# self
from ....define.std.dt.mesh import DataMeshField


class ExtraDataMeshField(DataMeshField):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
