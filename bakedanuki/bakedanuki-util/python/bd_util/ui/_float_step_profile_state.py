# coding: utf-8
"""FloatStepProfileをUiStateManagerへ接続する内部adapter。"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import ClassVar, cast

from . import qt
from ._ui_state_adapter import UiStateAdapter
from .binding.float.presentation import FloatUnitKind
from .float_step_profile import FloatStepProfile, FloatStepSetting


@dataclass(frozen=True)
class FloatStepProfileStateAdapter(UiStateAdapter):
    """複数識別子のStep設定を、一つのversion付き状態として保存する。"""

    state_type: ClassVar[str] = "float_step_profile"
    _VERSION: ClassVar[int] = 1
    profile: FloatStepProfile

    @property
    def state_object(self) -> qt.QObject:
        """状態を所有するProfileを返す。"""
        return self.profile

    def save_state(self) -> qt.QtCore.QByteArray | None:
        """設定項目を安定したJSONへ変換し、空の場合は保存対象外にする。"""
        entries = self.profile.entries
        if not entries:
            return None
        data = {
            "version": self._VERSION,
            "entries": [
                {
                    "key": entry.key,
                    "unit_kind": entry.unit_kind,
                    "single_step": entry.single_step,
                }
                for entry in entries
            ],
        }
        return qt.QtCore.QByteArray(
            json.dumps(
                data,
                ensure_ascii=False,
                allow_nan=False,
                separators=(",", ":"),
            ).encode("utf-8")
        )

    def restore_state(
        self, settings: qt.QtCore.QSettings, state_key: str
    ) -> bool:
        """形式全体を検証し、不正な個別項目だけを除いてProfileへ復元する。"""
        raw = settings.value(state_key)
        if not isinstance(raw, qt.QtCore.QByteArray):
            return False
        try:
            decoded: object = json.loads(raw.data())
            if not isinstance(decoded, dict):
                return False
            data = cast(dict[str, object], decoded)
            if (
                type(data.get("version")) is not int
                or data["version"] != self._VERSION
                or not isinstance(data.get("entries"), list)
            ):
                return False
            raw_entries = cast(list[object], data["entries"])
        except (TypeError, ValueError, UnicodeError):
            return False

        restored: list[FloatStepSetting] = []
        for raw_entry in raw_entries:
            if not isinstance(raw_entry, dict):
                continue
            entry = cast(dict[str, object], raw_entry)
            try:
                restored.append(
                    FloatStepSetting(
                        key=cast(str, entry.get("key")),
                        unit_kind=cast(FloatUnitKind, entry.get("unit_kind")),
                        single_step=cast(float, entry.get("single_step")),
                    )
                )
            except (TypeError, ValueError, OverflowError):
                continue
        self.profile.replace_entries(restored)
        return True
