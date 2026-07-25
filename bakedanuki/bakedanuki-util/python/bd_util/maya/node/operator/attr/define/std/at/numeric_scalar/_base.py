# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ......... import logger as u_logger
from ..scalar._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)

A = TypeVar("A", bound="NumericBaseAttrOperator")

P = TypeVar("P", bound="NumericBasePlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class NumericBasePlugOperator(ScalarBasePlugOperator[A]):
    __slots__ = ()

    # add
    def _add_attr_base(self, mfn_numeric_data_type: int):
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        # ファンクションを作成
        fn_attr = om.MFnNumericAttribute()
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


class NumericBaseAttrOperator(ScalarBaseAttrOperator[P]):
    __slots__ = ()


class NumericBaseField(ScalarBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], NumericBaseAttrOperator)
    PLUG_CLS = cast(Type[P], NumericBasePlugOperator)
