# coding: utf-8
"""sampleの任意Maya指定を検証し、公開APIへ渡す。"""

from __future__ import annotations

from .....maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from .....maya.ui import resolve_bool_plug


def validate_maya_view_names(
    node_name: object | None,
    attribute_name: object | None,
) -> tuple[str, str] | None:
    """任意指定のnode名とattribute名を組として検証する。"""
    for value, argument_name in (
        (node_name, "maya_node_name"),
        (attribute_name, "maya_attribute_name"),
    ):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(
                    f"{argument_name}にはstrまたはNoneを指定してください"
                )
            if not value:
                raise ValueError(
                    f"{argument_name}には空でないstrを指定してください"
                )
    if node_name is None and attribute_name is None:
        return None
    if not isinstance(node_name, str) or not isinstance(attribute_name, str):
        raise ValueError(
            "maya_node_nameとmaya_attribute_nameは両方指定してください"
        )
    return node_name, attribute_name


def resolve_optional_bool_plug(
    node_name: str | None,
    attribute_name: str | None,
) -> BoolPlugOperator | None:
    """Maya指定がある場合だけ公開resolverからbool plugを取得する。"""
    names = validate_maya_view_names(node_name, attribute_name)
    return None if names is None else resolve_bool_plug(*names)
