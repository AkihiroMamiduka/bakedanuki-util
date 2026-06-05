# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from ........ import logger as u_logger
from ...._core import AttrOperator, PlugOperator, AttributeField

A = TypeVar("A", bound="AttrOperator")

P = TypeVar("P", bound="PlugOperator")


logger = u_logger.get_logger(__name__, level=u_logger.DEBUG)


class FloatingPointScalarType:
    """
    float, double の、 通常の値/距離/角度、どの型なのかを表す列挙型
    """

    Numeric = 0
    DISTANCE = 1
    ANGLE = 2


class FloatingPointBasePlugOperator(PlugOperator[A]):
    __slots__ = ("_child_type",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 子アトリビュートの型を解析して保存
        self._child_type = None

    def _analyze_child_type(self) -> int:
        """
        子アトリビュートの型を解析する

        Raises:
            TypeError: 子アトリビュートの型が不明な場合に発生

        Returns:
            FloatingPointScalarType: float, double の、 通常の値/距離/角度、どの型なのかを表す列挙型
        """
        # キャッシュがあればそれを返す
        if self._child_type is not None:
            return self._child_type

        # 1つ目の子の属性から型を推測する
        plug = self.plug.child(0)
        attr = plug.attribute()

        # 型を推測
        plug_type = None
        if attr.hasFn(om.MFn.kUnitAttribute):
            fn = om.MFnUnitAttribute(attr)
            unit_type = fn.unitType()
            if unit_type == om.MFnUnitAttribute.kAngle:
                plug_type = FloatingPointScalarType.ANGLE
            elif unit_type == om.MFnUnitAttribute.kDistance:
                plug_type = FloatingPointScalarType.DISTANCE
        elif attr.hasFn(om.MFn.kNumericAttribute):
            fn = om.MFnNumericAttribute(attr)
            numeric_type = fn.numericType()
            if (
                numeric_type == om.MFnNumericData.kDouble
                or numeric_type == om.MFnNumericData.kFloat
            ):
                plug_type = FloatingPointScalarType.Numeric

        # 型がわからない場合はエラー
        if plug_type is None:
            raise TypeError(
                "{} {} {}: {}".format(
                    "子アトリビュートは、",
                    "double/doubleLinear/doubleAngle",
                    "のいずれかである必要があります",
                    attr.apiType(),
                )
            )

        # キャッシュする
        self._child_type = plug_type

        # 戻り値
        return plug_type


class FloatingPointBaseAttrOperator(AttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "abc"


class FloatingPointBaseField(AttributeField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], FloatingPointBaseAttrOperator)
    PLUG_CLS = cast(Type[P], FloatingPointBasePlugOperator)
