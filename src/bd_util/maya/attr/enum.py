# coding: utf-8
from enum import IntEnum


class AttributeEnum(IntEnum):
    @classmethod
    def to_enum_name(cls) -> str:
        return ":".join(
            [f"{c.name.replace('_', ' ').capitalize()}={c.value}" for c in cls]
        )
