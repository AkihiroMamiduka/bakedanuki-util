# coding: utf-8

import importlib
import pathlib
import shutil
import sys
from types import ModuleType

PACKAGE_NAME = __name__.split(".")[0]


def _is_package_module(name: str) -> bool:
    return name == PACKAGE_NAME or name.startswith(f"{PACKAGE_NAME}.")


def _get_package_module_names() -> list[str]:
    return [name for name in sys.modules if _is_package_module(name)]


def _remove_pycache() -> None:
    """
    パッケージ内、全てのキャッシュを削除する
    """
    # パッケージのモジュールを取得
    module = sys.modules.get(PACKAGE_NAME)

    # モジュールが見つからない場合は、__pycache__を削除できないため、処理を終了する
    if module is None:
        return

    # モジュールのファイルパスから、__pycache__ディレクトリを削除する
    module_file = module.__file__
    if module_file is None:
        return

    package_path = pathlib.Path(module_file).parent
    for path in package_path.rglob("__pycache__"):
        shutil.rmtree(path, ignore_errors=True)


def _remove_parent_module_attrs(module_names: list[str]) -> None:
    """
    親モジュールが保持している子モジュール参照を削除する。

    例:
        sys.modules["bd_util.maya"] を削除しても、
        bd_util.maya 属性には古いモジュールが残る場合がある。
        その参照を削除して、再 import 時に新しいモジュールを取得できるようにする。
    """
    for name in sorted(module_names, key=lambda n: n.count("."), reverse=True):
        parent_name, _, child_name = name.rpartition(".")
        if not parent_name:
            continue

        parent_module = sys.modules.get(parent_name)
        child_module = sys.modules.get(name)
        if parent_module is None or child_module is None:
            continue

        if getattr(parent_module, child_name, None) is child_module:
            delattr(parent_module, child_name)


def _remove_package_modules(module_names: list[str]) -> None:
    for name in sorted(module_names, key=lambda n: n.count("."), reverse=True):
        sys.modules.pop(name, None)


def reload_package(clear_pycache: bool = False) -> ModuleType:
    """
    パッケージをリロードする

    Args:
        clear_pycache (bool, optional): パッケージ内、全てのキャッシュを削除するかどうか.
                                        Defaults to False.
    """
    # キャッシュを削除してからリロードする場合は、__pycache__を削除する
    if clear_pycache:
        _remove_pycache()

    old_package = sys.modules.get(PACKAGE_NAME)
    module_names = _get_package_module_names()

    # 親モジュールが保持している子モジュール参照を削除する
    _remove_parent_module_attrs(module_names)

    # sys.modules からパッケージを削除し、import 順で作り直す
    _remove_package_modules(module_names)
    importlib.invalidate_caches()
    new_package = importlib.import_module(PACKAGE_NAME)

    # Maya コンソールなどで保持している bd_util 変数を、新しい内容へ寄せる
    if old_package is not None and old_package is not new_package:
        old_package.__dict__.clear()
        old_package.__dict__.update(new_package.__dict__)

    return new_package
