# coding: utf-8
"""複数のpackageが共有するMayaメインメニューを管理する。"""

from __future__ import annotations

import json
import os
import re
import tempfile
from collections.abc import Callable
from pathlib import Path
from typing import cast

from maya import cmds, mel

_ROOT_NAME = "bdUtilMainMenu"
_ROOT_TAG = "bd_util:menu:root"
_CATEGORY_PREFIX = "bdUtilCategory_"
_ITEM_PREFIX = "bdUtilItem_"
_AUTO_INSTALL_OPTION_VAR = "bakedanukiMenuAutoInstall"
_SHOW_MENU_ON_STARTUP_KEY = "show_menu_on_startup"
_LEGACY_AUTO_INSTALL_SETTING_KEY = "auto_install"
_AUTO_INSTALL_NAME = "bdUtilAutoInstallMenuOption"
_AUTO_INSTALL_TAG = "bd_util:menu:auto_install"
_AUTO_INSTALL_LABEL = "Maya 起動時に bd メニューを表示"
_IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_]*\Z")

__all__ = [
    "is_menu_auto_install_enabled",
    "set_menu_auto_install_enabled",
    "register_menu_item",
    "unregister_menu_owner",
]


def is_menu_auto_install_enabled() -> bool:
    """起動時の共有メニュー自動登録が有効か返す。

    専用ファイルがなければ旧optionVarを読み、どちらもなければ有効とする。
    """
    path = _auto_install_settings_path()
    if path.is_file():
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"bdメニュー設定の形式が不正です: {path}")
        enabled = data.get(
            _SHOW_MENU_ON_STARTUP_KEY,
            data.get(_LEGACY_AUTO_INSTALL_SETTING_KEY),
        )
        if type(enabled) is not bool:
            raise ValueError(f"bdメニュー設定の形式が不正です: {path}")
        return cast(bool, enabled)
    if not cmds.optionVar(exists=_AUTO_INSTALL_OPTION_VAR):
        return True
    return cast(int, cmds.optionVar(query=_AUTO_INSTALL_OPTION_VAR)) != 0


def _auto_install_settings_path() -> Path:
    """現在のMayaバージョン用の専用設定ファイルを返す。"""
    return (
        Path(cast(str, cmds.internalVar(userPrefDir=True)))
        / "bakedanuki"
        / "menu.json"
    )


def set_menu_auto_install_enabled(enabled: bool) -> None:
    """起動時の共有メニュー自動登録を専用ファイルへ保存する。

    変更したセッションのメニューは残し、次回起動時から自動登録に反映する。
    """
    path = _auto_install_settings_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None
    try:
        # 同じディレクトリへ一時保存してから置き換え、途中書込みを避ける
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=".menu-",
            suffix=".tmp",
            delete=False,
        ) as file:
            temp_path = Path(file.name)
            json.dump({_SHOW_MENU_ON_STARTUP_KEY: enabled}, file, indent=2)
            file.write("\n")
        os.replace(temp_path, path)
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)

    # 現在のメニューがあれば、外部からの設定変更もチェック表示へ反映する
    main_window = _main_window()
    if main_window is None:
        return
    root = f"{main_window}|{_ROOT_NAME}"
    option = f"{root}|{_AUTO_INSTALL_NAME}"
    if (
        cmds.menu(root, exists=True)
        and _is_owned_root(root)
        and option in _children(root)
        and _is_owned_auto_install_option(option)
    ):
        cmds.menuItem(option, edit=True, checkBox=enabled)


def _validate_identifier(value: str, field: str) -> None:
    """Maya UI名に使用できる安定した識別子を検証する。"""
    if not _IDENTIFIER.fullmatch(value):
        raise ValueError(
            f"{field}には英字で始まる英数字と_の識別子を指定してください"
        )


def _main_window() -> str | None:
    """UIを作成できるMaya main window名を返す。"""
    if cmds.about(batch=True):
        return None
    try:
        name = cast(
            str,
            mel.eval("global string $gMainWindow; $bdUtilTemp=$gMainWindow"),
        )
    except RuntimeError:
        return None
    if not name or not cmds.window(name, exists=True):
        return None
    return name


def _leaf(path: str) -> str:
    """Maya UIのfull pathから末尾のUI名を取り出す。"""
    return path.rsplit("|", 1)[-1]


def _children(parent: str) -> tuple[str, ...]:
    """menuの直下にある項目をfull pathで返す。"""
    items = cast(
        list[str] | None, cmds.menu(parent, query=True, itemArray=True)
    )
    return tuple(
        item if "|" in item else f"{parent}|{item}" for item in items or ()
    )


