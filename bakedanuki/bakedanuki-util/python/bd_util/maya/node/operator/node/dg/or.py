# coding: utf-8
from importlib import import_module

_GeneratedOr = import_module(
    f"{__package__}._generated.or"
)._GeneratedOr


class Or(_GeneratedOr):
    __slots__ = ()

    NODE_TYPE = "or"
