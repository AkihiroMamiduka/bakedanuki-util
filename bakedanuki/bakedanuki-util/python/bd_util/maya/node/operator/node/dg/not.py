# coding: utf-8
from importlib import import_module

GeneratedNot = import_module(f"{__package__}._generated.not").GeneratedNot


class Not(GeneratedNot):
    __slots__ = ()

    NODE_TYPE = "not"
