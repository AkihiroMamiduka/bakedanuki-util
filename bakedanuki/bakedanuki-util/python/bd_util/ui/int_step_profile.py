# coding: utf-8
"""用途側の識別子ごとに整数Stepを保持する。"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from typing import cast

from . import qt
from .binding.int._validation import require_step

__all__ = ["IntStepProfile", "IntStepSetting"]


def _require_key(value: object) -> str:
    """空でないStep設定の識別子を検証する。"""
    if not isinstance(value, str):
        raise TypeError("keyにはstrを指定してください")
    if not value:
        raise ValueError("keyには空でないstrを指定してください")
    return value


@dataclass(frozen=True)
class IntStepSetting:
    """識別子と正の整数刻み幅の設定。"""

    key: str
    single_step: int

    def __post_init__(self) -> None:
        """識別子と整数範囲を公開境界で検証する。"""
        object.__setattr__(self, "key", _require_key(self.key))
        object.__setattr__(self, "single_step", require_step(self.single_step))


class IntStepProfile(qt.QObject):
    """識別子ごとの整数Stepを保持し、実変更時だけ通知する。"""

    changed = qt.Signal()

    def __init__(self, parent: qt.QObject | None = None) -> None:
        """空のProfileを指定のQt所有者へ接続する。"""
        super().__init__(parent)
        self._steps: dict[str, int] = {}

    @property
    def entries(self) -> tuple[IntStepSetting, ...]:
        """現在の設定を識別子順の不変な列として返す。"""
        return tuple(
            IntStepSetting(key, step)
            for key, step in sorted(self._steps.items())
        )

    def single_step(self, key: str) -> int | None:
        """保存したStepを返す。未登録なら`None`。"""
        return self._steps.get(_require_key(key))

    def set_single_step(self, key: str, single_step: int) -> bool:
        """一つの設定を検証後に更新し、実変更時に`True`を返す。"""
        setting = IntStepSetting(key, single_step)
        updated = dict(self._steps)
        updated[setting.key] = setting.single_step
        return self._replace_steps(updated)

    def replace_entries(self, entries: Iterable[IntStepSetting]) -> bool:
        """全項目を検証後に置き換える。同じ識別子は後勝ち。"""
        updated: dict[str, int] = {}
        for entry in entries:
            candidate = cast(object, entry)
            if not isinstance(candidate, IntStepSetting):
                raise TypeError("entriesにはIntStepSettingを指定してください")
            updated[candidate.key] = candidate.single_step
        return self._replace_steps(updated)

    def remove(self, key: str) -> bool:
        """指定の保存値があれば削除し、実変更時に`True`を返す。"""
        key = _require_key(key)
        if key not in self._steps:
            return False
        updated = dict(self._steps)
        del updated[key]
        return self._replace_steps(updated)

    def clear(self) -> bool:
        """全保存値を削除し、実変更時に`True`を返す。"""
        return self._replace_steps({})

    def _replace_steps(self, steps: dict[str, int]) -> bool:
        """検証済みの内容へ置き換え、変化がある場合だけ通知する。"""
        if steps == self._steps:
            return False
        self._steps = steps
        self.changed.emit()
        return True