def _category_name(category: str) -> str:
    """categoryから再読み込み後も同じUI名を作る。"""
    return f"{_CATEGORY_PREFIX}{category}"


def _item_prefix(owner: str) -> str:
    """owner単位の削除に使用する衝突しない接頭辞を返す。"""
    return f"{_ITEM_PREFIX}{len(owner)}_{owner}_"


def _item_name(owner: str, item_id: str) -> str:
    """ownerとitem IDから安定したUI名を作る。"""
    return f"{_item_prefix(owner)}{item_id}"


def _category_tag(category: str) -> str:
    """categoryの所有を示すMaya docTagを返す。"""
    return f"bd_util:menu:category:{category}"


def _item_tag(owner: str, item_id: str) -> str:
    """項目の所有を示すMaya docTagを返す。"""
    return f"bd_util:menu:item:{owner}:{item_id}"


def _is_owned_root(root: str) -> bool:
    """既存のrootがこの基盤で作られたものか判定する。"""
    return cast(str, cmds.menu(root, query=True, docTag=True)) == _ROOT_TAG


def _is_owned_category(path: str, category: str) -> bool:
    """既存のcategoryがこの基盤で作られたものか判定する。"""
    return cast(
        str, cmds.menuItem(path, query=True, docTag=True)
    ) == _category_tag(category)


def _is_owned_item(path: str, owner: str, item_id: str) -> bool:
    """既存の項目が指定されたpackageに属するか判定する。"""
    return cast(
        str, cmds.menuItem(path, query=True, docTag=True)
    ) == _item_tag(owner, item_id)


def _is_owned_auto_install_option(path: str) -> bool:
    """既存の起動時表示項目がこの基盤に属するか判定する。"""
    return (
        cast(str, cmds.menuItem(path, query=True, docTag=True))
        == _AUTO_INSTALL_TAG
    )


def _ensure_auto_install_option(root: str) -> None:
    """起動時表示のチェック項目を共有メニューの末尾へ配置する。"""
    path = f"{root}|{_AUTO_INSTALL_NAME}"

    def invoke(*_args: object) -> None:
        """チェック項目の現状態を次回起動用の設定へ保存する。"""
        enabled = cast(bool, cmds.menuItem(path, query=True, checkBox=True))
        set_menu_auto_install_enabled(enabled)

    children = _children(root)
    if cmds.menuItem(path, exists=True):
        if not _is_owned_auto_install_option(path):
            raise RuntimeError(f"{path}は別のUIで使用されています")
        if children and children[-1] == path:
            cmds.menuItem(
                path,
                edit=True,
                label=_AUTO_INSTALL_LABEL,
                checkBox=is_menu_auto_install_enabled(),
                command=invoke,
            )
            return

        # 新しいcategoryより上にある項目や孤立項目を末尾へ作り直す
        cmds.deleteUI(path, menuItem=True)
        if cmds.menuItem(path, exists=True):
            if path in _children(root):
                raise RuntimeError(f"{path}を移動できませんでした")
            cmds.deleteUI(path, menuItem=True)
        if cmds.menuItem(path, exists=True):
            raise RuntimeError(f"{path}の旧項目を削除できませんでした")

    created = cast(
        str | bool,
        cmds.menuItem(
            _AUTO_INSTALL_NAME,
            parent=root,
            label=_AUTO_INSTALL_LABEL,
            checkBox=is_menu_auto_install_enabled(),
            command=invoke,
            docTag=_AUTO_INSTALL_TAG,
        ),
    )
    if not created or path not in _children(root):
        raise RuntimeError(f"{path}をmenuへ登録できませんでした")


def _owned_categories(root: str) -> tuple[str, ...]:
    """root直下の、この基盤が作成したcategoryだけを返す。"""
    categories: list[str] = []
    for path in _children(root):
        name = _leaf(path)
        if not name.startswith(_CATEGORY_PREFIX):
            continue
        category = name.removeprefix(_CATEGORY_PREFIX)
        if _is_owned_category(path, category):
            categories.append(path)
    return tuple(categories)


def _delete_empty_category(path: str) -> None:
    """他の項目がないcategoryだけを削除する。"""
    if not _children(path):
        cmds.deleteUI(path, menuItem=True)


def _delete_empty_root(root: str) -> None:
    """package項目のないrootと基盤所有の設定項目を片付ける。"""
    children = _children(root)
    option = f"{root}|{_AUTO_INSTALL_NAME}"
    if children == (option,) and _is_owned_auto_install_option(option):
        cmds.deleteUI(option, menuItem=True)
    if not _children(root):
        cmds.deleteUI(root, menu=True)


