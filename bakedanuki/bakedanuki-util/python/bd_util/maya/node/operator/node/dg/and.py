# coding: utf-8
from importlib import import_module

GeneratedAnd = import_module(
    f"{__package__}._generated.and"
).GeneratedAnd


class And(GeneratedAnd):
    __slots__ = ()

    NODE_TYPE = "and"
