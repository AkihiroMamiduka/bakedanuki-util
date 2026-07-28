# coding: utf-8

# self
from ...define.custom import (
    Float3Field,
)


class ExtraFloat3Field(Float3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
