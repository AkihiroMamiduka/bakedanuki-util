# coding: utf-8
from __future__ import annotations
from collections.abc import Callable
from typing import Any, Protocol, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ...._core import AttrOperator, PlugOperator, AttributeField
from ........py.error import UnsupportedOperationError

A = TypeVar("A", bound="AttrOperator[Any]")

P = TypeVar("P", bound="PlugOperator[Any]")

_DefaultObjectFactory = Callable[[object], om.MObject]


class _CreateTypedAttribute(Protocol):

    def __call__(
        self,
        long_name: str,
        short_name: str,
        mfn_data_type: int,
        default_object: om.MObject = ...,
        /,
    ) -> om.MObject: ...


class DataTypePlugOperator(PlugOperator[A]):
    __slots__ = ()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        # ファンクションを作成
        self._fn_attr = om.MFnTypedAttribute()

    # add
    def _add_attr_base(
        self,
        mfn_data_type: int,
        default_object_factory: _DefaultObjectFactory | None = None,
    ) -> None:
        # アトリビュートが既に存在する場合はスキップ
        if self.exists():
            return

        default_value = self._oprt_attr.default_value
        default_object: om.MObject | None = None
        if default_value is not None:
            if default_object_factory is None:
                raise UnsupportedOperationError(
                    f"{self._oprt_attr.DATA_TYPE} does not support "
                    "default_value."
                )
            default_object = default_object_factory(default_value)

        # アトリビュートを作成
        fn_attr = cast(om.MFnTypedAttribute, self._fn_attr)
        create_attr = cast(
            _CreateTypedAttribute,
            fn_attr.create,
        )
        if default_object is None:
            attr_obj = create_attr(
                self.long_name,
                self.short_name,
                mfn_data_type,
            )
        else:
            attr_obj = create_attr(
                self.long_name,
                self.short_name,
                mfn_data_type,
                default_object,
            )
        self._apply_mfn_attr_options(fn_attr)

        # ノードにアトリビュートを追加
        self._node.fn_node.addAttribute(attr_obj)


class DataTypeAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "typed"


class DataTypeField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataTypeAttrOperator)
    PLUG_CLS = cast(Type[P], DataTypePlugOperator)
