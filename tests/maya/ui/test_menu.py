# coding: utf-8
"""共有Mayaメニューの所有権と再登録を確認する。"""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Literal, cast

import pytest

from bd_util.maya.ui import (
    ensure_config_file,
    is_menu_auto_install_enabled,
    register_menu_item,
    set_menu_auto_install_enabled,
    unregister_menu_owner,
)
from bd_util.maya.ui import menu as menu_module
from bd_util.ui import qt


class FakeMenus:
    """Maya menu commandの所有関係を記録する小さな代替実装。"""

    def __init__(self, prefs_dir: Path) -> None:
        """menuとmenuItemを空の状態で用意する。"""
        self.menus: dict[str, dict[str, object]] = {}
        self.items: dict[str, dict[str, object]] = {}
        self.detached: set[str] = set()
        self.option_vars: dict[str, int] = {}
        self.refreshed_icons: dict[str, str] = {}
        self.prefs_dir = prefs_dir

    def refresh_icon(self, item_path: str, image: str) -> None:
        """作成済み項目だけに画像の再読込みが適用されるか記録する。"""
        assert item_path in self.items
        self.refreshed_icons[item_path] = image

    def internalVar(self, **kwargs: object) -> str:
        """一時ディレクトリをMayaのユーザー設定先として返す。"""
        assert kwargs == {"userPrefDir": True}
        return str(self.prefs_dir)

    def lsUI(self, **kwargs: object) -> list[str]:
        """作成済みmenuのfull pathを返す。"""
        assert kwargs == {"menus": True, "long": True}
        return list(self.menus)

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
        if kwargs.get("edit"):
            self.menus[name].update(kwargs)
            return name
        if kwargs.get("query"):
            if kwargs.get("docTag"):
                return self.menus[name]["docTag"]
            if kwargs.get("postMenuCommand"):
                return self.menus[name].get("postMenuCommand", "")
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
        self.menus[path] = {
            "docTag": kwargs["docTag"],
            "label": kwargs["label"],
        }
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
            if name in self.menus:
                self.menus[name].update(kwargs)
            return name
        path = f"{kwargs['parent']}|{name}"
        assert path not in self.items
        self.items[path] = dict(kwargs)
        if kwargs.get("subMenu"):
            self.menus[path] = {
                "docTag": kwargs["docTag"],
                "label": kwargs["label"],
            }
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
            # Mayaはsubmenu項目の削除後も同名のmenuを保持する
            self.detached.discard(name)
        else:
            raise AssertionError(kwargs)


