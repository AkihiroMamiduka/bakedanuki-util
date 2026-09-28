# coding: utf-8
from typing import Any, TypeVar, Type, cast

from maya.api import OpenMaya as om

from .......... import logger as u_logger
from .._base import (
    ScalarBaseAttrOperator,
    ScalarBasePlugOperator,
    ScalarBaseField,
)

A = TypeVar("A", bound="NumericBaseAttrOperator[Any]")

P = TypeVar("P", bound="NumericBasePlugOperator[Any]")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class NumericBasePlugOperator(ScalarBasePlugOperator[A]):
    """数値スカラー属性のプラグ操作を扱う基底クラス。"""

    __slots__ = ()

    @property
    def _numeric_fn_attr(self) -> om.MFnNumericAttribute:
        fn_attr = self._fn_attr
        if not isinstance(fn_attr, om.MFnNumericAttribute):
            raise RuntimeError(
                f"{type(self).__name__} numeric attribute is not initialized."
            )
        return fn_attr

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
    """数値スカラー属性の定義を扱う基底クラス。"""

    __slots__ = ()


class NumericBaseField(ScalarBaseField[A, P]):
    """数値スカラー属性の定義とプラグ操作を結ぶ基底ディスクリプタ。"""

    __slots__ = ()

    ATTR_CLS = cast(Type[A], NumericBaseAttrOperator)
    PLUG_CLS = cast(Type[P], NumericBasePlugOperator)
