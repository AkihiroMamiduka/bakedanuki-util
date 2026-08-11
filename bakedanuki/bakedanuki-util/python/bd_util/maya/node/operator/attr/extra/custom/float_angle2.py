# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    FloatAngle2Field,
)


class ExtraFloatAngle2Field(FloatAngle2Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
