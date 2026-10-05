# coding: utf-8
"""接続済み属性の標準値入力で共有する編集可否の照会。"""

from maya.api import OpenMaya as om

from ._connected_plug_write import inspect_connected_plug

__all__ = ["connected_plug_edit_reason"]


def connected_plug_edit_reason(plug: om.MPlug) -> str | None:
    """対応する接続済み属性なら`None`、編集不可なら理由を返す。

    通常の時間カーブ、Driven Key、Animation Layer の値入力を検証します。
    接続やキーは変更しません。未接続の属性はこの照会の対象外です。

    Args:
        plug: 入力接続を持つ数値・角度・距離・bool・enum の属性。

    Returns:
        編集不可の理由。対応する接続なら`None`。
    """
    try:
        inspect_connected_plug(plug)
    except RuntimeError as error:
        return str(error)
    return None
