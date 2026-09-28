# coding: utf-8
from typing import Any

from ....define.std.at.scalar.unit.range.float_linear import FloatLinearField


class ExtraFloatLinearField(FloatLinearField):
    """`FloatLinearField` を追加属性として扱うフィールド。"""

    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
