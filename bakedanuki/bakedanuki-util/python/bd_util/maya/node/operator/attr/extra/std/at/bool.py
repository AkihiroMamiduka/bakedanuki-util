# coding: utf-8
from typing import Any

from ....define.std.at.scalar.numeric.bool import BoolField


class ExtraBoolField(BoolField):
    """`BoolField` を追加属性として扱うフィールド。"""

    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
