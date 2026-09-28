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
    """MayaのuiScriptから呼び出す復元関数を指定する。

    Attributes:
        module: Maya 再起動後も import できる tool module の修飾名。
        function: 引数なしの復元関数名。既定は`restore`。

    Raises:
        ValueError: 名前がPythonの修飾名・識別子形式でない場合。
    """

    module: str
    function: str = "restore"

    def __post_init__(self) -> None:
        """uiScript へ埋め込める `module` と `function` の形式を検証する。"""
        # 実際のimportはMayaが復元するときに行い、ここでは名前の形式だけ調べる。
        if not _DOTTED_NAME_PATTERN.fullmatch(self.module):
            raise ValueError("moduleにはimport可能な修飾名を指定してください")
        if not _NAME_PATTERN.fullmatch(self.function):
            raise ValueError("functionにはPythonの関数名を指定してください")

    def to_ui_script(self) -> str:
        """workspaceControlに登録する復元用uiScriptを返す。"""
        # 共通入口からtoolの復元関数を呼ぶことで、Maya再起動後も復元できる。
        return (
            "from bd_util.maya.ui import restore_dockable; "
            f"restore_dockable({self.module!r}, {self.function!r})"
        )


def restore_dockable(module: str, function: str = "restore") -> Any:
    """tool の `module` を読み込み、dockable Window の復元関数を呼ぶ。

    Args:
        module: 復元関数を持つmoduleの修飾名。
        function: 引数なしの復元関数名。

    Returns:
        復元関数の戻り値。

    Raises:
        ImportError: `module` を読み込めない場合。
        AttributeError: `function` が `module` にない場合。
    """
    # Maya 再起動後の復元時に `module` を読み込む。
    imported_module = importlib.import_module(module)
    callback = cast(Callable[[], Any], getattr(imported_module, function))

    # 復元先のworkspaceControlがcurrent parentの間にWidgetを接続する。
    return callback()
