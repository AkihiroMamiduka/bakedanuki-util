# coding: utf-8
from typing import Any, TypeVar, Type, cast

# self
from ........... import logger as u_logger
from .._base import (
    UnitBaseAttrOperator,
    UnitBasePlugOperator,
    UnitBaseField,
)

A = TypeVar("A", bound="UnitBaseAttrOperator[Any]")

P = TypeVar("P", bound="UnitBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitRangeBasePlugOperator(UnitBasePlugOperator[A]):
    """単位付き属性の値域と推奨値域を設定するプラグ操作の基底クラス。"""

    __slots__ = ()

    def set_min(self, value: float) -> None:
        """属性の下限を即時設定する。

        Args:
            value: 許可する最小値。
        """
        self._unit_fn_attr.setMin(value)

    def set_max(self, value: float) -> None:
        """属性の上限を即時設定する。

        Args:
            value: 許可する最大値。
        """
        self._unit_fn_attr.setMax(value)

    def set_soft_min(self, value: float) -> None:
        """UI 上で使用する推奨下限を即時設定する。

        Args:
            value: 推奨する最小値。
        """
        self._unit_fn_attr.setSoftMin(value)

    def set_soft_max(self, value: float) -> None:
        """UI 上で使用する推奨上限を即時設定する。

        Args:
            value: 推奨する最大値。
        """
        self._unit_fn_attr.setSoftMax(value)

    def _add_attr_base(self, mfn_numeric_data_type: int):
        super()._add_attr_base(mfn_numeric_data_type)

        # 属性の追加後、指定された値域と推奨値域を適用する。
        v = self._oprt_attr.min_value
        if v is not None:
            self.set_min(v)
        v = self._oprt_attr.max_value
        if v is not None:
            self.set_max(v)
        v = self._oprt_attr.soft_min_value
        if v is not None:
            self.set_soft_min(v)
        v = self._oprt_attr.soft_max_value
        if v is not None:
            self.set_soft_max(v)


class UnitRangeBaseAttrOperator(UnitBaseAttrOperator[P]):
    __slots__ = ()


class UnitRangeBaseField(UnitBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitRangeBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitRangeBasePlugOperator)
