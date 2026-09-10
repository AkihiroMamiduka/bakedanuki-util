# coding: utf-8
from typing import Generic, Protocol, TypeVar

from .._python_attribute import PythonAttributeAccess
from ._validation import require_float
from .presentation import FloatPresentation, require_presentation

_InstanceT = TypeVar("_InstanceT")


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
        self._presentation = require_presentation(
            presentation if presentation is not None else FloatPresentation()
        )
        self._attribute = PythonAttributeAccess(instance, attribute_name)

        # getterを存在確認で実行せず、読み取り時に実値の型と有限性を検証する。
        self.read()

    @property
    def instance(self) -> _InstanceT:
        """正本のPython objectを具体型のまま返す。"""
        return self._attribute.instance

    @property
    def attribute_name(self) -> str:
        """正本として扱う単一のPython属性名を返す。"""
        return self._attribute.attribute_name

    @property
    def presentation(self) -> FloatPresentation:
        """生成時に指定したimmutableな表示情報を返す。"""
        return self._presentation

    @property
    def is_available(self) -> bool:
        """getterを呼ばず、対象属性が静的に存在するか返す。"""
        return self._attribute.is_available

    @property
    def is_writable(self) -> bool:
        """property・descriptor・slots・frozenの構造から編集可否を返す。"""
        return self._attribute.is_writable

    def read(self) -> float:
        """属性を変更せず、有限の実値をfloatで返す。"""
        return require_float(
            self._attribute.read(),
            f"attribute '{self.attribute_name}'",
        )

    def write(self, value: float) -> float:
        """有限値と入力範囲を検証し、setter適用後の実値を返す。"""
        value = require_float(value)
        self._attribute.require_writable()

        # 範囲は公開値の単位で検証し、setter実行前に不正な要求を拒否する。
        minimum = self._presentation.minimum
        maximum = self._presentation.maximum
        if minimum is not None and value < minimum:
            raise ValueError("valueは属性の下限未満です")
        if maximum is not None and value > maximum:
            raise ValueError("valueは属性の上限を超えています")
        self._attribute.write(value)
        return self.read()
