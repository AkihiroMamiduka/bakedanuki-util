# coding: utf-8
from enum import Enum


class AttributeEnum(Enum):
    """
    Maya の enumName 文字列を生成するための基底 Enum クラス。

    メンバー定義方法:
        LABEL = "表示文字列"              # 整数値は 0 から順に自動付与
        LABEL = ("表示文字列", 明示的整数)  # 整数値を明示的に指定

    Examples:
        class OperationEnum(AttributeEnum):
            NO_OPERATION = "No operation"
            SUM = "Sum"
            SUBTRACT = "Subtract"
            AVERAGE = "Average"

        class NodeStateEnum(AttributeEnum):
            NORMAL = "Normal"
            HAS_NO_EFFECT = "Has no effect"
            BLOCKING = "Blocking"
            WAITING_NORMAL = ("Waiting normal", 8)
            WAITING_HAS_NO_EFFECT = "Waiting has no effect"
            WAITING_BLOCKING = "Waiting blocking"
    """

    def __new__(cls, label: str, explicit_value: int | None = None):
        if explicit_value is not None:
            value = explicit_value
        else:
            existing = [m._value_ for m in cls.__members__.values()]
            value = max(existing, default=-1) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        obj.label = label
        return obj

    def __int__(self) -> int:
        return self._value_

    def __index__(self) -> int:
        return self._value_

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int):
            return self._value_ == other
        return super().__eq__(other)

    def __hash__(self) -> int:
        return hash(self._value_)

    @classmethod
    def to_enum_name(cls) -> str:
        return ":".join([f"{c.label}={c.value}" for c in cls])
