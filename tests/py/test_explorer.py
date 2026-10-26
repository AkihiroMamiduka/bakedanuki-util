"""Explorerの共通規則と、Shell API失敗時のCOM資源解放を検証する。"""

import ctypes
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from bd_util.py import path as path_module


@pytest.mark.parametrize("kind", ("file", "directory", "missing"))
def test_explorer_dispatches_by_actual_path_type(tmp_path, monkeypatch, kind):
    """ファイルを実行せず選択表示し、フォルダーは開き、不在なら起動しない。"""
    target = tmp_path / "日本語 空白,項目.json"
    if kind == "file":
        target.write_text("{}", encoding="utf-8")
    elif kind == "directory":
        target.mkdir()
    selected = Mock()
    opened = Mock()
    monkeypatch.setattr(path_module, "_select_file_in_explorer", selected)
    monkeypatch.setattr(path_module.os, "startfile", opened)
    if kind == "missing":
        with pytest.raises(FileNotFoundError):
            path_module.open_path_in_explorer(target)
    else:
        path_module.open_path_in_explorer(target)
    assert selected.call_args_list == (
        [((target,), {})] if kind == "file" else []
    )
    assert opened.call_args_list == (
        [((str(target),), {})] if kind == "directory" else []
    )


@pytest.mark.parametrize(
    "initialized,parsed,selected",
    (
        (0, 0, 0),
        (1, 0, 0),
        (-2147417850, 0, 0),
        (0, -1, 0),
        (0, 0, -1),
        (-1, 0, 0),
    ),
)
def test_shell_selection_balances_com_and_releases_item_ids(
    monkeypatch, initialized, parsed, selected
):
    """既存COM設定を壊さず、解析・選択のどちらの失敗でも所有資源を解放する。"""
    ole = SimpleNamespace(
        CoInitializeEx=Mock(return_value=initialized),
        CoUninitialize=Mock(),
        CoTaskMemFree=Mock(),
    )

    def parse(_name, _context, result, _flags, _attributes):
        """成功時だけShellが確保した項目IDを模擬する。"""
        if parsed >= 0:
            ctypes.cast(
                result, ctypes.POINTER(ctypes.c_void_p)
            ).contents.value = 42
        return parsed

    shell = SimpleNamespace(
        SHParseDisplayName=Mock(side_effect=parse),
        SHOpenFolderAndSelectItems=Mock(return_value=selected),
    )

    def library(name):
        """OS境界だけを置き換え、COMとShellの呼出し順を検証する。"""
        return ole if name == "ole32" else shell

    monkeypatch.setattr(ctypes, "WinDLL", library)
    failed_init = initialized < 0 and initialized != -2147417850
    if failed_init or parsed < 0 or selected < 0:
        with pytest.raises(OSError):
            path_module._select_file_in_explorer(
                Path("C:/日本語 空白,項目.json")
            )
    else:
        path_module._select_file_in_explorer(Path("C:/日本語 空白,項目.json"))
    assert ole.CoUninitialize.call_count == int(initialized >= 0)
    assert ole.CoTaskMemFree.call_count == int(not failed_init and parsed >= 0)
    assert shell.SHOpenFolderAndSelectItems.call_count == int(
        not failed_init and parsed >= 0
    )
