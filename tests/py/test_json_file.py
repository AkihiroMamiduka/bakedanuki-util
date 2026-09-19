from __future__ import annotations

import json
from pathlib import Path

import pytest

import bd_util as bdu
from bd_util.py import json_file


@pytest.mark.parametrize(
    "data",
    [None, True, False, 42, -0.25, "歩き", [], {}, {"配列": [1, "値", None]}],
)
def test_roundtrip(tmp_path, data):
    path = tmp_path / "設定" / "ツール" / "data.json"
    assert bdu.json_file is json_file
    assert json_file.write(path, data) == path
    assert json_file.read(str(path)) == data
    assert not path.read_bytes().startswith(b"\xef\xbb\xbf")
    assert path.read_text(encoding="utf-8") == json.dumps(
        data, ensure_ascii=False, indent=2
    )
    assert list(path.parent.iterdir()) == [path]


def test_tuples_and_reused_containers(tmp_path):
    shared = {"名前": "歩き"}
    path = tmp_path / "data.json"
    json_file.write(path, {"items": (shared, shared)})
    assert json_file.read(path) == {"items": [shared, shared]}


def test_pathlike_relative_path_and_no_extension_added(tmp_path, monkeypatch):
    class SettingsPath:
        def __fspath__(self):
            return "settings/data"

    monkeypatch.chdir(tmp_path)
    path = json_file.write(SettingsPath(), {"value": 1})
    assert path == Path("settings/data")
    assert json_file.read(SettingsPath()) == {"value": 1}
    assert not path.with_suffix(".json").exists()


@pytest.mark.parametrize("indent", [None, 0, 4])
def test_indentation(tmp_path, indent):
    data = {"values": [1, 2]}
    path = json_file.write(tmp_path / "data.json", data, indent=indent)
    assert path.read_text(encoding="utf-8") == json.dumps(data, indent=indent)


def test_parent_creation_can_be_disabled(tmp_path):
    path = tmp_path / "missing" / "data.json"
    with pytest.raises(FileNotFoundError):
        json_file.write(path, {}, create_parents=False)
    assert not path.parent.exists()
    path.parent.mkdir()
    assert json_file.write(path, {}, create_parents=False) == path


def test_overwrite_and_exclusive_creation(tmp_path):
    path = tmp_path / "data.json"
    json_file.write(path, {"first": 1}, overwrite=False)
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        json_file.write(path, {"second": 2}, overwrite=False)
    assert path.read_bytes() == before
    assert list(tmp_path.iterdir()) == [path]
    json_file.write(path, {"second": 2})
    assert json_file.read(path) == {"second": 2}


def test_exclusive_creation_handles_concurrent_destination(
    tmp_path, monkeypatch
):
    path = tmp_path / "data.json"
    operation = "rename" if json_file.os.name == "nt" else "link"
    commit = getattr(json_file.os, operation)

    def concurrent_save(source, destination):
        path.write_text('{"other": 1}', encoding="utf-8")
        return commit(source, destination)

    monkeypatch.setattr(json_file.os, operation, concurrent_save)
    with pytest.raises(FileExistsError):
        json_file.write(path, {"own": 2}, overwrite=False)
    assert json_file.read(path) == {"other": 1}
    assert list(tmp_path.iterdir()) == [path]


@pytest.mark.parametrize(
    "data,error",
    [
        ({"nested": [float("nan")]}, ValueError),
        (float("inf"), ValueError),
        (float("-inf"), ValueError),
        ({1: "not a string key"}, TypeError),
        ({"a": {None: 1}}, TypeError),
        ({"a": object()}, TypeError),
        (b"bytes", TypeError),
        ({1, 2}, TypeError),
    ],
)
def test_invalid_data_does_not_touch_files_or_create_parents(
    tmp_path, data, error
):
    path = tmp_path / "data.json"
    path.write_bytes(b"original")
    for target in (path, tmp_path / "missing" / "data.json"):
        with pytest.raises(error):
            json_file.write(target, data)
    assert path.read_bytes() == b"original"
    assert list(tmp_path.iterdir()) == [path]


