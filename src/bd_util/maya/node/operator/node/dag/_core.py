# coding: utf-8
import maya.cmds as cmds

from .._core import Node


class DAG(Node):
    __slots__ = ("long_name",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.long_name: str = cmds.ls(self.name, long=True)[0]

    @property
    def _cmd_access_name(self):
        return self.long_name

    def rename(self, **kwargs) -> str:
        new_name = super().rename(**kwargs)
        # rename 後のロングネームを更新
        self.long_name: str = cmds.ls(self.name, long=True)[0]
        return new_name