@pytest.fixture
def fake_menus(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> FakeMenus:
    """UI作成済みのMaya windowを代替し、各testで状態を分離する。"""
    fake = FakeMenus(tmp_path / "prefs")
    monkeypatch.delenv("BAKEDANUKI_CONFIG_FILE", raising=False)
    monkeypatch.setattr(menu_module, "cmds", fake)
    monkeypatch.setattr(menu_module, "_main_window", lambda: "MayaWindow")
    monkeypatch.setattr(menu_module, "_refresh_menu_icon", fake.refresh_icon)
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
    assert len(fake_menus.menus) == 2
    assert fake_menus.menus[root]["label"] == "bakedanuki"
    assert len(fake_menus.items) == 4
    item = f"{category}|bdUtilItem_8_bd_tools_bdChannelBox"
    option = f"{root}|bdUtilAutoInstallMenuOption"
    assert fake_menus.menu(root, query=True, itemArray=True)[-1] == option
    cast(Callable[..., object], fake_menus.items[item]["command"])("maya")
    assert called == ["new"]
    assert fake_menus.items[item]["sourceType"] == "python"

    unregister_menu_owner("bd_tools")
    assert item not in fake_menus.items
    assert category in fake_menus.items
    assert len(fake_menus.items) == 3
    unregister_menu_owner("bd_extra")
    assert not fake_menus.items
    assert not fake_menus.menus


def test_reregister_updates_script_and_language_in_both_directions(
    fake_menus: FakeMenus,
) -> None:
    """関数・MEL・Python文字列を同じ項目へ再登録し、言語を更新する。"""
    called: list[bool] = []
    arguments = dict(
        owner="bd_tools", category="tools", item_id="sample", label="Sample"
    )
    item = (
        "MayaWindow|bdUtilMainMenu|bdUtilCategory_tools|"
        "bdUtilItem_8_bd_tools_sample"
    )
    assert register_menu_item(command=lambda: None, **arguments)
    scripts: tuple[tuple[str, Literal["mel", "python"]], ...] = (
        ('print("MEL");', "mel"),
        ("print('Python')", "python"),
        ('print("MEL again");', "mel"),
    )
    for command, source_type in scripts:
        assert register_menu_item(
            command=command, source_type=source_type, **arguments
        )
        assert fake_menus.items[item]["command"] == command
        assert fake_menus.items[item]["sourceType"] == source_type
        assert len(fake_menus.items) == 3

    assert register_menu_item(command=lambda: called.append(True), **arguments)
    assert fake_menus.items[item]["sourceType"] == "python"
    cast(Callable[..., object], fake_menus.items[item]["command"])("maya")
    assert called == [True]


@pytest.mark.parametrize("command", ("", " ", "\r\n\t"))
def test_empty_script_is_rejected_before_ui_changes(
    fake_menus: FakeMenus, command: str
) -> None:
    """空のスクリプトではmenuを作成しない。"""
    with pytest.raises(ValueError, match="空でないスクリプト"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=command,
            source_type="mel",
        )
    assert not fake_menus.items
    assert not fake_menus.menus


@pytest.mark.parametrize(
    ("command", "source_type", "error", "message"),
    (
        (42, "python", TypeError, "文字列または呼び出し可能"),
        ("print('sample')", "invalid", ValueError, "melまたはpython"),
        (lambda: None, "mel", ValueError, "Python関数"),
    ),
)
def test_invalid_command_language_is_rejected_before_ui_changes(
    fake_menus: FakeMenus,
    command: object,
    source_type: str,
    error: type[Exception],
    message: str,
) -> None:
    """不正なコマンド型と言語の組合せではmenuを作成しない。"""
    with pytest.raises(error, match=message):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=cast(str, command),
            source_type=cast(Literal["mel", "python"], source_type),
        )
    assert not fake_menus.items
    assert not fake_menus.menus


def test_existing_owned_root_uses_new_display_label(
    fake_menus: FakeMenus,
) -> None:
    """旧表示名の共有menuを再利用し、項目を保って表示名だけ更新する。"""
    arguments = dict(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )
    assert register_menu_item(**arguments)
    root = "MayaWindow|bdUtilMainMenu"
    fake_menus.menus[root]["label"] = "bd"
    item_count = len(fake_menus.items)

    assert register_menu_item(**arguments)

    assert fake_menus.menus[root]["label"] == "bakedanuki"
    assert len(fake_menus.menus) == 2
    assert len(fake_menus.items) == item_count


def test_menu_icon_can_be_added_replaced_and_removed(
    fake_menus: FakeMenus, tmp_path: Path
) -> None:
    """同じ項目で画像を追加・交換・解除し、日本語を含むpathも渡せる。"""
    icon_dir = tmp_path / "日本語 icons"
    icon_dir.mkdir()
    image = qt.QImage(64, 64, qt.QImage.Format.Format_RGB32)
    image.fill(qt.QColor("white"))
    first = icon_dir / "first.png"
    second = icon_dir / "second.png"
    assert image.save(str(first))
    assert image.save(str(second))
    item = (
        "MayaWindow|bdUtilMainMenu|bdUtilCategory_tools|"
        "bdUtilItem_8_bd_tools_sample"
    )

    for icon_path in (None, first, str(second), None):
        assert register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
            icon_path=icon_path,
        )
        expected = Path(icon_path).as_posix() if icon_path else ""
        assert fake_menus.items[item]["image"] == expected
        assert fake_menus.refreshed_icons[item] == expected
        assert len(fake_menus.items) == 3


@pytest.mark.parametrize("invalid_kind", ["missing", "directory", "broken"])
def test_invalid_icon_warns_and_keeps_menu_command(
    fake_menus: FakeMenus, tmp_path: Path, invalid_kind: str
) -> None:
    """画像の欠落・フォルダ・破損では警告し、項目の起動処理を維持する。"""
    icon_path = tmp_path / "invalid.png"
    if invalid_kind == "directory":
        icon_path.mkdir()
    elif invalid_kind == "broken":
        icon_path.write_text("not an image", encoding="utf-8")
    called: list[bool] = []
    with pytest.warns(RuntimeWarning, match="アイコン画像を読み込めません"):
        assert register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: called.append(True),
            icon_path=icon_path,
        )
    item = (
        "MayaWindow|bdUtilMainMenu|bdUtilCategory_tools|"
        "bdUtilItem_8_bd_tools_sample"
    )
    assert fake_menus.items[item]["image"] == ""
    cast(Callable[..., object], fake_menus.items[item]["command"])()
    assert called == [True]


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


