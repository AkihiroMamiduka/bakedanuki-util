# coding: utf-8
from collections.abc import Sequence
from typing import overload, Self

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

    @overload
    def set_joint_orient_with_rotate(
        self,
        value: Sequence[float],
        /,
    ) -> Self: ...

    @overload
    def set_joint_orient_with_rotate(
        self,
        value: float,
        y: float,
        z: float,
        /,
    ) -> Self: ...

    def set_joint_orient_with_rotate(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
    ) -> Self:
        """姿勢を維持して ``jointOrient`` を設定し、差分を ``rotate`` で吸収する。"""
        joint_orient = self._normalize_rotation_value(
            value,
            values,
            "set_joint_orient_with_rotate",
        )
        self._validate_rotation_m_plugs(
            (self.jointOrient.plug, self.rotate.plug)
        )
        rotate_order = self.rotateOrder.get()
        current_rotate = self.rotate.get().as_tuple()
        current_joint_orient = self.jointOrient.get().as_tuple()
        compensated_rotate = self._quaternion_to_rotation(
            self._rotation_to_quaternion(current_rotate, rotate_order)
            * self._rotation_to_quaternion(
                current_joint_orient,
                om.MEulerRotation.kXYZ,
            )
            * self._rotation_to_quaternion(
                joint_orient,
                om.MEulerRotation.kXYZ,
            ).inverse(),
            rotate_order,
            current_rotate,
        )
        self.jointOrient.set(joint_orient)
        self.rotate.set(compensated_rotate)
        return self

    @overload
    def set_rotate_with_joint_orient(
        self,
        value: Sequence[float],
        /,
    ) -> Self: ...

    @overload
    def set_rotate_with_joint_orient(
        self,
        value: float,
        y: float,
        z: float,
        /,
    ) -> Self: ...

    def set_rotate_with_joint_orient(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
    ) -> Self:
        """姿勢を維持して ``rotate`` を設定し、差分を ``jointOrient`` で吸収する。"""
        rotate = self._normalize_rotation_value(
            value,
            values,
            "set_rotate_with_joint_orient",
        )
        self._validate_rotation_m_plugs(
            (self.jointOrient.plug, self.rotate.plug)
        )
        rotate_order = self.rotateOrder.get()
        current_rotate = self.rotate.get().as_tuple()
        current_joint_orient = self.jointOrient.get().as_tuple()
        compensated_joint_orient = self._quaternion_to_rotation(
            self._rotation_to_quaternion(rotate, rotate_order).inverse()
            * self._rotation_to_quaternion(current_rotate, rotate_order)
            * self._rotation_to_quaternion(
                current_joint_orient,
                om.MEulerRotation.kXYZ,
            ),
            om.MEulerRotation.kXYZ,
            current_joint_orient,
        )
        self.rotate.set(rotate)
        self.jointOrient.set(compensated_joint_orient)
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
