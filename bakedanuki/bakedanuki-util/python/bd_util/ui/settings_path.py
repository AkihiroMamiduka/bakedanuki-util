# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Self

_INVALID_CHARACTERS = frozenset('<>:"\\|?*')
_WINDOWS_RESERVED_NAMES = frozenset(
    {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        *(f"COM{index}" for index in range(1, 10)),
        *(f"LPT{index}" for index in range(1, 10)),
    }
)


def _require_string(value: object) -> str:
    """runtime値が文字列であることを検証する。"""
    # 静的型検査を迂回した呼び出しでも明確なTypeErrorを送出する。
    if not isinstance(value, str):
        raise TypeError("settings pathには文字列を指定してください")
    return value


def _validate_segment(segment: str) -> None:
    """settings pathを構成する1つのsegmentを検証する。"""
    # 空文字、相対移動、前後の空白を含む曖昧なsegmentを拒否する。
    if not segment or segment in {".", ".."} or segment != segment.strip():
        raise ValueError(f"無効なsettings path segmentです: {segment!r}")

    # filesystemやQSettings keyで問題になる文字と制御文字を拒否する。
    if any(character in _INVALID_CHARACTERS for character in segment) or any(
        ord(character) < 32 for character in segment
    ):
        raise ValueError(f"無効なsettings path segmentです: {segment!r}")

    # Windowsでdirectory名に使用できない末尾と予約名を拒否する。
    if segment.endswith((" ", ".")):
        raise ValueError(f"無効なsettings path segmentです: {segment!r}")
    base_name = segment.split(".", maxsplit=1)[0].upper()
    if base_name in _WINDOWS_RESERVED_NAMES:
        raise ValueError(f"Windows予約名は使用できません: {segment!r}")


@dataclass(frozen=True, slots=True, init=False)
class SettingsPath:
    """toolとINI内groupを表す安全な相対settings path。"""

    segments: tuple[str, ...]

    def __init__(self, value: str) -> None:
        """`/`区切りの文字列を検証して初期化する。"""
        # 文字列以外とWindows separatorを含むpathを明示的に拒否する。
        runtime_value = _require_string(value)
        if "\\" in runtime_value:
            raise ValueError("settings pathの区切りには'/'を使用してください")

        # tool名と1つ以上のgroupを必須として各segmentを検証する。
        segments = tuple(runtime_value.split("/"))
        if len(segments) < 2:
            raise ValueError(
                "settings pathにはtool名とgroupを指定してください"
            )
        for segment in segments:
            _validate_segment(segment)

        # 検証済みのsegmentだけをimmutableな状態として保持する。
        object.__setattr__(self, "segments", segments)

    @classmethod
    def from_value(cls, value: str | Self) -> Self:
        """文字列または既存instanceからSettingsPathを取得する。"""
        # 文字列だけを新規生成し、検証済みinstanceはそのまま再利用する。
        if isinstance(value, str):
            return cls(value)
        return value

    @property
    def tool_name(self) -> str:
        """物理directory名に使用するtool名を返す。"""
        # settings pathの先頭segmentをtool単位の識別子として使用する。
        return self.segments[0]

    @property
    def group_path(self) -> str:
        """toolのINI内で使用するgroup pathを返す。"""
        # tool名を除いた残りのsegmentをQSettings形式へ戻す。
        return "/".join(self.segments[1:])

    def __str__(self) -> str:
        """正規化済みのsettings pathを文字列として返す。"""
        # 保持しているsegmentをplatform非依存のseparatorで結合する。
        return "/".join(self.segments)
