# coding: utf-8
"""複数bool属性の編集と、変更通知によるUI連動のサンプル。"""

from .data import DisplayOptionsData
from .widget import DisplayOptionsWidget
from .window import DisplayOptionsWindow, dispose, show

__all__ = [
    "DisplayOptionsData",
    "DisplayOptionsWidget",
    "DisplayOptionsWindow",
    "dispose",
    "show",
]
