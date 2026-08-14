# coding: utf-8
from typing import Any

# self
from ....define.std.dt.vector_array import DataVectorArrayField


class ExtraDataVectorArrayField(DataVectorArrayField):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
