# coding: utf-8

# self
from ...define.custom import (
    Double4Field,
)


class ExtraDouble4Field(Double4Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
