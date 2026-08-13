# coding: utf-8
from __future__ import annotations
from collections.abc import Callable, Iterable
from typing import Any, Protocol, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

A = TypeVar("A", bound="DataTypeAttrOperator[Any]")

P = TypeVar("P", bound="DataTypePlugOperator[Any]")

T = TypeVar("T")

T_co = TypeVar("T_co", covariant=True)


class _ArrayData(Protocol[T_co]):
    def array(self) -> Iterable[T_co]: ...

    def create(self, values: object = ...) -> om.MObject: ...

    def set(self, values: object) -> None: ...


_ArrayDataFactory = Callable[..., _ArrayData[T]]

_ArrayFactory = Callable[[list[T]], object]


class DataArrayBasePlugOperator(DataTypePlugOperator[A]):
    __slots__ = ()

    # get
    def _get_array_data(
        self,
        fn_data_cls: _ArrayDataFactory[T],
    ) -> Iterable[T]:
        data_obj = cast(om.MObject, self.plug.asMDataHandle().data())
        return fn_data_cls(data_obj).array()

    def _get_array_values(
        self,
        fn_data_cls: _ArrayDataFactory[T],
    ) -> list[T]:
        return list(self._get_array_data(fn_data_cls))

    # set
    def _set_values(
        self,
        fn_data_cls: _ArrayDataFactory[T],
        array_cls: _ArrayFactory[T],
        values: list[T],
    ) -> None:
        """
        値をセットするヘルパー

        modifier.undoIt() 非対応

        Args:
            values (list[T]): セットする値のリスト
        """
        self.plug.setMObject(fn_data_cls().create(array_cls(values)))

    def _set_values_after_create(
        self,
        fn_data_cls: _ArrayDataFactory[T],
        array_cls: _ArrayFactory[T],
        values: list[T],
    ) -> None:
        fn_data = fn_data_cls()
        data_obj = fn_data.create()
        fn_data.set(array_cls(values))
        self.plug.setMObject(data_obj)


class DataArrayBaseAttrOperator(DataTypeAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "abc"


class DataArrayBaseField(DataTypeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataArrayBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DataArrayBasePlugOperator)
