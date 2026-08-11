# coding: utf-8
from typing import Any

# self
from ....define.std.dt.double_array import DataDoubleArrayField


class ExtraDataDoubleArrayField(DataDoubleArrayField):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
