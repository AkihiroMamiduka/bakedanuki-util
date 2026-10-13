# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from math import isclose, isfinite
from typing import Literal, cast

from maya.api import OpenMaya as om

from ...node.nodes import Nodes
from ...node.operator.node.dag.transform._core import Transform
from ...node.operator.node.dag.transform.joint import Joint

RotationAttribute = Literal["rotate", "rotateAxis", "jointOrient"]
AngleInputUnit = Literal["degrees", "display"]


@dataclass(frozen=True, slots=True)
class SetRotationPreservingPoseParams:
    """回転の設定先、補償先、共通の目標 XYZ を保持する。"""

    node_names: tuple[str, ...]
    values: tuple[float, float, float]
    target: RotationAttribute
    compensate_with: RotationAttribute
    angle_unit: AngleInputUnit = "degrees"

    def __post_init__(self) -> None:
        """Maya のコマンド実行前に引数の形を検証する。"""
        if not self.node_names or any(
            not isinstance(name, str) or not name for name in self.node_names
        ):
            raise ValueError("At least one node name is required.")
        if len(self.values) != 3 or any(
            isinstance(value, bool) or not isinstance(value, (int, float))
            for value in self.values
        ):
            raise TypeError("values must contain three numeric components.")
        if not all(isfinite(value) for value in self.values):
            raise ValueError("values must contain only finite components.")
        if self.target not in ("rotate", "rotateAxis", "jointOrient"):
            raise ValueError("Unsupported target rotation attribute.")
        if self.compensate_with not in (
            "rotate",
            "rotateAxis",
            "jointOrient",
        ):
            raise ValueError("Unsupported compensation rotation attribute.")
        if self.target == self.compensate_with:
            raise ValueError("Target and compensation attributes must differ.")
        if self.angle_unit not in ("degrees", "display"):
            raise ValueError("angle_unit must be 'degrees' or 'display'.")


def apply_set_rotation_preserving_pose(
    nodes: Nodes, params: SetRotationPreservingPoseParams
) -> list[str]:
    """親から順に姿勢維持の回転設定を確定し、変更した DAG path を返す。"""
    joint_required = "jointOrient" in (params.target, params.compensate_with)
    targets = _resolve_targets(
        params.node_names, joint_required=joint_required
    )
    values = _values_in_degrees(params.values, params.angle_unit)
    changed: list[str] = []

    for path, node_type in targets:
        node = _typed_node(nodes, path, node_type)
        current = tuple(getattr(node, params.target).get())
        if all(
            isclose(actual, desired, rel_tol=1.0e-14, abs_tol=1.0e-14)
            for actual, desired in zip(current, values)
        ):
            continue

        # 回転差分は NodeOperator の対応する属性群に吸収させる
        pair = params.target, params.compensate_with
        if pair == ("rotate", "rotateAxis"):
            node.set_rotate_with_rotate_axis(values)
        elif pair == ("rotateAxis", "rotate"):
            node.set_rotate_axis_with_rotate(values)
        else:
            assert isinstance(node, Joint)
            if pair == ("rotate", "jointOrient"):
                node.set_rotate_with_joint_orient(values)
            elif pair == ("jointOrient", "rotate"):
                node.set_joint_orient_with_rotate(values)
            elif pair == ("rotateAxis", "jointOrient"):
                node.set_rotate_axis_with_joint_orient(values)
            else:
                assert pair == ("jointOrient", "rotateAxis")
                node.set_joint_orient_with_rotate_axis(values)

        # 次のノードは先行ノードの確定後に評価する
        nodes.modifier_manager.do_it_dg()
        changed.append(path)

    return changed


def _resolve_targets(
    names: tuple[str, ...], *, joint_required: bool
) -> list[tuple[str, Literal["transform", "joint"]]]:
    """名前を一意の DAG path へ解決し、親から子へ並べる。"""
    targets: dict[str, Literal["transform", "joint"]] = {}
    for name in names:
        if any(char in name for char in ".*?[]"):
            raise ValueError(f"Expected one DAG node name: {name!r}")
        selection = om.MSelectionList()
        try:
            selection.add(name)
        except RuntimeError as error:
            raise ValueError(f"Node not found: {name}") from error
        if selection.length() != 1:
            raise ValueError(f"Expected one DAG node: {name!r}")
        try:
            path = selection.getDagPath(0)
        except TypeError as error:
            raise TypeError(
                f"Expected a transform or joint: {name}"
            ) from error
        type_name = om.MFnDependencyNode(path.node()).typeName
        if type_name not in ("transform", "joint"):
            raise TypeError(f"Expected a transform or joint: {name}")
        if joint_required and type_name != "joint":
            raise TypeError(f"jointOrient requires a joint: {name}")
        targets[path.fullPathName()] = cast(
            Literal["transform", "joint"], type_name
        )
    return sorted(targets.items(), key=lambda target: target[0].count("|"))


def _typed_node(
    nodes: Nodes, path: str, node_type: Literal["transform", "joint"]
) -> Transform | Joint:
    """解決済みの DAG path を型別 NodeOperator として取得する。"""
    if node_type == "joint":
        return nodes.existing.joint(path)
    return nodes.existing.transform(path)


def _values_in_degrees(
    values: tuple[float, float, float], angle_unit: AngleInputUnit
) -> tuple[float, float, float]:
    """表示単位の入力だけを degree に変換する。"""
    if angle_unit == "degrees":
        return values
    ui_unit = om.MAngle.uiUnit()
    converted = tuple(
        om.MAngle(value, ui_unit).asDegrees() for value in values
    )
    if not all(isfinite(value) for value in converted):
        raise ValueError("Converted rotation values must be finite.")
    return cast(tuple[float, float, float], converted)
