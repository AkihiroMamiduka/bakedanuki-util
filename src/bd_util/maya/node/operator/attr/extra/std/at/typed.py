# coding: utf-8

# self
from ...define.std.at.typed import TypedField


class ExtraTypedField(TypedField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
