# coding: utf-8
from collections.abc import Iterator

import pytest

from bd_util.ui import (
    BoolComboBox,
    BoolViewModel,
    EnumComboBox,
    EnumDefinition,
    EnumViewModel,
    qt,
)


@pytest.fixture
def combo(qt_application: qt.QApplication) -> Iterator[qt.QComboBox]:
    """表示件数が適用される標準styleのコンボを生成して破棄する。"""
    widget = qt.QComboBox()
    style = qt.QtWidgets.QStyleFactory.create("Windows")
    assert style is not None
    style.setParent(widget)
    widget.setStyle(style)
    widget.show()
    qt_application.processEvents()
    try:
        yield widget
    finally:
        widget.hidePopup()
        widget.close()
        widget.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )
        qt_application.processEvents()


def _open_popup(combo: qt.QComboBox, application: qt.QApplication) -> None:
    """候補を開き、表示領域とスクロール範囲の更新を完了する。"""
    combo.showPopup()
    application.processEvents()


def test_all_items_remain_visible_after_model_changes(
    combo: qt.QComboBox, qt_application: qt.QApplication
) -> None:
    """十件を超える候補を、追加・削除とmodel差し替え後も全件表示する。"""
    combo.addItems([f"Item {index}" for index in range(15)])
    _open_popup(combo, qt_application)
    assert combo.view().verticalScrollBar().maximum() == 0
    combo.hidePopup()

    # 生成時より増えた候補と、差し替え後の候補も制限しない
    combo.addItems([f"Added {index}" for index in range(10)])
    _open_popup(combo, qt_application)
    assert combo.view().verticalScrollBar().maximum() == 0
    combo.hidePopup()
    combo.removeItem(0)
    model = qt.QStandardItemModel(combo)
    for index in range(20):
        model.appendRow(qt.QStandardItem(f"Replaced {index}"))
    combo.setModel(model)
    _open_popup(combo, qt_application)
    assert combo.count() == 20
    assert combo.view().verticalScrollBar().maximum() == 0


def test_items_beyond_screen_remain_scrollable(
    combo: qt.QComboBox, qt_application: qt.QApplication
) -> None:
    """画面に収まらない候補は表示領域を縮めてスクロールで選択できる。"""
    combo.addItems([f"Item {index}" for index in range(1000)])
    _open_popup(combo, qt_application)
    screen = combo.screen()
    assert screen is not None
    assert combo.view().window().height() <= screen.geometry().height()
    scrollbar = combo.view().verticalScrollBar()
    assert scrollbar.maximum() > 0
    scrollbar.setValue(scrollbar.maximum())
    qt_application.processEvents()
    last_item = combo.model().index(combo.count() - 1, 0)
    assert (
        combo.view()
        .viewport()
        .rect()
        .intersects(combo.view().visualRect(last_item))
    )


def test_explicit_visible_item_limit_survives_reopening_and_model_changes(
    combo: qt.QComboBox, qt_application: qt.QApplication
) -> None:
    """利用側の明示件数は再表示とmodel差し替え後も保持する。"""
    combo.setMaxVisibleItems(3)
    combo.addItems([f"Item {index}" for index in range(20)])
    _open_popup(combo, qt_application)
    assert combo.view().verticalScrollBar().maximum() > 0
    combo.hidePopup()

    model = qt.QStandardItemModel(combo)
    for index in range(25):
        model.appendRow(qt.QStandardItem(f"Replaced {index}"))
    combo.setModel(model)
    _open_popup(combo, qt_application)
    assert combo.maxVisibleItems() == 3
    assert combo.view().verticalScrollBar().maximum() > 0


def test_binding_combos_inherit_common_visible_item_policy(
    qt_application: qt.QApplication,
) -> None:
    """enumとboolのViewも共通コンボの既定値と明示件数を継承する。"""
    owner = qt.QWidget()
    definition = EnumDefinition.from_mapping(
        {index: f"Item {index}" for index in range(25)}
    )
    enum_model = EnumViewModel(parent=owner, definition=definition)
    bool_model = BoolViewModel(False, owner)
    views = (
        EnumComboBox(enum_model, owner),
        BoolComboBox(bool_model, parent=owner),
    )
    try:
        for view in views:
            assert isinstance(view, qt.QComboBox)
            assert view.maxVisibleItems() >= view.count()
            view.setMaxVisibleItems(1)
            assert view.maxVisibleItems() == 1
    finally:
        owner.deleteLater()
        qt.QtCore.QCoreApplication.sendPostedEvents(
            None, qt.QEvent.Type.DeferredDelete
        )
        qt_application.processEvents()