def test_circular_data_is_rejected(tmp_path):
    data = {"items": []}
    data["items"].append(data)
    with pytest.raises(ValueError, match="Circular"):
        json_file.write(tmp_path / "missing" / "data.json", data)
    assert not list(tmp_path.iterdir())


@pytest.mark.parametrize(
    "options,error",
    [
        ({"indent": True}, TypeError),
        ({"indent": "  "}, TypeError),
        ({"indent": 1.5}, TypeError),
        ({"indent": -1}, ValueError),
        ({"overwrite": 1}, TypeError),
        ({"create_parents": "yes"}, TypeError),
    ],
)
def test_invalid_options_have_no_file_effects(tmp_path, options, error):
    with pytest.raises(error):
        json_file.write(tmp_path / "missing" / "data.json", {}, **options)
    assert not list(tmp_path.iterdir())


def test_bom_input(tmp_path):
    path = tmp_path / "data.json"
    path.write_text('{"名前": "歩き"}', encoding="utf-8-sig")
    assert json_file.read(path) == {"名前": "歩き"}


@pytest.mark.parametrize(
    "text", ["NaN", "Infinity", "-Infinity", "1e999", "-1e999"]
)
def test_nonfinite_input_is_rejected(tmp_path, text):
    path = tmp_path / "data.json"
    path.write_text('{"value": [' + text + "]}", encoding="utf-8")
    with pytest.raises(ValueError, match="JSON number"):
        json_file.read(path)


@pytest.mark.parametrize("text", ["", "{", '{"a": 1,}', "{} {}"])
def test_invalid_json_raises_decode_error(tmp_path, text):
    path = tmp_path / "data.json"
    path.write_text(text, encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        json_file.read(path)


def test_read_missing_file_does_not_create_parents(tmp_path):
    with pytest.raises(FileNotFoundError):
        json_file.read(tmp_path / "missing" / "data.json")
    assert not list(tmp_path.iterdir())


def test_decode_and_encode_errors_are_not_swallowed(tmp_path):
    path = tmp_path / "data.json"
    path.write_bytes(b"\xff\xfe")
    with pytest.raises(UnicodeDecodeError):
        json_file.read(path)
    with pytest.raises(UnicodeEncodeError):
        json_file.write(path, {"text": "\ud800"})
    assert path.read_bytes() == b"\xff\xfe"
    assert list(tmp_path.iterdir()) == [path]


@pytest.mark.parametrize("stage", ["write", "close", "commit"])
@pytest.mark.parametrize("existing", [False, True])
def test_failed_save_preserves_destination_and_cleans_temporary(
    tmp_path, monkeypatch, stage, existing
):
    path = tmp_path / "data.json"
    if existing:
        path.write_bytes(b"original")

    def fail_commit(source, destination):
        raise PermissionError("simulated commit failure")

    if stage == "commit":
        monkeypatch.setattr(json_file.os, "replace", fail_commit)
    else:
        make_temporary = json_file.tempfile.NamedTemporaryFile

        class FailingStream:
            def __init__(self, **kwargs):
                self.stream = make_temporary(**kwargs)
                self.name = self.stream.name

            def __enter__(self):
                return self

            def write(self, text):
                self.stream.write(text[:2])
                if stage == "write":
                    raise OSError("simulated write failure")

            def __exit__(self, *args):
                self.stream.close()
                if stage == "close":
                    raise OSError("simulated close failure")

        monkeypatch.setattr(
            json_file.tempfile, "NamedTemporaryFile", FailingStream
        )

    with pytest.raises(OSError, match="simulated"):
        json_file.write(path, {"updated": 1})
    if existing:
        assert path.read_bytes() == b"original"
    else:
        assert not path.exists()
    assert list(tmp_path.iterdir()) == ([path] if existing else [])


def test_file_parent_and_directory_destination_are_errors(tmp_path):
    parent_file = tmp_path / "file"
    parent_file.write_bytes(b"original")
    with pytest.raises(OSError):
        json_file.write(parent_file / "data.json", {})
    directory = tmp_path / "directory"
    directory.mkdir()
    with pytest.raises(OSError):
        json_file.write(directory, {})
    assert parent_file.read_bytes() == b"original"
    assert directory.is_dir()
    assert set(tmp_path.iterdir()) == {parent_file, directory}
