# coding: utf-8
from typing import Generic, Protocol, TypeVar

from .._python_attribute import PythonAttributeAccess
from .definition import EnumDefinition, require_definition, require_enum_value

_InstanceT = TypeVar("_InstanceT")


class EnumValueStore(Protocol):
    """enumの正本と選択肢へのアクセス境界。"""

    @property
    def is_available(self) -> bool:
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        raise NotImplementedError

    @property
    def definition(self) -> EnumDefinition:
        raise NotImplementedError

    def read(self) -> int:
        raise NotImplementedError

    def write(self, value: int) -> int:
        """選択要求を書き込み、setter適用後の実値を返す。"""
        raise NotImplementedError


class PythonEnumAttributeStore(Generic[_InstanceT]):
    """Python属性のintを正本とする。未定義の実値は補正しない。"""

    def __init__(
        self,
        instance: _InstanceT,
        attribute_name: str,
        *,
        definition: EnumDefinition,
    ) -> None:
        self._definition = require_definition(definition)
        self._attribute = PythonAttributeAccess(instance, attribute_name)
        self.read()

    @property
    def instance(self) -> _InstanceT:
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        return self._attribute.attribute_name

    @property
    def definition(self) -> EnumDefinition:
        return self._definition

    @property
    def is_available(self) -> bool:
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        return self._attribute.is_writable

    def read(self) -> int:
        return require_enum_value(self._attribute.read())

    def write(self, value: int) -> int:
        value = self._definition.require_value(value)
        self._attribute.write(value)
        return self.read()
