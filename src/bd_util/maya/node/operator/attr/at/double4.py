# coding: utf-8
from typing import TypeVar, Type, cast

# maya
from maya.api import OpenMaya as om

# self
from .compound_base._floating_point_compound import (
    FloatingPointBaseAttrOperator,
    FloatingPointBasePlugOperator,
    FloatingPointBaseField,
    FloatingPointScalarType,
)

A = TypeVar("A", bound="FloatingPointBaseAttrOperator")

P = TypeVar("P", bound="FloatingPointBasePlugOperator")


class Double4PlugOperator(FloatingPointBasePlugOperator[A]):
    __slots__ = ()

    # get
    def get(self) -> list[float]:
        # 型を推測
        self._analyze_child_type()

        # 型に合わせて、値を取得
        if self._child_type == FloatingPointScalarType.Numeric:
            value = [
                self.plug.child(0).asDouble(),
                self.plug.child(1).asDouble(),
                self.plug.child(2).asDouble(),
                self.plug.child(3).asDouble(),
            ]
        elif self._child_type == FloatingPointScalarType.DISTANCE:
            value = [
                self.plug.child(0).asMDistance().asCentimeters(),
                self.plug.child(1).asMDistance().asCentimeters(),
                self.plug.child(2).asMDistance().asCentimeters(),
                self.plug.child(3).asMDistance().asCentimeters(),
            ]
        elif self._child_type == FloatingPointScalarType.ANGLE:
            value = [
                self.plug.child(0).asMAngle().asDegrees(),
                self.plug.child(1).asMAngle().asDegrees(),
                self.plug.child(2).asMAngle().asDegrees(),
                self.plug.child(3).asMAngle().asDegrees(),
            ]

        # 戻り値
        return value

    # set
    def set(self, *value: float | list[float]):
        # 型を推測
        self._analyze_child_type()

        try:
            # set(x, y, z, w)
            try:
                # 型に合わせて、値をセット
                if self._child_type == FloatingPointScalarType.Numeric:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0), value[0]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1), value[1]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2), value[2]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3), value[3]
                    )
                elif self._child_type == FloatingPointScalarType.DISTANCE:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0),
                        om.MDistance(
                            value[0],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1),
                        om.MDistance(
                            value[1],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2),
                        om.MDistance(
                            value[2],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3),
                        om.MDistance(
                            value[3],
                            om.MDistance.uiUnit(),
                        ).asCentimeters(),
                    )
                elif self._child_type == FloatingPointScalarType.ANGLE:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0),
                        om.MAngle(value[0], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1),
                        om.MAngle(value[1], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2),
                        om.MAngle(value[2], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3),
                        om.MAngle(value[3], om.MAngle.uiUnit()).asRadians(),
                    )
            # set([x, y, z, w])
            except Exception:
                # 型に合わせて、値をセット
                if self._child_type == FloatingPointScalarType.Numeric:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0), value[0][0]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1), value[0][1]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2), value[0][2]
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3), value[0][3]
                    )
                elif self._child_type == FloatingPointScalarType.DISTANCE:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0),
                        om.MDistance(
                            value[0][0], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1),
                        om.MDistance(
                            value[0][1], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2),
                        om.MDistance(
                            value[0][2], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3),
                        om.MDistance(
                            value[0][3], om.MDistance.uiUnit()
                        ).asCentimeters(),
                    )
                elif self._child_type == FloatingPointScalarType.ANGLE:
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(0),
                        om.MAngle(value[0][0], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(1),
                        om.MAngle(value[0][1], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(2),
                        om.MAngle(value[0][2], om.MAngle.uiUnit()).asRadians(),
                    )
                    self._node._dg_mod.newPlugValueDouble(
                        self.plug.child(3),
                        om.MAngle(value[0][3], om.MAngle.uiUnit()).asRadians(),
                    )
        except Exception as e:
            raise TypeError(
                "Expected either {} or {}: {}".format(
                    "set(x, y, z, w)",
                    "set([x, y, z, w])",
                    value,
                )
            ) from e


class Double4AttrOperator(FloatingPointBaseAttrOperator[P]):
    __slots__ = ()

    ATTR_TYPE = "double4"


class Double4Field(FloatingPointBaseField[A, P]):
    __slots__ = ()

    ATTR_CLS = cast(Type[A], Double4AttrOperator)
    PLUG_CLS = cast(Type[P], Double4PlugOperator)
