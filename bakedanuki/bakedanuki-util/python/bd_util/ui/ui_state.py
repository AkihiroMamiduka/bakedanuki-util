# coding: utf-8
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import partial
from typing import TYPE_CHECKING, ClassVar

from .settings_path import SettingsPath
from . import qt
from ._ui_state_adapter import UiStateAdapter as _UiStateAdapter
from ._ui_state_adapter import UiStateValue, require_widget

if TYPE_CHECKING:
    from .float_step_profile import FloatStepProfile
    from .binding.float.view.range_slider_spin_box import (
        FloatRangeSliderSpinBox,
    )
    from .binding.float3.view.range_slider_spin_box import (
        Float3RangeSliderSpinBox,
    )

_STATE_KEY_PATTERN = re.compile(r"^[A-Za-z_]\w*$", re.ASCII)


@dataclass(frozen=True)
class _SplitterStateAdapter(_UiStateAdapter):
    """QSplitterの分割位置を保存・復元する。"""

    state_type: ClassVar[str] = "splitter"
    widget: qt.QtWidgets.QSplitter

    @property
    def state_object(self) -> qt.QtCore.QObject:
        """状態を所有するQSplitterを返す。"""
        return self.widget

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
class _TabWidgetStateAdapter(_UiStateAdapter):
    """QTabWidgetで現在選択されているタブを保存・復元する。"""

    state_type: ClassVar[str] = "tab_widget"
    widget: qt.QtWidgets.QTabWidget

    @property
    def state_object(self) -> qt.QtCore.QObject:
        """状態を所有するQTabWidgetを返す。"""
        return self.widget

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


@dataclass(frozen=True)
class _CheckableActionStateAdapter(_UiStateAdapter):
    """checkableなQActionのチェック状態を保存・復元する。"""

    state_type: ClassVar[str] = "checkable_action"
    action: qt.QAction

    @property
    def state_object(self) -> qt.QtCore.QObject:
        """状態を所有するQActionを返す。"""
        return self.action

    def save_state(self) -> int:
        """現在のチェック状態を0または1として取得する。"""
        return int(self.action.isChecked())

    def restore_state(
        self,
        settings: qt.QtCore.QSettings,
        state_key: str,
    ) -> bool:
        """保存値が0または1の場合だけQActionへ復元する。"""
        state = settings.value(state_key, -1, int)
        if not isinstance(state, int) or state not in (0, 1):
            return False
        self.action.setChecked(bool(state))
        return True


