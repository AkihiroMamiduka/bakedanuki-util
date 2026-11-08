"""ブラウザー起動APIの検証とOSへの委譲を確認する。"""

import webbrowser

import pytest

from bd_util.py import web
from bd_util.py.web import open_url


@pytest.mark.parametrize("result", [False, True])
@pytest.mark.parametrize(
    "url",
    [
        "http://example.test/",
        "https://example.test/docs/?q=1#part",
        "https://[2001:db8::1]:8443/help/",
        "https://例え.テスト/説明?q=日本語#節",
    ],
)
def test_open_url_passes_the_url_to_the_browser_and_returns_its_result(
    monkeypatch: pytest.MonkeyPatch, url: str, result: bool
) -> None:
    """URLと新規タブ指定をそのまま渡し、起動依頼の結果を返す。"""
    calls: list[tuple[str, int]] = []

    def fake_open(target: str, new: int = 0, autoraise: bool = True) -> bool:
        """実ブラウザーを開かず、起動引数を記録する。"""
        calls.append((target, new))
        return result

    monkeypatch.setattr(webbrowser, "open", fake_open)

    assert web.open_url(url) is result
    assert calls == [(url, 2)]


@pytest.mark.parametrize(
    "url",
    [
        "",
        "tools/tool/bd-channel-box/",
        "//example.test/",
        "file:///C:/help.html",
        "javascript:alert(1)",
        "https:///help/",
        "https://example.test:/",
        "https://[::1]invalid/",
        "https://[v1.example]/",
        "https://exa_mple.test/",
        "https://example.test/\n",
    ],
)
def test_open_url_rejects_invalid_urls_before_browser_delegation(
    monkeypatch: pytest.MonkeyPatch, url: str
) -> None:
    """HTTP/HTTPSの絶対URL以外ではブラウザーを起動しない。"""

    def fail_open(target: str, new: int = 0, autoraise: bool = True) -> bool:
        """不正なURLで起動を試みた場合だけテストを失敗させる。"""
        pytest.fail("不正なURLがブラウザーへ渡されました")

    monkeypatch.setattr(webbrowser, "open", fail_open)
    with pytest.raises(ValueError):
        open_url(url)


@pytest.mark.parametrize("error", [webbrowser.Error("browser"), OSError("os")])
def test_open_url_propagates_browser_errors(
    monkeypatch: pytest.MonkeyPatch, error: Exception
) -> None:
    """ブラウザー側の例外をFalseへ置き換えず呼び出し側へ伝える。"""

    def fail_open(target: str, new: int = 0, autoraise: bool = True) -> bool:
        """指定された起動エラーを再現する。"""
        raise error

    monkeypatch.setattr(webbrowser, "open", fail_open)
    with pytest.raises(type(error)) as caught:
        open_url("https://example.test/")
    assert caught.value is error
