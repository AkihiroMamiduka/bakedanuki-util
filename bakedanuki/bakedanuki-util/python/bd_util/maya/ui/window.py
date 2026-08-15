# coding: utf-8
from collections.abc import Callable
from typing import TypeVar

from PySide6 import QtWidgets

from ...ui import WindowController
from .main_window import get_main_window

WindowT = TypeVar("WindowT", bound=QtWidgets.QWidget)


class MayaWindowController(WindowController[WindowT]):
    """Maya main windowをfactoryへ渡して1つのwindowを管理する。"""

    def __init__(
        self,
        factory: Callable[[QtWidgets.QWidget | None], WindowT],
    ) -> None:
        """Maya main windowを受け取るfactoryで初期化する。"""
        # window生成時までMaya main windowの取得を遅延する。
        self._maya_factory = factory
        super().__init__(self._create_window)

    def _create_window(self) -> WindowT:
        """現在のMaya main windowを親としてwindowを生成する。"""
        # 生成のたびに最新のMaya main windowをfactoryへ渡す。
        return self._maya_factory(get_main_window())
