# coding: utf-8
"""モーダル画面の起点配置と、Qt版保存先選択の契約を確認する。"""

from pathlib import Path

import pytest

from bd_util.ui import (
    exec_dialog_near,
    get_existing_directory_near,
    get_open_file_names_near,
    get_save_file_name_near,
    place_dialog_near,
    qt,
    warning_near,
)
from bd_util.ui import dialog as dialog_module


@pytest.mark.parametrize("shown", (False, True))
def test_external_dialog_placement_preserves_later_user_movement(
    qt_application, monkeypatch, shown
) -> None:
    """表示前と表示中の両方で配置し、利用者の後続移動には追従しない。"""
    dialog = qt.QDialog()
    dialog.setWindowFlag(qt.Qt.WindowType.FramelessWindowHint, True)
    dialog.resize(300, 200)
    available = qt.QRect(0, 0, 800, 600)

    def geometry(_dialog, _position):
        """外部APIが開く画面にも共通の作業領域を与える。"""
        return available

    monkeypatch.setattr(dialog_module, "_available_geometry", geometry)
    if shown:
        dialog.show()
    try:
        with place_dialog_near(dialog, qt.QPoint(799, 599)):
            dialog.show()
            qt_application.processEvents()
            assert dialog.frameGeometry() == qt.QRect(500, 400, 300, 200)
            dialog.move(50, 60)
            qt_application.processEvents()
            assert dialog.pos() == qt.QPoint(50, 60)
        qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
        assert not dialog.findChildren(dialog_module._DialogPlacement)
        assert not dialog.findChildren(dialog_module._ChildMessageBoxPlacement)
    finally:
        dialog.close()
        dialog.deleteLater()


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
        assert not dialog.findChildren(dialog_module._ChildMessageBoxPlacement)
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


@pytest.mark.parametrize(
    "button",
    (
        qt.QMessageBox.StandardButton.Save,
        qt.QMessageBox.StandardButton.Discard,
        qt.QMessageBox.StandardButton.Cancel,
    ),
)
def test_warning_preserves_standard_buttons_and_default(
    qt_application, monkeypatch, button
) -> None:
    """確認の標準ボタンと初期選択を保ち、実行後は一時画面を破棄する。"""
    anchor = qt.QPoint(713, 529)
    buttons = (
        qt.QMessageBox.StandardButton.Save
        | qt.QMessageBox.StandardButton.Discard
        | qt.QMessageBox.StandardButton.Cancel
    )
    dialogs: list[qt.QMessageBox] = []

    def inspect(dialog, position):
        """標準警告と起点を確認し、選択されたボタン値を返す。"""
        assert isinstance(dialog, qt.QMessageBox)
        assert dialog.windowTitle() == "未保存"
        assert dialog.text() == "保存しますか？"
        assert dialog.icon() == qt.QMessageBox.Icon.Warning
        assert dialog.standardButtons() == buttons
        assert dialog.defaultButton() is dialog.button(
            qt.QMessageBox.StandardButton.Cancel
        )
        assert position == anchor
        dialogs.append(dialog)
        return button.value

    monkeypatch.setattr(dialog_module, "exec_dialog_near", inspect)
    assert (
        warning_near(
            None,
            "未保存",
            "保存しますか？",
            anchor,
            buttons,
            qt.QMessageBox.StandardButton.Cancel,
        )
        == button
    )
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    assert len(dialogs) == 1
    assert not qt.isValid(dialogs[0])


@pytest.mark.parametrize("accept", (False, True))
def test_open_file_dialog_preserves_multiple_selection_contract(
    qt_application, monkeypatch, tmp_path, accept
) -> None:
    """Qt版の既存複数ファイル選択と取消時の戻り値を維持する。"""
    paths = [str(tmp_path / "first.json"), str(tmp_path / "second.json")]
    anchor = qt.QPoint(713, 529)
    dialogs: list[qt.QFileDialog] = []

    def selected_files(_dialog):
        """複数の選択結果を返し、ファイルの読取りを発生させない。"""
        return paths

    def inspect(dialog, position):
        """複数選択用の設定と初期フォルダーを検査する。"""
        assert isinstance(dialog, qt.QFileDialog)
        assert dialog.testOption(qt.QFileDialog.Option.DontUseNativeDialog)
        assert dialog.acceptMode() == qt.QFileDialog.AcceptMode.AcceptOpen
        assert dialog.fileMode() == qt.QFileDialog.FileMode.ExistingFiles
        assert dialog.windowTitle() == "読込"
        assert Path(dialog.directory().absolutePath()) == tmp_path
        assert position == anchor
        dialogs.append(dialog)
        return int(
            qt.QDialog.DialogCode.Accepted
            if accept
            else qt.QDialog.DialogCode.Rejected
        )

    monkeypatch.setattr(qt.QFileDialog, "selectedFiles", selected_files)
    monkeypatch.setattr(dialog_module, "exec_dialog_near", inspect)
    result = get_open_file_names_near(
        None, "読込", str(tmp_path), "JSON (*.json)", anchor
    )
    assert result == ((paths, "JSON (*.json)") if accept else ([], ""))
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    assert len(dialogs) == 1
    assert not qt.isValid(dialogs[0])


