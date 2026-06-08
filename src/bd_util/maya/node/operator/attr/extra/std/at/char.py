# coding: utf-8

# self
from ...define.std.at.char import CharField


class ExtraCharField(CharField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
