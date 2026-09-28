# coding: utf-8
from typing import Any

from ...define.custom import (
    FloatLinear2Field,
)


class ExtraFloatLinear2Field(FloatLinear2Field):
    """`FloatLinear2Field` を追加属性として扱うフィールド。"""

    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
