# coding: utf-8
from ._core import DG
from ...attr.define.node_attr.pose_interpolator_manager import PoseInterpolatorDirectoryField
from ...attr.define.std.at.numeric_scalar_range.long import LongField


class PoseInterpolatorManager(DG):
    __slots__ = ()

    NODE_TYPE = "poseInterpolatorManager"

    poseInterpolatorDirectory = PoseInterpolatorDirectoryField(multi=True)
    tpdt = poseInterpolatorDirectory

    poseInterpolatorParent = LongField(multi=True)
    tppr = poseInterpolatorParent
