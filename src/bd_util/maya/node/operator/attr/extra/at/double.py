# coding: utf-8

# self
from ...std.at.double import DoubleField


class ExtraDoubleField(DoubleField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
