# coding: utf-8

from ..std.at.compound import (
    CompoundAttrOperator,
    CompoundPlugOperator,
    CompoundField,
)
from ..std.at.message import MessageField
from ..std.at.numeric_scalar.bool import BoolField
from ..std.at.numeric_scalar_range.long import LongField


class CameraLayerPlugOperator(
    CompoundPlugOperator["CameraLayerAttrOperator"]
):
    __slots__ = ()
    CHILD_ATTR_NAMES = (
        ("camera", "cam"),
        ("sceneData", "sda"),
        ("active", "act"),
        ("order", "ord"),
        ("clearDepth", "cld"),
    )

    camera = MessageField()
    cam = camera

    sceneData = MessageField()
    sda = sceneData

    active = BoolField()
    act = active

    order = LongField()
    ord = order

    clearDepth = BoolField()
    cld = clearDepth


class CameraLayerAttrOperator(
    CompoundAttrOperator[CameraLayerPlugOperator]
):
    __slots__ = ()

    camera = MessageField()
    cam = camera

    sceneData = MessageField()
    sda = sceneData

    active = BoolField()
    act = active

    order = LongField()
    ord = order

    clearDepth = BoolField()
    cld = clearDepth


class CameraLayerField(
    CompoundField[CameraLayerAttrOperator, CameraLayerPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = CameraLayerAttrOperator
    PLUG_CLS = CameraLayerPlugOperator
