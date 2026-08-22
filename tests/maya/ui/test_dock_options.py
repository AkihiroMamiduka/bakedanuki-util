# coding: utf-8
from types import SimpleNamespace

import pytest

from bd_util.maya.ui import DockArea, DockOptions, DockRestoreSpec
from bd_util.maya.ui.dock import restore as dock_restore


def test_dock_options_create_mixin_arguments() -> None:
    # 利用者向けの設定値をまとめて作成する。
    options = DockOptions(
        area=DockArea.LEFT,
        allowed_area=DockArea.ALL,
        floating=False,
        initial_width=420,
        initial_height=640,
        minimum_width=240,
        retain=True,
    )

    # MayaQWidgetDockableMixinの引数名と値へ変換されることを確認する。
    assert options.to_mixin_arguments("restore()") == {
        "floating": False,
        "area": "left",
        "allowedArea": "all",
        "retain": True,
        "uiScript": "restore()",
        "width": 420,
        "height": 640,
        "minWidth": 240,
    }


def test_dock_options_dispose_on_close_by_default() -> None:
    # 既定値ではworkspaceControlをclose時に削除する。
    options = DockOptions()

    # MayaQWidgetDockableMixinへretain=Falseを渡す。
    assert not options.retain
    assert options.to_mixin_arguments("restore()")["retain"] is False


@pytest.mark.parametrize(
    ("keyword", "value"),
    [
        ("initial_width", 0),
        ("initial_height", -1),
        ("minimum_width", 0),
    ],
)
def test_dock_options_reject_non_positive_size(
    keyword: str,
    value: int,
) -> None:
    # 検証対象のサイズだけを不正値へ置き換える。
    arguments = {keyword: value}

    # Mayaへ無効な初期サイズを渡す前に例外になることを確認する。
    with pytest.raises(ValueError):
        DockOptions(**arguments)


def test_dock_options_reject_all_as_initial_area() -> None:
    # allは許可領域専用で初期位置には利用できないことを確認する。
    with pytest.raises(ValueError):
        DockOptions(area=DockArea.ALL)


def test_dock_options_rejects_area_outside_allowed_area() -> None:
    # 初期位置と単一の許可領域が矛盾する設定を拒否する。
    with pytest.raises(ValueError):
        DockOptions(
            area=DockArea.RIGHT,
            allowed_area=DockArea.LEFT,
        )


@pytest.mark.parametrize(
    ("module", "function"),
    [
        ("invalid-module", "restore"),
        ("sample.module", "invalid-function"),
    ],
)
def test_restore_spec_rejects_unsafe_name(
    module: str,
    function: str,
) -> None:
    # uiScriptへ安全に埋め込めない名前を拒否することを確認する。
    with pytest.raises(ValueError):
        DockRestoreSpec(module=module, function=function)


def test_restore_spec_creates_importable_ui_script() -> None:
    # 利用者moduleの復元関数を指定する。
    restore_spec = DockRestoreSpec(
        module="sample_tool.ui.main_window",
        function="restore",
    )

    # 共通の遅延import入口を呼ぶuiScriptになることを確認する。
    assert restore_spec.to_ui_script() == (
        "from bd_util.maya.ui import restore_dockable; "
        "restore_dockable('sample_tool.ui.main_window', 'restore')"
    )


def test_restore_dockable_imports_module_and_calls_function(
    monkeypatch,
) -> None:
    # 復元関数の結果と呼び出し履歴を確認できるmoduleを用意する。
    calls: list[str] = []

    def restore() -> str:
        """復元関数の呼び出しを記録する。"""
        # 呼び出されたmoduleを識別できる値を残す。
        calls.append("restore")
        return "restored"

    module = SimpleNamespace(restore=restore)
    monkeypatch.setattr(
        dock_restore.importlib,
        "import_module",
        lambda name: module,
    )

    # 遅延importしたmoduleの指定関数が実行されることを確認する。
    assert dock_restore.restore_dockable("sample_tool.ui") == "restored"
    assert calls == ["restore"]
