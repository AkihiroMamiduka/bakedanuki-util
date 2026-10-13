# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from math import isclose, isfinite
from typing import Literal, cast

from maya.api import OpenMaya as om

from ...node.nodes import Nodes
from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
    Transform,
    TransformSpace,
)
from ...node.operator.node.dag.transform.joint import Joint

SetKind = Literal["translate", "rotate", "rotateAxis", "jointOrient"]
InputUnit = Literal["canonical", "display"]


@dataclass(frozen=True, slots=True)
class SetTransformCompensateChildrenParams:
    """子補償を伴う設定先、入力空間と XYZ を保持する。"""

    node_names: tuple[str, ...]
    values: tuple[float, float, float]
    space: TransformSpace = "local"
    input_unit: InputUnit = "canonical"
    compensate_child_translate: bool = True
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate"

    def __post_init__(self) -> None:
        """シーンを変更する前に引数の形を検証する。"""
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
        if self.space not in ("local", "world"):
            raise ValueError("space must be 'local' or 'world'.")
        if self.input_unit not in ("canonical", "display"):
            raise ValueError("input_unit must be 'canonical' or 'display'.")
        if not isinstance(self.compensate_child_translate, bool):
            raise TypeError("compensate_child_translate must be a bool.")
        if self.joint_child_compensation_attr not in (
            "rotate",
            "jointOrient",
        ):
            raise ValueError(
                "joint_child_compensation_attr must be 'rotate' or "
                "'jointOrient'."
            )


def apply_set_transform_compensate_children(
    nodes: Nodes,
    kind: SetKind,
    params: SetTransformCompensateChildrenParams,
) -> list[str]:
    """親から順に目標値を設定し、変更した DAG path を返す。"""
    targets = _resolve_targets(params.node_names, kind)
    values = _values_in_canonical_unit(
        params.values, kind=kind, input_unit=params.input_unit
    )
    changed: list[str] = []

    for path, node_type in targets:
        node = _typed_node(nodes, path, node_type)
        current = _current_values(node, kind)
        if params.space == "world":
            current_world = node.convert_transform_space_values(
                kind, current, from_space="local", to_space="world"
            )
            # 15桁表示の再入力誤差だけを許容し、微小な明示変更は残す
            if all(
                isclose(actual, desired, rel_tol=0.0, abs_tol=1.0e-15)
                for actual, desired in zip(current_world, values)
            ):
                continue
            local_values = node.convert_transform_space_values(
                kind, values, from_space="world", to_space="local"
            )
        else:
            local_values = values
        if current == local_values:
            continue

        # 子補償の設定は全種類とも NodeOperator に委ねる
        if kind == "translate":
            node.set_translate(
                local_values, space="local", compensate_children=True
            )
        elif kind == "rotate":
            node.set_rotate(
                local_values,
                space="local",
                compensate_children=True,
                compensate_child_translate=params.compensate_child_translate,
                joint_child_compensation_attr=(
                    params.joint_child_compensation_attr
                ),
            )
        elif kind == "rotateAxis":
            node.set_rotate_axis(
                local_values,
                space="local",
                compensate_children=True,
                compensate_child_translate=params.compensate_child_translate,
                joint_child_compensation_attr=(
                    params.joint_child_compensation_attr
                ),
            )
        else:
            assert isinstance(node, Joint)
            node.set_joint_orient(
                local_values,
                space="local",
                compensate_children=True,
                compensate_child_translate=params.compensate_child_translate,
                joint_child_compensation_attr=(
                    params.joint_child_compensation_attr
                ),
            )

        # 次の選択ノードは、先行ノードによる子補償の後で評価する
        nodes.modifier_manager.do_it_dg()
        changed.append(path)

    return changed


def _resolve_targets(
    names: tuple[str, ...], kind: SetKind
) -> list[tuple[str, Literal["transform", "joint"]]]:
    """対象を一意の DAG path へ解決し、親から子へ並べる。"""
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
        if kind == "jointOrient" and type_name != "joint":
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


def _current_values(
    node: Transform | Joint, kind: SetKind
) -> tuple[float, float, float]:
    """対象属性群の現在の canonical XYZ を返す。"""
    if kind == "translate":
        return node.translate.get().as_tuple()
    if kind == "rotate":
        return node.rotate.get().as_tuple()
    if kind == "rotateAxis":
        return node.rotateAxis.get().as_tuple()
    assert isinstance(node, Joint)
    return node.jointOrient.get().as_tuple()


def _values_in_canonical_unit(
    values: tuple[float, float, float],
    *,
    kind: SetKind,
    input_unit: InputUnit,
) -> tuple[float, float, float]:
    """表示単位の入力だけを cm または degree へ変換する。"""
    if input_unit == "canonical":
        return values
    if kind == "translate":
        ui_unit = om.MDistance.uiUnit()
        converted = tuple(
            om.MDistance(value, ui_unit).asCentimeters() for value in values
        )
    else:
        ui_unit = om.MAngle.uiUnit()
        converted = tuple(
            om.MAngle(value, ui_unit).asDegrees() for value in values
        )
    if not all(isfinite(value) for value in converted):
        raise ValueError("Converted values must be finite.")
    return cast(tuple[float, float, float], converted)
