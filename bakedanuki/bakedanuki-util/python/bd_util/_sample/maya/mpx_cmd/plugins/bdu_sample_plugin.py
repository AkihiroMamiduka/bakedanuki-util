# coding: utf-8

"""
plugin ファイル内では、絶対 import しか使用できない。
その為、相対import でコマンドを作成したい場合は、コマンドの実装を別ファイルに分ける必要があるみたい。
基本的には、コマンドの実装は、別ファイル。
登録のみを plugin ファイル内で行うと良さそう。
"""

# self
from ..cmds.sample_cmd_a.cmd import BDUSampleCommandA
from ..cmds.sample_cmd_b.cmd import BDUSampleCommandB


def initializePlugin(plugin):
    BDUSampleCommandA.initialize_plugin(plugin)
    BDUSampleCommandB.initialize_plugin(plugin)


def uninitializePlugin(plugin):
    BDUSampleCommandA.uninitialize_plugin(plugin)
    BDUSampleCommandB.uninitialize_plugin(plugin)
