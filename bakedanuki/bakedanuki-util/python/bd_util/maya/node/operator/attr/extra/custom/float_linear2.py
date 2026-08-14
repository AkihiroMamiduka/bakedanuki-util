# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    FloatLinear2Field,
)


class ExtraFloatLinear2Field(FloatLinear2Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
