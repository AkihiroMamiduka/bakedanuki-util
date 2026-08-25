# coding: utf-8
from typing import Literal, overload, Self, TypeVar

# maya
from maya.api import OpenMaya as om

# self
from ....modifier import ModifierManager
from .....transform import TransformMatrix
from .._core import NodeOperator, DEFAULT_VALUE_AUTO_ADD_ATTR

_DAGType = TypeVar("_DAGType", bound="DAG")


def _require_dag(value: object, argument_name: str) -> "DAG":
    if not isinstance(value, DAG):
        raise TypeError(
            f"{argument_name} must be DAG; got {type(value).__name__}"
        )
    return value


def _require_dag_type(
    value: object,
    argument_name: str,
) -> type["DAG"]:
    if not isinstance(value, type) or not issubclass(value, DAG):
        value_name = (
            value.__name__ if isinstance(value, type) else type(value).__name__
        )
        raise TypeError(
            f"{argument_name} must be a DAG NodeOperator class; "
            f"got {value_name}"
        )
    return value


def _require_bool(value: object, argument_name: str) -> bool:
    if not isinstance(value, bool):
        raise TypeError(
            f"{argument_name} must be bool; got {type(value).__name__}"
        )
    return value


def _matches_dag_type(
    node: "DAG",
    dag_type: type["DAG"],
    include_subclasses: bool,
) -> bool:
    if include_subclasses:
        return isinstance(node, dag_type)
    return type(node) is dag_type


def _matches_shape_filter(node: "DAG", include_shapes: bool) -> bool:
    return include_shapes or not node.m_obj.hasFn(om.MFn.kShape)


