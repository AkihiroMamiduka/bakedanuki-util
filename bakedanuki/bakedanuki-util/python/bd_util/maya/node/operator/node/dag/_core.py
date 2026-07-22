# coding: utf-8
from typing import Self

# maya
from maya.api import OpenMaya as om

# self
from ....modifier import ModifierManager
from .....transform import TransformMatrix
from .._core import NodeOperator, DEFAULT_VALUE_AUTO_ADD_ATTR


class DAG(NodeOperator):
    __slots__ = ("_dag_path",)

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        auto_add_attr = kwargs.pop(
            "auto_add_attr", DEFAULT_VALUE_AUTO_ADD_ATTR
        )
        rename_name = None
        if kwargs.get("m_obj") is not None and kwargs.get("name"):
            rename_name = kwargs.pop("name")

        super().__init__(*args, auto_add_attr=False, **kwargs)

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
        name=None,
        auto_add_attr=DEFAULT_VALUE_AUTO_ADD_ATTR,
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
        from ....existing_node import ExistingNode

        fn_dag = om.MFnDagNode(self.m_obj)
        parents = []
        for index in range(fn_dag.parentCount()):
            parent_obj = fn_dag.parent(index)
            if parent_obj.hasFn(om.MFn.kWorld):
                continue
            parent = ExistingNode(
                parent_obj,
                modifier_manager=self.modifier_manager,
                auto_add_attr=False,
            )
            if not isinstance(parent, DAG):
                raise TypeError(
                    "DAG parent did not resolve to DAG: "
                    f"{type(parent).__name__}"
                )
            parents.append(parent)
        return tuple(parents)

    def set_parent(self, parent: "DAG") -> Self:
        """local transform を維持して親変更を DAG modifier に積む。"""
        self._validate_set_parent(parent)
        self._dag_mod.reparentNode(self.m_obj, parent.m_obj)
        return self

    @staticmethod
    def _validate_parent(
        parent: "DAG",
        modifier_manager: ModifierManager,
    ) -> None:
        if not isinstance(parent, DAG):
            raise TypeError(f"parent must be DAG; got {type(parent).__name__}")
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

    @property
    def _cmd_access_name(self) -> str:
        return self.full_path

    def _get_instance_transform_matrix(
        self,
        attribute_name: str,
    ) -> TransformMatrix:
        instance_index = self._dag_path.instanceNumber()
        matrix_plug = getattr(self, attribute_name)[instance_index]
        return matrix_plug.transform_matrix

    def get_relative_matrix(self, dst_dag: "DAG") -> TransformMatrix:
        """self の行列を dst_dag 自身の空間で表して返す。"""
        if not isinstance(dst_dag, DAG):
            raise TypeError(
                f"dst_dag must be DAG; got {type(dst_dag).__name__}"
            )

        src_world_matrix = self._get_instance_transform_matrix("worldMatrix")
        dst_world_inverse_matrix = dst_dag._get_instance_transform_matrix(
            "worldInverseMatrix"
        )
        return src_world_matrix * dst_world_inverse_matrix

    def get_local_matrix(self, dst_dag: "DAG") -> TransformMatrix:
        """self の worldMatrix を再現する dst_dag の local 行列を返す。"""
        if not isinstance(dst_dag, DAG):
            raise TypeError(
                f"dst_dag must be DAG; got {type(dst_dag).__name__}"
            )

        src_world_matrix = self._get_instance_transform_matrix("worldMatrix")
        dst_parent_inverse_matrix = dst_dag._get_instance_transform_matrix(
            "parentInverseMatrix"
        )
        return src_world_matrix * dst_parent_inverse_matrix
