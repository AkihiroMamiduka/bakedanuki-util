# coding: utf-8
from __future__ import annotations
from typing import Any, TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .._core import DataTypeAttrOperator, DataTypePlugOperator, DataTypeField

A = TypeVar("A", bound="DataTypeAttrOperator[Any]")

P = TypeVar("P", bound="DataTypePlugOperator[Any]")


class DataNumericBasePlugOperator(DataTypePlugOperator[A]):
    __slots__ = ()

    # get
    def _get_data(self) -> list[float]:
        m_obj = self.plug.asMObject()
        fn_data = om.MFnNumericData(m_obj)
        return fn_data.getData()

    # set
    def _set_data(self, numeric_type, values: list[float]):
        """
        値をセットするヘルパー

        modifier.undoIt() 非対応

        Args:
            values (list[float]): セットする値のリスト
        """
        fn_data = om.MFnNumericData()
        obj = fn_data.create(numeric_type)
        fn_data.setData(*values)
        self.plug.setMObject(obj)


class DataNumericBaseAttrOperator(DataTypeAttrOperator[P]):
    __slots__ = ()

    DATA_TYPE = "abc"


class DataNumericBaseField(DataTypeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], DataNumericBaseAttrOperator)
    PLUG_CLS = cast(Type[P], DataNumericBasePlugOperator)
