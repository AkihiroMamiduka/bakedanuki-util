# coding: utf-8
"""属性などの識別子ごとに、浮動小数点のStep設定を保持する。"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from . import qt
from .binding.float.presentation import FloatUnitKind, require_unit_kind
from .binding.float.view.step_spin_box import require_step

__all__ = ["FloatStepProfile", "FloatStepSetting"]


def _require_key(value: object) -> str:
    """空でない文字列をStep設定の識別子として検証する。"""
    if not isinstance(value, str):
        raise TypeError("keyにはstrを指定してください")
    if not value:
        raise ValueError("keyには空でない文字列を指定してください")
    return value


@dataclass(frozen=True)
class FloatStepSetting:
    """識別子と単位種別に対応するstep設定。

    Attributes:
        key: 空でない設定識別子。
        unit_kind: 公開値の単位種別。
        single_step: 表示単位での正の刻み幅。
    """

    key: str
    unit_kind: FloatUnitKind
    single_step: float

    def __post_init__(self) -> None:
        """公開境界で識別子・単位種別・Step値を正規化する。"""
        object.__setattr__(self, "key", _require_key(self.key))
        object.__setattr__(
            self, "unit_kind", require_unit_kind(self.unit_kind)
        )
        object.__setattr__(
            self,
            "single_step",
            require_step(self.single_step, "single_step"),
        )


class FloatStepProfile(qt.QObject):
    """複数のstep設定を保持し、実変更時だけ通知する。

    Attributes:
        changed: 設定が変わると一度だけ通知するsignal。
    """

    changed = qt.Signal()

    def __init__(self, parent: qt.QObject | None = None) -> None:
        """空のStep設定を、任意のQt ownerへ結び付けて作成する。"""
        super().__init__(parent)
        self._steps: dict[tuple[str, FloatUnitKind], float] = {}

    @property
    def entries(self) -> tuple[FloatStepSetting, ...]:
        """識別子と単位種別で安定して並べた現在の設定を返す。"""
        return tuple(
            FloatStepSetting(key, unit_kind, single_step)
            for (key, unit_kind), single_step in sorted(self._steps.items())
        )

    def single_step(self, key: str, unit_kind: FloatUnitKind) -> float | None:
        """指定したstep設定を返す。

        Args:
            key: 設定識別子。
            unit_kind: 公開値の単位種別。

        Returns:
            表示単位の刻み幅。未登録なら`None`。
        """
        identity = (_require_key(key), require_unit_kind(unit_kind))
        return self._steps.get(identity)

    def set_single_step(
        self,
        key: str,
        unit_kind: FloatUnitKind,
        single_step: float,
    ) -> bool:
        """一つのstepを設定し、実変更時だけ通知する。

        Args:
            key: 設定識別子。
            unit_kind: 公開値の単位種別。
            single_step: 表示単位での正の刻み幅。

        Returns:
            設定が変わった場合は`True`。
        """
        setting = FloatStepSetting(key, unit_kind, single_step)
        updated = dict(self._steps)
        updated[(setting.key, setting.unit_kind)] = setting.single_step
        return self._replace_steps(updated)

    def replace_entries(self, entries: Iterable[FloatStepSetting]) -> bool:
        """全設定を置き換え、実変更時だけ通知する。

        Args:
            entries: 新しい設定。識別子と単位種別が重なる場合は後の項目が優先。

        Returns:
            設定が変わった場合は`True`。

        Raises:
            TypeError: FloatStepSetting以外を含む場合。
        """
        updated: dict[tuple[str, FloatUnitKind], float] = {}
        for entry in entries:
            candidate: object = entry
            if not isinstance(candidate, FloatStepSetting):
                raise TypeError(
                    "entriesにはFloatStepSettingを指定してください"
                )
            updated[(candidate.key, candidate.unit_kind)] = (
                candidate.single_step
            )
        return self._replace_steps(updated)

    def remove(self, key: str, unit_kind: FloatUnitKind) -> bool:
        """一つのstep設定を削除する。

        Args:
            key: 設定識別子。
            unit_kind: 公開値の単位種別。

        Returns:
            設定を削除した場合は`True`。
        """
        identity = (_require_key(key), require_unit_kind(unit_kind))
        if identity not in self._steps:
            return False
        updated = dict(self._steps)
        del updated[identity]
        return self._replace_steps(updated)

    def clear(self) -> bool:
        """全設定を削除し、内容があった場合だけ通知して`True`を返す。"""
        return self._replace_steps({})

    def _replace_steps(
        self, steps: dict[tuple[str, FloatUnitKind], float]
    ) -> bool:
        """検証済みの内部状態へ置き換え、実変更を通知する。"""
        if steps == self._steps:
            return False
        self._steps = steps
        self.changed.emit()
        return True
