# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ......... import logger as u_logger
from ....._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class UnitBasePlugOperator(PlugOperator[A]):
    __slots__ = ()

    def set_key_direct(self, value, frame: float):
        self._set_key_direct(value, frame)

    def insert_key_direct(self, frame: float, breakdown: bool = False) -> int:
        return self._insert_key_direct(frame, breakdown=breakdown)

    def delete_anim_curve(self) -> bool:
        return self._delete_anim_curve()

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

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class UnitBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class UnitBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], UnitBaseAttrOperator)
    PLUG_CLS = cast(Type[P], UnitBasePlugOperator)
