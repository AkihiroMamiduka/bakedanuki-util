# coding: utf-8

# self
from ...define.custom import (
    Long2Field,
)


class ExtraLong2Field(Long2Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
