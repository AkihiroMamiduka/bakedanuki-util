# coding: utf-8

# maya
from maya import cmds


def new_scene():
    cmds.file(new=True, force=True)
