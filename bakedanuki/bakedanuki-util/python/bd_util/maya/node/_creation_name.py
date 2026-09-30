"""作成予定ノードの名前と namespace を解決する。"""

from __future__ import annotations

from typing import cast

from maya.api import OpenMaya as om


def resolve_creation_name(
    name: str | None, namespace: str | None = None
) -> tuple[str | None, str | None]:
    """明示名を予約時の namespace に基づく絶対名へ変換する。

    Args:
        name: ノード名。`None` なら Maya の自動命名に委ねる。
        namespace: `name` に付ける namespace。先頭の `:` はルート起点。
            空文字列もルートを表し、`name` には namespace を含めない。

    Returns:
        絶対ノード名と、その namespace。自動命名時は両方 `None`。

    Raises:
        TypeError: `name` または `namespace` の型が不正な場合。
        ValueError: 名前が空、namespace の指定が重複または不正な場合。
    """
    if namespace is not None and not isinstance(cast(object, namespace), str):
        raise TypeError("namespace must be a string or None.")
    if name is None:
        if namespace is not None:
            raise ValueError("name is required when namespace is specified.")
        return None, None
    if not isinstance(cast(object, name), str):
        raise TypeError("name must be a string or None.")
    if not name or not name.rsplit(":", 1)[-1]:
        raise ValueError("name must include a nonempty node name.")

    if namespace is not None:
        if ":" in name:
            raise ValueError("name cannot include a namespace with namespace.")
        if not namespace or namespace == ":":
            absolute_name = f":{name}"
        elif namespace.startswith(":"):
            absolute_name = f"{namespace}:{name}"
        else:
            current = om.MNamespace.currentNamespace()
            absolute_name = (
                f"{current}{namespace}:{name}"
                if current == ":"
                else f"{current}:{namespace}:{name}"
            )
    elif name.startswith(":"):
        absolute_name = name
    else:
        current = om.MNamespace.currentNamespace()
        absolute_name = (
            f"{current}{name}" if current == ":" else f"{current}:{name}"
        )

    parts = absolute_name[1:].split(":")
    if any(
        not part or om.MNamespace.validateName(part) != part
        for part in parts[:-1]
    ):
        raise ValueError("namespace contains an invalid name.")
    absolute_namespace = ":" + ":".join(parts[:-1]) if len(parts) > 1 else ":"
    return absolute_name, absolute_namespace
