"""基準ファイルからの相対パス解決を検証する。"""

from pathlib import Path

import pytest

from bd_util.py.path import resolve_relative_path


@pytest.mark.parametrize("as_string", [False, True])
@pytest.mark.parametrize("relative_path", ["メニュー.png", "sub/data.json"])
def test_resolve_relative_path_uses_base_file_after_directory_change(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    as_string: bool,
    relative_path: str,
) -> None:
    """作業フォルダが変わっても基準ファイル配下のリソースを参照する。"""
    base_file = tmp_path / "ツール" / "resources" / "__init__.py"
    resource_file = base_file.parent / relative_path
    resource_file.parent.mkdir(parents=True)
    resource_file.write_bytes(b"resource")
    other_directory = tmp_path / "other"
    other_directory.mkdir()
    monkeypatch.chdir(other_directory)

    source = str(base_file) if as_string else base_file
    result = resolve_relative_path(
        base_file=source, relative_path=relative_path
    )
    assert result.read_bytes() == b"resource"


def test_resolve_relative_path_does_not_create_missing_resources(
    tmp_path: Path,
) -> None:
    """対象がなくてもパスだけ返し、フォルダやファイルを作成しない。"""
    base_file = tmp_path / "missing" / "resources" / "__init__.py"

    result = resolve_relative_path(base_file, "sub/missing.json")

    assert result.is_absolute()
    assert result == tmp_path / "missing/resources/sub/missing.json"
    assert not base_file.parent.exists()
