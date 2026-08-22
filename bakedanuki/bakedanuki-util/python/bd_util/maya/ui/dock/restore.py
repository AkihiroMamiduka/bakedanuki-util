# coding: utf-8
import importlib
import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, cast

_DOTTED_NAME_PATTERN = re.compile(
    r"^[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*$",
    re.ASCII,
)
_NAME_PATTERN = re.compile(r"^[A-Za-z_]\w*$", re.ASCII)


@dataclass(frozen=True)
class DockRestoreSpec:
    """MayaのuiScriptから呼び出す復元関数を表す。"""

    module: str
    function: str = "restore"

    def __post_init__(self) -> None:
        """import可能なmodule名と関数名か検証する。"""
        # uiScriptへ安全に埋め込めるPythonの修飾名だけを許可する。
        if not _DOTTED_NAME_PATTERN.fullmatch(self.module):
            raise ValueError("moduleにはimport可能な修飾名を指定してください")
        if not _NAME_PATTERN.fullmatch(self.function):
            raise ValueError("functionにはPythonの関数名を指定してください")

    def to_ui_script(self) -> str:
        """MayaのworkspaceControlへ登録するuiScriptを返す。"""
        # ライブラリ側の共通入口を経由して利用者moduleの復元関数を呼び出す。
        return (
            "from bd_util.maya.ui import restore_dockable; "
            f"restore_dockable({self.module!r}, {self.function!r})"
        )


def restore_dockable(module: str, function: str = "restore") -> Any:
    """指定moduleを読み込み、ドッキングウィンドウの復元関数を実行する。"""
    # Maya再起動後でもtool moduleを読み込めるよう遅延importする。
    imported_module = importlib.import_module(module)
    callback = cast(Callable[[], Any], getattr(imported_module, function))

    # 復元先のworkspaceControlがcurrent parentの間にWidgetを接続する。
    return callback()
