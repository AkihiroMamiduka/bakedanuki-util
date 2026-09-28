# coding: utf-8
from typing import Any

from ....define.std.at.generic import GenericField


class ExtraGenericField(GenericField):
    """`GenericField` を追加属性として扱うフィールド。"""

    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
