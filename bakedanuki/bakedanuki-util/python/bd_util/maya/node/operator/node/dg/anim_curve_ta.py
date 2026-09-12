# coding: utf-8
from ._generated.anim_curve_ta import GeneratedAnimCurveTA
from ._anim_curve_keyframes import AnimCurveKeyframes


class AnimCurveTA(GeneratedAnimCurveTA, AnimCurveKeyframes):
    __slots__ = ()

    NODE_TYPE = "animCurveTA"
