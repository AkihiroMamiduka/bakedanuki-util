"""同梱JSONを正本とするbakedanukiの公開サイト情報。"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Final, NoReturn, cast

from ..py.web._url import split_http_url

__all__ = ["SITE_BASE_URL", "build_url"]

_PAGE_PATH = re.compile(r"(?:[a-z0-9]+(?:-[a-z0-9]+)*/)+")


def _validate_page_path(page_path: object) -> None:
    """サイト基点からの相対パスまたはトップを表す空文字列を検証する。"""
    if not isinstance(page_path, str):
        raise ValueError("page_pathには文字列を指定してください")
    if page_path and _PAGE_PATH.fullmatch(page_path) is None:
        raise ValueError(
            "page_pathは小文字の英数字・ハイフンの階層と末尾の/で"
            "指定してください。先頭の/や空の階層は使えません"
        )


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """JSONオブジェクトの重複キーを拒否する。"""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"JSONのキーが重複しています: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> NoReturn:
    """JSONで定義されていない数値定数を拒否する。"""
    raise ValueError(f"JSONで使用できない定数です: {value}")


def _load_base_url() -> str:
    """同梱JSONの形式と基点URLを検証し、読み込んだ値を返す。"""
    data_path = Path(__file__).with_name("site.json")

    # 同梱ファイルを一度読み、読込失敗には対象ファイルを付ける
    try:
        text = data_path.read_text(encoding="utf-8")
    except OSError as error:
        raise OSError(
            f"サイト情報を読み込めません: {data_path}: {error}"
        ) from error
    except UnicodeError as error:
        raise ValueError(
            f"{data_path}: UTF-8のサイト情報を読み込めません: {error}"
        ) from error

    # JSONのキーと型を固定し、補正や仮URLへの代替を行わない
    try:
        payload = cast(
            object,
            json.loads(
                text,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_constant,
            ),
        )
        if not isinstance(payload, dict):
            raise ValueError("ルートにはJSONオブジェクトが必要です")
        data = cast(dict[str, object], payload)
        if set(data) != {"schema_version", "base_url"}:
            raise ValueError(
                "フィールドはschema_versionとbase_urlのみ指定してください"
            )
        schema_version = data["schema_version"]
        if type(schema_version) is not int or schema_version != 1:
            raise ValueError("schema_versionは整数の1で指定してください")
        base_url = data["base_url"]
        if not isinstance(base_url, str):
            raise ValueError("base_urlには文字列を指定してください")

        # 基点の共通パスを検証し、引数のパス結合で逸脱しない形にする
        parts = split_http_url(base_url)
        if (
            parts.scheme != "https"
            or parts.username is not None
            or parts.password is not None
            or "?" in base_url
            or "#" in base_url
            or not base_url.endswith("/")
        ):
            raise ValueError(
                "base_urlはユーザー情報・クエリ・フラグメントを含まない、"
                "末尾が/のHTTPS URLで指定してください"
            )
        _validate_page_path(parts.path[1:])
        return base_url
    except (ValueError, UnicodeError) as error:
        raise ValueError(f"{data_path}: {error}") from error


# JSONを正本とし、初回のモジュール読込時に検証した値だけを保持する
SITE_BASE_URL: Final[str] = _load_base_url()


def build_url(page_path: str) -> str:
    """サイト基点の共通パスを保って、ページの完成URLを返す。

    JSONの再読み込みや、ページの存在を調べる通信は行いません。

    Args:
        page_path: 先頭に `/` がなく、末尾が `/` の相対ページパス。
            小文字の英数字・ハイフンからなる階層を指定します。
            空文字列はサイトのトップページを表します。

    Returns:
        同梱JSONから読み込み済みの基点URLと結合した完成URL。

    Raises:
        ValueError: `page_path` が相対ページパスの形式を満たさない場合。
    """
    # 検証済みの基点へ相対パスを連結し、ホストや共通パスを変更させない
    _validate_page_path(page_path)
    return SITE_BASE_URL + page_path
