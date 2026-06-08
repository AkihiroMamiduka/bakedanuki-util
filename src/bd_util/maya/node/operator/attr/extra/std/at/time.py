# coding: utf-8

# self
from ....define.std.at.time import TimeField


class ExtraTimeField(TimeField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
