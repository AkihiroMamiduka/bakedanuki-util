# coding: utf-8
from abc import ABC, abstractmethod
from typing import ClassVar, TypeVar

from . import qt

UiStateValue = qt.QtCore.QByteArray | int
_Widget = TypeVar("_Widget", bound=qt.QWidget)


def require_widget(value: object, widget_type: type[_Widget]) -> _Widget:
    """公開登録APIの境界でWidgetの実行時の型を検証する。"""
    if not isinstance(value, widget_type):
        raise TypeError(f"widgetには{widget_type.__name__}を指定してください")
    return value


class UiStateAdapter(ABC):
    """1つのWidgetに対応する状態保存処理を定義する。"""

    state_type: ClassVar[str]

    @property
    def is_available(self) -> bool:
        """現在のWidgetから状態を取得・復元できるか返す。"""
        return qt.isValid(self.state_object)

    @property
    @abstractmethod
    def state_object(self) -> qt.QtCore.QObject:
        """状態を所有するQt objectを返す。"""
        raise NotImplementedError

    @abstractmethod
    def save_state(self) -> UiStateValue | None:
        """Widgetから保存可能な状態を取得する。"""
        raise NotImplementedError

    @abstractmethod
    def restore_state(
        self, settings: qt.QtCore.QSettings, state_key: str
    ) -> bool:
        """QSettingsから状態を読み取りWidgetへ復元する。"""
        raise NotImplementedError
