# coding: utf-8
"""Mayaツールの再表示情報がpackage reloadを越せることを確認する。"""

from __future__ import annotations

import sys
from types import ModuleType

import pytest

from bd_util.maya.ui import (
    register_open_tool,
    reopen_tools,
    snapshot_open_tools,
    unregister_open_tool,
)
from bd_util.maya.ui import reopen as reopen_module


def test_snapshot_keeps_only_open_tools_for_owner() -> None:
    """別packageと終了済みtoolを除き、遅れた旧Window通知を無視する。"""
    old_token = object()
    current_token = object()
    other_token = object()
    try:
        register_open_tool(
            "reopen_test_owner", "one", "sample.one", "show", token=old_token
        )
        register_open_tool(
            "reopen_test_other", "two", "sample.two", "show", token=other_token
        )
        register_open_tool(
            "reopen_test_owner",
            "one",
            "sample.one",
            "show",
            token=current_token,
        )
        unregister_open_tool("reopen_test_owner", "one", token=old_token)
        assert snapshot_open_tools("reopen_test_owner") == (
            ("reopen_test_owner", "one", "sample.one", "show"),
        )
        unregister_open_tool("reopen_test_owner", "one", token=current_token)
        assert snapshot_open_tools("reopen_test_owner") == ()
    finally:
        unregister_open_tool("reopen_test_owner", "one", token=current_token)
        unregister_open_tool("reopen_test_other", "two", token=other_token)


def test_snapshot_includes_dock_before_widget_restore(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """非アクティブな復元待ちdockもWindow未生成のまま再表示対象に含める。"""
    entry = ("reopen_test_owner", "lazy", "sample.lazy", "show")
    monkeypatch.setattr(
        reopen_module.workspace_control,
        "exists",
        lambda name: name == "lazyWorkspaceControl",
    )
    monkeypatch.setattr(
        reopen_module.cmds,
        "workspaceControl",
        lambda _name, **_flags: True,
    )
    assert snapshot_open_tools(
        "reopen_test_owner",
        dock_tools=((entry, "lazyWorkspaceControl"),),
    ) == (entry,)


def test_reopen_imports_current_module_and_continues_after_failure(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """保存した関数参照を使わず、失敗後も残りのtoolを開く。"""
    calls: list[str] = []
    module = ModuleType("reopen_test_module")

    def show() -> None:
        """新しいmoduleからの表示呼出しを記録する。"""
        calls.append("shown")

    setattr(module, "show", show)
    monkeypatch.setitem(sys.modules, module.__name__, module)
    entries = (
        ("owner", "missing", "reopen_test_module", "missing"),
        ("owner", "working", "reopen_test_module", "show"),
    )
    with pytest.raises(ExceptionGroup, match="再表示に失敗"):
        reopen_tools(entries)
    assert calls == ["shown"]
