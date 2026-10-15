# coding: utf-8
"""整数Step設定をUiStateManagerへ接続する内部adapter。"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import ClassVar, cast

from . import qt
from ._ui_state_adapter import UiStateAdapter
from .int_step_profile import IntStepProfile, IntStepSetting


@dataclass(frozen=True)
class IntStepProfileStateAdapter(UiStateAdapter):
    """整数Stepを独立した型・version付き状態として保存する。"""

    state_type: ClassVar[str] = "int_step_profile"
    _VERSION: ClassVar[int] = 1
    profile: IntStepProfile

    @property
    def state_object(self) -> qt.QObject:
        """保存状態を所有するProfileを返す。"""
        return self.profile

    def save_state(self) -> qt.QtCore.QByteArray | None:
        """設定を整数のJSONへ変換し、空なら保存対象から除く。"""
        if not self.profile.entries:
            return None
        data = {
            "version": self._VERSION,
            "entries": [
                {"key": entry.key, "single_step": entry.single_step}
                for entry in self.profile.entries
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
        """形式全体を検証し、不正な項目だけを除いて復元する。"""
        raw = settings.value(state_key)
        if not isinstance(raw, qt.QtCore.QByteArray):
            return False
        try:
            decoded: object = json.loads(bytes(raw.data()))
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
        entries: list[IntStepSetting] = []
        for raw_entry in raw_entries:
            if not isinstance(raw_entry, dict):
                continue
            entry = cast(dict[str, object], raw_entry)
            try:
                entries.append(
                    IntStepSetting(
                        cast(str, entry.get("key")),
                        cast(int, entry.get("single_step")),
                    )
                )
            except (TypeError, ValueError, OverflowError):
                continue
        self.profile.replace_entries(entries)
        return True
