"""同梱サイト情報の検証、URL生成、再読込の契約を確認する。"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Protocol, cast

import pytest

import bd_util as bdu
from bd_util import site


class _SiteAPI(Protocol):
    """別配置で読み込んだ公開サイトAPIの型境界を表す。"""

    SITE_BASE_URL: str

    def build_url(self, page_path: str) -> str:
        """検証済み基点へページパスを結合する。"""
        ...


def _load_site(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    content: bytes | None,
) -> _SiteAPI:
    """実装だけを別配置へ写し、同梱JSONを公開APIで検証する。"""
    source = Path(site.__file__).resolve()
    module_path = tmp_path / "site" / "__init__.py"
    module_path.parent.mkdir(exist_ok=True)
    module_path.write_bytes(source.read_bytes())
    if content is not None:
        (module_path.parent / "site.json").write_bytes(content)

    # util配下の別パッケージ名にして内部の相対importを維持する
    name = "bd_util._site_probe"
    spec = importlib.util.spec_from_file_location(
        name, module_path, submodule_search_locations=[str(module_path.parent)]
    )
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, name, module)
    spec.loader.exec_module(module)
    return cast(_SiteAPI, module)


def test_shipped_site_information_is_available() -> None:
    """実際の配布配置から確定した基点とトップページを取得できる。"""
    assert site.SITE_BASE_URL == "https://web.bakedanuki.workers.dev/"
    assert site.build_url("") == site.SITE_BASE_URL


@pytest.mark.parametrize(
    "base_url", ["https://example.test/", "https://example.test/docs/v1/"]
)
def test_site_uses_its_own_json_and_caches_validated_information(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, base_url: str
) -> None:
    """作業場所を変えても同梱JSONを読み、読込後の変更を再参照しない。"""
    monkeypatch.chdir(tmp_path)
    content = json.dumps({"schema_version": 1, "base_url": base_url})
    loaded = _load_site(tmp_path, monkeypatch, content.encode("utf-8"))
    (tmp_path / "site/site.json").write_text("{}", encoding="utf-8")

    assert loaded.SITE_BASE_URL == base_url
    assert loaded.build_url("") == base_url
    assert loaded.build_url("tools/tool/bd-channel-box/") == (
        base_url + "tools/tool/bd-channel-box/"
    )


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"{",
        b"[]",
        b"{}",
        b'\xef\xbb\xbf{"schema_version":1,"base_url":"https://example.test/"}',
        b"\xff",
        b'{"schema_version":true,"base_url":"https://example.test/"}',
        b'{"schema_version":1.0,"base_url":"https://example.test/"}',
        b'{"schema_version":2,"base_url":"https://example.test/"}',
        b'{"schema_version":1,"base_url":null}',
        b'{"schema_version":1,"base_url":NaN}',
        b'{"schema_version":1,"base_url":"https://example.test/","extra":0}',
        b'{"schema_version":1,"base_url":"https://example.test/",'
        b'"base_url":"https://other.test/"}',
    ],
)
def test_site_rejects_invalid_json_contract(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, content: bytes
) -> None:
    """不正な形式を補正せず、問題のファイルを明示して拒否する。"""
    with pytest.raises(ValueError, match="site\\.json"):
        _load_site(tmp_path, monkeypatch, content)


@pytest.mark.parametrize(
    "base_url",
    [
        "http://example.test/",
        "https:///",
        "https://example.test",
        "https://user:password@example.test/",
        "https://@example.test/",
        "https://example.test/?query=1",
        "https://example.test/#section",
        "https://example.test/?",
        "https://example.test/#",
        "https://example.test:/",
        "https://example.test:70000/",
        "https://[::1]invalid/",
        "https://example.test/docs//",
        "https://example.test/../",
        "https://example.test/Docs/",
        "https://example.test/%64ocs/",
        "https://example.test/with space/",
        "https://example.test/\n",
        "https://example.test/\x80",
    ],
)
def test_site_rejects_invalid_base_urls(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, base_url: str
) -> None:
    """絶対HTTPS基点、共通パス、末尾区切りの制約を保つ。"""
    content = json.dumps({"schema_version": 1, "base_url": base_url})
    with pytest.raises(ValueError, match="site\\.json"):
        _load_site(tmp_path, monkeypatch, content.encode("utf-8"))


@pytest.mark.parametrize(
    "page_path",
    [
        "/tools/",
        "//other.test/",
        "https://other.test/",
        "tools",
        "tools//tool/",
        "./tools/",
        "tools/../",
        "tools\\tool/",
        "tools/?query=1",
        "tools/#section",
        "tools/%2e%2e/",
        "Tools/",
        "tools/with space/",
        "tools/\n",
    ],
)
def test_build_url_rejects_paths_that_change_or_ambiguate_the_destination(
    page_path: str,
) -> None:
    """ホストや共通パスの置換につながる指定を暗黙に修正しない。"""
    with pytest.raises(ValueError):
        site.build_url(page_path)


def test_missing_site_json_reports_the_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """同梱ファイル欠落を代替URLで隠さず、対象を通知する。"""
    with pytest.raises(OSError, match="site\\.json"):
        _load_site(tmp_path, monkeypatch, None)


@pytest.mark.parametrize("first_module", ["bd_util.site", "bd_util.py.web"])
def test_regular_package_reload_refreshes_site_and_web_apis(
    tmp_path: Path,
    first_module: str,
) -> None:
    """両方のimport順で副作用がなく、正規reloadでAPIを更新できる。"""
    source = '''
import importlib
import json
import sys
import webbrowser
from pathlib import Path

import maya.standalone

maya.standalone.initialize(name="python")
sys.path.insert(0, sys.argv[1])
import bd_util as bdu

target = Path(bdu.__file__).resolve().parent / "site" / "site.json"
original_read = Path.read_text
original_open = webbrowser.open
base = ["https://first.test/docs/"]
reads = [0]
browser_calls: list[tuple[str, int]] = []

def read_site(
    path: Path, encoding: str | None = None, errors: str | None = None
) -> str:
    """サイトJSONだけを仮想化し、実ファイルを変更せず更新する。"""
    if path.resolve() == target:
        reads[0] += 1
        return json.dumps({"schema_version": 1, "base_url": base[0]})
    return original_read(path, encoding=encoding, errors=errors)

def open_browser(url: str, new: int = 0, autoraise: bool = True) -> bool:
    """ブラウザーへの起動依頼だけを記録し、実ブラウザーは開かない。"""
    browser_calls.append((url, new))
    return True

Path.read_text = read_site
webbrowser.open = open_browser
try:
    importlib.import_module(sys.argv[2])
    old_site = importlib.import_module("bd_util.site")
    old_web = importlib.import_module("bd_util.py.web")
    old_open_url = old_web.open_url
    assert old_site.SITE_BASE_URL == "https://first.test/docs/"
    assert browser_calls == []
    assert old_web.open_url(old_site.build_url("tools/")) is True
    base[0] = "https://second.test/docs/"
    assert old_site.build_url("tools/") == "https://first.test/docs/tools/"
    assert reads[0] == 1
    bdu.reload_package()
    new_site = importlib.import_module("bd_util.site")
    new_web = importlib.import_module("bd_util.py.web")
    assert new_site is not old_site
    assert new_web is not old_web
    assert new_web.open_url is not old_open_url
    assert new_site.SITE_BASE_URL == "https://second.test/docs/"
    assert new_site.build_url("tools/") == "https://second.test/docs/tools/"
    assert reads[0] == 2
    assert browser_calls == [("https://first.test/docs/tools/", 2)]
    assert new_web.open_url(new_site.build_url("tools/")) is True
    assert browser_calls == [
        ("https://first.test/docs/tools/", 2),
        ("https://second.test/docs/tools/", 2),
    ]
finally:
    Path.read_text = original_read
    webbrowser.open = original_open
'''
    python_root = str(Path(bdu.__file__).resolve().parent.parent)
    script_path = tmp_path / "reload_site.py"
    script_path.write_text(source, encoding="utf-8")
    result = subprocess.run(
        [sys.executable, "-B", str(script_path), python_root, first_module],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
    )
    assert result.returncode == 0, result.stdout + result.stderr
