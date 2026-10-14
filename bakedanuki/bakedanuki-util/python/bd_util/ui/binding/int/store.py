# coding: utf-8
from __future__ import annotations

from typing import Generic, Protocol, TypeVar

from .._python_attribute import PythonAttributeAccess
from ._validation import require_int
from .presentation import IntPresentation, require_presentation

_InstanceT = TypeVar("_InstanceT")


class IntValueStore(Protocol):
    """単一の符号付き32-bit整数の正本と入力範囲。"""

    @property
    def is_available(self) -> bool:
        """正本を利用できるか返す。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """正本を編集できるか返す。"""
        raise NotImplementedError

    @property
    def presentation(self) -> IntPresentation:
        """正本の入力範囲を返す。"""
        raise NotImplementedError

    def read(self) -> int:
        """正本の実値を整数のまま返す。"""
        raise NotImplementedError

    def write(self, value: int) -> int:
        """要求を適用し、確定後の実値を返す。"""
        raise NotImplementedError


class PythonIntAttributeStore(Generic[_InstanceT]):
    """Python objectの既存整数属性を正本とするStore。"""

    def __init__(
        self,
        instance: _InstanceT,
        attribute_name: str,
        *,
        presentation: IntPresentation | None = None,
    ) -> None:
        """属性を検証し、初期値を書き換えずに保持する。"""
        self._presentation = require_presentation(
            presentation if presentation is not None else IntPresentation()
        )
        self._attribute = PythonAttributeAccess(instance, attribute_name)
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        """対象の既存属性名を返す。"""
        return self._attribute.attribute_name

    @property
    def presentation(self) -> IntPresentation:
        """入力範囲を返す。"""
        return self._presentation

    @property
    def is_available(self) -> bool:
        """getterを呼ばず、属性の存在を返す。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """属性の構造から編集可否を返す。"""
        return self._attribute.is_writable

    def read(self) -> int:
        """型や精度を変えずに実値を返す。"""
        return require_int(
            self._attribute.read(), f"attribute '{self.attribute_name}'"
        )

    def write(self, value: int) -> int:
        """範囲をsetter実行前に検証し、setter後の実値を返す。"""
        value = require_int(value)
        self._attribute.require_writable()
        minimum = self._presentation.minimum
        maximum = self._presentation.maximum
        if minimum is not None and value < minimum:
            raise ValueError("valueは属性の下限未満です")
        if maximum is not None and value > maximum:
            raise ValueError("valueは属性の上限を超えています")
        self._attribute.write(value)
        return self.read()
