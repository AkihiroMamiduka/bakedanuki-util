# coding: utf-8
from __future__ import annotations

from struct import pack, unpack
from typing import cast

from maya.api import OpenMaya as om

from ....ui import FloatPresentation
from ....ui.binding.float._validation import require_float
from .float_plug_resolver import float_plug_kind

_DISTANCE_SUFFIXES = {
    om.MDistance.kMillimeters: " mm",
    om.MDistance.kCentimeters: " cm",
    om.MDistance.kMeters: " m",
    om.MDistance.kKilometers: " km",
    om.MDistance.kInches: " in",
    om.MDistance.kFeet: " ft",
    om.MDistance.kYards: " yd",
    om.MDistance.kMiles: " mi",
}
_ANGLE_SUFFIXES = {
    om.MAngle.kDegrees: " deg",
    om.MAngle.kRadians: " rad",
    om.MAngle.kAngMinutes: " arcmin",
    om.MAngle.kAngSeconds: " arcsec",
}


class FloatPlugValue:
    """Maya内部単位・既存APIの公開単位・画面単位の変換境界。"""

    def __init__(self, plug: om.MPlug) -> None:
        """plugの単位種別と格納精度を保持する。"""
        self.plug = plug
        self.kind = float_plug_kind(plug)
        self._is_float32 = self.kind == "number" and (
            om.MFnNumericAttribute(plug.attribute()).numericType()
            == om.MFnNumericData.kFloat
        )

    def read(self) -> float:
        """Mayaの実値をcm・degree・単位なしの公開値へ変換する。"""
        if self.kind == "distance":
            value = self.plug.asMDistance().asCentimeters()
        elif self.kind == "angle":
            value = self.plug.asMAngle().asDegrees()
        else:
            value = self.plug.asDouble()
        return require_float(value)

    def to_ui(self, value: float) -> float:
        """公開値をsetAttrが受け取る現在単位と格納精度へ変換する。"""
        value = require_float(value)
        original_value = value
        if self.kind == "distance":
            value = om.MDistance(value, om.MDistance.kCentimeters).asUnits(
                om.MDistance.uiUnit()
            )
        elif self.kind == "angle":
            value = om.MAngle(value, om.MAngle.kDegrees).asUnits(
                om.MAngle.uiUnit()
            )
        elif self._is_float32:
            try:
                value = cast(float, unpack("f", pack("f", value))[0])
            except OverflowError as error:
                raise ValueError(
                    "valueはMaya floatの範囲を超えています"
                ) from error
        if value == 0.0 and original_value != 0.0:
            raise ValueError("valueはMayaの書き込み単位では小さすぎます")
        return require_float(value)

    def matches(self, value: float) -> bool:
        """書き込みで得られる格納値と比較し、Python値の精度を保持する。"""
        ui_value = self.to_ui(value)
        if self.kind == "distance":
            expected = om.MDistance(
                ui_value, om.MDistance.uiUnit()
            ).asCentimeters()
            actual = self.plug.asMDistance().asCentimeters()
        elif self.kind == "angle":
            expected = om.MAngle(ui_value, om.MAngle.uiUnit()).asRadians()
            actual = self.plug.asMAngle().asRadians()
        else:
            expected = ui_value
            actual = self.plug.asDouble()
        return require_float(actual) == require_float(expected)

    @property
    def presentation(self) -> FloatPresentation:
        """現在の表示単位と公開単位でのMaya属性範囲を返す。"""
        if self.kind == "number":
            attribute = om.MFnNumericAttribute(self.plug.attribute())
            minimum = (
                require_float(attribute.getMin())
                if attribute.hasMin()
                else None
            )
            maximum = (
                require_float(attribute.getMax())
                if attribute.hasMax()
                else None
            )
            return FloatPresentation(minimum=minimum, maximum=maximum)
        unit_attribute = om.MFnUnitAttribute(self.plug.attribute())
        minimum = (
            self._unit_bound(unit_attribute.getMin())
            if unit_attribute.hasMin()
            else None
        )
        maximum = (
            self._unit_bound(unit_attribute.getMax())
            if unit_attribute.hasMax()
            else None
        )
        suffix = (
            _DISTANCE_SUFFIXES[om.MDistance.uiUnit()]
            if self.kind == "distance"
            else _ANGLE_SUFFIXES[om.MAngle.uiUnit()]
        )
        return FloatPresentation(self.to_ui(1.0), suffix, minimum, maximum)

    def _unit_bound(self, value: object) -> float:
        """距離・角度属性の境界値を公開単位へ変換する。"""
        if self.kind == "distance":
            return cast(om.MDistance, value).asCentimeters()
        return cast(om.MAngle, value).asDegrees()
