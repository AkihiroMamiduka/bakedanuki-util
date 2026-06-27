# coding: utf-8

# self
from ...define.custom.at.numeric_compound_base.double3 import Double3Field


class ExtraDouble3Field(Double3Field):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
