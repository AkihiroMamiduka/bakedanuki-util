# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.camera_view import (
    CenterOfInterestField,
    EyeField,
    TumblePivotField,
    UpField,
)
from ....attr.define.std.at.scalar.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ....attr.define.std.at.scalar.numeric.bool import BoolField
from ....attr.define.std.at.scalar.numeric.range.double import DoubleField
from ....attr.define.std.at.scalar.unit.range.double_linear import DoubleLinearField
from ....attr.define.std.dt.string import DataStringField


class ViewTypeEnumPlugOperator(EnumPlugOperator):
    __slots__ = ()

    _3D = 0
    _2D_PAN_SLASH_ZOOM = 1


class ViewTypeEnumAttrOperator(EnumAttrOperator):
    __slots__ = ()

    _3D = 0
    _2D_PAN_SLASH_ZOOM = 1

    NAME_MAP = {
        _3D: "3D",
        _2D_PAN_SLASH_ZOOM: "2D Pan/Zoom",
    }


class ViewTypeEnumField(
    EnumField[ViewTypeEnumAttrOperator, ViewTypeEnumPlugOperator]
):
    __slots__ = ()

    ATTR_CLS = ViewTypeEnumAttrOperator
    PLUG_CLS = ViewTypeEnumPlugOperator


class GeneratedCameraView(DG):
    __slots__ = ()

    NODE_TYPE = "cameraView"

    eye = EyeField(default_value=(60.0, 45.0, 60.0))
    e = eye
    eyeX = eye.eyeX
    ex = eyeX
    eyeY = eye.eyeY
    ey = eyeY
    eyeZ = eye.eyeZ
    ez = eyeZ

    centerOfInterest = CenterOfInterestField(default_value=(0.0, 0.0, 0.0))
    coi = centerOfInterest
    centerOfInterestX = centerOfInterest.centerOfInterestX
    cx = centerOfInterestX
    centerOfInterestY = centerOfInterest.centerOfInterestY
    cy = centerOfInterestY
    centerOfInterestZ = centerOfInterest.centerOfInterestZ
    cz = centerOfInterestZ

    up = UpField(default_value=(0.0, 1.0, 0.0))
    u = up
    upX = up.upX
    ux = upX
    upY = up.upY
    uy = upY
    upZ = up.upZ
    uz = upZ

    tumblePivot = TumblePivotField(default_value=(0.0, 0.0, 0.0))
    tp = tumblePivot
    tumblePivotX = tumblePivot.tumblePivotX
    tpx = tumblePivotX
    tumblePivotY = tumblePivot.tumblePivotY
    tpy = tumblePivotY
    tumblePivotZ = tumblePivot.tumblePivotZ
    tpz = tumblePivotZ

    horizontalAperture = DoubleField(default_value=1.4173200000000001)
    ha = horizontalAperture

    verticalAperture = DoubleField(default_value=0.94488)
    va = verticalAperture

    focalLength = DoubleField(default_value=35.0)
    fl = focalLength

    orthographicWidth = DoubleLinearField(default_value=10.0)
    ow = orthographicWidth

    orthographic = BoolField(default_value=False)
    o = orthographic

    panZoomEnabled = BoolField(default_value=False)
    pze = panZoomEnabled

    renderPanZoom = BoolField(default_value=False)
    rpz = renderPanZoom

    horizontalPan = DoubleField(default_value=0.0)
    hpn = horizontalPan

    verticalPan = DoubleField(default_value=0.0)
    vpn = verticalPan

    zoom = DoubleField(default_value=1.0, min_value=1e-10)
    zom = zoom

    viewType = ViewTypeEnumField(default_value=0)
    typ = viewType

    description = DataStringField()
    d = description
