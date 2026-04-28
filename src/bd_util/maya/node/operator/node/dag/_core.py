# coding: utf-8
import maya.cmds as cmds

from .._core import Node


class DAG(Node):

    @property
    def long_name(self) -> str:
        """
        DAG ノードのロングネーム（フルパス）を返す。

        DAG ノードは同一シーン内に同名のノードが複数存在できるため、
        階層パスを含むロングネームで一意に識別する。

        例: ``|group1|nodeName``

        Returns:
            str: ロングネーム文字列
        """
        return cmds.ls(self.name, long=True)[0]
