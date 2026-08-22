# coding: utf-8
import importlib
from collections.abc import Callable
from functools import partial
from typing import Protocol, cast

from maya import OpenMayaUI as omui
from maya import cmds

from ....logger import get_logger
from ....ui import ensure_window_on_screen as ensure_qt_window_on_screen
from ....ui import qt
from .options import DockArea

logger = get_logger(__name__)
maya_mixin = importlib.import_module("maya.app.general.mayaMixin")


class _QTimerType(Protocol):
    """PySide stub境界で使用するQTimer classの必要最小API。"""

    @staticmethod
    def singleShot(
        milliseconds: int,
        callback: Callable[[], None],
    ) -> None:
        """指定時間後にcallbackを一度だけ呼び出す。"""
        raise NotImplementedError


def _run_later(callback: Callable[[], None]) -> None:
    """次のQt event loopでcallbackを一度だけ呼び出す。"""
    # MayaによるworkspaceControlのlayout計算完了を0ms timerで待つ。
    timer_type = cast(_QTimerType, qt.QtCore.QTimer)
    timer_type.singleShot(0, callback)


def exists(name: str) -> bool:
    """指定したworkspaceControlが存在するか返す。"""
    # Maya commandのquery結果をboolへ揃える。
    return bool(cmds.workspaceControl(name, query=True, exists=True))


def restore(name: str) -> None:
    """workspaceControlを表示して現在のタブを前面へ移動する。"""
    # 非表示、折り畳み、背面タブの状態をMaya標準処理で復元する。
    cmds.workspaceControl(name, edit=True, restore=True)


def close(name: str) -> None:
    """workspaceControlを閉じる。"""
    # retain設定に応じたMaya標準のclose処理を実行する。
    cmds.workspaceControl(name, edit=True, close=True)


def is_floating(name: str) -> bool:
    """workspaceControlがfloating状態か返す。"""
    # Mayaが管理する現在の配置をqueryしてboolへ揃える。
    return bool(cmds.workspaceControl(name, query=True, floating=True))


def delete(name: str) -> None:
    """workspaceControlと格納されたWidgetを削除する。"""
    # controlとして削除し、通常のcloseと完全破棄を区別する。
    cmds.deleteUI(name, control=True)


def state_exists(name: str) -> bool:
    """workspaceControlの保存済み状態が存在するか返す。"""
    # Mayaがuser preferencesへ保持したstateの有無を問い合わせる。
    return bool(cmds.workspaceControlState(name, query=True, exists=True))


def remove_state(name: str) -> None:
    """workspaceControlの保存済み状態を削除する。"""
    # 次回生成時に初期DockOptionsが使われる状態へ戻す。
    cmds.workspaceControlState(name, remove=True)


def current_parent() -> int:
    """uiScript実行中の復元先workspaceControl pointerを返す。"""
    # Mayaが復元処理用に設定したcurrent parentを取得する。
    pointer = omui.MQtUtil.getCurrentParent()
    if not pointer:
        raise RuntimeError("workspaceControlの復元先を取得できません")
    return int(pointer)


def find_control(name: str) -> int:
    """Maya UI controlのpointerを名前から取得する。"""
    # Widgetの接続に利用できるMaya管理下のcontrolを検索する。
    pointer = omui.MQtUtil.findControl(name)
    if not pointer:
        raise RuntimeError(f"Maya UI controlを取得できません: {name}")
    return int(pointer)


def attach(window: qt.QtWidgets.QWidget, parent_pointer: int) -> None:
    """Widgetを指定workspaceControlへ接続する。"""
    # 固定objectNameからWidget pointerを解決してMaya layoutへ追加する。
    widget_pointer = find_control(window.objectName())
    omui.MQtUtil.addWidgetToMayaLayout(widget_pointer, parent_pointer)


def apply_allowed_area(
    window: qt.QtWidgets.QWidget,
    allowed_area: DockArea,
) -> bool:
    """親DockWidgetへ許可するドッキング領域を設定する。"""
    # Maya 2025のMixinがallowedAreaを適用しないためQt側のhostへ補完する。
    parent = window.parentWidget()
    if not isinstance(parent, qt.QtWidgets.QDockWidget):
        return False

    # 公開enumをQtのDockWidgetArea flagへ変換する。
    qt_area = {
        DockArea.TOP: qt.QtCore.Qt.DockWidgetArea.TopDockWidgetArea,
        DockArea.LEFT: qt.QtCore.Qt.DockWidgetArea.LeftDockWidgetArea,
        DockArea.RIGHT: qt.QtCore.Qt.DockWidgetArea.RightDockWidgetArea,
        DockArea.BOTTOM: qt.QtCore.Qt.DockWidgetArea.BottomDockWidgetArea,
        DockArea.ALL: qt.QtCore.Qt.DockWidgetArea.AllDockWidgetAreas,
    }[allowed_area]
    parent.setAllowedAreas(qt_area)
    return True


