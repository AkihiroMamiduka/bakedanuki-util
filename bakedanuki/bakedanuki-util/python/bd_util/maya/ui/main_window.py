# coding: utf-8
from typing import cast

from maya import OpenMayaUI as omui
from maya import cmds
from PySide6 import QtWidgets
from shiboken6 import wrapInstance


def get_main_window() -> QtWidgets.QWidget | None:
    """interactive Mayaのmain windowを取得する。"""
    # batch MayaとMaya初期化前ではUIへアクセスせずNoneを返す。
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
        QtWidgets.QWidget,
        wrapInstance(int(pointer), QtWidgets.QWidget),
    )
