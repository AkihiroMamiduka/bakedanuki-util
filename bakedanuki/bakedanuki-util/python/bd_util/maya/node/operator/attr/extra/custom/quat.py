# coding: utf-8

# self
from ...define.custom import (
    Quat4Field,
)


class ExtraQuat4Field(Quat4Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
