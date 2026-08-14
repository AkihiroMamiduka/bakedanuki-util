# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    DoubleAngle3Field,
)


class ExtraDoubleAngle3Field(DoubleAngle3Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
