# coding: utf-8
from importlib import import_module
from types import ModuleType

import pytest

from bd_util.ui import qt


def test_qt_facade_exposes_binding_information() -> None:
    # 実際に読み込まれたbinding名とversionを公開することを確認する。
    binding = import_module(qt.QT_BINDING)
    assert qt.QT_BINDING in {"PySide7", "PySide6"}
    assert qt.QT_BINDING_VERSION == binding.__version__
    assert qt.QT_BINDING_MAJOR_VERSION == int(
        qt.QT_BINDING.removeprefix("PySide")
    )


def test_qt_facade_exposes_original_modules() -> None:
    # 使用頻度の低いAPIへmodule経由でアクセスできることを確認する。
    assert qt.QtCore is import_module(f"{qt.QT_BINDING}.QtCore")
    assert qt.QtGui is import_module(f"{qt.QT_BINDING}.QtGui")
    assert qt.QtWidgets is import_module(f"{qt.QT_BINDING}.QtWidgets")


def test_qt_facade_exposes_common_aliases() -> None:
    # Core、Gui、Widgetsの頻出APIが元classと同一であることを確認する。
    assert qt.Qt is qt.QtCore.Qt
    assert qt.Signal is qt.QtCore.Signal
    assert qt.Slot is qt.QtCore.Slot
    assert qt.Property is qt.QtCore.Property
    assert qt.QAction is qt.QtGui.QAction
    assert qt.QIcon is qt.QtGui.QIcon
    assert qt.QWidget is qt.QtWidgets.QWidget
    assert qt.QLabel is qt.QtWidgets.QLabel
    assert qt.QVBoxLayout is qt.QtWidgets.QVBoxLayout


def test_load_binding_falls_back_only_when_root_package_is_missing(
    monkeypatch,
) -> None:
    """bindingのroot packageがない場合だけ次の候補へ進む。"""
    imported_names: list[str] = []

    def fake_import_module(name: str) -> ModuleType:
        """test用moduleを返し、先頭候補だけ不存在として扱う。"""
        imported_names.append(name)
        if name == "PySide7":
            raise ModuleNotFoundError(name="PySide7")
        return ModuleType(name)

    # 仮想候補を使い、PySide7不在後にPySide6一式を読み込む。
    monkeypatch.setattr(qt, "import_module", fake_import_module)
    modules = qt._load_binding(
        (("PySide7", "shiboken7"), ("PySide6", "shiboken6"))
    )

    assert modules.name == "PySide6"
    assert imported_names == [
        "PySide7",
        "PySide6",
        "PySide6.QtCore",
        "PySide6.QtGui",
        "PySide6.QtWidgets",
        "shiboken6",
    ]


def test_load_binding_does_not_hide_internal_import_error(monkeypatch) -> None:
    """発見したbinding内部のimport errorをfallbackで隠さない。"""
    imported_names: list[str] = []

    def fake_import_module(name: str) -> ModuleType:
        """binding内部依存の不足を再現する。"""
        imported_names.append(name)
        if name == "PySide7":
            raise ModuleNotFoundError(name="missing_dependency")
        return ModuleType(name)

    # PySide7内部の問題をそのまま通知し、PySide6を試さないことを確認する。
    monkeypatch.setattr(qt, "import_module", fake_import_module)
    with pytest.raises(ModuleNotFoundError) as error:
        qt._load_binding((("PySide7", "shiboken7"), ("PySide6", "shiboken6")))

    assert error.value.name == "missing_dependency"
    assert imported_names == ["PySide7"]


def test_load_binding_reports_all_missing_candidates(monkeypatch) -> None:
    """全候補が存在しない場合に確認対象を含むerrorを返す。"""

    def fake_import_module(name: str) -> ModuleType:
        """指定されたroot packageを不存在として扱う。"""
        raise ModuleNotFoundError(name=name)

    # 利用可能なbindingがない環境のerror messageを確認する。
    monkeypatch.setattr(qt, "import_module", fake_import_module)
    with pytest.raises(
        ImportError,
        match="PySide7, PySide6",
    ):
        qt._load_binding((("PySide7", "shiboken7"), ("PySide6", "shiboken6")))


def test_qt_facade_exposes_shiboken_helpers(qt_application) -> None:
    # facade経由で生成したWidgetのC++ pointerをshiboken helperで取得する。
    widget = qt.QWidget()
    pointer = int(qt.getCppPointer(widget)[0])

    # helperが同じQt wrapperを有効なobjectとして解決することを確認する。
    wrapped = qt.wrapInstance(pointer, qt.QWidget)
    assert wrapped is widget
    assert qt.isValid(wrapped)

    # testで生成したWidgetをQt event loopへ削除予約する。
    widget.deleteLater()
    qt_application.processEvents()


def test_qt_facade_defines_explicit_public_api() -> None:
    # 利用者向けのmodule、頻出alias、shiboken helperが公開対象に含まれる。
    expected_names = {
        "QtCore",
        "QtGui",
        "QtWidgets",
        "Qt",
        "Signal",
        "Slot",
        "Property",
        "QWidget",
        "QLabel",
        "wrapInstance",
        "getCppPointer",
        "isValid",
    }
    assert expected_names <= set(qt.__all__)
