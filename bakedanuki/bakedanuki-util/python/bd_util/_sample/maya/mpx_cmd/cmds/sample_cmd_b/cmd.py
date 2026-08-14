# coding: utf-8

"""
plugin から呼ばれるコマンド本体。
このモジュール内では、相対import を使用して、コマンドを実装することができる。
"""

# maya
from maya import OpenMaya as om

# self
from ......maya.mpx_cmd.base.cmd import MPxCommandBase
from . import some_cmd


class BDUSampleCommandB(MPxCommandBase):
    COMMAND_NAME = "bduSampleCommandB"

    def do_process(self, args: om.MArgList) -> None:
        some_cmd.create(self.mod)
