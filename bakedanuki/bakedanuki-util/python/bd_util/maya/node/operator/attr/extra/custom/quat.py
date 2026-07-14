# coding: utf-8

# self
from ...define.custom.at.scalar_compound.numeric_compound.double_compound.double4_compound.quat_compound.quat import (
    Quat4Field,
)


class ExtraQuat4Field(Quat4Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
