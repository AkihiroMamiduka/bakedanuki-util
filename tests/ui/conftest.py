# coding: utf-8
from collections.abc import Iterator
from typing import cast

import pytest
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
