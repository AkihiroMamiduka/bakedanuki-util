"""Maya UI互換性テストを対象別に実行するランナー。"""

from __future__ import annotations

import argparse
import platform
import sys
from pathlib import Path

_REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
_PYTHON_ROOT = _REPOSITORY_ROOT / "bakedanuki" / "bakedanuki-util" / "python"
_PYTEST_ROOT = _REPOSITORY_ROOT / ".test"
_TEST_PATHS = {
    "qt": _REPOSITORY_ROOT / "tests" / "ui",
    "maya": _REPOSITORY_ROOT / "tests" / "maya" / "ui",
}


def _prepare_import_paths() -> None:
    """pytestとbd_utilのimportパスを追加する。"""

    # リポジトリ内実装とtest専用環境のpytestを優先して読み込む。
    sys.path[:0] = [str(_PYTEST_ROOT), str(_PYTHON_ROOT)]


def _print_environment() -> int:
    """Maya、Python、Qt bindingのバージョンを表示する。"""

    # 実際にfacadeをimportし、各Mayaのbinding選択まで確認する。
    from maya.api import OpenMaya as om

    from bd_util.ui import qt

    print(
        "UI environment: Maya {}, Python {}, {} {}".format(
            om.MGlobal.mayaVersion(),
            platform.python_version(),
            qt.QT_BINDING,
            qt.QT_BINDING_VERSION,
        )
    )
    return 0


def _run_tests(target: str, test_path: str | None, keyword: str | None) -> int:
    """指定されたUIテスト群を実行する。"""

    # Mayaごとのmayapyプロセス内でpytestを起動する。
    import pytest

    # root conftestのMaya初期化より先にWidget用applicationを確保する。
    application = None
    if target == "qt":
        from bd_util.ui import qt

        application = qt.QApplication.instance()
        if application is None:
            application = qt.QApplication([])
        if not isinstance(application, qt.QApplication):
            raise RuntimeError("Qt/UI testにはQApplicationが必要です")

    pytest_args = ["-p", "no:cacheprovider"]
    if keyword:
        pytest_args.extend(("-k", keyword))
    pytest_args.append(test_path or str(_TEST_PATHS[target]))
    return pytest.main(pytest_args)


def _windows_clipboard_text() -> str:
    """Qtとは別のWindows APIから実clipboardのUnicode文字列を読む。"""
    import ctypes

    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32
    user32.OpenClipboard.argtypes = [ctypes.c_void_p]
    user32.OpenClipboard.restype = ctypes.c_bool
    user32.GetClipboardData.argtypes = [ctypes.c_uint]
    user32.GetClipboardData.restype = ctypes.c_void_p
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]

    if not user32.OpenClipboard(None):
        raise RuntimeError("Windows clipboardを開けません")
    try:
        handle = user32.GetClipboardData(13)  # CF_UNICODETEXT
        if not handle:
            raise RuntimeError("Windows clipboardにUnicode文字列がありません")
        pointer = kernel32.GlobalLock(handle)
        if not pointer:
            raise RuntimeError("Windows clipboardの文字列を読めません")
        try:
            return ctypes.wstring_at(pointer)
        finally:
            kernel32.GlobalUnlock(handle)
    finally:
        user32.CloseClipboard()


def _run_native_clipboard() -> int:
    """表示したViewからWindowsの実clipboardへのコピーを検証する。"""
    from bd_util.ui import Float3Binding, Float3Label, JsonClipboard, qt

    application = qt.QApplication.instance()
    if application is None:
        application = qt.QApplication([])
    if not isinstance(application, qt.QApplication):
        raise RuntimeError("Windows clipboard testにはQApplicationが必要です")
    if application.platformName() != "windows":
        raise RuntimeError(
            "Windows clipboard testにはWindows Qt platformが必要です"
        )

    clipboard = application.clipboard()
    saved = qt.QtCore.QMimeData()
    original = clipboard.mimeData()
    if original is not None:
        for mime_type in original.formats():
            saved.setData(mime_type, original.data(mime_type))

    class Values:
        value = (1.235, 2.346, 3.457)

    owner = qt.QWidget()
    binding = Float3Binding.from_attribute(Values(), "value", parent=owner)
    view = Float3Label(binding, owner, decimals=3)
    layout = qt.QHBoxLayout(owner)
    layout.addWidget(view)
    try:
        owner.show()
        application.processEvents()
        for label in (view.x_label, view.y_label, view.z_label):
            label.setFocus()
            label.setSelection(0, len(label.text()))
            application.processEvents()
            qt.QApplication.sendEvent(
                label,
                qt.QtGui.QKeyEvent(
                    qt.QEvent.Type.KeyPress,
                    qt.Qt.Key.Key_C,
                    qt.Qt.KeyboardModifier.ControlModifier,
                ),
            )
            application.processEvents()
            expected = label.text()
            actual = _windows_clipboard_text()
            if actual != expected:
                raise AssertionError(
                    f"{label.accessibleName()} axis copy failed"
                )

        adapter = JsonClipboard(
            "application/x-bd-native-test+json", "BD_NATIVE/1\n"
        )
        document = {"value": 3}
        adapter.write(document)
        application.processEvents()
        if adapter.read() != document:
            raise AssertionError("JSON clipboard round trip failed")
        expected = 'BD_NATIVE/1\n{"value":3}'
        actual = _windows_clipboard_text().replace("\r\n", "\n")
        if actual != expected:
            raise AssertionError("JSON text fallback failed")
        print(
            "Windows clipboard integration passed for Float3Label and JsonClipboard."
        )
        return 0
    finally:
        clipboard.setMimeData(saved)
        owner.close()
        binding.dispose()
        application.processEvents()


def main() -> int:
    """指定された環境確認またはUIテストを実行する。"""

    # PowerShellから渡された検証対象を解釈する。
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target", choices=("environment", "qt", "maya", "native-clipboard")
    )
    parser.add_argument("--test-path")
    parser.add_argument("--keyword")
    args = parser.parse_args()

    _prepare_import_paths()
    if args.target == "environment":
        return _print_environment()
    if args.target == "native-clipboard":
        return _run_native_clipboard()
    return _run_tests(args.target, args.test_path, args.keyword)


if __name__ == "__main__":
    raise SystemExit(main())
