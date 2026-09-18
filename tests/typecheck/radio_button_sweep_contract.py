# coding: utf-8
"""任意参加のなぞり選択と共有編集セッションの公開型を固定する。"""

from typing import assert_type

from bd_util.maya.ui import MayaEditSession
from bd_util.ui import RadioButtonSweep, qt

viewport = qt.QWidget()
sweep = RadioButtonSweep(viewport)
assert_type(sweep.add_button(qt.QRadioButton(viewport)), None)
assert_type(sweep.is_active, bool)
assert_type(sweep.finish(), None)
assert_type(sweep.clear(), None)
assert_type(sweep.dispose(), None)
session = MayaEditSession(viewport, chunk_name="Test")
assert_type(session.is_editing, bool)
assert_type(session.begin(), None)
with session.write():
    pass
assert_type(session.finish(), None)
assert_type(session.dispose(), None)
