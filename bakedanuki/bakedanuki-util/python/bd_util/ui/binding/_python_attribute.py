# coding: utf-8
from inspect import getattr_static
from typing import Generic, Protocol, TypeVar, cast

_InstanceT = TypeVar("_InstanceT")
_MISSING = object()


class _DataclassParams(Protocol):
    """dataclassの書き込み可否に必要な属性だけを参照する。"""

    frozen: bool


class PythonAttributeAccess(Generic[_InstanceT]):
    """値の型に依存せず、Python属性の存在・編集可否・読み書きを扱う。"""

    def __init__(self, instance: _InstanceT, attribute_name: object) -> None:
        """属性名と静的な存在を検証し、getterを呼ばずに保持する。"""
        if not isinstance(attribute_name, str):
            raise TypeError("attribute_nameにはstrを指定してください")
        if not attribute_name:
            raise ValueError("attribute_nameには空でないstrを指定してください")
        self._instance = instance
        self._attribute_name = attribute_name
        if not self.is_available:
            raise AttributeError(
                f"{type(instance).__name__}にattribute '{attribute_name}'は存在しません"
            )

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._instance

    @property
    def attribute_name(self) -> str:
        """正本として扱う属性名を返す。"""
        return self._attribute_name

    @property
    def is_available(self) -> bool:
        """getterを呼ばず、対象属性が静的に存在するか返す。"""
        return (
            getattr_static(self._instance, self._attribute_name, _MISSING)
            is not _MISSING
        )

    @property
    def is_writable(self) -> bool:
        """property・descriptor・slots・frozenの構造から編集可否を返す。"""
        if not self.is_available or self._is_frozen_dataclass:
            return False

        # propertyとdescriptorはクラスに定義されたsetterを確認する。
        descriptor = cast(
            object,
            getattr_static(
                type(self._instance), self._attribute_name, _MISSING
            ),
        )
        if isinstance(descriptor, property):
            return descriptor.fset is not None
        if descriptor is not _MISSING:
            setter = cast(
                object, getattr_static(type(descriptor), "__set__", _MISSING)
            )
            if setter is not _MISSING:
                return True

        # 通常属性はinstanceの辞書へ書き込める場合に編集を許可する。
        return (
            getattr_static(self._instance, "__dict__", _MISSING)
            is not _MISSING
        )

    def read(self) -> object:
        """利用可能な属性の実値を型変換せずに返す。"""
        if not self.is_available:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'は利用できません"
            )
        return getattr(self._instance, self._attribute_name)

    def require_writable(self) -> None:
        """編集できない属性への変更要求を拒否する。"""
        if not self.is_writable:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'へ書き込めません"
            )

    def write(self, value: object) -> None:
        """属性全体のsetterを1回呼び、実値の検証はStoreへ委ねる。"""
        self.require_writable()
        setattr(self._instance, self._attribute_name, value)

    @property
    def _is_frozen_dataclass(self) -> bool:
        """正本が変更を禁止するfrozen dataclassか返す。"""
        params = cast(
            object,
            getattr_static(
                type(self._instance), "__dataclass_params__", _MISSING
            ),
        )
        return (
            False
            if params is _MISSING
            else cast(_DataclassParams, params).frozen
        )
