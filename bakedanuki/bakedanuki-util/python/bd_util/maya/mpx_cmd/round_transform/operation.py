# coding: utf-8
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, cast

from maya.api import OpenMaya as om

from ...node.nodes import Nodes
from ...node.operator.node.dag.transform._core import (
    JointChildCompensationAttr,
    Transform,
)
from ...node.operator.node.dag.transform.joint import Joint
from ...rounding import RoundingUnit, round_maya_scalar

RoundKind = Literal["translate", "rotate", "rotateAxis", "jointOrient"]


@dataclass(frozen=True, slots=True)
class RoundTransformParams:
    """丸め対象、桁数、子補償条件を保持する。"""

    node_names: tuple[str, ...]
    ndigits: int = 0
    rounding_unit: RoundingUnit = "canonical"
    compensate_children: bool = False
    compensate_child_translate: bool = False
    joint_child_compensation_attr: JointChildCompensationAttr = "rotate"

    def __post_init__(self) -> None:
        if not self.node_names or any(not name for name in self.node_names):
            raise ValueError("At least one node name is required.")
        if not isinstance(self.ndigits, int) or isinstance(self.ndigits, bool):
            raise TypeError("ndigits must be an integer.")
        if self.rounding_unit not in ("canonical", "display"):
            raise ValueError("rounding_unit must be 'canonical' or 'display'.")
        if not isinstance(self.compensate_children, bool):
            raise TypeError("compensate_children must be a bool.")
        if not isinstance(self.compensate_child_translate, bool):
            raise TypeError("compensate_child_translate must be a bool.")
        if self.compensate_child_translate and not self.compensate_children:
            raise ValueError(
                "compensate_child_translate requires compensate_children."
            )
        if self.joint_child_compensation_attr not in (
            "rotate",
            "jointOrient",
        ):
            raise ValueError(
                "joint_child_compensation_attr must be 'rotate' or "
                "'jointOrient'."
            )


def apply_round_transform(
    nodes: Nodes,
    kind: RoundKind,
    params: RoundTransformParams,
) -> list[str]:
    """親から順に丸めと子補償を実行し、変更したフル DAG path を返す。"""
    targets = _resolve_targets(params.node_names, kind)
    changed: list[str] = []
    value_kind: Literal["distance", "angle"] = (
        "distance" if kind == "translate" else "angle"
    )

    for path, node_type in targets:
        node = _typed_node(nodes, path, node_type)
        current_values = _current_values(node, kind)
        rounded_values = tuple(
            round_maya_scalar(
                value,
                params.ndigits,
                kind=value_kind,
                rounding_unit=params.rounding_unit,
            )
            for value in current_values
        )
        if current_values == rounded_values:
            continue

        if kind == "translate":
            node.round_translate(
                params.ndigits,
                rounding_unit=params.rounding_unit,
                compensate_children=params.compensate_children,
            )
        else:
            kwargs = {
                "rounding_unit": params.rounding_unit,
                "compensate_children": params.compensate_children,
                "compensate_child_translate": params.compensate_child_translate,
                "joint_child_compensation_attr": (
                    params.joint_child_compensation_attr
                ),
            }
            if kind == "rotate":
                node.round_rotate(params.ndigits, **kwargs)
            elif kind == "rotateAxis":
                node.round_rotate_axis(params.ndigits, **kwargs)
            else:
                assert isinstance(node, Joint)
                node.round_joint_orient(params.ndigits, **kwargs)

        # 次の選択ノードは、親による補償後の値から丸める。
        nodes.modifier_manager.do_it_dg()
        changed.append(path)

    return changed


def _resolve_targets(
    names: tuple[str, ...], kind: RoundKind
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
    node: Transform | Joint, kind: RoundKind
) -> tuple[float, float, float]:
    """対象属性群の現在値を cm または degree で返す。"""
    if kind == "translate":
        return node.translate.get().as_tuple()
    if kind == "rotate":
        return node.rotate.get().as_tuple()
    if kind == "rotateAxis":
        return node.rotateAxis.get().as_tuple()
    assert isinstance(node, Joint)
    return node.jointOrient.get().as_tuple()