def _ensure_root(main_window: str) -> str:
    """所有が確認できる共有rootを作成または再利用する。"""
    root = f"{main_window}|{_ROOT_NAME}"
    if cmds.menu(root, exists=True):
        if not _is_owned_root(root):
            raise RuntimeError(f"{root}は別のUIで使用されています")
        return root
    cmds.menu(
        _ROOT_NAME,
        parent=main_window,
        label="bd",
        tearOff=False,
        docTag=_ROOT_TAG,
    )
    return root


def _ensure_category(root: str, category: str) -> str:
    """所有が確認できるcategory submenuを作成または再利用する。"""
    path = f"{root}|{_category_name(category)}"
    if cmds.menuItem(path, exists=True):
        if not _is_owned_category(path, category):
            raise RuntimeError(f"{path}は別のUIで使用されています")
        return path
    cmds.menuItem(
        _category_name(category),
        parent=root,
        label=category,
        subMenu=True,
        tearOff=False,
        docTag=_category_tag(category),
    )
    return path


def register_menu_item(
    *,
    owner: str,
    category: str,
    item_id: str,
    label: str,
    command: Callable[[], object],
) -> bool:
    """`bd > category`へpackage所有の項目を登録する。

    同じownerとitem IDは再登録で更新し、別categoryへ移した場合は
    古い項目を削除する。batchまたはmain window未生成時は何もせずFalseを返す。
    """
    _validate_identifier(owner, "owner")
    _validate_identifier(category, "category")
    _validate_identifier(item_id, "item_id")
    if not label:
        raise ValueError("labelには空でない文字列を指定してください")
    if not callable(command):
        raise TypeError("commandには呼び出し可能な値を指定してください")

    main_window = _main_window()
    if main_window is None:
        return False

    # MayaのitemArrayに属する項目だけを現役とみなし、旧menu内の項目を探す
    root = _ensure_root(main_window)
    target_category = f"{root}|{_category_name(category)}"
    target_name = _item_name(owner, item_id)
    item_path = f"{target_category}|{target_name}"
    if cmds.menuItem(target_category, exists=True) and not _is_owned_category(
        target_category, category
    ):
        raise RuntimeError(f"{target_category}は別のUIで使用されています")
    if cmds.menuItem(item_path, exists=True) and not _is_owned_item(
        item_path, owner, item_id
    ):
        raise RuntimeError(f"{item_path}は別のUIで使用されています")

    current_item: str | None = None
    for old_category in _owned_categories(root):
        for old_item in _children(old_category):
            if not _is_owned_item(old_item, owner, item_id):
                continue
            if old_category == target_category and current_item is None:
                current_item = old_item
            else:
                cmds.deleteUI(old_item, menuItem=True)
                _delete_empty_category(old_category)

    target_category = _ensure_category(root, category)

    def invoke(*_args: object) -> object:
        """Mayaが渡すUI引数を除いて登録された処理を呼ぶ。"""
        return command()

    if current_item is not None:
        cmds.menuItem(current_item, edit=True, label=label, command=invoke)
        _ensure_auto_install_option(root)
        return True

    # deleteUI直後の旧項目は同名で存在しても新しいsubmenuに属さない
    if cmds.menuItem(item_path, exists=True):
        if item_path in _children(target_category):
            raise RuntimeError(f"{item_path}が重複しています")
        cmds.deleteUI(item_path, menuItem=True)
        if cmds.menuItem(item_path, exists=True):
            raise RuntimeError(f"{item_path}の旧項目を削除できませんでした")

    created = cast(
        str | bool,
        cmds.menuItem(
            target_name,
            parent=target_category,
            label=label,
            command=invoke,
            docTag=_item_tag(owner, item_id),
        ),
    )
    if not created or item_path not in _children(target_category):
        raise RuntimeError(f"{item_path}をmenuへ登録できませんでした")
    _ensure_auto_install_option(root)
    return True


def unregister_menu_owner(owner: str) -> None:
    """指定packageの項目だけを削除し、空になったmenuを片付ける。"""
    _validate_identifier(owner, "owner")
    main_window = _main_window()
    if main_window is None:
        return
    root = f"{main_window}|{_ROOT_NAME}"
    if not cmds.menu(root, exists=True) or not _is_owned_root(root):
        return

    # Maya UIに残る名前とdocTagから所有を判定し、module状態に依存しない
    prefix = _item_prefix(owner)
    for category in _owned_categories(root):
        for item in _children(category):
            name = _leaf(item)
            if name.startswith(prefix) and _is_owned_item(
                item, owner, name.removeprefix(prefix)
            ):
                cmds.deleteUI(item, menuItem=True)
        _delete_empty_category(category)

    _delete_empty_root(root)
