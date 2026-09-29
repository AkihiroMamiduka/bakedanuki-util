# coding: utf-8
from typing import Generic, Protocol, TypeVar

from .._python_attribute import PythonAttributeAccess
from ._validation import require_string

_InstanceT = TypeVar("_InstanceT")


class StringValueStore(Protocol):
    """一つの文字列を正本として読み書きする契約。"""

    @property
    def is_available(self) -> bool:
        """正本を読み取れる場合は`True`。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """正本へ変更を要求できる場合は`True`。"""
        raise NotImplementedError

    def read(self) -> str:
        """正本の確定文字列を返す。"""
        raise NotImplementedError

    def write(self, value: str) -> str:
        """変更要求後に読み直した実値を返す。"""
        raise NotImplementedError


class PythonStringAttributeStore(Generic[_InstanceT]):
    """既存のPython文字列属性を正本として扱う。"""

    def __init__(self, instance: _InstanceT, attribute_name: str) -> None:
        """対象属性を検証し、初期値を読み取る。"""
        self._attribute = PythonAttributeAccess(instance, attribute_name)
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        """正本の属性名を返す。"""
        return self._attribute.attribute_name

    @property
    def is_available(self) -> bool:
        """getterを呼ばず属性の存在を返す。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """属性構造から編集可否を返す。"""
        return self._attribute.is_writable

    def read(self) -> str:
        """正本を型変換せず読み取る。"""
        return require_string(
            self._attribute.read(), f"attribute '{self.attribute_name}'"
        )

    def write(self, value: str) -> str:
        """setterを一度呼び、補正後の実値を返す。"""
        self._attribute.write(require_string(value))
        return self.read()
