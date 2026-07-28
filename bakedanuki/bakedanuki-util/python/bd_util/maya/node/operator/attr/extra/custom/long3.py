# coding: utf-8

# self
from ...define.custom import (
    Long3Field,
)


class ExtraLong3Field(Long3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