def test_config_file_is_created_once(fake_menus: FakeMenus) -> None:
    """コメント例を自動生成し、利用者が編集した内容を保持する。"""
    path = ensure_config_file()
    assert path == fake_menus.prefs_dir / "bakedanuki" / "config.toml"
    content = path.read_text(encoding="utf-8")
    assert content.startswith("[menu]\n")
    assert (
        "# parent_menu を指定しない場合、bakedanuki は最上位メニューに表示されます。"
        in content
    )
    assert "# parent_menu = " in content

    path.write_text("# 個別に編集した内容\n", encoding="utf-8")
    assert ensure_config_file() == path
    assert path.read_text(encoding="utf-8") == "# 個別に編集した内容\n"


def test_nested_root_preserves_existing_parent(fake_menus: FakeMenus) -> None:
    """既存メニュー配下にrootを作り、解除では既存メニューを残す。"""
    parent = cast(
        str,
        fake_menus.menu(
            "customToolsMenu",
            parent="MayaWindow",
            label="tools",
            docTag="other",
        ),
    )
    parent = cast(
        str,
        fake_menus.menuItem(
            "freeToolsMenu",
            parent=parent,
            label="free_tools",
            subMenu=True,
            docTag="other",
        ),
    )
    path = ensure_config_file()
    path.write_text(f'[menu]\nparent_menu = "{parent}"\n', encoding="utf-8")

    assert register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )
    root = f"{parent}|bdUtilMainMenu"
    assert root in fake_menus.menus
    assert root in fake_menus.items
    assert "MayaWindow|bdUtilMainMenu" not in fake_menus.menus
    assert register_menu_item(
        owner="bd_rig",
        category="rig",
        item_id="sample",
        label="Rig sample",
        command=lambda: None,
    )

    set_menu_auto_install_enabled(False)
    option = f"{root}|bdUtilAutoInstallMenuOption"
    assert fake_menus.items[option]["checkBox"] is False
    unregister_menu_owner("bd_tools")
    assert root in fake_menus.menus
    assert f"{root}|bdUtilCategory_tools" not in fake_menus.menus
    assert f"{root}|bdUtilCategory_rig" in fake_menus.menus
    unregister_menu_owner("bd_rig")
    assert root not in fake_menus.menus
    assert parent in fake_menus.menus
    assert "MayaWindow|customToolsMenu" in fake_menus.menus
    assert register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )


@pytest.mark.parametrize("initialized", (False, True))
def test_nested_root_follows_existing_menu_items(
    fake_menus: FakeMenus,
    monkeypatch: pytest.MonkeyPatch,
    initialized: bool,
) -> None:
    """遅延生成される既存項目の後へ追加し、再登録や解除でも維持する。"""
    parent = "MayaWindow|customToolsMenu"
    fake_menus.menu(
        "customToolsMenu", parent="MayaWindow", label="tools", docTag="other"
    )
    fake_menus.menu(
        parent,
        edit=True,
        postMenuCommand="buildExistingMenu",
        postMenuCommandOnce=True,
    )
    calls: list[str] = []

    def build_existing_menu(path: str) -> None:
        """親が空の間だけ既存項目を生成するMayaの処理を模倣する。"""
        assert path == parent
        assert not fake_menus.menu(path, query=True, itemArray=True)
        calls.append(path)
        fake_menus.menuItem(
            "existingItem", parent=path, label="Existing", docTag="other"
        )

    monkeypatch.setattr(
        menu_module, "_emit_menu_about_to_show", build_existing_menu
    )
    if initialized:
        build_existing_menu(parent)
        calls.clear()
    ensure_config_file().write_text(
        f'[menu]\nparent_menu = "{parent}"\n', encoding="utf-8"
    )

    for _ in range(2):
        assert register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
        assert fake_menus.menu(parent, query=True, itemArray=True) == [
            f"{parent}|existingItem",
            f"{parent}|bdUtilMainMenu",
        ]
    assert calls == ([] if initialized else [parent])
    assert fake_menus.menus[parent]["postMenuCommand"] == "buildExistingMenu"
    assert fake_menus.menus[parent]["postMenuCommandOnce"] is True

    unregister_menu_owner("bd_tools")
    assert fake_menus.menu(parent, query=True, itemArray=True) == [
        f"{parent}|existingItem"
    ]