class DAG(NodeOperator):
    __slots__ = ("_dag_path",)

    def __init__(
        self,
        modifier_manager: ModifierManager,
        name: str | None = None,
        m_obj: om.MObject | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
    ) -> None:
        rename_name = name if m_obj is not None and name else None
        super_name = None if rename_name is not None else name

        super().__init__(
            modifier_manager,
            name=super_name,
            m_obj=m_obj,
            auto_add_attr=False,
        )

        # dag_path
        self._dag_path = om.MDagPath.getAPathTo(self.m_obj)

        if rename_name:
            self._dag_mod.renameNode(self.m_obj, rename_name)

        # auto_add_attr
        if auto_add_attr and self._extra_attributes:
            self._auto_add_extra_attrs()

    @classmethod
    def create(
        cls,
        modifier_manager: ModifierManager,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: "DAG | None" = None,
    ) -> Self:
        if cls.NODE_TYPE is None:
            raise ValueError(f"{cls.__name__} must define NODE_TYPE")

        if parent is not None:
            cls._validate_parent(parent, modifier_manager)

        # ノード作成
        parent_obj = (
            parent.m_obj if parent is not None else om.MObject.kNullObj
        )
        m_obj = modifier_manager.dag_mod.createNode(cls.NODE_TYPE, parent_obj)
        modifier_manager.record_pending_dag_parent(m_obj, parent_obj)

        # インスタンス生成
        return cls(
            modifier_manager,
            m_obj=m_obj,
            name=name,
            auto_add_attr=auto_add_attr,
        )

    @property
    def _dag_mod(self) -> om.MDagModifier:
        return self.modifier_manager.dag_mod

    @property
    def full_path(self) -> str:
        """現在の DAG フルパスを返す。"""
        return self._dag_path.fullPathName()

    @property
    def is_instanced(self) -> bool:
        """複数の DAG パスを持つ場合は True を返す。"""
        return len(om.MDagPath.getAllPathsTo(self.m_obj)) > 1

    @property
    def parent(self) -> "DAG | None":
        """直接の親を返す。ワールド直下では None を返す。"""
        if self.is_instanced:
            raise RuntimeError(
                "parent is ambiguous for an instanced DAG node: "
                f"{self.name}"
            )

        parents = self.parents
        if not parents:
            return None
        return parents[0]

    @property
    def parents(self) -> tuple["DAG", ...]:
        """ワールドを除く、すべての直接の親を返す。"""
        fn_dag = om.MFnDagNode(self.m_obj)
        parents: list[DAG] = []
        for index in range(fn_dag.parentCount()):
            parent_obj = fn_dag.parent(index)
            if parent_obj.hasFn(om.MFn.kWorld):
                continue
            parents.append(self._wrap_existing_dag(parent_obj))
        return tuple(parents)

    @overload
    def children(
        self,
        *,
        filter_type: None = None,
        include_subclasses: Literal[True] = True,
        include_shapes: bool = True,
    ) -> tuple["DAG", ...]: ...

    @overload
    def children(
        self,
        *,
        filter_type: type[_DAGType],
        include_subclasses: bool = True,
        include_shapes: bool = True,
    ) -> tuple[_DAGType, ...]: ...

    def children(
        self,
        *,
        filter_type: object = None,
        include_subclasses: object = True,
        include_shapes: object = True,
    ) -> tuple["DAG", ...]:
        """Mayaのchild index順で、条件に一致する直接の子を返す。"""
        include_subclasses_value = _require_bool(
            include_subclasses,
            "include_subclasses",
        )
        include_shapes_value = _require_bool(
            include_shapes,
            "include_shapes",
        )
        if filter_type is None and not include_subclasses_value:
            raise ValueError("include_subclasses=False requires filter_type")

        fn_dag = om.MFnDagNode(self.m_obj)
        children = tuple(
            self._wrap_existing_dag(fn_dag.child(index))
            for index in range(fn_dag.childCount())
        )
        if filter_type is None:
            return tuple(
                child
                for child in children
                if _matches_shape_filter(child, include_shapes_value)
            )

        dag_type = _require_dag_type(filter_type, "filter_type")
        return tuple(
            child
            for child in children
            if _matches_shape_filter(child, include_shapes_value)
            and _matches_dag_type(
                child,
                dag_type,
                include_subclasses_value,
            )
        )

    @overload
    def ancestors(
        self,
        *,
        filter_type: None = None,
        include_subclasses: Literal[True] = True,
        until: None = None,
    ) -> tuple["DAG", ...]: ...

    @overload
    def ancestors(
        self,
        *,
        filter_type: None = None,
        include_subclasses: Literal[True] = True,
        until: "DAG | None",
    ) -> tuple["DAG", ...] | None: ...

    @overload
    def ancestors(
        self,
        *,
        filter_type: type[_DAGType],
        include_subclasses: bool = True,
        until: None = None,
    ) -> tuple[_DAGType, ...]: ...

    @overload
    def ancestors(
        self,
        *,
        filter_type: type[_DAGType],
        include_subclasses: bool = True,
        until: "DAG | None",
    ) -> tuple[_DAGType, ...] | None: ...

    def ancestors(
        self,
        *,
        filter_type: object = None,
        include_subclasses: object = True,
        until: object = None,
    ) -> tuple["DAG", ...] | None:
        """保持pathの直接親からroot方向へ、条件に一致する祖先を返す。"""
        include_subclasses_value = _require_bool(
            include_subclasses,
            "include_subclasses",
        )
        if filter_type is None and not include_subclasses_value:
            raise ValueError("include_subclasses=False requires filter_type")

        dag_type = (
            None
            if filter_type is None
            else _require_dag_type(filter_type, "filter_type")
        )
        until_node = None if until is None else _require_dag(until, "until")
        path = om.MDagPath(self._dag_path)
        ancestors: list[DAG] = []
        until_found = until_node is None
        while path.length():
            path.pop()
            ancestor_obj = path.node()
            if ancestor_obj.hasFn(om.MFn.kWorld):
                break
            ancestor = self._wrap_existing_dag(ancestor_obj)
            if dag_type is None or _matches_dag_type(
                ancestor,
                dag_type,
                include_subclasses_value,
            ):
                ancestors.append(ancestor)
            if until_node is not None and ancestor.m_obj == until_node.m_obj:
                until_found = True
                break
        if not until_found:
            return None
        return tuple(ancestors)

    @overload
    def descendants(
        self,
        *,
        filter_type: None = None,
        include_subclasses: Literal[True] = True,
        include_shapes: bool = True,
    ) -> tuple["DAG", ...]: ...

    @overload
    def descendants(
        self,
        *,
        filter_type: type[_DAGType],
        include_subclasses: bool = True,
        include_shapes: bool = True,
    ) -> tuple[_DAGType, ...]: ...

    def descendants(
        self,
        *,
        filter_type: object = None,
        include_subclasses: object = True,
        include_shapes: object = True,
    ) -> tuple["DAG", ...]:
        """条件に一致する子孫をdepth-first pre-orderで返す。"""
        include_subclasses_value = _require_bool(
            include_subclasses,
            "include_subclasses",
        )
        include_shapes_value = _require_bool(
            include_shapes,
            "include_shapes",
        )
        if filter_type is None and not include_subclasses_value:
            raise ValueError("include_subclasses=False requires filter_type")

        dag_type = (
            None
            if filter_type is None
            else _require_dag_type(filter_type, "filter_type")
        )
        descendants: list[DAG] = []
        stack = list(reversed(self.children()))
        while stack:
            descendant = stack.pop()
            if _matches_shape_filter(
                descendant,
                include_shapes_value,
            ) and (
                dag_type is None
                or _matches_dag_type(
                    descendant,
                    dag_type,
                    include_subclasses_value,
                )
            ):
                descendants.append(descendant)
            stack.extend(reversed(descendant.children()))
        return tuple(descendants)

    @overload
    def descendant_chain(
        self,
        child_index: int = 0,
        *,
        until: None = None,
    ) -> tuple["DAG", ...]: ...

    @overload
    def descendant_chain(
        self,
        child_index: int = 0,
        *,
        until: "DAG | None",
    ) -> tuple["DAG", ...] | None: ...

    def descendant_chain(
        self,
        child_index: object = 0,
        *,
        until: object = None,
    ) -> tuple["DAG", ...] | None:
        """各階層で同じchild indexを選び、末端まで返す。"""
        if isinstance(child_index, bool) or not isinstance(child_index, int):
            raise TypeError(
                f"child_index must be int; got {type(child_index).__name__}"
            )
        if child_index < 0:
            raise ValueError(
                f"child_index must be non-negative; got {child_index}"
            )

        until_node = None if until is None else _require_dag(until, "until")
        chain: list[DAG] = []
        current = self
        until_found = until_node is None
        while True:
            fn_dag = om.MFnDagNode(current.m_obj)
            if child_index >= fn_dag.childCount():
                break
            current = self._wrap_existing_dag(fn_dag.child(child_index))
            chain.append(current)
            if until_node is not None and current.m_obj == until_node.m_obj:
                until_found = True
                break
        if not until_found:
            return None
        return tuple(chain)

    def _wrap_existing_dag(self, m_obj: om.MObject) -> "DAG":
        from ....existing_node import ExistingNode

        node = ExistingNode(
            m_obj,
            modifier_manager=self.modifier_manager,
            auto_add_attr=False,
        )
        if not isinstance(node, DAG):
            raise TypeError(
                "DAG hierarchy node did not resolve to DAG: "
                f"{type(node).__name__}"
            )
        return node

    def set_parent(self, parent: "DAG") -> Self:
        """local transform を維持して親変更を DAG modifier に積む。"""
        self._validate_set_parent(parent)
        self._dag_mod.reparentNode(self.m_obj, parent.m_obj)
        self.modifier_manager.record_pending_dag_parent(
            self.m_obj,
            parent.m_obj,
        )
        return self

    @staticmethod
    def _validate_parent(
        parent: "DAG",
        modifier_manager: ModifierManager,
    ) -> None:
        parent = _require_dag(parent, "parent")
        if not parent.m_obj.hasFn(om.MFn.kTransform):
            raise TypeError("parent must be a transform DAG node")
        if parent.is_instanced:
            raise RuntimeError(
                "an instanced DAG node cannot be used as parent: "
                f"{parent.name}"
            )
        if (
            not parent.full_path
            and parent.modifier_manager is not modifier_manager
        ):
            raise ValueError(
                "an uncommitted parent must share the same ModifierManager"
            )

    def _validate_set_parent(self, parent: "DAG") -> None:
        if self.is_instanced:
            raise RuntimeError(
                "set_parent is not supported for an instanced DAG node: "
                f"{self.name}"
            )
        self._validate_parent(parent, self.modifier_manager)
        if parent.m_obj == self.m_obj:
            raise ValueError("a DAG node cannot be parented to itself")
        if self.modifier_manager.would_create_dag_cycle(
            self.m_obj,
            parent.m_obj,
        ):
            raise ValueError("a DAG node cannot be parented to its descendant")

    @property
    def cmd_access_name(self) -> str:
        return self.full_path

    def _get_instance_transform_matrix(
        self,
        attribute_name: str,
    ) -> TransformMatrix:
        instance_index = self._dag_path.instanceNumber()
        matrix_plug = getattr(self, attribute_name)[instance_index]
        value = matrix_plug.get()
        if value is None:
            raise ValueError(
                f"Plug does not contain a matrix value: "
                f"{matrix_plug.plug.name()}"
            )
        return value

    def get_relative_matrix(self, dst_dag: "DAG") -> TransformMatrix:
        """self の行列を dst_dag 自身の空間で表して返す。"""
        dst_dag = _require_dag(dst_dag, "dst_dag")

        src_world_matrix = self._get_instance_transform_matrix("worldMatrix")
        dst_world_inverse_matrix = dst_dag._get_instance_transform_matrix(
            "worldInverseMatrix"
        )
        return src_world_matrix * dst_world_inverse_matrix

    def get_local_matrix(self, dst_dag: "DAG") -> TransformMatrix:
        """self の worldMatrix を再現する dst_dag の local 行列を返す。"""
        dst_dag = _require_dag(dst_dag, "dst_dag")

        src_world_matrix = self._get_instance_transform_matrix("worldMatrix")
        dst_parent_inverse_matrix = dst_dag._get_instance_transform_matrix(
            "parentInverseMatrix"
        )
        return src_world_matrix * dst_parent_inverse_matrix
