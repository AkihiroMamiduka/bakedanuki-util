# coding: utf-8
from collections.abc import Sequence
from typing import ClassVar, overload, Self

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
        closest_to: _RotationValue | None = None,
    ) -> _RotationValue:
        euler = quaternion.asEulerRotation()
        euler.reorderIt(order)
        if closest_to is not None:
            euler = euler.closestSolution(
                Transform._rotation_to_euler(closest_to, order)
            )
        return (
            om.MAngle(euler.x, om.MAngle.kRadians).asDegrees(),
            om.MAngle(euler.y, om.MAngle.kRadians).asDegrees(),
            om.MAngle(euler.z, om.MAngle.kRadians).asDegrees(),
        )

    @staticmethod
    def _rotation_to_euler(
        rotation: _RotationValue,
        order: int,
    ) -> om.MEulerRotation:
        return om.MEulerRotation(
            om.MAngle(rotation[0], om.MAngle.kDegrees).asRadians(),
            om.MAngle(rotation[1], om.MAngle.kDegrees).asRadians(),
            om.MAngle(rotation[2], om.MAngle.kDegrees).asRadians(),
            order,
        )

    @classmethod
    def _rotation_to_quaternion(
        cls,
        rotation: _RotationValue,
        order: int,
    ) -> om.MQuaternion:
        return cls._rotation_to_euler(rotation, order).asQuaternion()

    @staticmethod
    def _normalize_rotation_value(
        value: float | Sequence[float],
        values: tuple[float, ...],
        method_name: str,
    ) -> _RotationValue:
        normalized_values: tuple[object, ...] = (value, *values)
        if len(normalized_values) == 1:
            first_value = normalized_values[0]
            if isinstance(first_value, Sequence) and not isinstance(
                first_value, (str, bytes)
            ):
                normalized_values = tuple(first_value)

        if len(normalized_values) != 3 or any(
            isinstance(component, Sequence)
            and not isinstance(component, (str, bytes))
            for component in normalized_values
        ):
            raise TypeError(
                f"Expected either {method_name}(x, y, z) or "
                f"{method_name}([x, y, z]): {normalized_values}"
            )

        try:
            x, y, z = (float(component) for component in normalized_values)
        except (TypeError, ValueError) as error:
            raise TypeError(
                f"Expected either {method_name}(x, y, z) or "
                f"{method_name}([x, y, z]): {normalized_values}"
            ) from error
        return x, y, z

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

    @overload
    def set_rotate_axis_with_rotate(
        self,
        value: Sequence[float],
        /,
    ) -> Self: ...

    @overload
    def set_rotate_axis_with_rotate(
        self,
        value: float,
        y: float,
        z: float,
        /,
    ) -> Self: ...

    def set_rotate_axis_with_rotate(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
    ) -> Self:
        """姿勢を維持して ``rotateAxis`` を設定し、差分を ``rotate`` で吸収する。"""
        rotate_axis = self._normalize_rotation_value(
            value,
            values,
            "set_rotate_axis_with_rotate",
        )
        self._validate_rotation_m_plugs(
            (self.rotateAxis.plug, self.rotate.plug)
        )
        rotate_order = self.rotateOrder.get()
        current_rotate_axis = self.rotateAxis.get().as_tuple()
        current_rotate = self.rotate.get().as_tuple()
        compensated_rotate = self._quaternion_to_rotation(
            self._rotation_to_quaternion(
                rotate_axis,
                om.MEulerRotation.kXYZ,
            ).inverse()
            * self._rotation_to_quaternion(
                current_rotate_axis,
                om.MEulerRotation.kXYZ,
            )
            * self._rotation_to_quaternion(current_rotate, rotate_order),
            rotate_order,
            current_rotate,
        )
        self.rotateAxis.set(rotate_axis)
        self.rotate.set(compensated_rotate)
        return self

    @overload
    def set_rotate_with_rotate_axis(
        self,
        value: Sequence[float],
        /,
    ) -> Self: ...

    @overload
    def set_rotate_with_rotate_axis(
        self,
        value: float,
        y: float,
        z: float,
        /,
    ) -> Self: ...

    def set_rotate_with_rotate_axis(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
    ) -> Self:
        """姿勢を維持して ``rotate`` を設定し、差分を ``rotateAxis`` で吸収する。"""
        rotate = self._normalize_rotation_value(
            value,
            values,
            "set_rotate_with_rotate_axis",
        )
        self._validate_rotation_m_plugs(
            (self.rotateAxis.plug, self.rotate.plug)
        )
        rotate_order = self.rotateOrder.get()
        current_rotate_axis = self.rotateAxis.get().as_tuple()
        current_rotate = self.rotate.get().as_tuple()
        compensated_rotate_axis = self._quaternion_to_rotation(
            self._rotation_to_quaternion(
                current_rotate_axis,
                om.MEulerRotation.kXYZ,
            )
            * self._rotation_to_quaternion(current_rotate, rotate_order)
            * self._rotation_to_quaternion(rotate, rotate_order).inverse(),
            om.MEulerRotation.kXYZ,
            current_rotate_axis,
        )
        self.rotate.set(rotate)
        self.rotateAxis.set(compensated_rotate_axis)
        return self

    def _combined_rotation(self) -> om.MQuaternion:
        fn_transform = om.MFnTransform(self.m_obj)
        return fn_transform.rotateOrientation(
            om.MSpace.kTransform
        ) * fn_transform.rotation(asQuaternion=True)

    def _rotation_m_plugs(self) -> tuple[om.MPlug, ...]:
        return self.rotateAxis.plug, self.rotate.plug

    def _validate_rotation_plugs(self) -> None:
        self._validate_rotation_m_plugs(self._rotation_m_plugs())

    @staticmethod
    def _validate_rotation_m_plugs(plugs: tuple[om.MPlug, ...]) -> None:
        blocked_plug_names: list[str] = []
        for plug in plugs:
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
