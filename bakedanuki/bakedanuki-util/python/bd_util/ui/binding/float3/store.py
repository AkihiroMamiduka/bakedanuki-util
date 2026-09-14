# coding: utf-8
from __future__ import annotations

from collections.abc import Callable
from typing import Generic, Protocol, TypeVar, cast

from .._python_attribute import PythonAttributeAccess
from ..float._validation import require_float
from ..float.presentation import FloatPresentation, require_presentation
from ..float.store import FloatValueStore
from .value import Float3, require_float3

_InstanceT = TypeVar("_InstanceT")


def _require_presentations(
    value: object,
) -> tuple[FloatPresentation, FloatPresentation, FloatPresentation]:
    """全軸共通またはXYZごとの表示情報を検証する。"""
    if value is None:
        value = FloatPresentation()
    if isinstance(value, FloatPresentation):
        return value, value, value
    if not isinstance(value, tuple):
        raise TypeError(
            "presentationにはFloatPresentationまたはその3成分tupleを指定してください"
        )
    values = cast(tuple[object, ...], value)
    if len(values) != 3:
        raise ValueError("presentationにはXYZの3成分を指定してください")
    return (
        require_presentation(values[0]),
        require_presentation(values[1]),
        require_presentation(values[2]),
    )


class Float3ValueStore(Protocol):
    """3つのscalar Storeと、正本への一括読み書きの境界。"""

    @property
    def components(
        self,
    ) -> tuple[FloatValueStore, FloatValueStore, FloatValueStore]:
        """X・Y・Zの正本にアクセスするStoreを返す。"""
        raise NotImplementedError

    @property
    def is_available(self) -> bool:
        """3成分の正本を読み取れるか返す。"""
        raise NotImplementedError

    @property
    def is_writable(self) -> bool:
        """3成分すべてを書き込めるか返す。"""
        raise NotImplementedError

    def read(self) -> Float3:
        """丸めていない公開単位の3成分を返す。"""
        raise NotImplementedError

    def write(self, value: Float3) -> Float3:
        """3成分を一括設定し、確定した実値を返す。"""
        raise NotImplementedError


class _PythonFloat3ComponentStore(Generic[_InstanceT]):
    """tupleの各軸を既存のscalar ViewModelへ公開する。"""

    def __init__(
        self,
        attribute: PythonAttributeAccess[_InstanceT],
        index: int,
        presentation: FloatPresentation,
        read: Callable[[], Float3],
        write: Callable[[int, float], float],
    ) -> None:
        """正本の利用状態と、親Storeの各軸用読み書きを参照する。"""
        self._attribute = attribute
        self._index = index
        self._presentation = presentation
        self._read = read
        self._write = write

    @property
    def is_available(self) -> bool:
        """親属性の静的な存在を確認する。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """親属性のsetterへ書き込めるか返す。"""
        return self._attribute.is_writable

    @property
    def presentation(self) -> FloatPresentation:
        """この軸の表示情報と入力範囲を返す。"""
        return self._presentation

    def read(self) -> float:
        """親属性の最新値からこの軸の値を返す。"""
        return self._read()[self._index]

    def write(self, value: float) -> float:
        """他成分を保持してこの軸を変更し、setter適用後の値を返す。"""
        return self._write(self._index, value)


class PythonFloat3AttributeStore(Generic[_InstanceT]):
    """Python属性の3成分tupleを正本として、各軸と一括編集を提供する。"""

    def __init__(
        self,
        instance: _InstanceT,
        attribute_name: str,
        *,
        presentation: (
            FloatPresentation
            | tuple[FloatPresentation, FloatPresentation, FloatPresentation]
            | None
        ) = None,
    ) -> None:
        """属性と表示情報を検証し、初期値を書き換えずに各軸のStoreを作る。"""
        self._presentations = _require_presentations(presentation)
        self._attribute = PythonAttributeAccess(instance, attribute_name)
        self.read()

        # 各軸は同じ属性を参照し、値を別々のPython属性へ複製しない。
        self._components = tuple(
            _PythonFloat3ComponentStore(
                self._attribute, index, item, self.read, self._write_component
            )
            for index, item in enumerate(self._presentations)
        )

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        """正本として扱う単一のPython属性名を返す。"""
        return self._attribute.attribute_name

    @property
    def presentations(
        self,
    ) -> tuple[FloatPresentation, FloatPresentation, FloatPresentation]:
        """XYZそれぞれの表示情報を返す。"""
        return self._presentations

    @property
    def components(
        self,
    ) -> tuple[FloatValueStore, FloatValueStore, FloatValueStore]:
        """各軸をscalar ViewModelへ接続するStoreを返す。"""
        return self._components[0], self._components[1], self._components[2]

    @property
    def is_available(self) -> bool:
        """getterを呼ばず、親属性が静的に存在するか返す。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """親属性全体のsetterへ書き込めるか返す。"""
        return self._attribute.is_writable

    def read(self) -> Float3:
        """3成分tupleの実値を、属性を書き換えずにfloatへ正規化する。"""
        value = self._attribute.read()
        if not isinstance(value, tuple):
            raise TypeError(
                f"attribute '{self.attribute_name}'には3成分tupleを指定してください"
            )
        return require_float3(cast(tuple[object, ...], value))

    def write(self, value: Float3) -> Float3:
        """全成分を事前検証してsetterを1回呼び、確定値を返す。"""
        values = require_float3(value)
        self._attribute.require_writable()
        for index, item in enumerate(values):
            self._require_component_range(index, item)
        self._attribute.write(values)
        return self.read()

    def _write_component(self, index: int, value: float) -> float:
        """編集軸だけの範囲を検証し、他軸の最新実値を含むtupleで再代入する。"""
        value = require_float(value)
        self._attribute.require_writable()
        self._require_component_range(index, value)

        # 表示の丸めや未同期の外部変更を上書きせず、正本の残り2成分を保持する。
        current = self.read()
        values = tuple(
            value if axis == index else current[axis] for axis in range(3)
        )
        self._attribute.write(require_float3(values))
        return self.read()[index]

    def _require_component_range(self, index: int, value: float) -> None:
        """変更を要求した軸の公開単位で入力範囲を検証する。"""
        presentation = self._presentations[index]
        if presentation.minimum is not None and value < presentation.minimum:
            raise ValueError(f"value[{index}]は属性の下限未満です")
        if presentation.maximum is not None and value > presentation.maximum:
            raise ValueError(f"value[{index}]は属性の上限を超えています")
