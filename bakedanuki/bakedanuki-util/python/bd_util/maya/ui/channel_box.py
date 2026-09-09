# coding: utf-8
from maya import cmds


def get_channel_box_precision() -> int:
    """Change Precisionの設定を取得する。未設定・不正な値は標準の3桁を返す。"""
    if not cmds.optionVar(exists="channelsPrecision"):
        return 3
    precision: object = cmds.optionVar(query="channelsPrecision")
    # Maya標準のChange Precisionダイアログは1〜15桁を受け付ける。
    if (
        isinstance(precision, int)
        and not isinstance(precision, bool)
        and 1 <= precision <= 15
    ):
        return precision
    return 3
