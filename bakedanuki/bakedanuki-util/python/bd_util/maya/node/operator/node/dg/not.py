# coding: utf-8
from importlib import import_module

_GeneratedNot = import_module(
    f"{__package__}._generated.not"
)._GeneratedNot


class Not(_GeneratedNot):
    __slots__ = ()

    NODE_TYPE = "not"
