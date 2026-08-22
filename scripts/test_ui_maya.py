"""Maya UI互換性テストを対象別に実行するランナー。"""

from __future__ import annotations

import argparse
import os
import platform
import sys
from pathlib import Path

_REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
_PYTHON_ROOT = _REPOSITORY_ROOT / "bakedanuki" / "bakedanuki-util" / "python"
_PYTEST_ROOT = Path(os.environ["TEMP"]) / "codex-mayapy-pytest"
_TEST_PATHS = {
    "qt": _REPOSITORY_ROOT / "tests" / "ui",
    "maya": _REPOSITORY_ROOT / "tests" / "maya" / "ui",
}


def _prepare_import_paths() -> None:
    """pytestとbd_utilのimportパスを追加する。"""

    # リポジトリ内実装と一時配置したpytestを優先して読み込む。
    sys.path[:0] = [str(_PYTEST_ROOT), str(_PYTHON_ROOT)]


def _print_environment() -> int:
    """Maya、Python、Qt bindingのバージョンを表示する。"""

    # 実際にfacadeをimportし、各Mayaのbinding選択まで確認する。
    from maya.api import OpenMaya as om

    from bd_util.ui import qt

    print(
        "UI environment: Maya {}, Python {}, {} {}".format(
            om.MGlobal.mayaVersion(),
            platform.python_version(),
            qt.QT_BINDING,
            qt.QT_BINDING_VERSION,
        )
    )
    return 0


def _run_tests(target: str) -> int:
    """指定されたUIテスト群を実行する。"""

    # Mayaごとのmayapyプロセス内でpytestを起動する。
    import pytest

    return pytest.main(["-p", "no:cacheprovider", str(_TEST_PATHS[target])])


def main() -> int:
    """指定された環境確認またはUIテストを実行する。"""

    # PowerShellから渡された検証対象を解釈する。
    parser = argparse.ArgumentParser()
    parser.add_argument("target", choices=("environment", "qt", "maya"))
    args = parser.parse_args()

    _prepare_import_paths()
    if args.target == "environment":
        return _print_environment()
    return _run_tests(args.target)


if __name__ == "__main__":
    raise SystemExit(main())
