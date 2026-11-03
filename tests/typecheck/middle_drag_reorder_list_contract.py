# coding: utf-8
"""中ドラッグ一覧の移動要求とQt標準APIの公開型を固定する。"""

from typing import assert_type

from bd_util.ui import ListReorderRequest, MiddleDragReorderListWidget, qt

widget = MiddleDragReorderListWidget(qt.QWidget())
request = ListReorderRequest(rows=(1, 3), before_row=5)
assert_type(request.rows, tuple[int, ...])
assert_type(request.before_row, int)
assert_type(widget.cancel_reorder(), None)
assert_type(widget.count(), int)
assert_type(widget.selectedItems(), list[qt.QListWidgetItem])
assert_type(widget.reorder_requested, qt.QtCore.SignalInstance)
