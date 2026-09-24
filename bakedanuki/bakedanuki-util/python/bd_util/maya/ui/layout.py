# coding: utf-8
from __future__ import annotations

from typing import Protocol, TypeVar, overload, runtime_checkable

from ...ui import SettingsPath, qt
from .dock import MayaDockableWindow, MayaDockableWindowController
from .settings import create_ui_state_manager, create_window_state_store
from .window import MayaWindowController

WindowT = TypeVar("WindowT", bound=qt.QtWidgets.QWidget)
DockWindowT = TypeVar("DockWindowT", bound=MayaDockableWindow)


class _DisposableUiController(Protocol):
    """統合resetで必要なcontrollerの共通破棄API。"""

    def dispose(self) -> None:
        """管理中のWindowを完全破棄する。"""
        raise NotImplementedError


class _ShowableUiController(_DisposableUiController, Protocol):
    """統合reset後にWindowを再表示できるcontroller。"""

    def show(self) -> qt.QtWidgets.QWidget:
        """Windowを生成または再表示して返す。"""
        raise NotImplementedError


@runtime_checkable
class _WorkspaceStateController(Protocol):
    """Maya workspaceControlの保存配置を削除できるcontroller。"""

    def reset_workspace_state(self) -> None:
        """WindowとworkspaceControlの保存済み配置を削除する。"""
        raise NotImplementedError


@overload
def reset_ui_layout(
    controller: MayaWindowController[WindowT],
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> bool: ...


@overload
def reset_ui_layout(
    controller: MayaDockableWindowController[DockWindowT],
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> bool: ...


def reset_ui_layout(
    controller: _DisposableUiController,
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> bool:
    """Windowを破棄し、指定したUI配置の保存値を削除する。

    Args:
        controller: 通常Windowまたはdockable Windowのcontroller。
        settings_path: 削除するtoolとgroup。通常Windowでは保存先と一致させる。
        clear_window_state: geometryなどのWindow状態を削除するか。
        clear_widget_state: SplitterなどのWidget内部状態を削除するか。

    Returns:
        指定したINI状態をすべて削除できた場合は`True`。

    Raises:
        ValueError: 通常Windowの保存先とsettings_pathが異なる場合。
    """
    return _reset_ui_layout(
        controller,
        settings_path,
        clear_window_state=clear_window_state,
        clear_widget_state=clear_widget_state,
    )


@overload
def reset_and_show_ui_layout(
    controller: MayaWindowController[WindowT],
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> WindowT: ...


@overload
def reset_and_show_ui_layout(
    controller: MayaDockableWindowController[DockWindowT],
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> DockWindowT: ...


def reset_and_show_ui_layout(
    controller: _ShowableUiController,
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool = True,
    clear_widget_state: bool = True,
) -> qt.QtWidgets.QWidget:
    """UI配置を削除し、初期状態のWindowを表示する。

    Args:
        controller: 通常Windowまたはdockable Windowのcontroller。
        settings_path: 削除するtoolとgroup。通常Windowでは保存先と一致させる。
        clear_window_state: geometryなどのWindow状態を削除するか。
        clear_widget_state: SplitterなどのWidget内部状態を削除するか。

    Returns:
        再生成して表示した具体型のWindow。

    Raises:
        ValueError: 通常Windowの保存先とsettings_pathが異なる場合。
        RuntimeError: INI状態の削除に失敗した場合。
    """
    # 削除失敗時に古い配置を復元しないよう、再表示は成功後だけにする。
    if not _reset_ui_layout(
        controller,
        settings_path,
        clear_window_state=clear_window_state,
        clear_widget_state=clear_widget_state,
    ):
        raise RuntimeError(
            f"UI配置をリセットできなかったため再表示しません: {settings_path}"
        )

    return controller.show()


def _reset_ui_layout(
    controller: _DisposableUiController,
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool,
    clear_widget_state: bool,
) -> bool:
    """controller破棄後に指定された保存済みUI配置を削除する。"""
    # controllerを破棄する前に保存先を確定し、取り違えを検出する。
    resolved_path = SettingsPath.from_value(settings_path)
    if (
        clear_window_state
        and isinstance(controller, MayaWindowController)
        and controller.settings_path is not None
        and controller.settings_path != resolved_path
    ):
        raise ValueError(
            "settings_pathはMayaWindowControllerの保存先と一致させてください"
        )

    window_state_store = (
        create_window_state_store(resolved_path)
        if clear_window_state
        else None
    )
    ui_state_manager = (
        create_ui_state_manager(resolved_path) if clear_widget_state else None
    )

    # dockable WindowはMayaのworkspace stateも一緒に消す。
    if isinstance(controller, _WorkspaceStateController):
        controller.reset_workspace_state()
    else:
        controller.dispose()

    # 破棄に伴う最終保存が終わってからINIを消し、古い状態の復活を防ぐ。
    clear_results: list[bool] = []
    if window_state_store is not None:
        clear_results.append(window_state_store.clear())
    if ui_state_manager is not None:
        clear_results.append(ui_state_manager.clear())
    return all(clear_results)
