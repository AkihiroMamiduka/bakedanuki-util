# coding: utf-8
from typing import Self

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from ._generated.joint import GeneratedJoint


class Joint(GeneratedJoint):
    __slots__ = ()

    NODE_TYPE = "joint"

    def rotation_to_joint_orient(self) -> Self:
        """現在の回転を ``jointOrient`` へ集約して DG modifier に積む。"""
        self._validate_rotation_plugs()
        rotation = self._quaternion_to_rotation(
            self._combined_rotation(),
            om.MEulerRotation.kXYZ,
        )
        self.rotateAxis.set(self._ZERO_ROTATION)
        self.rotate.set(self._ZERO_ROTATION)
        self.jointOrient.set(rotation)
        return self

    def _combined_rotation(self) -> om.MQuaternion:
        return super()._combined_rotation() * oma.MFnIkJoint(
            self.m_obj
        ).orientation(asQuaternion=True)

    def _rotation_m_plugs(self) -> tuple[om.MPlug, ...]:
        return (*super()._rotation_m_plugs(), self.jointOrient.plug)

    def _set_rotation_values(
        self,
        *,
        rotate_axis: tuple[float, float, float],
        rotate: tuple[float, float, float],
    ) -> None:
        super()._set_rotation_values(
            rotate_axis=rotate_axis,
            rotate=rotate,
        )
        self.jointOrient.set(self._ZERO_ROTATION)
