# coding: utf-8
"""共有Mayaメニューの所有権と再登録を確認する。"""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import cast

import pytest

from bd_util.maya.ui import (
    is_menu_auto_install_enabled,
    register_menu_item,
    set_menu_auto_install_enabled,
    unregister_menu_owner,
)
from bd_util.maya.ui import menu as menu_module


class FakeMenus:
    """Maya menu commandの所有関係を記録する小さな代替実装。"""

    def __init__(self, prefs_dir: Path) -> None:
        """menuとmenuItemを空の状態で用意する。"""
        self.menus: dict[str, dict[str, object]] = {}
        self.items: dict[str, dict[str, object]] = {}
        self.detached: set[str] = set()
        self.option_vars: dict[str, int] = {}
        self.prefs_dir = prefs_dir

    def internalVar(self, **kwargs: object) -> str:
        """一時ディレクトリをMayaのユーザー設定先として返す。"""
        assert kwargs == {"userPrefDir": True}
        return str(self.prefs_dir)

    def optionVar(self, **kwargs: object) -> object:
        """起動時表示に使うMaya preferenceを模倣する。"""
        if "exists" in kwargs:
            return kwargs["exists"] in self.option_vars
        if "query" in kwargs:
            return self.option_vars[cast(str, kwargs["query"])]
        raise AssertionError("旧optionVarへ書き込んではいけません")

    def savePrefs(self, **kwargs: object) -> None:
        """メニュー操作がMayaの一般設定を保存しないことを確認する。"""
        raise AssertionError("savePrefsを呼んではいけません")

    def menu(self, name: str, **kwargs: object) -> object:
        """menuの作成・照会を模倣する。"""
        if kwargs.get("exists"):
            return name in self.menus
        if kwargs.get("query"):
            if kwargs.get("docTag"):
                return self.menus[name]["docTag"]
            if kwargs.get("itemArray"):
                return [
                    path
                    for path in self.items
                    if path.rpartition("|")[0] == name
                    and path not in self.detached
                ]
            raise AssertionError(kwargs)
        path = f"{kwargs['parent']}|{name}"
        assert path not in self.menus
        self.menus[path] = {"docTag": kwargs["docTag"]}
        return path

    def menuItem(self, name: str, **kwargs: object) -> object:
        """menuItemの作成・編集・照会を模倣する。"""
        if kwargs.get("exists"):
            return name in self.items
        if kwargs.get("query"):
            if kwargs.get("docTag"):
                return self.items[name]["docTag"]
            if kwargs.get("checkBox"):
                return self.items[name]["checkBox"]
            raise AssertionError(kwargs)
        if kwargs.get("edit"):
            self.items[name].update(kwargs)
            return name
        path = f"{kwargs['parent']}|{name}"
        assert path not in self.items
        self.items[path] = dict(kwargs)
        return path

    def deleteUI(self, name: str, **kwargs: object) -> None:
        """指定されたmenuまたはmenuItemを削除する。"""
        if kwargs.get("menu"):
            assert not any(path.startswith(f"{name}|") for path in self.items)
            del self.menus[name]
        elif kwargs.get("menuItem"):
            assert not any(
                path.startswith(f"{name}|")
                for path in self.items
                if path != name
            )
            del self.items[name]
            self.detached.discard(name)
        else:
            raise AssertionError(kwargs)


@pytest.fixture
def fake_menus(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeMenus:
    """UI作成済みのMaya windowを代替し、各testで状態を分離する。"""
    fake = FakeMenus(tmp_path / "prefs")
    monkeypatch.setattr(menu_module, "cmds", fake)
    monkeypatch.setattr(menu_module, "_main_window", lambda: "MayaWindow")
    return fake


def test_menu_is_not_created_in_batch_maya(maya_cmds) -> None:
    """batch Mayaでは共有menuを作成しない。"""
    assert maya_cmds.about(batch=True)
    assert not register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="bdChannelBox",
        label="bdChannelBox",
        command=lambda: None,
    )


def test_owners_share_category_and_reregister_in_place(
    fake_menus: FakeMenus,
) -> None:
    """同じcategory内でownerを分離し、再登録時はcallbackを更新する。"""
    called: list[str] = []
    arguments = dict(
        category="tools", item_id="bdChannelBox", label="bdChannelBox"
    )
    assert register_menu_item(
        owner="bd_tools", command=lambda: called.append("old"), **arguments
    )
    assert register_menu_item(
        owner="bd_extra",
        category="tools",
        item_id="other",
        label="Other",
        command=lambda: called.append("other"),
    )
    assert register_menu_item(
        owner="bd_tools", command=lambda: called.append("new"), **arguments
    )

    root = "MayaWindow|bdUtilMainMenu"
    category = f"{root}|bdUtilCategory_tools"
    assert len(fake_menus.menus) == 1
    assert len(fake_menus.items) == 4
    item = f"{category}|bdUtilItem_8_bd_tools_bdChannelBox"
    option = f"{root}|bdUtilAutoInstallMenuOption"
    assert fake_menus.menu(root, query=True, itemArray=True)[-1] == option
    cast(Callable[..., object], fake_menus.items[item]["command"])("maya")
    assert called == ["new"]

    unregister_menu_owner("bd_tools")
    assert item not in fake_menus.items
    assert category in fake_menus.items
    assert len(fake_menus.items) == 3
    unregister_menu_owner("bd_extra")
    assert not fake_menus.items
    assert not fake_menus.menus


