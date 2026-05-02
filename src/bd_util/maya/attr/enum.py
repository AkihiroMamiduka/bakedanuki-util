# coding: utf-8
from enum import IntEnum


class AttributeEnum(IntEnum):
    @classmethod
    def to_enum_name(cls):
        return ":".join([c.value for c in cls])
