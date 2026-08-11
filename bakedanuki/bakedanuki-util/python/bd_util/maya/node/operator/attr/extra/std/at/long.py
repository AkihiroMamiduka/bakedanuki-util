# coding: utf-8
from typing import Any

# self
from ....define.std.at.scalar.numeric.range.long import LongField


class ExtraLongField(LongField):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.extra = True
