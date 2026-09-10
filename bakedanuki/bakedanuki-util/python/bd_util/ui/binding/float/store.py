# coding: utf-8
from inspect import getattr_static
from typing import Generic, Protocol, TypeVar, cast

from ._validation import require_float
from .presentation import FloatPresentation, require_presentation

_InstanceT = TypeVar("_InstanceT")
_MISSING = object()


class _DataclassParams(Protocol):
    """dataclassの書き込み可否に必要な属性だけを参照する。"""

    frozen: bool


def _require_attribute_name(value: object) -> str:
    """空でないPython属性名を検証して返す。"""
    if not isinstance(value, str):
        raise TypeError("attribute_nameにはstrを指定してください")
    if not value:
        raise ValueError("attribute_nameには空でないstrを指定してください")
    return value


class FloatValueStore(Protocol):
    """単一の浮動小数点値の正本への読み書きと表示情報。"""

    @property
    def is_available(self) -> bool:
        """正本の属性が利用可能か返す。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """正本の属性へ変更を要求できるか返す。"""
        raise NotImplementedError

    @property
    def presentation(self) -> FloatPresentation:
        """公開単位から表示単位への変換と入力範囲を返す。"""
        raise NotImplementedError

    def read(self) -> float:
        """丸めていない公開単位の実値を返す。"""
        raise NotImplementedError

    def write(self, value: float) -> float:
        """公開単位の要求を書き込み、確定後の実値を返す。"""
        raise NotImplementedError


class PythonFloatAttributeStore(Generic[_InstanceT]):
    """Python objectの数値属性を正本として読み書きするStore。"""

    def __init__(
        self,
        instance: _InstanceT,
        attribute_name: str,
        *,
        presentation: FloatPresentation | None = None,
    ) -> None:
        """既存属性と表示情報を検証し、初期値を書き換えずに保持する。"""
        self._instance = instance
        self._attribute_name = _require_attribute_name(attribute_name)
        self._presentation = require_presentation(
            presentation if presentation is not None else FloatPresentation()
        )

        # getterを存在確認で実行せず、読み取り時に実値の型と有限性を検証する。
        if not self.is_available:
            raise AttributeError(
                f"{type(instance).__name__}にattribute "
                f"'{self._attribute_name}'は存在しません"
            )
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._instance

    @property
    def attribute_name(self) -> str:
        """正本として扱う単一のPython属性名を返す。"""
        return self._attribute_name

    @property
    def presentation(self) -> FloatPresentation:
        """生成時に指定したimmutableな表示情報を返す。"""
        return self._presentation

    @property
    def is_available(self) -> bool:
        """getterを呼ばず、対象属性が静的に存在するか返す。"""
        attribute = cast(
            object,
            getattr_static(self._instance, self._attribute_name, _MISSING),
        )
        return attribute is not _MISSING

    @property
    def is_writable(self) -> bool:
        """property・descriptor・slots・frozenの構造から編集可否を返す。"""
        if not self.is_available or self._is_frozen_dataclass:
            return False

        # propertyとdescriptorはクラスに定義されたsetterの有無を確認する。
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
                object,
                getattr_static(type(descriptor), "__set__", _MISSING),
            )
            if setter is not _MISSING:
                return True

        # 通常属性はinstanceの辞書へ書き込める場合に編集を許可する。
        instance_dict = cast(
            object, getattr_static(self._instance, "__dict__", _MISSING)
        )
        return instance_dict is not _MISSING

    def read(self) -> float:
        """属性を変更せず、有限の実値をfloatで返す。"""
        if not self.is_available:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'は利用できません"
            )
        return require_float(
            getattr(self._instance, self._attribute_name),
            f"attribute '{self._attribute_name}'",
        )

    def write(self, value: float) -> float:
        """有限値と入力範囲を検証し、setter適用後の実値を返す。"""
        value = require_float(value)
        if not self.is_writable:
            raise RuntimeError(
                f"同期対象attribute '{self._attribute_name}'へ書き込めません"
            )

        # 範囲は公開値の単位で検証し、setter実行前に不正な要求を拒否する。
        minimum = self._presentation.minimum
        maximum = self._presentation.maximum
        if minimum is not None and value < minimum:
            raise ValueError("valueは属性の下限未満です")
        if maximum is not None and value > maximum:
            raise ValueError("valueは属性の上限を超えています")
        setattr(self._instance, self._attribute_name, value)
        return self.read()

    @property
    def _is_frozen_dataclass(self) -> bool:
        """正本が変更を禁止するfrozen dataclassか返す。"""
        params = cast(
            object,
            getattr_static(
                type(self._instance), "__dataclass_params__", _MISSING
            ),
        )
        if params is _MISSING:
            return False
        return cast(_DataclassParams, params).frozen
