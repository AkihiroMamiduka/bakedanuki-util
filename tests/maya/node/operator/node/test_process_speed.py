# coding: utf-8
from __future__ import annotations

from types import SimpleNamespace

import pytest

import bd_util._test.maya.node.operator.node.process_speed as process_speed

pytestmark = pytest.mark.maya


def test_pymel_benchmarks_available_with_versioned_caches(
    monkeypatch,
    tmp_path,
):
    pymel_dir = tmp_path / "pymel"
    cache_dir = pymel_dir / "cache"
    cache_dir.mkdir(parents=True)
    init_path = pymel_dir / "__init__.py"
    init_path.touch()

    for cache_name in process_speed._PYMEL_VERSIONED_CACHE_NAMES:
        (cache_dir / f"{cache_name}2026.py").touch()

    spec = SimpleNamespace(origin=str(init_path))
    monkeypatch.setattr(
        process_speed.importlib.util, "find_spec", lambda _: spec
    )
    monkeypatch.setattr(process_speed, "_current_maya_version", lambda: "2026")

    assert process_speed._pymel_benchmarks_available()


def test_pymel_benchmarks_unavailable_with_missing_cache(
    monkeypatch,
    tmp_path,
):
    pymel_dir = tmp_path / "pymel"
    cache_dir = pymel_dir / "cache"
    cache_dir.mkdir(parents=True)
    init_path = pymel_dir / "__init__.py"
    init_path.touch()

    (cache_dir / "mayaApi2026.py").touch()

    spec = SimpleNamespace(origin=str(init_path))
    monkeypatch.setattr(
        process_speed.importlib.util, "find_spec", lambda _: spec
    )
    monkeypatch.setattr(process_speed, "_current_maya_version", lambda: "2026")

    assert not process_speed._pymel_benchmarks_available()


def test_run_benchmarks_skips_only_pymel_when_unavailable(monkeypatch):
    executed = []

    def benchmark_cmds():
        executed.append("cmds")

    def benchmark_pm():
        executed.append("pymel")

    def benchmark_om():
        executed.append("open_maya")

    monkeypatch.setattr(
        process_speed,
        "_pymel_benchmarks_available",
        lambda: False,
    )

    process_speed._run_benchmarks(
        (benchmark_cmds, benchmark_pm, benchmark_om),
        accurate=False,
        repeat_count=3,
    )

    assert executed == ["cmds", "open_maya"]


def test_run_benchmarks_includes_pymel_when_available(monkeypatch):
    executed = []

    def benchmark_cmds():
        executed.append("cmds")

    def benchmark_pm():
        executed.append("pymel")

    monkeypatch.setattr(
        process_speed,
        "_pymel_benchmarks_available",
        lambda: True,
    )

    process_speed._run_benchmarks(
        (benchmark_cmds, benchmark_pm),
        accurate=False,
        repeat_count=3,
    )

    assert executed == ["cmds", "pymel"]
