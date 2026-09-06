# coding: utf-8
"""1つのBoolViewModelを複数Windowで共有するsample。"""

# 共通dataを再公開し、Managerを明示的に生成する入口を用意する。
from ..data import VisibilityData
from .manager import SharedBoolViewsManager
from .widget import SharedBoolViewsWidget
from .window import SharedBoolViewsWindow

__all__ = [
    "SharedBoolViewsManager",
    "SharedBoolViewsWidget",
    "SharedBoolViewsWindow",
    "VisibilityData",
]