@pytest.mark.parametrize("accept", (False, True))
def test_directory_dialog_uses_qt_and_preserves_navigation(
    qt_application, monkeypatch, tmp_path, accept
) -> None:
    """既存フォルダーへ移動して確定でき、取消と一時画面の破棄を維持する。"""
    chosen = tmp_path / "chosen"
    chosen.mkdir()
    anchor = qt.QPoint(713, 529)
    dialogs: list[qt.QFileDialog] = []
    execute = dialog_module.exec_dialog_near

    def inspect(dialog, position):
        """Qt版の既存フォルダー選択を検査して通常のモーダル処理へ渡す。"""
        assert isinstance(dialog, qt.QFileDialog)
        assert dialog.testOption(qt.QFileDialog.Option.DontUseNativeDialog)
        assert dialog.testOption(qt.QFileDialog.Option.ShowDirsOnly)
        assert dialog.acceptMode() == qt.QFileDialog.AcceptMode.AcceptOpen
        assert dialog.fileMode() == qt.QFileDialog.FileMode.Directory
        assert dialog.windowTitle() == "出力先"
        assert Path(dialog.directory().absolutePath()) == tmp_path
        assert position == anchor
        dialogs.append(dialog)

        def close() -> None:
            """別の既存フォルダーへ移動し、選択または取消を実行する。"""
            dialog.setDirectory(str(chosen))
            if accept:
                dialog.accept()
            else:
                dialog.reject()

        timer = qt.QTimer(dialog)
        timer.setSingleShot(True)
        timer.timeout.connect(close)
        timer.start(30)
        return execute(dialog, position)

    monkeypatch.setattr(dialog_module, "exec_dialog_near", inspect)
    result = get_existing_directory_near(None, "出力先", str(tmp_path), anchor)
    if accept:
        assert Path(result) == chosen
    else:
        assert result == ""
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)
    assert len(dialogs) == 1
    assert not qt.isValid(dialogs[0])
    assert sorted(path.name for path in tmp_path.iterdir()) == ["chosen"]


@pytest.mark.parametrize("kind", ("file", "missing"))
def test_directory_dialog_rejects_non_directory_results(
    qt_application, monkeypatch, tmp_path, kind
) -> None:
    """実行境界から不正な確定結果が返っても、ファイルや未作成pathを返さない。"""
    selected = tmp_path / "chosen"
    if kind == "file":
        selected.write_text("existing file", encoding="utf-8")

    def selected_files(_dialog):
        """フォルダー以外のパスが選択結果に混入した状態を再現する。"""
        return [str(selected)]

    def accept(_dialog, _position):
        """既存性の最終確認を検査するため、確定済みの結果を返す。"""
        return int(qt.QDialog.DialogCode.Accepted)

    monkeypatch.setattr(qt.QFileDialog, "selectedFiles", selected_files)
    monkeypatch.setattr(dialog_module, "exec_dialog_near", accept)
    assert (
        get_existing_directory_near(None, "出力先", str(tmp_path), qt.QPoint())
        == ""
    )
    qt.QApplication.sendPostedEvents(None, qt.QEvent.Type.DeferredDelete)


