# coding: utf-8
"""Maya標準画面の捕捉・寸法・起点と、取消や失敗時の監視解除を検証する。"""

from pathlib import Path

import pytest

from bd_util.maya.ui import dialog as maya_dialog
from bd_util.ui import dialog as ui_dialog
from bd_util.ui import qt


@pytest.mark.parametrize(
    "outcome", ("accept", "cancel", "missing", "command_error", "no_dialog")
)
def test_maya_directory_selection_tracks_only_the_new_dialog(
    qt_application, tmp_path: Path, monkeypatch, outcome: str
) -> None:
    """同名の既存画面を動かさず、今回の標準画面だけへ寸法と起点を適用する。"""
    caption = "フォルダーを選択"
    anchor = qt.QPoint(1590, 990)
    available = qt.QRect(0, 0, 1600, 1000)
    initial_size = qt.QSize(900, 650)
    existing = qt.QFileDialog()
    existing.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
    existing.setWindowTitle(caption)
    existing.resize(700, 500)
    existing.show()
    qt_application.processEvents()
    before = existing.geometry()
    created: list[qt.QFileDialog] = []

    def geometry(_dialog, position):
        """対象画面の起点を確認し、十分な広さの作業領域を返す。"""
        assert position == anchor
        return available

    def choose(**kwargs):
        """Mayaの表示通知を再現し、実際のQt画面へ適用された寸法を調べる。"""
        assert kwargs == {
            "caption": caption,
            "startingDirectory": str(tmp_path),
            "dialogStyle": 2,
            "fileMode": 3,
            "okCaption": "選択",
            "cancelCaption": "キャンセル",
        }
        if outcome == "command_error":
            raise RuntimeError("injected Maya command failure")
        if outcome == "no_dialog":
            return None
        # 別の新規画面と、同名の既存画面はいずれも今回の対象にしない
        unrelated = qt.QFileDialog()
        unrelated.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
        unrelated.setWindowTitle("別の画面")
        unrelated.resize(700, 500)
        created.append(unrelated)
        unrelated.show()
        existing.show()
        qt_application.processEvents()
        assert existing.geometry() == before
        assert unrelated.size() == qt.QSize(700, 500)

        dialog = qt.QFileDialog()
        dialog.setOption(qt.QFileDialog.Option.DontUseNativeDialog, True)
        dialog.setWindowTitle(caption)
        dialog.setWindowFlag(qt.Qt.WindowType.FramelessWindowHint, True)
        created.append(dialog)
        dialog.show()
        qt_application.processEvents()
        assert dialog.size() == initial_size
        assert available.contains(dialog.frameGeometry())
        assert dialog.frameGeometry().right() == available.right()
        assert dialog.frameGeometry().bottom() == available.bottom()
        # 初期配置後の手動調整を、監視で元へ戻さないことも確認する
        dialog.resize(850, 600)
        dialog.move(50, 60)
        qt_application.processEvents()
        assert dialog.pos() == qt.QPoint(50, 60)
        assert dialog.size() == qt.QSize(850, 600)
        dialog.hide()
        if outcome == "cancel":
            return None
        return [
            str(tmp_path / "missing" if outcome == "missing" else tmp_path)
        ]

    monkeypatch.setattr(ui_dialog, "_available_geometry", geometry)
    monkeypatch.setattr(maya_dialog.cmds, "fileDialog2", choose)
    try:
        if outcome in ("command_error", "no_dialog"):
            with pytest.raises(RuntimeError):
                maya_dialog.get_existing_directory_near(
                    existing,
                    caption,
                    str(tmp_path),
                    anchor,
                    initial_size=initial_size,
                )
        else:
            result = maya_dialog.get_existing_directory_near(
                existing,
                caption,
                str(tmp_path),
                anchor,
                initial_size=initial_size,
            )
            assert result == (str(tmp_path) if outcome == "accept" else "")
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        assert not existing.findChildren(maya_dialog._MayaDirectoryPlacement)
        for dialog in created:
            assert not dialog.findChildren(ui_dialog._DialogPlacement)
            assert not dialog.findChildren(ui_dialog._ChildMessageBoxPlacement)
    finally:
        for dialog in created:
            dialog.close()
            dialog.deleteLater()
        existing.close()
        existing.deleteLater()
        qt_application.processEvents()


@pytest.mark.parametrize("size", (qt.QSize(0, 650), qt.QSize(1200, -1)))
def test_maya_directory_rejects_invalid_initial_dimensions(
    qt_application, monkeypatch, size: qt.QSize
) -> None:
    """正でない設定寸法ではMayaの画面を開かず、明示的に失敗させる。"""

    def refuse(**_kwargs):
        """無効な設定でMayaのコマンドを呼び出すことを拒否する。"""
        raise AssertionError("Mayaの画面を開いてはいけません")

    monkeypatch.setattr(maya_dialog.cmds, "fileDialog2", refuse)
    with pytest.raises(ValueError):
        maya_dialog.get_existing_directory_near(
            None, "フォルダー", "", qt.QPoint(), initial_size=size
        )
