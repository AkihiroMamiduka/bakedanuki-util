# coding: utf-8
from importlib import import_module

_GeneratedAnd = import_module(
    f"{__package__}._generated.and"
)._GeneratedAnd


class And(_GeneratedAnd):
    __slots__ = ()

    NODE_TYPE = "and"
