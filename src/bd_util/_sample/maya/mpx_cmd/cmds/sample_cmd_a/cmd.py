# coding: utf-8

"""
plugin から呼ばれるコマンド本体。
このモジュール内では、相対import を使用して、コマンドを実装することができる。
"""

# self
from bd_util import MPxCommandBase
from . import some_cmd


class BDUSampleCommandA(MPxCommandBase):
    COMMAND_NAME = "bduSampleCommandA"

    def do_process(self, args):
        some_cmd.create(self.mod)
