# coding: utf-8
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import ClassVar

from .settings_path import SettingsPath
from . import qt

UiStateValue = qt.QtCore.QByteArray | int
_STATE_KEY_PATTERN = re.compile(r"^[A-Za-z_]\w*$", re.ASCII)


class _UiStateAdapter(ABC):
    """1つのWidgetに対応する状態保存処理を定義する。"""

    state_type: ClassVar[str]

    @abstractmethod
    def save_state(self) -> UiStateValue | None:
        """Widgetから保存可能な状態を取得する。"""
        raise NotImplementedError

    @abstractmethod
    def restore_state(
        self,
        settings: qt.QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """QSettingsから状態を読み取りWidgetへ復元する。"""
        raise NotImplementedError


@dataclass(frozen=True)
class _SplitterStateAdapter(_UiStateAdapter):
    """QSplitterの分割位置を保存・復元する。"""

    state_type: ClassVar[str] = "splitter"
    widget: qt.QtWidgets.QSplitter

    def save_state(self) -> qt.QtCore.QByteArray:
        """QSplitterの現在の状態を取得する。"""
        # Qt標準形式を使い、orientationや各領域のサイズをまとめて保存する。
        return self.widget.saveState()

    def restore_state(
        self,
        settings: qt.QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """保存済みのQSplitter状態を復元する。"""
        # INI内の値をQByteArrayとして読み取り、Qt標準処理へ渡す。
        state = settings.value(
            state_key,
            qt.QtCore.QByteArray(),
            qt.QtCore.QByteArray,
        )
        if not isinstance(state, qt.QtCore.QByteArray) or state.isEmpty():
            return False
        return self.widget.restoreState(state)


@dataclass(frozen=True)
class _HeaderStateAdapter(_UiStateAdapter):
    """QHeaderViewの列幅と表示順を保存・復元する。"""

    state_type: ClassVar[str] = "header"
    widget: qt.QtWidgets.QHeaderView

    def save_state(self) -> qt.QtCore.QByteArray:
        """QHeaderViewの現在の状態を取得する。"""
        # Qt標準形式を使い、列幅や並び順などをまとめて保存する。
        return self.widget.saveState()

    def restore_state(
        self,
        settings: qt.QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """保存済みのQHeaderView状態を復元する。"""
        # INI内の値をQByteArrayとして読み取り、Qt標準処理へ渡す。
        state = settings.value(
            state_key,
            qt.QtCore.QByteArray(),
            qt.QtCore.QByteArray,
        )
        if not isinstance(state, qt.QtCore.QByteArray) or state.isEmpty():
            return False
        return self.widget.restoreState(state)


@dataclass(frozen=True)
class _TabWidgetStateAdapter(_UiStateAdapter):
    """QTabWidgetで現在選択されているタブを保存・復元する。"""

    state_type: ClassVar[str] = "tab_widget"
    widget: qt.QtWidgets.QTabWidget

    def save_state(self) -> int | None:
        """QTabWidgetの現在のindexを取得する。"""
        # タブが存在しない場合は復元できる状態がないため保存対象外にする。
        index = self.widget.currentIndex()
        return None if index < 0 else index

    def restore_state(
        self,
        settings: qt.QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """保存済みの選択タブを復元する。"""
        # 現在のタブ数で有効なindexだけをWidgetへ反映する。
        index = settings.value(state_key, -1, int)
        if not isinstance(index, int) or not 0 <= index < self.widget.count():
            return False
        self.widget.setCurrentIndex(index)
        return True


class UiStateManager:
    """明示登録されたWidgetの内部状態をQSettingsで管理する。"""

    SCHEMA_VERSION: ClassVar[int] = 1
    _STATE_GROUP: ClassVar[str] = "ui_state"
    _SCHEMA_VERSION_KEY: ClassVar[str] = "schema_version"
    _WIDGETS_GROUP: ClassVar[str] = "widgets"

    def __init__(
        self,
        settings: qt.QtCore.QSettings,
        settings_path: SettingsPath,
    ) -> None:
        """保存先QSettingsとsettings pathを受け取って初期化する。"""
        # 保存先とWidgetごとのadapterを保持する。
        self._settings = settings
        self._settings_path = settings_path
        self._adapters: dict[str, _UiStateAdapter] = {}

    @property
    def settings_path(self) -> SettingsPath:
        """UI stateの保存先を表すsettings pathを返す。"""
        # 初期化時に検証済みのSettingsPathをそのまま公開する。
        return self._settings_path

    @property
    def file_name(self) -> str:
        """QSettingsが使用するファイル名を返す。"""
        # 実際にQSettingsが解決した保存先を取得する。
        return self._settings.fileName()

    @property
    def registered_keys(self) -> tuple[str, ...]:
        """現在登録されているstate keyを返す。"""
        # 登録順を保ったimmutableな値として公開する。
        return tuple(self._adapters)

    def register_splitter(
        self,
        key: str,
        widget: qt.QtWidgets.QSplitter,
    ) -> None:
        """QSplitterの分割位置を保存対象として登録する。"""
        # Splitter専用adapterを共通登録処理へ渡す。
        self._register(key, _SplitterStateAdapter(widget))

    def register_header(
        self,
        key: str,
        widget: qt.QtWidgets.QHeaderView,
    ) -> None:
        """QHeaderViewの列幅と表示順を保存対象として登録する。"""
        # Header専用adapterを共通登録処理へ渡す。
        self._register(key, _HeaderStateAdapter(widget))

    def register_tab_widget(
        self,
        key: str,
        widget: qt.QtWidgets.QTabWidget,
    ) -> None:
        """QTabWidgetの選択タブを保存対象として登録する。"""
        # TabWidget専用adapterを共通登録処理へ渡す。
        self._register(key, _TabWidgetStateAdapter(widget))

    def save(self) -> bool:
        """登録済みWidgetの現在の内部状態を保存する。"""
        # settings path配下のui_state groupだけを今回の登録内容で更新する。
        self._settings.beginGroup(self._settings_path.group_path)
        self._settings.beginGroup(self._STATE_GROUP)
        try:
            self._settings.setValue(
                self._SCHEMA_VERSION_KEY,
                self.SCHEMA_VERSION,
            )

            # 登録済みkeyだけを更新し、別managerが保存したWidget状態は維持する。
            for key, adapter in self._adapters.items():
                widget_group = f"{self._WIDGETS_GROUP}/{key}"
                self._settings.remove(widget_group)
                state = adapter.save_state()
                if state is None:
                    continue

                # adapterの型識別子とQtが生成した状態値を保存する。
                self._settings.setValue(
                    f"{widget_group}/type",
                    adapter.state_type,
                )
                self._settings.setValue(f"{widget_group}/state", state)
        finally:
            self._settings.endGroup()
            self._settings.endGroup()

        # Maya終了前にも反映されるよう変更内容を即座に同期する。
        self._settings.sync()
        return self._settings.status() == qt.QtCore.QSettings.Status.NoError

    def restore(self) -> frozenset[str]:
        """保存済み状態を登録済みWidgetへ復元し、成功したkeyを返す。"""
        restored_keys: set[str] = set()
        removed_invalid_state = False

        # manager専用groupからschemaとWidgetごとの状態を読み取る。
        self._settings.beginGroup(self._settings_path.group_path)
        self._settings.beginGroup(self._STATE_GROUP)
        try:
            if not self._settings.contains(self._SCHEMA_VERSION_KEY):
                return frozenset()
            schema_version = self._settings.value(
                self._SCHEMA_VERSION_KEY,
                -1,
                int,
            )
            if schema_version != self.SCHEMA_VERSION:
                return frozenset()

            # 登録済みの型と保存時の型が一致する状態だけを復元する。
            for key, adapter in self._adapters.items():
                widget_group = f"{self._WIDGETS_GROUP}/{key}"
                state_type = self._settings.value(
                    f"{widget_group}/type",
                    "",
                    str,
                )
                if not state_type:
                    continue
                if (
                    state_type != adapter.state_type
                    or not adapter.restore_state(
                        self._settings,
                        f"{widget_group}/state",
                    )
                ):
                    self._settings.remove(widget_group)
                    removed_invalid_state = True
                    continue
                restored_keys.add(key)
        finally:
            self._settings.endGroup()
            self._settings.endGroup()

        # 壊れた個別状態を削除した場合だけファイルへ同期する。
        if removed_invalid_state:
            self._settings.sync()
        return frozenset(restored_keys)

    def clear(self) -> bool:
        """管理対象のUI stateをすべて削除する。"""
        # geometryなど同じsettings pathにある他の情報を残して専用groupだけ削除する。
        self._settings.beginGroup(self._settings_path.group_path)
        try:
            self._settings.remove(self._STATE_GROUP)
        finally:
            self._settings.endGroup()

        # 削除結果をファイルへ反映して成否を返す。
        self._settings.sync()
        return self._settings.status() == qt.QtCore.QSettings.Status.NoError

    def _register(self, key: object, adapter: _UiStateAdapter) -> None:
        """検証済みのkeyでWidget adapterを登録する。"""
        # QSettingsの階層を壊さない単純な固定識別子だけを許可する。
        if not isinstance(key, str):
            raise TypeError("UI state keyには文字列を指定してください")
        if not _STATE_KEY_PATTERN.fullmatch(key):
            raise ValueError(
                "UI state keyにはPython識別子として有効な名前を指定してください"
            )
        if key in self._adapters:
            raise ValueError(f"UI state keyは既に登録されています: {key}")

        # 呼び出し順を維持したdictへadapterを追加する。
        self._adapters[key] = adapter
