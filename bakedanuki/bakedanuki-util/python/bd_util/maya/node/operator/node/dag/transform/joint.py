# coding: utf-8
from collections.abc import Sequence
from typing import cast, overload, Self

from maya.api import OpenMaya as om
from maya.api import OpenMayaAnim as oma

from .._core import DAG
from ._core import (
    AimCoordinateSpace,
    JointChildCompensationAttr,
    ScalarPlugProtocol,
    Transform,
    TransformSpace,
)
from ._generated.joint import GeneratedJoint


class Joint(GeneratedJoint):
    __slots__ = ()

    NODE_TYPE = "joint"

    def _joint_orient_value_plugs(
        self,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        return (
            cast(ScalarPlugProtocol, self.jointOrientX),
            cast(ScalarPlugProtocol, self.jointOrientY),
            cast(ScalarPlugProtocol, self.jointOrientZ),
        )

    def _current_child_compensation_rotation_values(
        self,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> tuple[float, float, float]:
        if joint_child_compensation_attr == "rotate":
            return self.rotate.get().as_tuple()
        return self.jointOrient.get().as_tuple()

    def _child_compensation_rotation_values(
        self,
        target_local_rotation: om.MQuaternion,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> tuple[float, float, float]:
        if joint_child_compensation_attr == "rotate":
            current_rotate = self.rotate.get().as_tuple()
            return self._quaternion_to_rotation(
                self._rotate_from_combined_rotation(target_local_rotation),
                self.rotateOrder.get(),
                current_rotate,
            )
        current_joint_orient = self.jointOrient.get().as_tuple()
        return self._quaternion_to_rotation(
            self._joint_orient_from_combined_rotation(target_local_rotation),
            om.MEulerRotation.kXYZ,
            current_joint_orient,
        )

    def _child_compensation_rotation_plugs(
        self,
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> tuple[
        ScalarPlugProtocol,
        ScalarPlugProtocol,
        ScalarPlugProtocol,
    ]:
        if joint_child_compensation_attr == "rotate":
            return self._rotate_value_plugs()
        return self._joint_orient_value_plugs()

    def _transformation_with_child_compensation_rotation(
        self,
        rotation: tuple[float, float, float],
        joint_child_compensation_attr: JointChildCompensationAttr,
    ) -> om.MTransformationMatrix:
        if joint_child_compensation_attr == "rotate":
            transformation = om.MFnTransform(self.m_obj).transformation()
            rotate_order = self.rotateOrder.get()
            transformation.setRotation(
                self._rotation_to_euler(rotation, rotate_order)
            )
            return transformation

        return self._transformation_with_joint_orient(rotation)

    def _transformation_with_joint_orient(
        self,
        joint_orient: tuple[float, float, float],
    ) -> om.MTransformationMatrix:
        transformation = om.MFnTransform(self.m_obj).transformation()
        rotate_order = self.rotateOrder.get()
        current_rotate = self.rotate.get().as_tuple()
        current_joint_orient = self.jointOrient.get().as_tuple()
        proxy_rotation = (
            self._rotation_to_quaternion(current_rotate, rotate_order)
            * self._rotation_to_quaternion(
                joint_orient,
                om.MEulerRotation.kXYZ,
            )
            * self._rotation_to_quaternion(
                current_joint_orient,
                om.MEulerRotation.kXYZ,
            ).inverse()
        )
        transformation.setRotation(proxy_rotation)
        return transformation

    @overload
    def set_joint_orient(
        self,
        value: Sequence[float],
        /,
        *,
        space: TransformSpace = "local",
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    @overload
    def set_joint_orient(
        self,
        value: float,
        y: float,
        z: float,
        /,
        *,
        space: TransformSpace = "local",
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self: ...

    def set_joint_orient(
        self,
        value: float | Sequence[float],
        /,
        *values: float,
        space: TransformSpace = "local",
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """姿勢を ``jointOrient`` へ設定し、必要に応じて子を補償する。

        Args:
            value: 3成分の値、またはX成分。
            values: ``value`` がX成分の場合のY、Z成分。
            space: 値を解釈する空間。``"local"`` は属性値、``"world"`` は
                最終的なworld姿勢として扱う。
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
        joint_orient = self._normalize_vector3_value(
            value,
            values,
            "set_joint_orient",
        )
        space = self._require_transform_space(space)
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        current_joint_orient = self.jointOrient.get().as_tuple()
        if space == "world":
            joint_orient = self._quaternion_to_rotation(
                self._joint_orient_from_combined_rotation(
                    self._local_rotation_from_world_rotation(
                        joint_orient,
                        om.MEulerRotation.kXYZ,
                    )
                ),
                om.MEulerRotation.kXYZ,
                current_joint_orient,
            )
        parent_changes = self._value_changes(
            self._joint_orient_value_plugs(),
            current_joint_orient,
            joint_orient,
            use_tolerance=space == "world",
        )
        if not parent_changes:
            return self
        if not compensate_children:
            self._validate_rotation_m_plugs(
                tuple(plug.plug for plug, _ in parent_changes)
            )
            self._queue_value_changes(parent_changes)
            return self

        target_transformation = self._transformation_with_joint_orient(
            joint_orient
        )
        return self._set_with_child_compensation(
            parent_changes=parent_changes,
            parent_changes_are_rotation=True,
            target_local_matrix=target_transformation.asMatrix(),
            compensate_child_rotation=True,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    def round_joint_orient(
        self,
        ndigits: int = 0,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """``jointOrient`` を丸め、必要に応じて子のworld姿勢を補償する。

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
        current_joint_orient = self.jointOrient.get().as_tuple()
        target_joint_orient = self._rounded_values(
            current_joint_orient,
            ndigits,
        )
        return self.set_joint_orient(
            target_joint_orient,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

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

    def match_rotation_to_joint_orient(
        self,
        source: DAG,
        *,
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """world姿勢を ``jointOrient`` で合わせ、必要に応じて子を補償する。

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

        current_joint_orient = self.jointOrient.get().as_tuple()
        rotation = self._quaternion_to_rotation(
            self._joint_orient_from_combined_rotation(
                self._match_local_rotation(source)
            ),
            om.MEulerRotation.kXYZ,
            current_joint_orient,
        )
        return self.set_joint_orient(
            rotation,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

    def aim_to_joint_orient(
        self,
        aim_target: "Transform | str | Sequence[float]",
        *,
        aim_axis: Sequence[float] = (1.0, 0.0, 0.0),
        up_target: "Transform | str | Sequence[float] | None" = None,
        up_axis: Sequence[float] = (0.0, 1.0, 0.0),
        coordinate_space: AimCoordinateSpace = "world",
        compensate_children: bool = False,
        compensate_child_translate: bool = False,
        joint_child_compensation_attr: JointChildCompensationAttr = "rotate",
    ) -> Self:
        """エイムで求めたworld姿勢を ``jointOrient`` へ設定する。

        引数と計算仕様は :meth:`Transform.aim_to_rotate` と共通で、変更する
        回転属性だけが異なる。
        """
        (
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        ) = self._require_rotation_child_compensation_options(
            compensate_children,
            compensate_child_translate,
            joint_child_compensation_attr,
        )
        target_local_rotation = self._aim_local_rotation(
            aim_target,
            aim_axis=aim_axis,
            up_target=up_target,
            up_axis=up_axis,
            coordinate_space=coordinate_space,
        )
        current_joint_orient = self.jointOrient.get().as_tuple()
        rotation = self._quaternion_to_rotation(
            self._joint_orient_from_combined_rotation(target_local_rotation),
            om.MEulerRotation.kXYZ,
            current_joint_orient,
        )
        return self.set_joint_orient(
            rotation,
            compensate_children=compensate_children,
            compensate_child_translate=compensate_child_translate,
            joint_child_compensation_attr=joint_child_compensation_attr,
        )

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
        joint_orient = self._normalize_vector3_value(
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
        rotate = self._normalize_vector3_value(
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

    def _rotate_from_combined_rotation(
        self,
        rotation: om.MQuaternion,
    ) -> om.MQuaternion:
        joint_orient = self._rotation_to_quaternion(
            self.jointOrient.get().as_tuple(),
            om.MEulerRotation.kXYZ,
        )
        return (
            super()._rotate_from_combined_rotation(rotation)
            * joint_orient.inverse()
        )

    def _rotate_axis_from_combined_rotation(
        self,
        rotation: om.MQuaternion,
    ) -> om.MQuaternion:
        joint_orient = self._rotation_to_quaternion(
            self.jointOrient.get().as_tuple(),
            om.MEulerRotation.kXYZ,
        )
        return super()._rotate_axis_from_combined_rotation(
            rotation * joint_orient.inverse()
        )

    def _joint_orient_from_combined_rotation(
        self,
        rotation: om.MQuaternion,
    ) -> om.MQuaternion:
        rotate_axis = self._rotation_to_quaternion(
            self.rotateAxis.get().as_tuple(),
            om.MEulerRotation.kXYZ,
        )
        rotate = self._rotation_to_quaternion(
            self.rotate.get().as_tuple(),
            self.rotateOrder.get(),
        )
        return rotate.inverse() * rotate_axis.inverse() * rotation

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
