"""旧コントローラー専用テストの既定除外と明示実行を確認する。"""

from pathlib import Path

import pytest

pytest_plugins = ["pytester"]


@pytest.fixture
def selection_suite(pytester: pytest.Pytester) -> pytest.Pytester:
    """選択hookだけを読み込み、Maya初期化なしで収集条件を検証する。"""
    conftest_path = Path(__file__).resolve().parents[1] / "conftest.py"
    pytester.makeconftest(f"""
import importlib.util

spec = importlib.util.spec_from_file_location("selection_conftest", {str(conftest_path)!r})
selection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(selection)
pytest_addoption = selection.pytest_addoption
pytest_collection_modifyitems = selection.pytest_collection_modifyitems
pytest_configure = selection._validate_controller_shape_options
""")
    pytester.makeini(
        "[pytest]\n"
        "markers =\n"
        "    controller_shape: optional controller shape tests\n"
    )
    pytester.makepyfile(test_bd_controller_probe="""
def test_controller(request):
    assert request.node.get_closest_marker("controller_shape") is not None
""")
    mixed = pytester.path / "mixed"
    mixed.mkdir()
    (mixed / "test_controller_shape_probe.py").write_text(
        "def test_controller(request):\n"
        '    assert request.node.get_closest_marker("controller_shape") is not None\n',
        encoding="utf-8",
    )
    (mixed / "test_native_metadata.py").write_text(
        "def test_general(request):\n"
        '    assert request.node.get_closest_marker("controller_shape") is None\n',
        encoding="utf-8",
    )
    return pytester


@pytest.mark.parametrize("args", [(), (".",), ("--exclude-controller-shape",)])
def test_default_suite_deselects_controller_files(
    selection_suite: pytest.Pytester, args: tuple[str, ...]
) -> None:
    """既定の全件・directory実行は専用テストをskipせず除外する。"""
    result = selection_suite.runpytest_inprocess(*args, "-q")
    result.assert_outcomes(passed=1, deselected=2)


def test_include_option_runs_all_controller_files(
    selection_suite: pytest.Pytester,
) -> None:
    """明示includeでは通常テストと専用テストを実行する。"""
    result = selection_suite.runpytest_inprocess(
        "--include-controller-shape", "-q"
    )
    result.assert_outcomes(passed=3)


@pytest.mark.parametrize(
    "target",
    [
        "test_bd_controller_probe.py",
        "test_bd_controller_probe.py::test_controller",
    ],
)
def test_explicit_controller_file_runs_without_option(
    selection_suite: pytest.Pytester, target: str
) -> None:
    """専用ファイルとnodeidの明示指定はそのテストを実行する。"""
    result = selection_suite.runpytest_inprocess(target, "-q")
    result.assert_outcomes(passed=1)


def test_explicit_file_does_not_include_controller_files_from_directory(
    selection_suite: pytest.Pytester,
) -> None:
    """明示ファイルの併記はdirectory配下の別専用テストを有効にしない。"""
    result = selection_suite.runpytest_inprocess(
        "mixed", "test_bd_controller_probe.py", "-q"
    )
    result.assert_outcomes(passed=2, deselected=1)


def test_explicit_exclude_overrides_explicit_file(
    selection_suite: pytest.Pytester,
) -> None:
    """suite wrapperの明示excludeはファイル指定より優先する。"""
    result = selection_suite.runpytest_inprocess(
        "--exclude-controller-shape", "test_bd_controller_probe.py", "-q"
    )
    result.assert_outcomes(deselected=1)
    assert result.ret == pytest.ExitCode.NO_TESTS_COLLECTED


def test_controller_marker_is_available_to_marker_selection(
    selection_suite: pytest.Pytester,
) -> None:
    """分類markerはpytest標準のmarker選択より前に付与する。"""
    result = selection_suite.runpytest_inprocess(
        "--include-controller-shape", "-m", "controller_shape", "-q"
    )
    result.assert_outcomes(passed=2, deselected=1)


def test_include_and_exclude_options_are_mutually_exclusive(
    selection_suite: pytest.Pytester,
) -> None:
    """相反する実行指定は利用者へエラーとして報告する。"""
    result = selection_suite.runpytest_inprocess(
        "--include-controller-shape", "--exclude-controller-shape", "-q"
    )
    assert result.ret == pytest.ExitCode.USAGE_ERROR
    result.stderr.fnmatch_lines(["*cannot be used together*"])
