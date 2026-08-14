# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    Short3Field,
)


class ExtraShort3Field(Short3Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
