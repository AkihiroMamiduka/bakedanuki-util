# coding: utf-8
from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .......... import logger as u_logger
from .._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)
from .._round import RoundScalarPlugOperatorMixin

A = TypeVar("A", bound="UnitBaseAttrOperator[Any]")

P = TypeVar("P", bound="UnitBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitBasePlugOperator(
    RoundScalarPlugOperatorMixin,
    ScalarBasePlugOperator[A],
):
    __slots__ = ()

    @property
    def _unit_fn_attr(self) -> om.MFnUnitAttribute:
        fn_attr = self._fn_attr
        if not isinstance(fn_attr, om.MFnUnitAttribute):
            raise RuntimeError(
                f"{type(self).__name__} unit attribute is not initialized."
            )
        return fn_attr

    # add
    def _add_attr_base(self, mfn_numeric_data_type: int):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnUnitAttribute()
        self._fn_attr = fn_attr

        # アトリビュートを作成
        attr_obj = fn_attr.create(
            self.long_name,
            self.short_name,
            mfn_numeric_data_type,
            self._oprt_attr.default_value,
        )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class UnitBaseAttrOperator(ScalarBaseAttrOperator[P]):
    __slots__ = ()


class UnitBaseField(ScalarBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitBasePlugOperator)
