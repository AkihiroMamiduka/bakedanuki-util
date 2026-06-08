# coding: utf-8
# self
from ....define.std.at.enum import EnumField


class ExtraEnumField(EnumField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
