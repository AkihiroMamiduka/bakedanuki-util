# coding: utf-8
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import cast


def require_enum_value(value: object) -> int:
    """boolや暗黙変換を受け入れず、Python整数を返す。"""
    if not isinstance(value, int) or isinstance(value, bool):
        raise TypeError("valueにはbool以外のintを指定してください")
    return int(value)


def _require_name(value: object) -> str:
    if not isinstance(value, str):
        raise TypeError("nameにはstrを指定してください")
    if not value:
        raise ValueError("nameには空でないstrを指定してください")
    return value


def _require_items(value: object) -> tuple[EnumItem, ...]:
    if not isinstance(value, tuple):
        raise TypeError("itemsにはEnumItemのtupleを指定してください")
    for item in cast(tuple[object, ...], value):
        if not isinstance(item, EnumItem):
            raise TypeError("itemsにはEnumItemを指定してください")
    return cast(tuple[EnumItem, ...], value)


@dataclass(frozen=True)
class EnumItem:
    """整数値と項目名。View内の位置は値とは独立している。"""

    value: int
    name: str

    def __post_init__(self) -> None:
        require_enum_value(self.value)
        _require_name(self.name)


@dataclass(frozen=True)
class EnumDefinition:
    """順序を持つ不変の選択肢。空の定義では編集を停止する。"""

    items: tuple[EnumItem, ...] = ()

    def __post_init__(self) -> None:
        items = _require_items(self.items)
        values: set[int] = set()
        names: set[str] = set()
        for item in items:
            if item.value in values or item.name in names:
                raise ValueError("enumの値と項目名はそれぞれ重複できません")
            values.add(item.value)
            names.add(item.name)

    @classmethod
    def from_mapping(cls, names: Mapping[int, str]) -> EnumDefinition:
        """mappingの順序を維持して値と項目名を取り込む。"""
        return cls(
            tuple(EnumItem(value, name) for value, name in names.items())
        )

    def item_for_value(self, value: int) -> EnumItem | None:
        """未定義の実値は例外にせずNoneを返す。"""
        value = require_enum_value(value)
        return next((item for item in self.items if item.value == value), None)

    def require_value(self, value: int) -> int:
        """変更要求が定義に含まれていることを検証する。"""
        value = require_enum_value(value)
        if self.item_for_value(value) is None:
            raise ValueError(f"enumに定義されていない値です: {value}")
        return value

    def matches(self, other: EnumDefinition) -> bool:
        """表示順に依存せず、値と名前の対応が等しいか返す。"""
        return {item.value: item.name for item in self.items} == {
            item.value: item.name for item in other.items
        }


def require_definition(value: object) -> EnumDefinition:
    """Store境界で定義の型を検証する。"""
    if not isinstance(value, EnumDefinition):
        raise TypeError("definitionにはEnumDefinitionを指定してください")
    return value
