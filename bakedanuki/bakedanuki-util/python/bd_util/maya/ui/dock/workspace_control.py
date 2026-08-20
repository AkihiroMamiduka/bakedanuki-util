# coding: utf-8
import importlib
from typing import cast

from maya import OpenMayaUI as omui
from maya import cmds

from ....logger import get_logger
from ....ui import qt
from .options import DockArea

logger = get_logger(__name__)
maya_mixin = importlib.import_module("maya.app.general.mayaMixin")


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