def test_explicit_config_file_takes_priority(
    fake_menus: FakeMenus, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """起動環境で指定したTOMLを個人用TOMLより優先する。"""
    parent = cast(
        str,
        fake_menus.menu(
            "customToolsMenu",
            parent="MayaWindow",
            label="tools",
            docTag="other",
        ),
    )
    personal = ensure_config_file()
    personal.write_text(
        '[menu]\nparent_menu = "MayaWindow|missingMenu"\n',
        encoding="utf-8",
    )
    external = tmp_path / "project-a.toml"
    external.write_text(
        f'[menu]\nparent_menu = "{parent}"\n', encoding="utf-8"
    )
    monkeypatch.setenv("BAKEDANUKI_CONFIG_FILE", str(external))

    assert register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )
    assert f"{parent}|bdUtilMainMenu" in fake_menus.menus
    assert personal.read_text(encoding="utf-8").startswith("[menu]")


def test_missing_placement_parent_never_falls_back(
    fake_menus: FakeMenus,
) -> None:
    """設定された親がなければ最上位へ黙って配置しない。"""
    path = ensure_config_file()
    path.write_text(
        '[menu]\nparent_menu = "MayaWindow|missingMenu"\n',
        encoding="utf-8",
    )
    with pytest.raises(RuntimeError, match="既存メニューが見つかりません"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert not fake_menus.menus


def test_missing_explicit_file_never_falls_back(
    fake_menus: FakeMenus, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    """起動環境で指定したファイルがなければ個人用へ切り替えない。"""
    external = tmp_path / "missing-project.toml"
    monkeypatch.setenv("BAKEDANUKI_CONFIG_FILE", str(external))
    with pytest.raises(FileNotFoundError, match="設定が見つかりません"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert not fake_menus.menus


def test_relative_explicit_file_is_rejected(
    fake_menus: FakeMenus, monkeypatch: pytest.MonkeyPatch
) -> None:
    """起動ディレクトリで意味が変わる相対パスを受け付けない。"""
    monkeypatch.setenv("BAKEDANUKI_CONFIG_FILE", "project-a.toml")
    with pytest.raises(ValueError, match="絶対パス"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert not fake_menus.menus


def test_placement_change_waits_for_restart(fake_menus: FakeMenus) -> None:
    """起動中の配置変更は重複rootを作らず、旧rootを解除できる。"""
    assert register_menu_item(
        owner="bd_tools",
        category="tools",
        item_id="sample",
        label="Sample",
        command=lambda: None,
    )
    parent = cast(
        str,
        fake_menus.menu(
            "customToolsMenu",
            parent="MayaWindow",
            label="tools",
            docTag="other",
        ),
    )
    path = ensure_config_file()
    path.write_text(f'[menu]\nparent_menu = "{parent}"\n', encoding="utf-8")
    with pytest.raises(RuntimeError, match="再起動後"):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert "MayaWindow|bdUtilMainMenu" in fake_menus.menus
    assert f"{parent}|bdUtilMainMenu" not in fake_menus.menus
    unregister_menu_owner("bd_tools")
    assert "MayaWindow|bdUtilMainMenu" not in fake_menus.menus


@pytest.mark.parametrize(
    "content, message",
    (
        ('[menu]\nparent_menu = "MayaWindow|"\n', "完全なUIパス"),
        ("[menu]\nparent_menu = 42\n", "parent_menu"),
        ("[menu]\nparent_mneu = 'typo'\n", "未知のキー"),
        ("parent_menu = 'typo'\n", "未知のキー"),
        ("menu = 42\n", "形式が不正"),
        ("[menu]\nparent_menu = [\n", "TOMLが不正"),
    ),
)
def test_invalid_placement_is_reported(
    fake_menus: FakeMenus, content: str, message: str
) -> None:
    """設定の誤記を最上位への暗黙の配置に変えない。"""
    path = ensure_config_file()
    path.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError, match=message):
        register_menu_item(
            owner="bd_tools",
            category="tools",
            item_id="sample",
            label="Sample",
            command=lambda: None,
        )
    assert not fake_menus.menus
