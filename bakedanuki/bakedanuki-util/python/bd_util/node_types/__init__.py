# coding: utf-8
"""型注釈にも利用できる Maya ノードクラスの公開入口。"""

from . import maya2025, maya2026, maya2027
from ._runtime import __getattr__ as __getattr__
from ._runtime import __dir__ as _runtime_dir
from ._runtime import available_class_names as available_class_names
from ._runtime import resolve as resolve


def __dir__() -> list[str]:
    """現在の Maya で参照できるノードクラス名を返す。"""
    return sorted(set(globals()) | set(_runtime_dir()))
