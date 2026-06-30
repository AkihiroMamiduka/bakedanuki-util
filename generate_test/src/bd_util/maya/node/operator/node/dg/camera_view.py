# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.camera_view import (
    CenterOfInterestField,
    EyeField,
    TumblePivotField,
    UpField,
)
from ...attr.define.std.at.enum import (
    EnumAttrOperator,
    EnumPlugOperator,
    EnumField,
)
from ...attr.define.std.at.numeric_scalar.bool import BoolField
from ...attr.define.std.at.numeric_scalar_range.double import DoubleField
from ...attr.define.std.at.unit_scalar_range.double_linear import DoubleLinearField
from ...attr.define.std.dt.string import DataStringField


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


class CameraView(DG):
    __slots__ = ()

    NODE_TYPE = "cameraView"

    eye = EyeField()
    e = eye
    eyeX = eye.eyeX
    ex = eyeX
    eyeY = eye.eyeY
    ey = eyeY
    eyeZ = eye.eyeZ
    ez = eyeZ

    centerOfInterest = CenterOfInterestField()
    coi = centerOfInterest
    centerOfInterestX = centerOfInterest.centerOfInterestX
    cx = centerOfInterestX
    centerOfInterestY = centerOfInterest.centerOfInterestY
    cy = centerOfInterestY
    centerOfInterestZ = centerOfInterest.centerOfInterestZ
    cz = centerOfInterestZ

    up = UpField()
    u = up
    upX = up.upX
    ux = upX
    upY = up.upY
    uy = upY
    upZ = up.upZ
    uz = upZ

    tumblePivot = TumblePivotField()
    tp = tumblePivot
    tumblePivotX = tumblePivot.tumblePivotX
    tpx = tumblePivotX
    tumblePivotY = tumblePivot.tumblePivotY
    tpy = tumblePivotY
    tumblePivotZ = tumblePivot.tumblePivotZ
    tpz = tumblePivotZ

    horizontalAperture = DoubleField()
    ha = horizontalAperture

    verticalAperture = DoubleField()
    va = verticalAperture

    focalLength = DoubleField()
    fl = focalLength

    orthographicWidth = DoubleLinearField()
    ow = orthographicWidth

    orthographic = BoolField()
    o = orthographic

    panZoomEnabled = BoolField()
    pze = panZoomEnabled

    renderPanZoom = BoolField()
    rpz = renderPanZoom

    horizontalPan = DoubleField()
    hpn = horizontalPan

    verticalPan = DoubleField()
    vpn = verticalPan

    zoom = DoubleField()
    zom = zoom

    viewType = ViewTypeEnumField()
    typ = viewType

    description = DataStringField()
    d = description
