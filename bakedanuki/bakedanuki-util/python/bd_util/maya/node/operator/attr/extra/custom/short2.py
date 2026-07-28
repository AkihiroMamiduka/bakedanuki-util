# coding: utf-8

# self
from ...define.custom import (
    Short2Field,
)


class ExtraShort2Field(Short2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
