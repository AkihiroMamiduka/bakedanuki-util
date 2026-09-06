# coding: utf-8
from collections.abc import Iterator
from typing import cast

import pytest
from maya import standalone
from PySide6 import QtWidgets


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
