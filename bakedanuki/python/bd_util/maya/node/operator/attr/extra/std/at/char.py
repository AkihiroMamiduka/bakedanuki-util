# coding: utf-8

# self
from ....define.std.at.numeric_scalar_range.char import CharField


class ExtraCharField(CharField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
