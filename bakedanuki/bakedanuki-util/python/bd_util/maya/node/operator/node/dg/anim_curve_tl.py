# coding: utf-8
from ._generated.anim_curve_tl import GeneratedAnimCurveTL
from ._anim_curve_keyframes import AnimCurveKeyframes


class AnimCurveTL(GeneratedAnimCurveTL, AnimCurveKeyframes):
    __slots__ = ()

    NODE_TYPE = "animCurveTL"
