# coding: utf-8
from typing import cast

from maya import OpenMayaUI as omui
from maya import cmds

from ...ui import qt


def get_main_window() -> qt.QtWidgets.QWidget | None:
    """Mayaのmain windowをQt Widgetとして取得する。

    Returns:
        interactive Mayaのmain window。batchまたは未初期化なら`None`。
    """
    # batch・未初期化環境ではMaya UI APIへ進まない。
    try:
        if cmds.about(batch=True):
            return None
    except AttributeError:
        return None

    # Mayaが保持するmain windowのpointerを取得する。
    pointer = omui.MQtUtil.mainWindow()
    if not pointer:
        return None

    # C++側のpointerをPySide6のQWidget wrapperへ変換する。
    return cast(
        qt.QtWidgets.QWidget,
        qt.wrapInstance(int(pointer), qt.QtWidgets.QWidget),
    )
