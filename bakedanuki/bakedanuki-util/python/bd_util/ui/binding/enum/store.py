# coding: utf-8
from typing import Generic, Protocol, TypeVar

from .._python_attribute import PythonAttributeAccess
from .definition import EnumDefinition, require_definition, require_enum_value

_InstanceT = TypeVar("_InstanceT")


class EnumValueStore(Protocol):
    """enumの正本と選択肢へのアクセス境界。"""

    @property
    def is_available(self) -> bool:
        """正本の属性が存在する場合は`True`。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """正本の属性へ変更を要求できる場合は`True`。"""
        raise NotImplementedError

    @property
    def definition(self) -> EnumDefinition:
        """値と表示名の対応を返す。"""
        raise NotImplementedError

    def read(self) -> int:
        """未定義値も補正せず、正本の整数値を返す。"""
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
        """既存の整数属性と選択肢を接続する。

        Args:
            instance: 属性を持つPython object。
            attribute_name: 正本として扱う既存属性名。
            definition: 書き込み可能な整数値と表示名の対応。
        """
        self._definition = require_definition(definition)
        self._attribute = PythonAttributeAccess(instance, attribute_name)
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        """正本として扱う属性名を返す。"""
        return self._attribute.attribute_name

    @property
    def definition(self) -> EnumDefinition:
        """生成時に指定した選択肢を返す。"""
        return self._definition

    @property
    def is_available(self) -> bool:
        """getterを呼ばずに属性の存在を判定する。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """propertyやdescriptorの構造から編集可否を判定する。"""
        return self._attribute.is_writable

    def read(self) -> int:
        """未定義値も補正せず、正本の整数値を返す。"""
        return require_enum_value(self._attribute.read())

    def write(self, value: int) -> int:
        """定義済みの値を設定し、setter適用後の実値を返す。

        Args:
            value: 選択肢に含まれる整数値。

        Raises:
            ValueError: valueが選択肢にない場合。
        """
        value = self._definition.require_value(value)
        self._attribute.write(value)
        return self.read()
