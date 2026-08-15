# coding: utf-8
from bd_util.maya.ui import get_main_window


def test_main_window_is_none_in_batch_maya(maya_cmds) -> None:
    # test環境がbatch Mayaとして初期化されていることを確認する。
    assert maya_cmds.about(batch=True)

    # batch Mayaではmain windowを取得しないことを確認する。
    assert get_main_window() is None
