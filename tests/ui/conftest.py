# coding: utf-8
from collections.abc import Iterator
from typing import cast

import pytest
from maya import standalone
from PySide6 import QtGui, QtWidgets


@pytest.fixture(autouse=True)
def isolate_sample_editor_settings(monkeypatch, tmp_path):
    """永続化サンプルの検証を実ユーザーの設定と他testから隔離する。"""
    from bd_util.maya.ui import settings as maya_settings
    from bd_util.ui import qt

    create_settings = maya_settings._create_ui_settings

    def create_sample_settings(path):
        """浮動小数点サンプルだけをtestごとの一時INIへ差し替える。"""
        if path.tool_name in {"float_sample", "float3_sample"}:
            return qt.QtCore.QSettings(
                str(tmp_path / f"{path.tool_name}.ini"),
                qt.QtCore.QSettings.Format.IniFormat,
            )
        return create_settings(path)

    monkeypatch.setattr(
        maya_settings, "_create_ui_settings", create_sample_settings
    )


@pytest.fixture(scope="session")
def qt_application() -> Iterator[QtWidgets.QApplication]:
    """QWidget testで共有するQApplicationを提供する。"""
    # 既存applicationがなければtest session用に生成する。
    application = QtWidgets.QApplication.instance()
    if application is None:
        application = QtWidgets.QApplication([])
    elif not isinstance(application, QtWidgets.QApplication):
        # Maya standaloneがQGuiApplicationを生成済みの場合は競合を避ける。
        pytest.skip(
            "QApplicationが必要ですが、Maya standaloneによって"
            "QGuiApplicationが生成済みです"
        )

    # 生成または取得したapplicationをsession全体で共有する。
    yield cast(QtWidgets.QApplication, application)


@pytest.fixture
def saved_clipboard(
    qt_application: QtWidgets.QApplication,
) -> Iterator[QtGui.QClipboard]:
    """test前のclipboard内容を複製し、終了時に戻す。"""
    from bd_util.ui import qt

    clipboard = qt_application.clipboard()
    saved = qt.QtCore.QMimeData()
    original = clipboard.mimeData()
    if original is not None:
        for mime_type in original.formats():
            saved.setData(mime_type, original.data(mime_type))
    try:
        yield clipboard
    finally:
        clipboard.setMimeData(saved)


@pytest.fixture(scope="session")
def maya_standalone(
    qt_application: QtWidgets.QApplication,
) -> Iterator[None]:
    """QApplication生成後にMayaを初期化し、test session終了まで維持する。"""
    # UI生成後にMayaを初期化し、既に初期化済みの環境も許容する。
    initialized_here = False
    try:
        standalone.initialize(name="python")
        initialized_here = True
    except RuntimeError:
        pass

    # 複数sampleのtestで同じMaya環境を共有する。
    yield

    # このfixtureが初期化した場合だけsession終了時に解放する。
    if initialized_here:
        standalone.uninitialize()
