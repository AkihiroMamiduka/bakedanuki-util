# coding: utf-8
"""開いているMayaツールをリロード後に再表示するための情報を管理する。"""

from __future__ import annotations

import importlib
from collections.abc import Callable, Sequence
from typing import TypeAlias, cast

from maya import cmds

from .dock import workspace_control

OpenTool: TypeAlias = tuple[str, str, str, str]
DockTool: TypeAlias = tuple[OpenTool, str]

# 登録順を保ち、遅れて届いた旧Windowの終了通知はtokenで区別する
_open_tools: dict[tuple[str, str], tuple[OpenTool, object]] = {}

__all__ = [
    "OpenTool",
    "DockTool",
    "register_open_tool",
    "unregister_open_tool",
    "snapshot_open_tools",
    "reopen_tools",
]


def register_open_tool(
    owner: str,
    tool_id: str,
    module: str,
    function: str,
    *,
    token: object,
) -> None:
    """表示済みツールの再表示先を、現在のWindowのtokenと共に記録する。"""
    if not all((owner, tool_id, module, function)):
        raise ValueError("再表示情報には空でない名前を指定してください")
    _open_tools[(owner, tool_id)] = (
        (owner, tool_id, module, function),
        token,
    )


def unregister_open_tool(owner: str, tool_id: str, *, token: object) -> None:
    """登録時と同じWindowから届いた終了通知だけを反映する。"""
    key = (owner, tool_id)
    current = _open_tools.get(key)
    if current is not None and current[1] is token:
        del _open_tools[key]


def snapshot_open_tools(
    owner: str, *, dock_tools: Sequence[DockTool] = ()
) -> tuple[OpenTool, ...]:
    """指定packageの開いているtoolと未生成の復元待ちdockを返す。"""
    entries = [
        entry for entry, _token in _open_tools.values() if entry[0] == owner
    ]
    known_keys = {(entry[0], entry[1]) for entry in entries}

    # MayaがWidgetをまだ生成していないdockもcontrolの表示状態から補う
    workspace_query = cast(Callable[..., object], cmds.workspaceControl)
    for entry, control_name in dock_tools:
        key = (entry[0], entry[1])
        if entry[0] != owner or key in known_keys:
            continue
        if workspace_control.exists(control_name) and bool(
            workspace_query(control_name, query=True, visible=True)
        ):
            entries.append(entry)
            known_keys.add(key)
    return tuple(entries)


def reopen_tools(entries: Sequence[OpenTool]) -> None:
    """新しいmoduleの表示関数を呼び、失敗したツールをまとめて通知する。"""
    errors: list[Exception] = []
    for owner, tool_id, module_name, function_name in entries:
        try:
            module = importlib.import_module(module_name)
            show = cast(object, getattr(module, function_name))
            if not callable(show):
                raise TypeError(
                    f"{module_name}.{function_name}は呼び出せません"
                )
            show()
        except Exception as error:
            errors.append(
                RuntimeError(
                    f"{owner}.{tool_id}を再表示できませんでした: {error}"
                )
            )
    if errors:
        raise ExceptionGroup("ツールの再表示に失敗しました", errors)
