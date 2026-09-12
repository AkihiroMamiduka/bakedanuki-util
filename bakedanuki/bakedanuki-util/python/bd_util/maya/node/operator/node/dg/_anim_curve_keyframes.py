"""Time-input curve behavior shared by every version's generated schema."""

from maya.api import OpenMaya as om

from ....modifier import ModifierManager
from ...attr.keyframe import CurveKeyframeManager


class AnimCurveKeyframes:
    __slots__ = ()

    m_obj: om.MObject
    _modifier_manager: ModifierManager

    @property
    def keyframe(self) -> CurveKeyframeManager:
        """このカーブ自身を、同じModifierManagerで操作する。"""
        return CurveKeyframeManager(
            self.m_obj, modifier_manager=self._modifier_manager
        )
