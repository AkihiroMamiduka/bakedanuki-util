# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    DoubleLinear3Field,
)


class ExtraDoubleLinear3Field(DoubleLinear3Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
