# coding: utf-8

# maya
from maya import cmds


def new_scene():
    cmds.file(newFile=True, force=True)
