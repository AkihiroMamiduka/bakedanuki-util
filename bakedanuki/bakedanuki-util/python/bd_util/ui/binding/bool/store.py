# coding: utf-8
from __future__ import annotations

from inspect import getattr_static
from typing import Generic, Protocol, TypeVar, cast

_InstanceT = TypeVar("_InstanceT")
_MISSING = object()


class _DataclassParams(Protocol):
    """frozen判定に必要なdataclass paramsの最小境界。"""

    frozen: bool


def _require_bool(value: object, argument_name: str) -> bool:
    """値をboolとして検証して返す。"""
    if not isinstance(value, bool):
        raise TypeError(
            f"{argument_name}にはboolを指定してください: "
            f"{type(value).__name__}"
        )
    return value


def _require_attribute_name(value: object) -> str:
    """値を空でないattribute名として検証して返す。"""
    if not isinstance(value, str):
        raise TypeError(
            "attribute_nameにはstrを指定してください: "
            f"{type(value).__name__}"
        )
    if not value:
        raise ValueError("attribute_nameには空でないstrを指定してください")
    return value


class BoolValueStore(Protocol):
    """BoolViewModelが任意の値の正本を扱うための境界。"""

    @property
    def is_available(self) -> bool:
        """値の正本が読み取り可能か返す。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """値の正本が書き込み可能か返す。"""
        raise NotImplementedError

    def read(self) -> bool:
        """値の正本から現在値を返す。"""
        raise NotImplementedError

    def write(self, value: bool) -> bool:
        """値の正本へ書き込み、確定した実値を返す。"""
        raise NotImplementedError


class PythonBoolAttributeStore(Generic[_InstanceT]):
    """Python objectのbool attributeを値の正本として扱うStore。"""

    def __init__(
        self,
        instance: _InstanceT,
        attribute_name: str,
    ) -> None:
        """同期対象instanceとattribute名を受け取って初期化する。"""
        self._instance = instance
        self._attribute_name = _require_attribute_name(attribute_name)

        if not self.is_available:
            raise AttributeError(
                f"{type(instance).__name__}にattribute "
                f"'{self._attribute_name}'は存在しません"
            )
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """同期対象のPython objectを返す。"""
        return self._instance

    @property
    def attribute_name(self) -> str:
        """同期対象のattribute名を返す。"""
        return self._attribute_name

    @property
    def is_available(self) -> bool:
        """対象attributeが存在するか返す。"""
        attribute = cast(
            object,
            getattr_static(
                self._instance,
                self._attribute_name,
                _MISSING,
            ),
        )
        return attribute is not _MISSING

    @property
    def is_writable(self) -> bool:
        """対象attributeへ書き込めることを静的に判定して返す。"""
        if not self.is_available or self._is_frozen_dataclass:
            return False

        descriptor = cast(
            object,
            getattr_static(
                type(self._instance),
                self._attribute_name,
                _MISSING,
            ),
        )
        if isinstance(descriptor, property):
            return descriptor.fset is not None
        if descriptor is not _MISSING:
            descriptor_setter = cast(
                object,
                getattr_static(
                    type(descriptor),
                    "__set__",
                    _MISSING,
                ),
            )
            if descriptor_setter is not _MISSING:
                return True

        instance_dict = cast(
            object,
            getattr_static(
                self._instance,
                "__dict__",
                _MISSING,
            ),
        )
        return instance_dict is not _MISSING

    def read(self) -> bool:
        """対象attributeの現在値を返す。"""
        if not self.is_available:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'は利用できません"
            )
        value = getattr(self._instance, self._attribute_name)
        return _require_bool(
            value,
            f"attribute '{self._attribute_name}'",
        )

    def write(self, value: bool) -> bool:
        """対象attributeへ値を書き込み、確定した実値を返す。"""
        value = _require_bool(value, "value")
        if not self.is_writable:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'へ書き込めません"
            )
        setattr(self._instance, self._attribute_name, value)
        return self.read()

    @property
    def _is_frozen_dataclass(self) -> bool:
        """同期対象がfrozen dataclassのinstanceか返す。"""
        params = cast(
            object,
            getattr_static(
                type(self._instance),
                "__dataclass_params__",
                _MISSING,
            ),
        )
        if params is _MISSING:
            return False
        return cast(_DataclassParams, params).frozen
