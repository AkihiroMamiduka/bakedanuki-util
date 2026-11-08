"""Web関連APIで共有するURL構造の検証。"""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import SplitResult, urlsplit

_HOST_LABEL = re.compile(r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?")


def _validate_hostname(hostname: str) -> None:
    """DNS名またはIPv6アドレスとしてホスト部分を検証する。"""
    # IPv6は標準ライブラリに構文の検証を任せる
    if ":" in hostname:
        ipaddress.IPv6Address(hostname)
        return

    # 国際化ドメインは検証時だけASCIIへ変換し、元のURLを保持する
    ascii_hostname = hostname.encode("idna").decode("ascii")
    domain = ascii_hostname.removesuffix(".")
    labels = domain.split(".")
    if len(domain) > 253 or any(
        _HOST_LABEL.fullmatch(label) is None for label in labels
    ):
        raise ValueError("ホスト名の形式が不正です")


def split_http_url(url: object) -> SplitResult:
    """HTTPまたはHTTPSの絶対URLを検証して分解する。"""
    # URL解析前の文字列を調べ、解析時に除去される制御文字も拒否する
    if not isinstance(url, str) or not url:
        raise ValueError("Web URLには空でない文字列を指定してください")
    if "\\" in url or any(
        character.isspace()
        or ord(character) < 32
        or 127 <= ord(character) <= 159
        for character in url
    ):
        raise ValueError(
            "Web URLに空白・制御文字・バックスラッシュは使えません"
        )

    # ホストとポートも評価し、不正なauthorityをブラウザーへ渡さない
    try:
        parts = urlsplit(url)
        hostname = parts.hostname
        _ = parts.port
        if parts.scheme not in ("http", "https") or hostname is None:
            raise ValueError("HTTPまたはHTTPSのホスト付き絶対URLが必要です")
        if parts.netloc.endswith(":"):
            raise ValueError("ポート番号が空です")
        authority = parts.netloc.rsplit("@", 1)[-1]
        if authority.startswith("["):
            ipaddress.IPv6Address(hostname)
            suffix = authority[authority.index("]") + 1 :]
            if suffix and not suffix.startswith(":"):
                raise ValueError("IPv6の閉じ括弧の後ろが不正です")
        _validate_hostname(hostname)
    except (ValueError, UnicodeError) as error:
        raise ValueError(f"Web URLの形式が不正です: {error}") from error
    return parts
