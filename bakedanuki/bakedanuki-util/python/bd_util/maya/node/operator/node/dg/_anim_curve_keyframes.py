"""Maya バージョン間で共用するアニメーションカーブ操作。"""

from maya.api import OpenMaya as om

from ....modifier import ModifierManager
from ...attr.keyframe import CurveKeyframeManager


class AnimCurveKeyframes:
    """カーブ自身のキーフレーム操作を公開する共通クラス。"""

    __slots__ = ()

    m_obj: om.MObject
    _modifier_manager: ModifierManager

    @property
    def keyframe(self) -> CurveKeyframeManager:
        """同じ ModifierManager を使うキーフレーム操作を返す。"""
        return CurveKeyframeManager(
            self.m_obj, modifier_manager=self._modifier_manager
        )
