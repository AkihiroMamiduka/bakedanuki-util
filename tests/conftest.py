# coding: utf-8
from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[1]
PACKAGE_PYTHON_DIR = ROOT_DIR / "bakedanuki" / "bakedanuki-util" / "python"

if str(PACKAGE_PYTHON_DIR) not in sys.path:
    sys.path.insert(0, str(PACKAGE_PYTHON_DIR))


def pytest_addoption(parser: pytest.Parser) -> None:
    """`bdControllerShape` 専用テストの実行範囲を選ぶ。"""
    group = parser.getgroup("controller shape")
    group.addoption(
        "--include-controller-shape",
        action="store_true",
        help="Include the bdControllerShape-specific tests in suite runs.",
    )
    group.addoption(
        "--exclude-controller-shape",
        action="store_true",
        help="Deselect bdControllerShape-specific tests, including explicit files.",
    )


def _validate_controller_shape_options(config: pytest.Config) -> None:
    if config.getoption("include_controller_shape") and config.getoption(
        "exclude_controller_shape"
    ):
        raise pytest.UsageError(
            "--include-controller-shape and --exclude-controller-shape "
            "cannot be used together"
        )


def _explicit_test_paths(config: pytest.Config) -> set[Path]:
    if config.args_source != pytest.Config.ArgsSource.ARGS:
        return set()
    result = set()
    for arg in config.args:
        path = (config.invocation_params.dir / arg.split("::", 1)[0]).resolve()
        if path.is_file():
            result.add(path)
    return result


@pytest.hookimpl(tryfirst=True)
def pytest_collection_modifyitems(
    config: pytest.Config, items: list[pytest.Item]
) -> None:
    """専用ファイルを分類し、通常実行では実行対象から除外する。"""
    for item in items:
        if (
            item.path.name.startswith(
                ("test_bd_controller_", "test_controller_shape_")
            )
            and item.path.suffix == ".py"
        ):
            item.add_marker("controller_shape")
    if config.getoption("include_controller_shape"):
        return

    explicit_paths = (
        set()
        if config.getoption("exclude_controller_shape")
        else _explicit_test_paths(config)
    )
    selected, deselected = [], []
    for item in items:
        if (
            item.get_closest_marker("controller_shape") is not None
            and item.path.resolve() not in explicit_paths
        ):
            deselected.append(item)
        else:
            selected.append(item)
    if deselected:
        items[:] = selected
        config.hook.pytest_deselected(items=deselected)


def pytest_configure(config: pytest.Config) -> None:
    """実行範囲を検証し、利用可能なMaya standaloneを初期化する。"""
    _validate_controller_shape_options(config)
    try:
        import maya.standalone
    except Exception:
        return

    try:
        maya.standalone.initialize(name="python")
    except Exception:
        pass
