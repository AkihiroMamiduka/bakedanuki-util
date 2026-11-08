"""HTTPとHTTPSのURLを既定ブラウザーへ渡す実装。"""

from __future__ import annotations

import webbrowser

from ._url import split_http_url

__all__ = ["open_url"]


def open_url(url: str) -> bool:
    """Web URLをブラウザーへ渡し、起動依頼の成否を返す。

    ページの存在やHTTP応答は確認しません。新しいタブ等の最終的な
    表示方法は、OSとブラウザーの設定に従います。

    Args:
        url: ホストを持つHTTPまたはHTTPSの絶対URL。

    Returns:
        ブラウザーへの起動依頼が成功した場合は `True`。

    Raises:
        ValueError: `url` がWeb URLの形式を満たさない場合。
        webbrowser.Error: ブラウザー制御に失敗した場合。
        OSError: OSでのブラウザー起動に失敗した場合。
    """
    # 起動前に検証し、成否と例外を呼び出し側へそのまま返す
    split_http_url(url)
    return webbrowser.open(url, new=2)
