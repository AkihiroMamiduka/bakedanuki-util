"""リソースのパス解決と、Windows Explorerでのパス表示。"""

import os
import sys
from pathlib import Path

__all__ = ["resolve_relative_path", "open_path_in_explorer"]


def resolve_relative_path(base_file: str | Path, relative_path: str) -> Path:
    """基準ファイルのあるフォルダから相対パスを絶対パスへ解決する。

    対象の存在確認、読み込みやファイル作成は行わない。

    Args:
        base_file: 呼び出し元の `__file__`、または基準ファイルのパス。
            相対パスの場合は呼び出し時の作業フォルダから解決する。
        relative_path: 基準ファイルのフォルダからの相対パス。
            `sub/file.png` のようなサブフォルダを含む指定も受け付ける。

    Returns:
        基準ファイルの配置から組み立てた対象の絶対パス。
    """
    return Path(base_file).resolve().parent / relative_path


def _select_file_in_explorer(path: Path) -> None:
    """Shellの項目IDで親フォルダーを開き、Unicodeのファイル名も選択する。"""
    import ctypes
    from ctypes import wintypes
    from typing import cast

    ole = ctypes.WinDLL("ole32")
    shell = ctypes.WinDLL("shell32")
    initialize = ole.CoInitializeEx
    initialize.argtypes = [ctypes.c_void_p, wintypes.DWORD]
    initialize.restype = ctypes.c_long
    uninitialize = ole.CoUninitialize
    uninitialize.argtypes = []
    uninitialize.restype = None
    release = ole.CoTaskMemFree
    release.argtypes = [ctypes.c_void_p]
    release.restype = None
    parse = shell.SHParseDisplayName
    parse.argtypes = [
        wintypes.LPCWSTR,
        ctypes.c_void_p,
        ctypes.POINTER(ctypes.c_void_p),
        wintypes.DWORD,
        ctypes.c_void_p,
    ]
    parse.restype = ctypes.c_long
    select = shell.SHOpenFolderAndSelectItems
    select.argtypes = [
        ctypes.c_void_p,
        wintypes.UINT,
        ctypes.c_void_p,
        wintypes.DWORD,
    ]
    select.restype = ctypes.c_long

    # Mayaが既に異なるCOM apartmentを使用している場合は、その初期化を利用する
    initialized = cast(int, initialize(None, 2))
    if initialized < 0 and initialized != -2147417850:
        raise OSError(
            f"COMを初期化できません: 0x{initialized & 0xFFFFFFFF:08X}"
        )
    item = ctypes.c_void_p()
    try:
        result = cast(int, parse(str(path), None, ctypes.byref(item), 0, None))
        if result >= 0:
            result = cast(int, select(item, 0, None, 0))
        if result < 0:
            raise OSError(
                f"エクスプローラで選択できません: {path}\n"
                f"HRESULT: 0x{result & 0xFFFFFFFF:08X}"
            )
    finally:
        if item.value:
            release(item)
        if initialized >= 0:
            uninitialize()


def open_path_in_explorer(path: str | Path) -> None:
    """ファイルは親で選択し、ディレクトリは中身をExplorerで表示する。

    bakedanuki系のExplorer操作は、ツールやファイル形式によらずこの規則を使用します。
    ファイルを関連付けされたアプリケーションで実行することはありません。

    Args:
        path: 対象パス。相対パスは現在の作業フォルダー基準で絶対化します。

    Raises:
        OSError: 対象が存在しない、アクセスできない、またはShell操作に失敗した場合。
        NotImplementedError: Windows以外で呼び出した場合。
    """
    if sys.platform != "win32":
        raise NotImplementedError("Explorer操作はWindowsで使用してください")
    target = Path(os.path.abspath(Path(path).expanduser()))
    if target.is_dir():
        os.startfile(str(target))
    elif target.is_file():
        _select_file_in_explorer(target)
    else:
        raise FileNotFoundError(
            f"対象のファイルまたはフォルダーがありません: {target}"
        )
