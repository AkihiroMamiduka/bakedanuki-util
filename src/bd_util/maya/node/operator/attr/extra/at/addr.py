# coding: utf-8

# self
from ...std.at.addr import AddrField


class ExtraAddrField(AddrField):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.extra = True