def test_reregister_can_move_item_to_other_category(
    fake_menus: FakeMenus,
) -> None:
    """同じ項目を別categoryへ移しても重複を残さない。"""
    for category in ("tools", "physics"):
        assert register_menu_item(
            owner="bd_tools",
            category=category,
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert len(fake_menus.items) == 3
    assert any("bdUtilCategory_physics" in path for path in fake_menus.items)
    assert not any("bdUtilCategory_tools" in path for path in fake_menus.items)


def test_reregister_recreates_detached_item(fake_menus: FakeMenus) -> None:
    """削除直後にUI registryへ残った孤立項目を作り直す。"""
    called: list[str] = []
    arguments = dict(
        owner="bd_tools",
        category="tools",
        item_id="bdChannelBox",
        label="bdChannelBox",
    )
    assert register_menu_item(
        command=lambda: called.append("old"), **arguments
    )
    category = "MayaWindow|bdUtilMainMenu|bdUtilCategory_tools"
    item = f"{category}|bdUtilItem_8_bd_tools_bdChannelBox"
    fake_menus.detached.add(item)
    assert fake_menus.menuItem(item, exists=True)
    assert not fake_menus.menu(category, query=True, itemArray=True)

    assert register_menu_item(
        command=lambda: called.append("new"), **arguments
    )
    assert fake_menus.menu(category, query=True, itemArray=True) == [item]
    cast(Callable[..., object], fake_menus.items[item]["command"])("maya")
    assert called == ["new"]


def test_auto_install_checkbox_changes_only_next_startup(
    fake_menus: FakeMenus,
) -> None:
    """チェックOFFを保存し、現在のメニューと明示登録は維持する。"""
    assert is_menu_auto_install_enabled()
    assert register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )
    root = "MayaWindow|bdUtilMainMenu"
    option = f"{root}|bdUtilAutoInstallMenuOption"
    assert fake_menus.items[option]["checkBox"] is True

    fake_menus.menuItem(option, edit=True, checkBox=False)
    cast(Callable[..., object], fake_menus.items[option]["command"])()
    assert not is_menu_auto_install_enabled()
    setting_path = fake_menus.prefs_dir / "bakedanuki" / "menu.json"
    assert json.loads(setting_path.read_text(encoding="utf-8")) == {
        "show_menu_on_startup": False
    }
    assert option in fake_menus.items
    assert register_menu_item(
        owner="bd_rig",
        category="rig",
        item_id="sample",
        label="Rig sample",
        command=lambda: None,
    )
    assert fake_menus.menu(root, query=True, itemArray=True)[-1] == option
    assert fake_menus.items[option]["checkBox"] is False

    set_menu_auto_install_enabled(True)
    assert is_menu_auto_install_enabled()
    assert fake_menus.items[option]["checkBox"] is True
    assert json.loads(setting_path.read_text(encoding="utf-8")) == {
        "show_menu_on_startup": True
    }


def test_legacy_option_var_is_read_until_dedicated_file_exists(
    fake_menus: FakeMenus,
) -> None:
    """旧OFF設定を引き継ぎ、専用ファイル保存後はそちらを優先する。"""
    fake_menus.option_vars["bakedanukiMenuAutoInstall"] = 0
    assert not is_menu_auto_install_enabled()
    set_menu_auto_install_enabled(True)
    assert is_menu_auto_install_enabled()
    assert fake_menus.option_vars["bakedanukiMenuAutoInstall"] == 0


def test_legacy_json_key_is_read_until_next_setting_change(
    fake_menus: FakeMenus,
) -> None:
    """旧JSONキーのOFFを保持し、次の変更から新しいキーだけで保存する。"""
    setting_path = fake_menus.prefs_dir / "bakedanuki" / "menu.json"
    setting_path.parent.mkdir(parents=True)
    setting_path.write_text('{"auto_install": false}\n', encoding="utf-8")
    assert not is_menu_auto_install_enabled()

    set_menu_auto_install_enabled(True)

    assert is_menu_auto_install_enabled()
    assert json.loads(setting_path.read_text(encoding="utf-8")) == {
        "show_menu_on_startup": True
    }


def test_new_json_key_takes_priority_over_legacy_key(
    fake_menus: FakeMenus,
) -> None:
    """新旧キーが両方ある場合は新しい表示設定を優先する。"""
    setting_path = fake_menus.prefs_dir / "bakedanuki" / "menu.json"
    setting_path.parent.mkdir(parents=True)
    setting_path.write_text(
        '{"show_menu_on_startup": false, "auto_install": true}\n',
        encoding="utf-8",
    )
    assert not is_menu_auto_install_enabled()


def test_foreign_root_is_never_modified(fake_menus: FakeMenus) -> None:
    """固定UI名が他者に占有されていても編集・削除しない。"""
    root = "MayaWindow|bdUtilMainMenu"
    fake_menus.menus[root] = {"docTag": "other"}
    with pytest.raises(RuntimeError, match="別のUI"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    unregister_menu_owner("bd_tools")
    assert fake_menus.menus == {root: {"docTag": "other"}}


def test_invalid_identifier_is_rejected(fake_menus: FakeMenus) -> None:
    """UI名に使えない識別子でMaya UIを変更しない。"""
    with pytest.raises(ValueError, match="owner"):
        register_menu_item(
            owner="other|package",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert not fake_menus.menus
