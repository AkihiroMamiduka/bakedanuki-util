# coding: utf-8
from typing import ClassVar, Self

from maya.api import OpenMaya as om

from .._core import DAG
from ._generated.transform import GeneratedTransform

_RotationValue = tuple[float, float, float]


class Transform(GeneratedTransform):
    __slots__ = ()

    NODE_TYPE = "transform"
    _ZERO_ROTATION: ClassVar[_RotationValue] = (0.0, 0.0, 0.0)

    @staticmethod
    def _quaternion_to_rotation(
        quaternion: om.MQuaternion,
        order: int,
    ) -> _RotationValue:
        euler = quaternion.asEulerRotation()
        euler.reorderIt(order)
        return (
            om.MAngle(euler.x, om.MAngle.kRadians).asDegrees(),
            om.MAngle(euler.y, om.MAngle.kRadians).asDegrees(),
            om.MAngle(euler.z, om.MAngle.kRadians).asDegrees(),
        )

    def rotation_to_rotate(self) -> Self:
        """現在の回転を ``rotate`` へ集約して DG modifier に積む。"""
        self._validate_rotation_plugs()
        rotation = self._quaternion_to_rotation(
            self._combined_rotation(),
            self.rotateOrder.get(),
        )
        self._set_rotation_values(
            rotate_axis=self._ZERO_ROTATION,
            rotate=rotation,
        )
        return self

    def rotation_to_rotate_axis(self) -> Self:
        """現在の回転を ``rotateAxis`` へ集約して DG modifier に積む。"""
        self._validate_rotation_plugs()
        rotation = self._quaternion_to_rotation(
            self._combined_rotation(),
            om.MEulerRotation.kXYZ,
        )
        self._set_rotation_values(
            rotate_axis=rotation,
            rotate=self._ZERO_ROTATION,
        )
        return self

    def _combined_rotation(self) -> om.MQuaternion:
        fn_transform = om.MFnTransform(self.m_obj)
        return fn_transform.rotateOrientation(
            om.MSpace.kTransform
        ) * fn_transform.rotation(asQuaternion=True)

    def _rotation_m_plugs(self) -> tuple[om.MPlug, ...]:
        return self.rotateAxis.plug, self.rotate.plug

    def _validate_rotation_plugs(self) -> None:
        blocked_plug_names: list[str] = []
        for plug in self._rotation_m_plugs():
            blocked_children = [
                plug.child(index).name()
                for index in range(plug.numChildren())
                if plug.child(index).isDestination
                or plug.child(index).isFreeToChange() != om.MPlug.kFreeToChange
            ]
            if blocked_children:
                blocked_plug_names.extend(blocked_children)
            elif (
                plug.isDestination
                or plug.isFreeToChange() != om.MPlug.kFreeToChange
            ):
                blocked_plug_names.append(plug.name())

        if blocked_plug_names:
            raise RuntimeError(
                "Rotation plugs must be unlocked and have no incoming "
                "connections: " + ", ".join(blocked_plug_names)
            )

    def _set_rotation_values(
        self,
        *,
        rotate_axis: _RotationValue,
        rotate: _RotationValue,
    ) -> None:
        self.rotateAxis.set(rotate_axis)
        self.rotate.set(rotate)

    def set_parent(
        self,
        parent: DAG,
        *,
        preserve_world_transform: bool = False,
    ) -> Self:
        """
        親変更を積み、必要に応じて現在の world transform を維持する。
        """
        if not preserve_world_transform:
            return super().set_parent(parent)

        self._validate_set_parent(parent)
        self._dag_mod.pythonCommandToExecute(
            self._parent_python_command(parent)
        )
        self.modifier_manager.record_pending_dag_parent(
            self.m_obj,
            parent.m_obj,
        )
        return self

    def set_parent_to_world(
        self,
        *,
        preserve_world_transform: bool = False,
    ) -> Self:
        """ワールド直下への親変更を DAG modifier に積む。"""
        if self.is_instanced:
            raise RuntimeError(
                "set_parent_to_world is not supported for an instanced "
                f"DAG node: {self.name}"
            )

        if preserve_world_transform:
            self._dag_mod.pythonCommandToExecute(
                self._parent_python_command(None)
            )
        else:
            self._dag_mod.reparentNode(self.m_obj)
        self.modifier_manager.record_pending_dag_parent(
            self.m_obj,
            om.MObject.kNullObj,
        )
        return self

    def _parent_python_command(self, parent: DAG | None) -> str:
        """undo 可能な absolute parent command を UUID 指定で返す。"""
        child_uuid = om.MFnDependencyNode(self.m_obj).uuid().asString()
        command = (
            "from maya import cmds as _cmds; "
            f"_child = _cmds.ls({child_uuid!r}, long=True)[0]; "
        )
        if parent is None:
            return command + (
                "_cmds.parent(_child, world=True, absolute=True)"
            )

        parent_uuid = om.MFnDependencyNode(parent.m_obj).uuid().asString()
        return command + (
            f"_parent = _cmds.ls({parent_uuid!r}, long=True)[0]; "
            "_cmds.parent(_child, _parent, absolute=True)"
        )