class UiStateManager:
    """登録したWidgetの内部状態をQSettingsへ保存・復元する。

    Splitter位置、選択タブ、checkable Actionなどを同じsettings pathで管理する。
    登録keyはASCII英字か`_`で始まり、以降は英数字か`_`を使用する。
    """

    SCHEMA_VERSION: ClassVar[int] = 1
    _STATE_GROUP: ClassVar[str] = "ui_state"
    _SCHEMA_VERSION_KEY: ClassVar[str] = "schema_version"
    _WIDGETS_GROUP: ClassVar[str] = "widgets"

    def __init__(
        self,
        settings: qt.QtCore.QSettings,
        settings_path: SettingsPath,
    ) -> None:
        """保存先とINI内のgroupを指定する。

        Args:
            settings: 保存先のQSettings。
            settings_path: tool名とgroup名を含むパス。
        """
        self._settings = settings
        self._settings_path = settings_path
        self._adapters: dict[str, _UiStateAdapter] = {}
        self._cached_states: dict[str, UiStateValue | None] = {}

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
        """Splitterの分割位置を保存対象として登録する。

        Args:
            key: manager内で一意な登録名。
            widget: 保存対象のQSplitter。

        Raises:
            TypeError: keyが文字列でない場合。
            ValueError: keyが無効か、登録済みの場合。
        """
        self._register(key, _SplitterStateAdapter(widget))

        # 操作中はメモリへ退避し、ファイルへの書き込みはsave時にまとめる。
        widget.splitterMoved.connect(partial(self._capture_state, key))
        self._capture_state(key)

    def register_tab_widget(
        self,
        key: str,
        widget: qt.QtWidgets.QTabWidget,
    ) -> None:
        """選択中のタブを保存対象として登録する。

        Args:
            key: manager内で一意な登録名。
            widget: 保存対象のQTabWidget。

        Raises:
            TypeError: keyが文字列でない場合。
            ValueError: keyが無効か、登録済みの場合。
        """
        self._register(key, _TabWidgetStateAdapter(widget))

        # タブ変更を退避しておき、Widget破棄後のsave_cachedでも利用する。
        widget.currentChanged.connect(partial(self._capture_state, key))
        self._capture_state(key)

    def register_checkable_action(
        self,
        key: str,
        action: qt.QAction,
    ) -> None:
        """checkableなQActionのチェック状態を登録する。

        Args:
            key: manager内で一意な登録名。
            action: `setCheckable(True)`を設定したQAction。

        Raises:
            TypeError: actionがQActionでないか、keyが文字列でない場合。
            ValueError: actionがcheckableでないか、keyが無効・登録済みの場合。
        """
        if not isinstance(action, qt.QAction):
            raise TypeError("actionにはQActionを指定してください")
        if not action.isCheckable():
            raise ValueError("actionにはcheckableなQActionを指定してください")
        self._register(key, _CheckableActionStateAdapter(action))

        # 切替時は状態だけを退避し、ファイルへの書き込みはsave時にまとめる。
        action.toggled.connect(partial(self._capture_state, key))
        self._capture_state(key)

    def save(self) -> bool:
        """生存中のWidgetの状態を収集して保存する。

        Returns:
            QSettingsへの同期に成功した場合は`True`。
        """
        # 全状態の収集を終えてから保存し、途中の失敗で既存値を壊さない。
        for key, adapter in self._adapters.items():
            if not adapter.is_available:
                continue

            try:
                state = adapter.save_state()
            except RuntimeError:
                # 状態取得中にC++ objectが破棄された場合は以前の保存値を維持する。
                if not adapter.is_available:
                    continue
                raise
            self._cached_states[key] = state

        # 収集に成功した最新状態をまとめて永続化する。
        return self.save_cached()

    def save_cached(self) -> bool:
        """変更時に退避した状態を、Widgetへ再アクセスせず保存する。

        Returns:
            QSettingsへの同期に成功した場合は`True`。
        """
        # 終了処理中のWidgetへ触れず、最後に退避できた状態だけを使う。
        collected_states = {
            key: (self._adapters[key], state)
            for key, state in self._cached_states.items()
            if key in self._adapters
        }

        # 状態収集後にsettings path配下の今回更新できるWidgetだけを書き換える。
        self._settings.beginGroup(self._settings_path.group_path)
        self._settings.beginGroup(self._STATE_GROUP)
        try:
            self._settings.setValue(
                self._SCHEMA_VERSION_KEY,
                self.SCHEMA_VERSION,
            )

            # 退避のないWidgetと別managerが保存したWidgetの状態は変更せず維持する。
            for key, (adapter, state) in collected_states.items():
                widget_group = f"{self._WIDGETS_GROUP}/{key}"
                self._settings.remove(widget_group)
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
        """保存済み状態を登録済みWidgetへ復元する。

        Returns:
            復元できたkeyの集合。未保存・型不一致・破棄済みは含まない。
        """
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
                if not adapter.is_available:
                    continue

                widget_group = f"{self._WIDGETS_GROUP}/{key}"
                state_type = self._settings.value(
                    f"{widget_group}/type",
                    "",
                    str,
                )
                if not state_type:
                    continue
                try:
                    state_restored = (
                        state_type == adapter.state_type
                        and adapter.restore_state(
                            self._settings,
                            f"{widget_group}/state",
                        )
                    )
                except RuntimeError:
                    # 復元中に破棄されたWidgetでは保存済み値を削除しない。
                    if not adapter.is_available:
                        continue
                    raise

                if not state_restored:
                    self._settings.remove(widget_group)
                    self._cached_states.pop(key, None)
                    removed_invalid_state = True
                    continue

                # 復元直後の状態を退避し、次のsignal前に破棄されても維持する。
                self._capture_state(key)
                restored_keys.add(key)
        finally:
            self._settings.endGroup()
            self._settings.endGroup()

        # 壊れた個別状態を削除した場合だけファイルへ同期する。
        if removed_invalid_state:
            self._settings.sync()
        return frozenset(restored_keys)

    def clear(self) -> bool:
        """このmanagerのUI stateだけを削除する。

        Returns:
            QSettingsへの同期に成功した場合は`True`。
        """
        # 同じsettings pathのgeometryなど、別の設定は残す。
        self._cached_states.clear()
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
        self._validate_key(key)
        assert isinstance(key, str)
        self._adapters[key] = adapter

    def _validate_key(self, key: object) -> None:
        """登録前に識別子の形式と重複を検証する。"""
        # QSettingsの階層を壊さない単純な固定識別子だけを許可する。
        if not isinstance(key, str):
            raise TypeError("UI state keyには文字列を指定してください")
        if not _STATE_KEY_PATTERN.fullmatch(key):
            raise ValueError(
                "UI state keyにはPython識別子として有効な名前を指定してください"
            )
        if key in self._adapters:
            raise ValueError(f"UI state keyは既に登録されています: {key}")

    def _capture_state(self, key: str, *_args: object) -> bool:
        """Widgetが生存中に最新状態をmemoryへ退避する。"""
        # signal発火元に対応する登録済みadapterだけを処理する。
        adapter = self._adapters.get(key)
        if adapter is None:
            return False

        if not adapter.is_available:
            return False

        try:
            state = adapter.save_state()
        except RuntimeError:
            # signal処理中にC++ objectが破棄された場合は以前の退避状態を維持する。
            if not adapter.is_available:
                return False
            raise

        # QSettingsへ頻繁に書き込まず、次回saveがまとめて永続化する。
        self._cached_states[key] = state
        return True

    def register_float_step_profile(
        self, key: str, profile: FloatStepProfile
    ) -> None:
        """Profileの複数のstep設定を一つのkeyで保存対象にする。

        Args:
            key: manager内で一意な登録名。
            profile: 生存中のFloatStepProfile。

        Raises:
            TypeError: profileの型またはkeyが不正な場合。
            ValueError: keyが無効か、登録済みの場合。
            RuntimeError: profileが破棄済みの場合。
        """
        from ._float_step_profile_state import FloatStepProfileStateAdapter
        from .float_step_profile import FloatStepProfile

        self._validate_key(key)
        candidate: object = profile
        if not isinstance(candidate, FloatStepProfile):
            raise TypeError("profileにはFloatStepProfileを指定してください")
        if not qt.isValid(candidate):
            raise RuntimeError("登録対象のProfileは破棄されています")
        self._register(key, FloatStepProfileStateAdapter(candidate))
        candidate.changed.connect(partial(self._capture_state, key))
        self._capture_state(key)

    def register_float_range_slider_spin_box(
        self, key: str, widget: FloatRangeSliderSpinBox
    ) -> None:
        """単一値ViewのMin・Max・step設定を保存対象にする。

        Args:
            key: manager内で一意な登録名。
            widget: 生存中のFloatRangeSliderSpinBox。

        Raises:
            TypeError: widgetの型またはkeyが不正な場合。
            ValueError: keyが無効か、登録済みの場合。
            RuntimeError: widgetが破棄済みの場合。
        """
        from ._float_view_state import FloatRangeStateAdapter

        self._validate_key(key)
        adapter = FloatRangeStateAdapter(widget)
        adapter.require_available()
        self._register(key, adapter)
        widget.settingsChanged.connect(partial(self._capture_state, key))
        self._capture_state(key)

    def register_float3_range_slider_spin_box(
        self, key: str, widget: Float3RangeSliderSpinBox
    ) -> None:
        """XYZの範囲設定を`key_x`・`key_y`・`key_z`へ登録する。

        Args:
            key: 3軸のkeyに共通する名前。生成されるkeyも未登録であること。
            widget: 生存中のFloat3RangeSliderSpinBox。

        Raises:
            TypeError: widgetの型またはkeyが不正な場合。
            ValueError: keyや生成されるkeyが無効・登録済みの場合。
            RuntimeError: widgetまたはいずれかの軸Viewが破棄済みの場合。
        """
        from .binding.float3.view.range_slider_spin_box import (
            Float3RangeSliderSpinBox,
        )
        from ._float_view_state import FloatRangeStateAdapter

        self._validate_key(key)
        require_widget(widget, Float3RangeSliderSpinBox)
        if not qt.isValid(widget):
            raise RuntimeError("登録対象のViewは破棄されています")
        entries = tuple(
            zip(
                (f"{key}_x", f"{key}_y", f"{key}_z"),
                (widget.x_editor, widget.y_editor, widget.z_editor),
            )
        )
        # 全軸を先に検証し、一部の軸だけが登録される状態を避ける。
        for axis_key, editor in entries:
            self._validate_key(axis_key)
            FloatRangeStateAdapter(editor).require_available()
        for axis_key, editor in entries:
            self.register_float_range_slider_spin_box(axis_key, editor)
