# coding: utf-8
import builtins
import math
from collections.abc import Sequence
from typing import cast, ClassVar, Literal, overload, Protocol, Self

from maya.api import OpenMaya as om

from .._core import DAG
from ._generated.transform import GeneratedTransform

_RotationValue = tuple[float, float, float]
_Vector3Value = tuple[float, float, float]
_PositionAxes = Literal["x", "y", "z", "xy", "xz", "yz", "xyz"]
_PositionSpace = Literal["world", "local", "object"]
JointChildCompensationAttr = Literal["rotate", "jointOrient"]


class ScalarPlugProtocol(Protocol):
    @property
    def plug(self) -> om.MPlug: ...

    def set(self, value: float) -> None: ...


ValueChange = tuple[ScalarPlugProtocol, float]

_POSITION_AXES = frozenset(("x", "y", "z", "xy", "xz", "yz", "xyz"))
_POSITION_AXIS_INDEX = {"x": 0, "y": 1, "z": 2}
_POSITION_SPACES = frozenset(("world", "local", "object"))


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
            closest_to_euler = Transform._rotation_to_euler(
                closest_to,
                order,
            )
            closest_euler = euler.closestSolution(closest_to_euler)
            if not quaternion.isEquivalent(
                closest_euler.asQuaternion(),
                1.0e-10,
            ):
                closest_euler = euler.closestCut(closest_to_euler)
            if quaternion.isEquivalent(
                closest_euler.asQuaternion(),
                1.0e-10,
            ):
                euler = closest_euler
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
    def _normalize_vector3_value(
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

        scalar_values = cast(tuple[float, ...], normalized_values)
        try:
            x, y, z = (float(component) for component in scalar_values)
        except (TypeError, ValueError) as error:
            raise TypeError(
                f"Expected either {method_name}(x, y, z) or "
                f"{method_name}([x, y, z]): {normalized_values}"
            ) from error
        return x, y, z

    @staticmethod
    def _rounded_values(
        values: _Vector3Value,
        ndigits: int,
    ) -> _Vector3Value:
        return cast(
            _Vector3Value,
            tuple(builtins.round(value, ndigits) for value in values),
        )

    @staticmethod
    def _require_compensate_children(value: object) -> bool:
        if not isinstance(value, bool):
            raise TypeError(
                "compensate_children must be bool; "
                f"got {type(value).__name__}"
            )
        return value

    @staticmethod
    def _require_compensate_child_translate(value: object) -> bool:
        if not isinstance(value, bool):
            raise TypeError(
                "compensate_child_translate must be bool; "
                f"got {type(value).__name__}"
            )
        return value

    @staticmethod
    def _require_joint_child_compensation_attr(
        value: object,
    ) -> JointChildCompensationAttr:
        if not isinstance(value, str):
            raise TypeError(
                "joint_child_compensation_attr must be str; "
                f"got {type(value).__name__}"
            )
        if value not in ("rotate", "jointOrient"):
            raise ValueError(
                "joint_child_compensation_attr must be 'rotate' or "
                f"'jointOrient'; got {value!r}"
            )
        return value

    def _require_rotation_child_compensation_options(
        self,
        compensate_children: object,
        compensate_child_translate: object,
        joint_child_compensation_attr: object,
    ) -> tuple[bool, bool, JointChildCompensationAttr]:
        validated_compensate_children = self._require_compensate_children(
            compensate_children
        )
        validated_compensate_child_translate = (
            self._require_compensate_child_translate(
                compensate_child_translate
            )
        )
        validated_joint_child_compensation_attr = (
            self._require_joint_child_compensation_attr(
                joint_child_compensation_attr
            )
        )
        if (
            validated_compensate_child_translate
            and not validated_compensate_children
        ):
            raise ValueError(
                "compensate_child_translate=True requires "
                "compensate_children=True"
            )
        return (
            validated_compensate_children,
            validated_compensate_child_translate,
            validated_joint_child_compensation_attr,
        )

    @staticmethod
    def _value_changes(
        plugs: tuple[
            ScalarPlugProtocol,
            ScalarPlugProtocol,
            ScalarPlugProtocol,
        ],
        current_values: _Vector3Value,
        target_values: _Vector3Value,
        *,
        use_tolerance: bool = False,
    ) -> tuple[ValueChange, ...]:
        changes: list[ValueChange] = []
        for plug, current_value, target_value in zip(
            plugs,
            current_values,
            target_values,
        ):
            is_unchanged = (
                math.isclose(
                    current_value,
                    target_value,
                    rel_tol=1.0e-12,
                    abs_tol=1.0e-12,
                )
                if use_tolerance
                else current_value == target_value
            )
            if not is_unchanged:
                changes.append((plug, target_value))
        return tuple(changes)

    def _translate_value_plugs(
        self,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        return (
            cast(ScalarPlugProtocol, self.translateX),
            cast(ScalarPlugProtocol, self.translateY),
            cast(ScalarPlugProtocol, self.translateZ),
        )

    def _rotate_value_plugs(
        self,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        return (
            cast(ScalarPlugProtocol, self.rotateX),
            cast(ScalarPlugProtocol, self.rotateY),
            cast(ScalarPlugProtocol, self.rotateZ),
        )

    def _rotate_axis_value_plugs(
        self,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        return (
            cast(ScalarPlugProtocol, self.rotateAxisX),
            cast(ScalarPlugProtocol, self.rotateAxisY),
            cast(ScalarPlugProtocol, self.rotateAxisZ),
        )

    @staticmethod
    def _queue_value_changes(changes: tuple[ValueChange, ...]) -> None:
        for plug, value in changes:
            plug.set(value)

    def _child_compensation_rotation_values(
        self,
        target_local_rotation: om.MQuaternion,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> _RotationValue:
        current_rotate = self.rotate.get().as_tuple()
        return self._quaternion_to_rotation(
            self._rotate_from_combined_rotation(target_local_rotation),
            self.rotateOrder.get(),
            current_rotate,
        )

    def _child_compensation_rotation_plugs(
        self,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        return self._rotate_value_plugs()

    def _transformation_with_child_compensation_rotation(
        self,
        rotation: _RotationValue,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> om.MTransformationMatrix:
        transformation = om.MFnTransform(self.m_obj).transformation()
        transformation.setRotation(
            self._rotation_to_euler(rotation, self.rotateOrder.get())
        )
        return transformation

    def _transformation_with_rotate_axis(
        self,
        rotate_axis: _RotationValue,
    ) -> om.MTransformationMatrix:
        transformation = om.MFnTransform(self.m_obj).transformation()
        current_rotate_axis = self.rotateAxis.get().as_tuple()
        proxy_rotation = (
            self._rotation_to_quaternion(
                current_rotate_axis,
                om.MEulerRotation.kXYZ,
            ).inverse()
            * self._rotation_to_quaternion(
                rotate_axis,
                om.MEulerRotation.kXYZ,
            )
            * self._rotation_to_quaternion(
                self.rotate.get().as_tuple(),
                self.rotateOrder.get(),
            )
        )
        transformation.setRotation(proxy_rotation)
        return transformation

    def _set_with_child_compensation(
        self,
        *,
        parent_changes: tuple[ValueChange, ...],
        parent_changes_are_rotation: bool,
        target_local_matrix: om.MMatrix,
        compensate_child_rotation: bool,
        compensate_child_translate: bool,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> Self:
        if self.is_instanced:
            raise RuntimeError(
                "Child compensation is not supported for an instanced "
                f"DAG node: {self.name}"
            )

        children = tuple(
            child
            for child in self.children(
                filter_type=Transform,
                include_shapes=False,
            )
            if child.inheritsTransform.get()
        )
        instanced_children = tuple(
            child.name for child in children if child.is_instanced
        )
        if instanced_children:
            raise RuntimeError(
                "Child compensation is not supported for instanced child "
                "DAG nodes: " + ", ".join(instanced_children)
            )

        position_changes: list[ValueChange] = []
        rotation_changes: list[ValueChange] = []
        if parent_changes_are_rotation:
            rotation_changes.extend(parent_changes)
        else:
            position_changes.extend(parent_changes)

        if children:
            target_parent_world_matrix = (
                target_local_matrix
                * self._get_instance_transform_matrix("parentMatrix").matrix
            )
            for child in children:
                child_world_matrix = child._get_instance_transform_matrix(
                    "worldMatrix"
                ).matrix
                effective_parent_matrix = (
                    child.offsetParentMatrix.get().matrix
                    * target_parent_world_matrix
                )
                effective_parent_inverse = effective_parent_matrix.inverse()
                child_transformation = om.MFnTransform(
                    child.m_obj
                ).transformation()

                if compensate_child_rotation:
                    target_local_matrix_for_child = (
                        child_world_matrix * effective_parent_inverse
                    )
                    target_local_rotation = om.MTransformationMatrix(
                        target_local_matrix_for_child
                    ).rotation(asQuaternion=True)
                    target_child_rotation = (
                        child._child_compensation_rotation_values(
                            target_local_rotation,
                            joint_child_compensation_attr,
                        )
                    )
                    current_child_rotation = (
                        child._current_child_compensation_rotation_values(
                            joint_child_compensation_attr
                        )
                    )
                    rotation_changes.extend(
                        self._value_changes(
                            child._child_compensation_rotation_plugs(
                                joint_child_compensation_attr
                            ),
                            current_child_rotation,
                            target_child_rotation,
                            use_tolerance=True,
                        )
                    )
                    child_transformation = (
                        child._transformation_with_child_compensation_rotation(
                            target_child_rotation,
                            joint_child_compensation_attr,
                        )
                    )

                if compensate_child_translate:
                    predicted_world_matrix = (
                        child_transformation.asMatrix()
                        * effective_parent_matrix
                    )
                    world_delta = om.MVector(
                        child_world_matrix[12] - predicted_world_matrix[12],
                        child_world_matrix[13] - predicted_world_matrix[13],
                        child_world_matrix[14] - predicted_world_matrix[14],
                    )
                    translate_delta = world_delta * effective_parent_inverse
                    current_translate = child.translate.get().as_tuple()
                    target_translate = (
                        current_translate[0] + translate_delta.x,
                        current_translate[1] + translate_delta.y,
                        current_translate[2] + translate_delta.z,
                    )
                    position_changes.extend(
                        self._value_changes(
                            child._translate_value_plugs(),
                            current_translate,
                            target_translate,
                            use_tolerance=True,
                        )
                    )

        self._validate_position_m_plugs(
            tuple(plug.plug for plug, _ in position_changes)
        )
        self._validate_rotation_m_plugs(
            tuple(plug.plug for plug, _ in rotation_changes)
        )
        self._queue_value_changes((*position_changes, *rotation_changes))
        return self

    def _current_child_compensation_rotation_values(
        self,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> _RotationValue:
        return self.rotate.get().as_tuple()

    @overload
    def set_translate(
        self,
        value: Sequence[float],
        /,
        *,
        compensate_children: bool = False,
    ) -> Self: ...

    @overload
    def set_translate(
        self,
        value: float,
        y: float,
        z: float,
        /,
        *,
        compensate_children: bool = False,
    ) -> Self: ...

    def set_translate(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
        compensate_children: bool = False,
    ) -> Self:
        """``translate`` を設定し、必要に応じて子のworld位置を補償する。

        Args:
            value: 3成分の値、またはX成分。
            values: ``value`` がX成分の場合のY、Z成分。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world位置を維持するように子の ``translate`` を補償する。

        Notes:
            値の単位はcentimeter。変更は ``ModifierManager.do_it_dg()`` の
            実行時に反映される。
        """
        translate = self._normalize_vector3_value(
            value,
            values,
            "set_translate",
        )
        compensate_children = self._require_compensate_children(
            compensate_children
        )
        current_translate = self.translate.get().as_tuple()
        parent_changes = self._value_changes(
            self._translate_value_plugs(),
            current_translate,
            translate,
        )
        if not parent_changes:
            return self
        if not compensate_children:
            self._validate_position_m_plugs(
                tuple(plug.plug for plug, _ in parent_changes)
            )
            self._queue_value_changes(parent_changes)
            return self

        target_transformation = om.MFnTransform(self.m_obj).transformation()
        target_transformation.setTranslation(
            om.MVector(*translate),
            om.MSpace.kTransform,
        )
        return self._set_with_child_compensation(
            parent_changes=parent_changes,
            parent_changes_are_rotation=False,
            target_local_matrix=target_transformation.asMatrix(),
            compensate_child_rotation=False,
            compensate_child_translate=True,
            joint_child_compensation_attr="rotate",
        )

    def round_translate(
        self,
        ndigits: int = 0,
        *,
        compensate_children: bool = False,
    ) -> Self:
        """``translate`` を丸め、必要に応じて子のworld位置を補償する。

        Args:
            ndigits: 丸める小数点以下の桁数。負の値も指定できる。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world位置を維持するように子の ``translate`` を補償する。

        Notes:
            Python組み込みの ``round()`` と同じ偶数丸めを使用する。
            値の単位はcentimeter。変更は ``ModifierManager.do_it_dg()`` の
            実行時に反映される。
        """
        current_translate = self.translate.get().as_tuple()
        target_translate = self._rounded_values(current_translate, ndigits)
        return self.set_translate(
            target_translate,
            compensate_children=compensate_children,
        )

    @overload
    def set_rotate_axis(
        self,
        value: Sequence[float],
        /,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    @overload
    def set_rotate_axis(
        self,
        value: float,
        y: float,
        z: float,
        /,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    def set_rotate_axis(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """``rotateAxis`` を設定し、必要に応じて子のworld姿勢を補償する。

        Args:
            value: 3成分の値、またはX成分。
            values: ``value`` がX成分の場合のY、Z成分。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            値の単位はdegreeで、回転順は固定XYZ。Transform子は ``rotate``、
            Joint子は既定で ``rotate``を補償する。変更は
            ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        rotate_axis = self._normalize_vector3_value(
            value,
            values,
            "set_rotate_axis",
        )
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        current_rotate_axis = self.rotateAxis.get().as_tuple()
        parent_changes = self._value_changes(
            self._rotate_axis_value_plugs(),
            current_rotate_axis,
            rotate_axis,
        )
        if not parent_changes:
            return self
        if not compensate_children:
            self._validate_rotation_m_plugs(
                tuple(plug.plug for plug, _ in parent_changes)
            )
            self._queue_value_changes(parent_changes)
            return self

        target_transformation = self._transformation_with_rotate_axis(
            rotate_axis
        )
        return self._set_with_child_compensation(
            parent_changes=parent_changes,
            parent_changes_are_rotation=True,
            target_local_matrix=target_transformation.asMatrix(),
            compensate_child_rotation=True,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    def round_rotate_axis(
        self,
        ndigits: int = 0,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """``rotateAxis`` を丸め、必要に応じて子のworld姿勢を補償する。

        Args:
            ndigits: 丸める小数点以下の桁数。負の値も指定できる。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            Python組み込みの ``round()`` と同じ偶数丸めを使用する。
            値の単位はdegreeで、回転順は固定XYZ。Transform子は ``rotate``、
            Joint子は既定で ``rotate``を補償する。変更は
            ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        current_rotate_axis = self.rotateAxis.get().as_tuple()
        target_rotate_axis = self._rounded_values(
            current_rotate_axis,
            ndigits,
        )
        return self.set_rotate_axis(
            target_rotate_axis,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    @overload
    def set_rotate(
        self,
        value: Sequence[float],
        /,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    @overload
    def set_rotate(
        self,
        value: float,
        y: float,
        z: float,
        /,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    def set_rotate(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """``rotate`` を設定し、必要に応じて子のworld姿勢を補償する。

        Args:
            value: 3成分の値、またはX成分。
            values: ``value`` がX成分の場合のY、Z成分。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            値の単位はdegree。Transform子は ``rotate``、Joint子は既定で
            ``rotate``を補償する。変更は ``ModifierManager.do_it_dg()`` の
            実行時に反映される。
        """
        rotate = self._normalize_vector3_value(
            value,
            values,
            "set_rotate",
        )
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        current_rotate = self.rotate.get().as_tuple()
        parent_changes = self._value_changes(
            self._rotate_value_plugs(),
            current_rotate,
            rotate,
        )
        if not parent_changes:
            return self
        if not compensate_children:
            self._validate_rotation_m_plugs(
                tuple(plug.plug for plug, _ in parent_changes)
            )
            self._queue_value_changes(parent_changes)
            return self

        target_transformation = om.MFnTransform(self.m_obj).transformation()
        target_transformation.setRotation(
            self._rotation_to_euler(
                rotate,
                self.rotateOrder.get(),
            )
        )
        return self._set_with_child_compensation(
            parent_changes=parent_changes,
            parent_changes_are_rotation=True,
            target_local_matrix=target_transformation.asMatrix(),
            compensate_child_rotation=True,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    def round_rotate(
        self,
        ndigits: int = 0,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """``rotate`` を丸め、必要に応じて子のworld姿勢を補償する。

        Args:
            ndigits: 丸める小数点以下の桁数。負の値も指定できる。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            Python組み込みの ``round()`` と同じ偶数丸めを使用する。
            値の単位はdegree。Transform子は ``rotate``、Joint子は既定で
            ``rotate``を補償する。変更は ``ModifierManager.do_it_dg()`` の
            実行時に反映される。
        """
        current_rotate = self.rotate.get().as_tuple()
        target_rotate = self._rounded_values(current_rotate, ndigits)
        return self.set_rotate(
            target_rotate,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
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

    def match_position(
        self,
        source: DAG,
        *,
        axes: _PositionAxes = "xyz",
        space: _PositionSpace = "world",
        compensate_children: bool = False,
    ) -> Self:
        """DAG原点の位置を合わせ、必要に応じて子のworld位置を補償する。

        Args:
            source: 位置を合わせるDAGノード。
            axes: 位置を合わせる軸。
            space: 部分軸を評価する空間。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world位置を維持するように子の ``translate`` を補償する。

        Notes:
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        source = self._validate_match_source(source)
        axes = self._validate_position_axes(axes)
        space = self._validate_position_space(space)
        compensate_children = self._require_compensate_children(
            compensate_children
        )
        self._validate_match_instances(source)
        if self.m_obj == source.m_obj:
            return self

        source_position = source._get_instance_transform_matrix(
            "worldMatrix"
        ).translate
        destination_position = self._get_instance_transform_matrix(
            "worldMatrix"
        ).translate
        world_delta = om.MVector(
            source_position.x - destination_position.x,
            source_position.y - destination_position.y,
            source_position.z - destination_position.z,
        )
        if axes != "xyz":
            basis_rotation = self._position_basis_rotation(space)
            basis_delta = world_delta.rotateBy(basis_rotation.inverse())
            basis_components = (basis_delta.x, basis_delta.y, basis_delta.z)
            masked_delta = om.MVector(
                *(
                    basis_components[index] if axis in axes else 0.0
                    for axis, index in _POSITION_AXIS_INDEX.items()
                )
            )
            world_delta = masked_delta.rotateBy(basis_rotation)

        parent_inverse_matrix = self._get_instance_transform_matrix(
            "parentInverseMatrix"
        ).matrix
        translate_delta = world_delta * parent_inverse_matrix
        current_translate = self.translate.get()
        translate_values = (
            current_translate.x + translate_delta.x,
            current_translate.y + translate_delta.y,
            current_translate.z + translate_delta.z,
        )
        return self.set_translate(
            translate_values,
            compensate_children=compensate_children,
        )

    def match_rotation_to_rotate(
        self,
        source: DAG,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """world姿勢を ``rotate`` で合わせ、必要に応じて子を補償する。

        Args:
            source: 姿勢を合わせるDAGノード。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            Transform子は ``rotate``、Joint子は既定で ``rotate`` を補償する。
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        source = self._validate_match_source(source)
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        self._validate_match_instances(source)
        if self.m_obj == source.m_obj:
            return self

        rotate_order = self.rotateOrder.get()
        current_rotate = self.rotate.get().as_tuple()
        rotation = self._quaternion_to_rotation(
            self._rotate_from_combined_rotation(
                self._match_local_rotation(source)
            ),
            rotate_order,
            current_rotate,
        )
        return self.set_rotate(
            rotation,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    def match_rotation_to_rotate_axis(
        self,
        source: DAG,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """world姿勢を ``rotateAxis`` で合わせ、必要に応じて子を補償する。

        Args:
            source: 姿勢を合わせるDAGノード。
            compensate_children: ``True`` の場合、直接のTransform / Joint子の
                world姿勢を維持するように補償する。
            compensate_child_translate: ``True`` の場合、子の ``translate`` も
                補償してworld位置を維持する。``compensate_children=True`` が必要。
            joint_child_compensation_attr: Joint子のworld姿勢を補償する属性。

        Notes:
            Transform子は ``rotate``、Joint子は既定で ``rotate`` を補償する。
            変更は ``ModifierManager.do_it_dg()`` の実行時に反映される。
        """
        source = self._validate_match_source(source)
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        self._validate_match_instances(source)
        if self.m_obj == source.m_obj:
            return self

        current_rotate_axis = self.rotateAxis.get().as_tuple()
        rotation = self._quaternion_to_rotation(
            self._rotate_axis_from_combined_rotation(
                self._match_local_rotation(source)
            ),
            om.MEulerRotation.kXYZ,
            current_rotate_axis,
        )
        return self.set_rotate_axis(
            rotation,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

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
        rotate_axis = self._normalize_vector3_value(
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
        rotate = self._normalize_vector3_value(
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

    @staticmethod
    def _validate_match_source(source: object) -> DAG:
        if not isinstance(source, DAG):
            raise TypeError(f"source must be DAG; got {type(source).__name__}")
        return source

    @staticmethod
    def _validate_position_axes(axes: object) -> _PositionAxes:
        if not isinstance(axes, str):
            raise TypeError(f"axes must be str; got {type(axes).__name__}")
        if axes not in _POSITION_AXES:
            raise ValueError(
                f"Unsupported position axes: {axes!r}. "
                "Expected one of: x, y, z, xy, xz, yz, xyz"
            )
        return axes

    @staticmethod
    def _validate_position_space(space: object) -> _PositionSpace:
        if not isinstance(space, str):
            raise TypeError(f"space must be str; got {type(space).__name__}")
        if space not in _POSITION_SPACES:
            supported = ", ".join(sorted(_POSITION_SPACES))
            raise ValueError(
                f"Unsupported position space: {space!r}. "
                f"Expected one of: {supported}"
            )
        return space

    def _validate_match_instances(self, source: DAG) -> None:
        instanced_nodes = tuple(
            node.name for node in (self, source) if node.is_instanced
        )
        if instanced_nodes:
            raise RuntimeError(
                "Transform matching is not supported for instanced DAG "
                "nodes: " + ", ".join(instanced_nodes)
            )

    def _position_basis_rotation(
        self,
        space: _PositionSpace,
    ) -> om.MQuaternion:
        if space == "world":
            return om.MQuaternion()
        attribute_name = "parentMatrix" if space == "local" else "worldMatrix"
        transform_matrix = self._get_instance_transform_matrix(attribute_name)
        return transform_matrix.transformation_matrix.rotation(
            asQuaternion=True
        )

    def _match_local_rotation(self, source: DAG) -> om.MQuaternion:
        local_matrix = source.get_local_matrix(self)
        return local_matrix.transformation_matrix.rotation(asQuaternion=True)

    def _rotate_from_combined_rotation(
        self,
        rotation: om.MQuaternion,
    ) -> om.MQuaternion:
        rotate_axis = self._rotation_to_quaternion(
            self.rotateAxis.get().as_tuple(),
            om.MEulerRotation.kXYZ,
        )
        return rotate_axis.inverse() * rotation

    def _rotate_axis_from_combined_rotation(
        self,
        rotation: om.MQuaternion,
    ) -> om.MQuaternion:
        rotate = self._rotation_to_quaternion(
            self.rotate.get().as_tuple(),
            self.rotateOrder.get(),
        )
        return rotation * rotate.inverse()

    def _rotation_m_plugs(self) -> tuple[om.MPlug, ...]:
        return self.rotateAxis.plug, self.rotate.plug

    def _validate_rotation_plugs(self) -> None:
        self._validate_rotation_m_plugs(self._rotation_m_plugs())

    @staticmethod
    def _validate_rotation_m_plugs(plugs: tuple[om.MPlug, ...]) -> None:
        blocked_plug_names: list[str] = []
        for plug in plugs:
            try:
                child_count = plug.numChildren()
            except TypeError:
                child_count = 0
            blocked_children = [
                plug.child(index).name()
                for index in range(child_count)
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

    @staticmethod
    def _validate_position_m_plugs(plugs: tuple[om.MPlug, ...]) -> None:
        blocked_plug_names = [
            plug.name()
            for plug in plugs
            if plug.isDestination
            or plug.isFreeToChange() != om.MPlug.kFreeToChange
        ]
        if blocked_plug_names:
            raise RuntimeError(
                "Position plugs must be unlocked and have no incoming "
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