@pytest.mark.parametrize("overwrite", (False, True))
def test_save_overwrite_confirmation_uses_the_original_anchor(
    qt_application, monkeypatch, tmp_path, overwrite
) -> None:
    """Qt内部の上書き確認も元の起点へ配置し、標準の取消処理を保つ。"""
    initial = tmp_path / "existing.json"
    initial.write_text("original", encoding="utf-8")
    available = qt.QRect(0, 0, 1600, 1200)
    anchor = qt.QPoint(1200, 850)
    owner = qt.QWidget()
    frames: list[qt.QRect] = []
    buttons: list[qt.QMessageBox.StandardButton] = []
    file_dialogs: list[qt.QFileDialog] = []
    messages: list[qt.QMessageBox] = []
    timed_out: list[bool] = []

    def geometry(_dialog, _position):
        """外枠の中心が起点と一致する大きさの作業領域を返す。"""
        return available

    def accept_file() -> None:
        """既存パスを確定してQt標準の上書き確認へ進む。"""
        file_dialogs[0].accept()

    def inspect() -> None:
        """生成された保存画面と確認を取得し、確認の記録を予約する。"""
        for widget in qt_application.topLevelWidgets():
            if (
                isinstance(widget, qt.QFileDialog)
                and widget.parentWidget() is owner
                and widget.isVisible()
                and not file_dialogs
            ):
                file_dialogs.append(widget)
                accept_timer.start(30)
            elif (
                isinstance(widget, qt.QMessageBox)
                and widget.parentWidget() in file_dialogs
                and widget.isVisible()
                and not messages
            ):
                messages.append(widget)
                capture_timer.start(30)

    def capture_message() -> None:
        """表示後の遅延補正を待ち、標準ボタンで確認結果を返す。"""
        message = messages[0]
        frames.append(message.frameGeometry())
        buttons.append(message.standardButtons())
        message.button(
            qt.QMessageBox.StandardButton.Yes
            if overwrite
            else qt.QMessageBox.StandardButton.No
        ).click()
        if not overwrite:
            file_dialogs[0].reject()

    def timeout() -> None:
        """確認が現れない場合もテストを終了し、失敗条件を記録する。"""
        timed_out.append(True)
        for message in owner.findChildren(qt.QMessageBox):
            message.reject()
        for dialog in file_dialogs:
            dialog.reject()

    monkeypatch.setattr(dialog_module, "_available_geometry", geometry)
    accept_timer = qt.QTimer(owner)
    accept_timer.setSingleShot(True)
    accept_timer.timeout.connect(accept_file)
    capture_timer = qt.QTimer(owner)
    capture_timer.setSingleShot(True)
    capture_timer.timeout.connect(capture_message)
    watcher = qt.QTimer(owner)
    watcher.timeout.connect(inspect)
    watcher.start(10)
    safety = qt.QTimer(owner)
    safety.setSingleShot(True)
    safety.timeout.connect(timeout)
    safety.start(2000)
    try:
        result = get_save_file_name_near(
            owner, "保存", str(initial), "JSON (*.json)", anchor
        )
        if overwrite:
            assert Path(result[0]) == initial
            assert result[1] == "JSON (*.json)"
        else:
            assert result == ("", "")
        assert not timed_out
        assert len(frames) == 1
        assert available.contains(frames[0])
        assert abs(frames[0].center().x() - anchor.x()) <= 1
        assert abs(frames[0].center().y() - anchor.y()) <= 1
        assert buttons == [
            qt.QMessageBox.StandardButton.Yes
            | qt.QMessageBox.StandardButton.No
        ]
        assert initial.read_text(encoding="utf-8") == "original"
    finally:
        watcher.stop()
        safety.stop()
        owner.deleteLater()
        qt_application.processEvents()


def test_nested_message_box_placement_ignores_other_windows(
    qt_application, monkeypatch
) -> None:
    """親階層に属さない警告の配置を、短命な監視が変更しない。"""
    dialog = qt.QDialog()
    unrelated = qt.QMessageBox()
    unrelated.setText("別の処理")
    unrelated.move(31, 47)
    anchor = qt.QPoint(1200, 850)
    placements: list[qt.QDialog] = []

    def geometry(watched, _position):
        """配置を要求された画面だけを記録する。"""
        placements.append(watched)
        return qt.QRect(0, 0, 1600, 1200)

    def show_unrelated() -> None:
        """対象ダイアログの実行中に、無関係な警告を表示する。"""
        unrelated.show()
        close_timer.start(30)

    def close() -> None:
        """無関係な警告と対象のモーダル画面を閉じる。"""
        unrelated.close()
        dialog.accept()

    monkeypatch.setattr(dialog_module, "_available_geometry", geometry)
    show_timer = qt.QTimer(dialog)
    show_timer.setSingleShot(True)
    show_timer.timeout.connect(show_unrelated)
    close_timer = qt.QTimer(dialog)
    close_timer.setSingleShot(True)
    close_timer.timeout.connect(close)
    show_timer.start(30)
    try:
        exec_dialog_near(dialog, anchor)
        assert placements
        assert unrelated not in placements
    finally:
        unrelated.deleteLater()
        dialog.deleteLater()
        qt_application.processEvents()
