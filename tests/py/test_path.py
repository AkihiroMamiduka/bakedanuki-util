"""同梱アイコンのパス解決を検証する。"""

from pathlib import Path

import pytest

from bd_util.py.path import icon_path


@pytest.mark.parametrize("as_string", [False, True])
def test_icon_path_uses_module_location_after_working_directory_change(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, as_string: bool
) -> None:
    """作業フォルダが変わっても基準ファイルの隣の画像を参照する。"""
    module_file = tmp_path / "ツール" / "icon" / "__init__.py"
    module_file.parent.mkdir(parents=True)
    image_file = module_file.with_name("メニュー.png")
    image_file.write_bytes(b"resource")
    other_directory = tmp_path / "other"
    other_directory.mkdir()
    monkeypatch.chdir(other_directory)

    source = str(module_file) if as_string else module_file
    assert icon_path(source, "メニュー.png").read_bytes() == b"resource"


def test_icon_path_keeps_missing_images_for_consumer_validation(
    tmp_path: Path,
) -> None:
    """欠けた画像もパスだけ返し、フォルダやファイルを作成しない。"""
    module_file = tmp_path / "missing" / "icon" / "__init__.py"

    result = icon_path(module_file, "missing.png")

    assert result.is_absolute()
    assert result == module_file.with_name("missing.png")
    assert not module_file.parent.exists()
