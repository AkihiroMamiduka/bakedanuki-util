# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.camera_set import CameraLayerField


class _GeneratedCameraSet(DG):
    __slots__ = ()

    NODE_TYPE = "cameraSet"

    cameraLayer = CameraLayerField(multi=True)
    cl = cameraLayer