def _is_maya_main_window(widget: qt.QtWidgets.QWidget) -> bool:
    """WidgetがMayaのmain windowか返す。"""
    # floating外枠の誤判定でMaya本体を移動しないようC++ pointerを比較する。
    main_window_pointer = omui.MQtUtil.mainWindow()
    if not main_window_pointer:
        return False

    try:
        widget_pointers = qt.getCppPointer(widget)
    except (RuntimeError, TypeError):
        return False
    return bool(
        widget_pointers and int(widget_pointers[0]) == int(main_window_pointer)
    )


def find_floating_host(
    name: str,
    window: qt.QtWidgets.QWidget,
) -> qt.QtWidgets.QWidget | None:
    """workspaceControlを包むfloating最上位Widgetを返す。"""
    # Maya 2025では内容Widgetの直接の親がQWidgetになるため名前で接続を確認する。
    if not qt.isValid(window):
        return None
    workspace_widget = window.parent()
    if (
        not isinstance(workspace_widget, qt.QtWidgets.QWidget)
        or workspace_widget.objectName() != name
        or not qt.isValid(workspace_widget)
    ):
        return None

    # 親階層の最上位Windowだけを外枠とし、Maya本体は必ず対象外にする。
    floating_host = workspace_widget.window()
    if (
        floating_host is window
        or not qt.isValid(floating_host)
        or not floating_host.isWindow()
        or _is_maya_main_window(floating_host)
    ):
        return None
    return floating_host


def ensure_on_screen(
    name: str,
    window: qt.QtWidgets.QWidget,
) -> bool:
    """floating workspaceControlの外枠を現在のscreenへ補正する。"""
    # docked状態と破棄済みcontrolはMayaのlayout管理へ委ねる。
    if not qt.isValid(window) or not exists(name) or not is_floating(name):
        return False

    # Maya versionごとの中間Widget差を吸収し、floating最上位外枠だけを補正する。
    floating_host = find_floating_host(name, window)
    if floating_host is None:
        return False
    return ensure_qt_window_on_screen(floating_host)


def _ensure_on_screen_later(
    name: str,
    window: qt.QtWidgets.QWidget,
) -> None:
    """予約済みworkspaceControlの画面外補正を実行する。"""
    # 補正有無は自動処理では公開せず、明示APIだけboolを返す。
    ensure_on_screen(name, window)


def schedule_ensure_on_screen(
    name: str,
    window: qt.QtWidgets.QWidget,
) -> None:
    """workspaceControl接続後の画面外補正を予約する。"""
    # Mayaの保存配置が外枠へ反映された後にfloating状態とgeometryを確認する。
    _run_later(partial(_ensure_on_screen_later, name, window))


def register(name: str, window: qt.QtWidgets.QWidget) -> None:
    """Maya mixinへworkspaceControlとWidgetの対応を登録する。"""
    # 復元後もdock closeとfloating変更のcallbackが届くよう対応を保持する。
    registry = cast(
        dict[str, qt.QtWidgets.QWidget],
        maya_mixin.mixinWorkspaceControls,
    )
    registry[name] = window


def unregister(name: str) -> None:
    """Maya mixinからworkspaceControlの登録を解除する。"""
    # 完全破棄後に古いWidgetへcallbackが送られないよう参照を外す。
    registry = cast(
        dict[str, qt.QtWidgets.QWidget],
        maya_mixin.mixinWorkspaceControls,
    )
    registry.pop(name, None)


def tab_to(name: str, target: str) -> bool:
    """workspaceControlを対象controlのタブとして配置する。"""
    # 対象が存在しない環境では現在のドッキング位置を維持する。
    if not exists(target):
        logger.warning(
            "タブ化するworkspaceControlが見つかりません: %s", target
        )
        return False

    # -1を指定して既存タブ列の末尾へ追加する。
    cmds.workspaceControl(
        name,
        edit=True,
        tabToControl=(target, -1),
    )
    return True
