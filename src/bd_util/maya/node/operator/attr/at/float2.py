# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .base._floating_point_compound import (
    FloatingPointBaseAttrOperator,
    FloatingPointBasePlugOperator,
    FloatingPointBaseField,
    FloatingPointScalarType,
)

A = TypeVar("A", bound="FloatingPointBaseAttrOperator")

P = TypeVar("P", bound="FloatingPointBasePlugOperator")


class Float2PlugOperator(FloatingPointBasePlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        # 型を推測
        self._analyze_child_type()

        # 型に合わせて、値を取得
        if self._child_type == FloatingPointScalarType.Numeric:
            value = [
                self.plug.child(0).asFloat(),
                self.plug.child(1).asFloat(),
            ]
        elif self._child_type == FloatingPointScalarType.DISTANCE:
            value = [
                self.plug.child(0).asMDistance().asCentimeters(),
                self.plug.child(1).asMDistance().asCentimeters(),
            ]
        elif self._child_type == FloatingPointScalarType.ANGLE:
            value = [
                self.plug.child(0).asMAngle().asDegrees(),
                self.plug.child(1).asMAngle().asDegrees(),
            ]

        # 戻り値
        return value

    # set
    def set(self, *value: float | list[float]):
        # 型を推測
        self._analyze_child_type()

        try:
            # set(x, y)
            try:
                # 型に合わせて、値をセット
                if self._child_type == FloatingPointScalarType.Numeric:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0), value[0]
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1), value[1]
                    )
                elif self._child_type == FloatingPointScalarType.DISTANCE:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0),
                        om.MDistance(
                            value[0],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1),
                        om.MDistance(
                            value[1],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                elif self._child_type == FloatingPointScalarType.ANGLE:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0),
                        om.MAngle(value[0], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1),
                        om.MAngle(value[1], om.MAngle.uiUnit()).asRadians(),
                    )
            # set([x, y])
            except Exception:
                # 型に合わせて、値をセット
                if self._child_type == FloatingPointScalarType.Numeric:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0), value[0][0]
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1), value[0][1]
                    )
                elif self._child_type == FloatingPointScalarType.DISTANCE:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0),
                        om.MDistance(
                            value[0][0], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1),
                        om.MDistance(
                            value[0][1], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                elif self._child_type == FloatingPointScalarType.ANGLE:
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(0),
                        om.MAngle(value[0][0], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueFloat(
                        self.plug.child(1),
                        om.MAngle(value[0][1], om.MAngle.uiUnit()).asRadians(),
                    )

        except Exception as e:
            raise TypeError(
                f"Expected either set(x, y) or set([x, y]): {value}"
            ) from e


class Float2AttrOperator(FloatingPointBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "float2"


class Float2Field(FloatingPointBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Float2AttrOperator)
    PLUG_CLS = cast(Type[P], Float2PlugOperator)
