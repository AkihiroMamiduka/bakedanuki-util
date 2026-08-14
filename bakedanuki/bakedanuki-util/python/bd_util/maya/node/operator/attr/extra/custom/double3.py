# coding: utf-8
from typing import Any

# self
from ...define.custom import (
    Double3Field,
)


class ExtraDouble3Field(Double3Field):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
