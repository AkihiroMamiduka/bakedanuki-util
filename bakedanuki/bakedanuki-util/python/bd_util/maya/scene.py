# coding: utf-8

# maya
from maya import cmds


def new_scene():
    """現在のシーンを破棄し、保存確認なしで新規シーンを開く。"""
    cmds.file(newFile=True, force=True)
