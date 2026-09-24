# coding: utf-8
from __future__ import annotations

import keyword
import re
from collections.abc import Callable
from importlib import resources
from typing import TYPE_CHECKING, cast

from .._maya_version import is_node_type_available
from .._node_class_resolver import (
    CREATOR_PACKAGES,
    DAG_SHAPE_NODE_PACKAGE,
    DAG_TRANSFORM_NODE_PACKAGE,
    resolve_node_class,
)
from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator
from ..operator.node.dag._core import DAG
from ..operator.node.dag.shape._core import Shape
from ..operator.node.dag.transform._core import Transform
from ._shape_types import CREATABLE_SHAPE_NODE_TYPES
from ._shape_with_transform import ShapeWithTransformCreator
from ._transform_types import CREATABLE_TRANSFORM_NODE_TYPES

if TYPE_CHECKING:
    from ..operator.node.dg.anim_layer import AnimLayer

_NODE_TYPE_PATTERN = re.compile(
    r"^\s*NODE_TYPE\s*=\s*[\"']([^\"']+)[\"']",
    re.MULTILINE,
)


def _node_type_to_creator_name(node_type: str) -> str:
    if keyword.iskeyword(node_type):
        return f"{node_type}_"
    return node_type


class NodeCreator:
    """指定した型のノード作成を ModifierManager に予約する。"""

    __slots__ = (
        "__dict__",
        "_modifier_manager",
        "_node_names_cache",
        "_with_transform",
    )

    def __init__(self, modifier_manager: ModifierManager | None = None):
        self._modifier_manager = modifier_manager or ModifierManager()
        self._node_names_cache: tuple[str, ...] | None = None
        self._with_transform = ShapeWithTransformCreator(
            self._modifier_manager,
            self._creator_node_class,
        )

    @property
    def modifier_manager(self) -> ModifierManager:
        """ノード作成を予約する先。"""
        return self._modifier_manager

    @property
    def with_transform(self) -> ShapeWithTransformCreator:
        """Transform と Shape をまとめて作成する入口。"""
        return self._with_transform

    def create(
        self,
        node_name: str,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: DAG | None = None,
    ) -> NodeOperator:
        """指定した Maya ノード型の作成を予約する。

        Args:
            node_name: Maya のノード型名。
            name: 作成するノードの名前。省略時は Maya に委ねる。
            auto_add_attr: 定義済みの extra attribute を追加するか。既定は True。
            parent: DAG ノードの親。DG ノードには指定できない。

        Returns:
            作成予定のノードを包む NodeOperator。

        Raises:
            TypeError: DG ノードに parent を指定した場合。
            AttributeError: 作成できないノード型を指定した場合。
        """
        node_cls = self._creator_node_class(node_name)
        if not issubclass(node_cls, DAG):
            if parent is not None:
                raise TypeError(
                    f"parent is only supported for DAG nodes: {node_name}"
                )
            return node_cls.create(
                self._modifier_manager,
                name=name,
                auto_add_attr=auto_add_attr,
            )
        return node_cls.create(
            self._modifier_manager,
            name=name,
            auto_add_attr=auto_add_attr,
            parent=parent,
        )

    def node_class(self, node_name: str) -> type[NodeOperator]:
        """Maya ノード型に対応する NodeOperator クラスを返す。

        Args:
            node_name: Maya のノード型名。

        Returns:
            対応する NodeOperator クラス。
        """
        return resolve_node_class(node_name)

    def animLayer(
        self,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        override: bool = False,
    ) -> AnimLayer:
        """ベースと階層接続を含むアニメーションレイヤーの作成を予約する。

        Args:
            name: 作成するレイヤー名。
            auto_add_attr: 定義済みの extra attribute を追加するか。既定は True。
            override: 上書きモードのレイヤーにするか。

        Returns:
            作成予定のアニメーションレイヤー。
        """
        node_cls = cast(
            "type[AnimLayer]", self._creator_node_class("animLayer")
        )
        return node_cls.create(
            self._modifier_manager, name, auto_add_attr, override=override
        )

    def _creator_node_class(self, node_name: str) -> type[NodeOperator]:
        node_cls = resolve_node_class(node_name, CREATOR_PACKAGES)
        if (
            issubclass(node_cls, Shape)
            and node_cls.NODE_TYPE not in CREATABLE_SHAPE_NODE_TYPES
        ):
            raise AttributeError(f"Unsupported node type: {node_name}")
        if (
            issubclass(node_cls, Transform)
            and node_cls.NODE_TYPE not in CREATABLE_TRANSFORM_NODE_TYPES
        ):
            raise AttributeError(f"Unsupported node type: {node_name}")
        return node_cls

    def available_node_names(self) -> tuple[str, ...]:
        """現在の Maya で作成できるノード型名を返す。"""
        if self._node_names_cache is not None:
            return self._node_names_cache

        names: set[str] = set()
        for package_name in CREATOR_PACKAGES:
            for path in resources.files(package_name).iterdir():
                if (
                    not path.is_file()
                    or not path.name.endswith(".py")
                    or path.name == "__init__.py"
                ):
                    continue
                try:
                    node_type = _read_node_type(
                        path.read_text(encoding="utf-8")
                    )
                except ValueError:
                    continue
                if (
                    package_name == DAG_SHAPE_NODE_PACKAGE
                    and node_type not in CREATABLE_SHAPE_NODE_TYPES
                ):
                    continue
                if (
                    package_name == DAG_TRANSFORM_NODE_PACKAGE
                    and node_type not in CREATABLE_TRANSFORM_NODE_TYPES
                ):
                    continue
                if not is_node_type_available(node_type):
                    continue
                names.add(_node_type_to_creator_name(node_type))

        sorted_names = sorted(names)
        self._node_names_cache = tuple(sorted_names)
        return self._node_names_cache

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        node_cls = self._creator_node_class(node_name)

        if issubclass(node_cls, Shape):

            def _create_shape(
                name: str | None = None,
                auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
                *,
                parent: Transform,
            ) -> NodeOperator:
                return node_cls.create(
                    self._modifier_manager,
                    name=name,
                    auto_add_attr=auto_add_attr,
                    parent=parent,
                )

            create_func: Callable[..., NodeOperator] = _create_shape

        elif issubclass(node_cls, DAG):

            def _create_dag(
                name: str | None = None,
                auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
                *,
                parent: DAG | None = None,
            ) -> NodeOperator:
                return node_cls.create(
                    self._modifier_manager,
                    name=name,
                    auto_add_attr=auto_add_attr,
                    parent=parent,
                )

            create_func: Callable[..., NodeOperator] = _create_dag

        else:

            def _create_dg(
                name: str | None = None,
                auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
            ) -> NodeOperator:
                return node_cls.create(
                    self._modifier_manager,
                    name=name,
                    auto_add_attr=auto_add_attr,
                )

            create_func = _create_dg

        create_func.__name__ = node_name
        create_func.__qualname__ = f"{type(self).__name__}.{node_name}"
        parent_doc = ""
        if issubclass(node_cls, Shape):
            parent_doc = "    parent: 親の Transform。\n"
        elif issubclass(node_cls, DAG):
            parent_doc = "    parent: 親の DAG ノード。\n"
        create_func.__doc__ = (
            f"{node_cls.NODE_TYPE} ノードの作成を予約する。\n\n"
            "Args:\n"
            "    name: 作成するノードの名前。省略時は Maya に委ねる。\n"
            "    auto_add_attr: 定義済みの extra attribute を追加するか。既定は True。\n"
            f"{parent_doc}\nReturns:\n"
            f"    {node_cls.__name__} インスタンス。"
        )
        setattr(self, node_name, create_func)
        return create_func

    def __dir__(self) -> list[str]:
        return sorted(
            set(super().__dir__()) | set(self.available_node_names())
        )


def _read_node_type(code: str) -> str:
    match = _NODE_TYPE_PATTERN.search(code)
    if match is None:
        raise ValueError("NODE_TYPE definition not found.")
    return match.group(1)
