# coding: utf-8
from .._core import DG
from ....attr.define.node_attr.pose_interpolator_manager import PoseInterpolatorDirectoryField
from ....attr.define.std.at.scalar.numeric.range.long import LongField


class GeneratedPoseInterpolatorManager(DG):
    __slots__ = ()

    NODE_TYPE = "poseInterpolatorManager"

    poseInterpolatorDirectory = PoseInterpolatorDirectoryField(multi=True)
    tpdt = poseInterpolatorDirectory

    poseInterpolatorParent = LongField(multi=True, default_value=0)
    tppr = poseInterpolatorParent
