# coding: utf-8
import importlib
import sys
import shutil
import pathlib

PACKAGE_NAME = __name__.split(".")[0]


def _remove_pycache():
    """
    パッケージ内、全てのキャッシュを削除する
    """
    # パッケージのモジュールを取得
    module = sys.modules.get(PACKAGE_NAME)

    # モジュールが見つからない場合は、__pycache__を削除できないため、処理を終了する
    if not module:
        return

    # モジュールのファイルパスから、__pycache__ディレクトリを削除する
    package_path = pathlib.Path(module.__file__).parent
    for path in package_path.rglob("__pycache__"):
        shutil.rmtree(path, ignore_errors=True)


def reload_package(clear_pycache=False):
    """
    パッケージをリロードする

    Args:
        clear_pycache (bool, optional): パッケージ内、全てのキャッシュを削除するかどうか.
                                        Defaults to False.
    """
    # キャッシュを削除してからリロードする場合は、__pycache__を削除する
    if clear_pycache:
        _remove_pycache()

    # パッケージ内のすべてのモジュールをリロードする
    modules = [name for name in sys.modules if name.startswith(PACKAGE_NAME)]
    for name in reversed(modules):
        importlib.reload(sys.modules[name])
