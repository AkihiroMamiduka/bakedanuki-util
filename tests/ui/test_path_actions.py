"""パス操作の全文コピー、読取専用欄と、失敗通知の起点を検証する。"""

import pytest

from bd_util.ui import PathLineEdit, add_path_actions, qt
from bd_util.ui import path as path_module


@pytest.mark.parametrize("exists", (False, True))
def test_path_menu_preserves_existing_actions_and_copies_missing_paths(
    qt_application, tmp_path, exists
):
    """標準項目を保持し、不在パスも全体をコピーして開く操作だけを無効にする。"""
    target = tmp_path / "日本語 空白,項目.json"
    if exists:
        target.write_text("{}", encoding="utf-8")
    menu = qt.QMenu()
    standard = menu.addAction("既存の操作")
    try:
        add_path_actions(menu, target, qt.QPoint(300, 400))
        assert menu.actions()[0] is standard
        section, opened, copied = menu.actions()[1:]
        assert section.text() == "パス"
        assert not section.isEnabled()
        assert opened.isEnabled() == exists
        copied.trigger()
        assert qt.QApplication.clipboard().text() == str(target)
    finally:
        menu.deleteLater()


def test_open_failure_after_menu_creation_warns_at_original_anchor(
    qt_application, tmp_path, monkeypatch
):
    """表示後に消えた対象はExplorerを起動せず、右クリック位置へ失敗を通知する。"""
    target = tmp_path / "removed.json"
    target.write_text("{}", encoding="utf-8")
    parent = qt.QWidget()
    menu = qt.QMenu(parent)
    origin = qt.QPoint(300, 400)
    add_path_actions(menu, target, origin)
    target.unlink()
    warnings = []

    def warn(widget, title, message, anchor):
        """対象の消失と起点が通知へ渡ることを記録する。"""
        assert widget is parent
        assert "removed.json" in message
        warnings.append((title, anchor))

    monkeypatch.setattr(path_module, "warning_near", warn)
    try:
        menu.actions()[-2].trigger()
        assert warnings == [("パスを開けません", origin)]
    finally:
        parent.deleteLater()


def test_path_line_edit_keeps_standard_selection_copy_and_adds_full_copy(
    qt_application, tmp_path
):
    """読取専用欄の部分コピーとパスメニューの全文コピーを区別する。"""
    target = tmp_path / "出力 フォルダー"
    target.mkdir()
    edit = PathLineEdit(target)
    seen = []

    errors = []
    timer = qt.QTimer(edit)
    timer.setSingleShot(True)

    def execute():
        """標準メニューを保ったまま、パス全体をコピーする操作を実行する。"""
        menu = qt.QApplication.activePopupWidget()
        try:
            assert isinstance(menu, qt.QMenu)
            assert len(menu.actions()) > 3
            assert menu.actions()[-3].text() == "パス"
            menu.actions()[-1].trigger()
            seen.append("copied")
        except Exception as error:
            errors.append(error)
        finally:
            if isinstance(menu, qt.QMenu):
                menu.close()

    timer.timeout.connect(execute)
    try:
        assert edit.isReadOnly() and edit.isEnabled()
        edit.setSelection(0, 3)
        edit.copy()
        assert qt.QApplication.clipboard().text() == str(target)[:3]
        point = qt.QPoint(20, 10)
        event = qt.QtGui.QContextMenuEvent(
            qt.QtGui.QContextMenuEvent.Reason.Mouse, point, point
        )
        timer.start(0)
        qt.QApplication.sendEvent(edit, event)
        if errors:
            raise errors[0]
        assert seen == ["copied"]
        assert qt.QApplication.clipboard().text() == str(target)
    finally:
        timer.stop()
        edit.deleteLater()
