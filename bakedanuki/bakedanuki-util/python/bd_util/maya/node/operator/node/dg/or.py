# coding: utf-8
from importlib import import_module

GeneratedOr = import_module(f"{__package__}._generated.or").GeneratedOr


class Or(GeneratedOr):
    __slots__ = ()

    NODE_TYPE = "or"
