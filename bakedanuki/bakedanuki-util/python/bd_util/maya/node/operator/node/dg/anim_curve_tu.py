# coding: utf-8
from ._generated.anim_curve_tu import GeneratedAnimCurveTU
from ._anim_curve_keyframes import AnimCurveKeyframes


class AnimCurveTU(GeneratedAnimCurveTU, AnimCurveKeyframes):
    __slots__ = ()

    NODE_TYPE = "animCurveTU"
