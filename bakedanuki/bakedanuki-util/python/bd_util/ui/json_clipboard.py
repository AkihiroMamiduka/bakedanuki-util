# coding: utf-8
"""型固有のschemaから独立した、JSON用OSクリップボード。"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import cast

from . import qt

__all__ = ["JsonClipboard"]


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    """重複keyによる解釈の差を拒否してJSON objectを返す。"""
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"JSONのkeyが重複しています: {key}")
        result[key] = value
    return result


def _reject_constant(value: str) -> object:
    """JSON標準外のNaNとInfinityを拒否する。"""
    raise ValueError(f"JSONに有限でない数値は使用できません: {value}")


@dataclass(frozen=True)
class JsonClipboard:
    """UTF-8 JSONをcustom MIMEとmarker付きtextへ同時に保存する。

    Attributes:
        mime_type: `application/`で始まる固有のMIME type。
        text_marker: 改行で終わる固有のtext/plain識別子。
        max_bytes: JSON本文の最大UTF-8 byte数。
    """

    mime_type: str
    text_marker: str
    max_bytes: int = 1024 * 1024

    def __post_init__(self) -> None:
        """他形式との誤認を避ける識別子と容量上限を検証する。"""
        if not isinstance(self.mime_type, str):
            raise TypeError("mime_typeにはstrを指定してください")
        if not self.mime_type.startswith("application/"):
            raise ValueError("mime_typeにはapplication形式を指定してください")
        if not isinstance(self.text_marker, str):
            raise TypeError("text_markerにはstrを指定してください")
        if not self.text_marker or not self.text_marker.endswith("\n"):
            raise ValueError("text_markerは改行で終わる識別子にしてください")
        if not isinstance(self.max_bytes, int) or isinstance(
            self.max_bytes, bool
        ):
            raise TypeError("max_bytesにはintを指定してください")
        if self.max_bytes <= 0:
            raise ValueError("max_bytesは1以上にしてください")

    @staticmethod
    def _clipboard() -> qt.QtGui.QClipboard:
        """現在のGUI applicationが所有するグローバルclipboardを返す。"""
        application = qt.QApplication.instance()
        if not isinstance(application, qt.QApplication):
            raise RuntimeError("OSクリップボードにはQApplicationが必要です")
        return application.clipboard()

    def contains(self) -> bool:
        """対応MIMEまたは専用markerがある場合は`True`。

        Raises:
            RuntimeError: QApplicationが存在しない場合。
        """
        mime_data = self._clipboard().mimeData()
        if mime_data is None:
            return False
        return mime_data.hasFormat(self.mime_type) or (
            mime_data.hasText()
            and mime_data.text().startswith(self.text_marker)
        )

    def write(self, document: object) -> None:
        """JSON化できる値を二つの形式でOSへ保存する。

        Args:
            document: JSONへ変換する値。

        Raises:
            ValueError: JSONへ変換できないか、容量上限を超える場合。
            RuntimeError: QApplicationが存在しない場合。
        """
        try:
            text = json.dumps(
                document,
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
            )
        except (TypeError, ValueError) as error:
            raise ValueError("documentをJSONへ変換できません") from error
        encoded = text.encode("utf-8")
        self._require_size(encoded)
        mime_data = qt.QtCore.QMimeData()
        mime_data.setData(self.mime_type, qt.QByteArray(encoded))
        mime_data.setText(self.text_marker + text)
        self._clipboard().setMimeData(mime_data)

    def read(self) -> object:
        """識別済みJSONを外部入力として検証し、読み込む。

        Returns:
            JSONから復元したPython値。利用側でschema検証する。

        Raises:
            ValueError: 対応形式がないか、容量・UTF-8・JSONが不正な場合。
            RuntimeError: QApplicationが存在しない場合。
        """
        mime_data = self._clipboard().mimeData()
        if mime_data is None:
            raise ValueError("OSクリップボードにデータがありません")
        if mime_data.hasFormat(self.mime_type):
            encoded = bytes(mime_data.data(self.mime_type))
        elif mime_data.hasText() and mime_data.text().startswith(
            self.text_marker
        ):
            encoded = mime_data.text()[len(self.text_marker) :].encode("utf-8")
        else:
            raise ValueError("対応するJSONデータがありません")
        self._require_size(encoded)
        try:
            text = encoded.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError("clipboardデータはUTF-8ではありません") from error
        try:
            return cast(
                object,
                json.loads(
                    text,
                    object_pairs_hook=_unique_object,
                    parse_constant=_reject_constant,
                ),
            )
        except (json.JSONDecodeError, ValueError, RecursionError) as error:
            raise ValueError("clipboardのJSONを解析できません") from error

    def _require_size(self, encoded: bytes) -> None:
        """解析前にbyte数を制限して過大な外部入力を拒否する。"""
        if len(encoded) > self.max_bytes:
            raise ValueError(
                f"clipboardデータは{self.max_bytes} bytes以下にしてください"
            )
