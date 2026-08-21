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
    """Windowを破棄し、MayaとINIに保存されたUI配置をまとめて削除する。"""
    # close-onlyの低レベルAPIとして共通reset処理の成否を返す。
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
    """UI配置をリセットし、初期状態のWindowを生成して返す。"""
    # reset失敗時は古い保存値を復元する可能性があるため再表示しない。
    if not _reset_ui_layout(
        controller,
        settings_path,
        clear_window_state=clear_window_state,
        clear_widget_state=clear_widget_state,
    ):
        raise RuntimeError(
            f"UI配置をリセットできなかったため再表示しません: {settings_path}"
        )

    # controllerが保持する具体的なWindow型を初期配置で再生成する。
    return controller.show()


def _reset_ui_layout(
    controller: _DisposableUiController,
    settings_path: str | SettingsPath,
    *,
    clear_window_state: bool,
    clear_widget_state: bool,
) -> bool:
    """controller破棄後に指定された保存済みUI配置を削除する。"""
    # controllerを変更する前にsettings pathと保存先を検証して初期化する。
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

    # dockable Windowでは完全破棄に加えてMayaのworkspace stateも削除する。
    if isinstance(controller, _WorkspaceStateController):
        controller.reset_workspace_state()
    else:
        controller.dispose()

    # dispose時の最終保存後にINIをclearし、保存値が復活しない順序を維持する。
    clear_results: list[bool] = []
    if window_state_store is not None:
        clear_results.append(window_state_store.clear())
    if ui_state_manager is not None:
        clear_results.append(ui_state_manager.clear())
    return all(clear_results)
