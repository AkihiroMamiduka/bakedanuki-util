# coding: utf-8
"""モーダル画面の起点配置と、Qt版保存先選択の契約を確認する。"""

from pathlib import Path

import pytest

from bd_util.ui import exec_dialog_near, get_save_file_name_near, qt
from bd_util.ui import dialog as dialog_module


@pytest.mark.parametrize(
    "available,anchor,size",
    (
        (qt.QRect(0, 0, 800, 600), qt.QPoint(400, 300), qt.QSize(320, 180)),
        (qt.QRect(0, 0, 800, 600), qt.QPoint(0, 0), qt.QSize(320, 180)),
        (qt.QRect(0, 0, 800, 600), qt.QPoint(799, 599), qt.QSize(320, 180)),
        (
            qt.QRect(-1900, -200, 1900, 1000),
            qt.QPoint(-1898, -198),
            qt.QSize(320, 180),
        ),
        (
            qt.QRect(2560, 0, 1920, 1080),
            qt.QPoint(4478, 1078),
            qt.QSize(320, 180),
        ),
        (qt.QRect(0, 0, 300, 200), qt.QPoint(299, 199), qt.QSize(900, 700)),
    ),
)
def test_modal_dialog_frame_fits_the_anchor_screen(
    qt_application, monkeypatch, available, anchor, size
) -> None:
    """画面端・負座標・過大サイズでも、外枠を作業領域内へ収める。"""
    dialog = qt.QDialog()
    dialog.setWindowFlag(qt.Qt.WindowType.FramelessWindowHint, True)
    dialog.resize(size)
    dialog.setMinimumSize(size)
    captured: list[qt.QRect] = []

    def geometry(_dialog, position):
        """実モニターの代わりに、指定した起点の作業領域を返す。"""
        assert position == anchor
        return available

    def close() -> None:
        """表示と遅延補正の後に実際の外枠を記録して閉じる。"""
        captured.append(dialog.frameGeometry())
        dialog.accept()

    monkeypatch.setattr(dialog_module, "_available_geometry", geometry)
    timer = qt.QTimer(dialog)
    timer.setSingleShot(True)
    timer.timeout.connect(close)
    timer.start(20)
    try:
        assert (
            exec_dialog_near(dialog, anchor) == qt.QDialog.DialogCode.Accepted
        )
        assert len(captured) == 1
        assert available.contains(captured[0])
        if anchor == qt.QPoint(400, 300):
            assert captured[0].topLeft() == qt.QPoint(240, 210)
        assert dialog.minimumSize() == size
    finally:
        dialog.deleteLater()
        qt_application.processEvents()


def test_dialog_restores_layout_constraint_after_fitting_a_small_screen(
    qt_application, monkeypatch
) -> None:
    """内容の最小寸法を一時的に緩めても、終了後は元の制約へ戻す。"""
    dialog = qt.QDialog()
    dialog.setWindowFlag(qt.Qt.WindowType.FramelessWindowHint, True)
    child = qt.QWidget(dialog)
    child.setMinimumSize(900, 700)
    layout = qt.QVBoxLayout(dialog)
    layout.addWidget(child)
    original = layout.sizeConstraint()
    available = qt.QRect(0, 0, 300, 200)
    captured: list[qt.QRect] = []

    def geometry(_dialog, _position):
        """内容よりも小さい作業領域を返す。"""
        return available

    def close() -> None:
        """制約を緩めた状態の実寸を記録する。"""
        captured.append(dialog.frameGeometry())
        dialog.reject()

    monkeypatch.setattr(dialog_module, "_available_geometry", geometry)
    timer = qt.QTimer(dialog)
    timer.setSingleShot(True)
    timer.timeout.connect(close)
    timer.start(20)
    try:
        assert (
            exec_dialog_near(dialog, qt.QPoint(299, 199))
            == qt.QDialog.DialogCode.Rejected
        )
        assert available.contains(captured[0])
        assert layout.sizeConstraint() == original
    finally:
        dialog.deleteLater()
        qt_application.processEvents()


def test_modal_execution_failure_removes_placement_callbacks(
    qt_application, monkeypatch
) -> None:
    """実行失敗でも位置補正のQObjectとタイマーを残さない。"""
    dialog = qt.QDialog()

    def fail(_dialog):
        """モーダル実行の例外境界を再現する。"""
        raise RuntimeError("injected execution failure")

    monkeypatch.setattr(qt.QDialog, "exec", fail)
    try:
        with pytest.raises(RuntimeError, match="injected"):
            exec_dialog_near(dialog, qt.QPoint(20, 20))
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        assert not dialog.findChildren(dialog_module._DialogPlacement)
    finally:
        dialog.deleteLater()
        qt_application.processEvents()


@pytest.mark.parametrize("accept", (False, True))
def test_save_file_dialog_uses_qt_and_preserves_file_selection_contract(
    qt_application, monkeypatch, tmp_path, accept
) -> None:
    """Qt版・拡張子・初期名・取消を検証し、実ファイルは作成しない。"""
    initial = tmp_path / "Original_copy.json"
    anchor = qt.QPoint(789, 567)
    seen: list[str] = []

    def inspect(dialog, position):
        """配置共通処理へ渡る保存画面の設定を検査する。"""
        assert isinstance(dialog, qt.QFileDialog)
        assert dialog.testOption(qt.QFileDialog.Option.DontUseNativeDialog)
        assert dialog.acceptMode() == qt.QFileDialog.AcceptMode.AcceptSave
        assert dialog.fileMode() == qt.QFileDialog.FileMode.AnyFile
        assert not dialog.testOption(
            qt.QFileDialog.Option.DontConfirmOverwrite
        )
        assert dialog.defaultSuffix() == "json"
        assert position == anchor
        assert Path(dialog.directory().absolutePath()) == tmp_path
        assert Path(dialog.selectedFiles()[0]) == initial
        seen.append(dialog.windowTitle())
        dialog.selectFile("Chosen")
        return int(
            qt.QDialog.DialogCode.Accepted
            if accept
            else qt.QDialog.DialogCode.Rejected
        )

    monkeypatch.setattr(dialog_module, "exec_dialog_near", inspect)
    result = get_save_file_name_near(
        None, "保存先", str(initial), "JSON (*.json)", anchor, "json"
    )
    assert seen == ["保存先"]
    if accept:
        assert Path(result[0]) == tmp_path / "Chosen.json"
        assert result[1] == "JSON (*.json)"
    else:
        assert result == ("", "")
    assert not (tmp_path / "Chosen.json").exists()
    qt_application.processEvents()
