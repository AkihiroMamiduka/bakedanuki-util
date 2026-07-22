# coding: utf-8
from __future__ import annotations

import importlib
import keyword
import re
from collections.abc import Callable, Iterator
from importlib import resources

from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator
from ..operator.node.dag._core import DAG

_VALID_MODULE_NAME_PATTERN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_NODE_TYPE_PATTERN = re.compile(
    r"^\s*NODE_TYPE\s*=\s*[\"']([^\"']+)[\"']",
    re.MULTILINE,
)


def _camel_to_snake(name: str) -> str:
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", name)
    return name.lower().lstrip("_")


def _node_type_to_creator_name(node_type: str) -> str:
    if keyword.iskeyword(node_type):
        return f"{node_type}_"
    return node_type


def _node_module_name(package_name: str, module_name: str) -> str:
    if package_name.endswith(".transform") and module_name == "transform":
        return "_core"
    if package_name.endswith(".shape") and module_name == "shape":
        return "_core"
    return module_name


def _iter_node_module_paths(
    packages: tuple[str, ...],
    module_name: str,
) -> Iterator[str]:
    for package_name in packages:
        node_module_name = _node_module_name(package_name, module_name)
        package_files = resources.files(package_name)
        if not package_files.joinpath(f"{node_module_name}.py").is_file():
            continue
        yield f"{package_name}.{node_module_name}"


class NodeCreator:
    __slots__ = (
        "_modifier_manager",
        "_node_cls_cache",
        "_creator_cache",
        "_node_names_cache",
    )

    _DG_PACKAGE = "bd_util.maya.node.operator.node.dg"
    _DAG_PACKAGE = "bd_util.maya.node.operator.node.dag"
    _DAG_TRANSFORM_PACKAGE = "bd_util.maya.node.operator.node.dag.transform"
    _DAG_SHAPE_PACKAGE = "bd_util.maya.node.operator.node.dag.shape"
    _NODE_CLASS_PACKAGES = (
        _DG_PACKAGE,
        _DAG_PACKAGE,
        _DAG_TRANSFORM_PACKAGE,
        _DAG_SHAPE_PACKAGE,
    )
    _CREATOR_PACKAGES = (
        _DG_PACKAGE,
        _DAG_TRANSFORM_PACKAGE,
    )

    def __init__(self, modifier_manager: ModifierManager | None = None):
        self._modifier_manager = modifier_manager or ModifierManager()
        self._node_cls_cache: dict[
            tuple[tuple[str, ...], str], type[NodeOperator]
        ] = {}
        self._creator_cache: dict[str, Callable[..., NodeOperator]] = {}
        self._node_names_cache: tuple[str, ...] | None = None

    @property
    def modifier_manager(self) -> ModifierManager:
        return self._modifier_manager

    def create(
        self,
        node_name: str,
        name: str | None = None,
        auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
        *,
        parent: DAG | None = None,
    ) -> NodeOperator:
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
        return self._node_class_from_packages(
            node_name,
            self._NODE_CLASS_PACKAGES,
        )

    def _creator_node_class(self, node_name: str) -> type[NodeOperator]:
        return self._node_class_from_packages(
            node_name,
            self._CREATOR_PACKAGES,
        )

    def _node_class_from_packages(
        self,
        node_name: str,
        packages: tuple[str, ...],
    ) -> type[NodeOperator]:
        module_name = self._normalize_node_name(node_name)
        cache_key = (packages, module_name)

        cached = self._node_cls_cache.get(cache_key)
        if cached is not None:
            return cached

        module = None
        for module_path in _iter_node_module_paths(packages, module_name):
            try:
                module = importlib.import_module(module_path)
            except ModuleNotFoundError as e:
                if e.name == module_path:
                    continue
                raise
            break

        if module is None:
            raise AttributeError(f"Unsupported node type: {node_name}")

        node_classes = [
            obj
            for obj in vars(module).values()
            if isinstance(obj, type)
            and obj.__module__ == module.__name__
            and issubclass(obj, NodeOperator)
            and obj is not NodeOperator
            and getattr(obj, "NODE_TYPE", None) is not None
        ]
        if not node_classes:
            raise AttributeError(
                f"NodeOperator class not found: {module_path}"
            )
        if len(node_classes) > 1:
            class_names = ", ".join(cls.__name__ for cls in node_classes)
            raise RuntimeError(
                "{} {}: {}".format(
                    "Multiple NodeOperator classes found in",
                    module_path,
                    class_names,
                )
            )

        node_cls = node_classes[0]
        self._node_cls_cache[cache_key] = node_cls
        return node_cls

    def available_node_names(self) -> tuple[str, ...]:
        if self._node_names_cache is not None:
            return self._node_names_cache

        names: set[str] = set()
        for package_name in self._CREATOR_PACKAGES:
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
                names.add(_node_type_to_creator_name(node_type))

        sorted_names = sorted(names)
        self._node_names_cache = tuple(sorted_names)
        return self._node_names_cache

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        cached = self._creator_cache.get(node_name)
        if cached is not None:
            return cached

        node_cls = self._creator_node_class(node_name)

        if issubclass(node_cls, DAG):

            def _create(
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

        else:

            def _create(
                name: str | None = None,
                auto_add_attr: bool = DEFAULT_VALUE_AUTO_ADD_ATTR,
            ) -> NodeOperator:
                return node_cls.create(
                    self._modifier_manager,
                    name=name,
                    auto_add_attr=auto_add_attr,
                )

        _create.__name__ = node_name
        _create.__qualname__ = f"{type(self).__name__}.{node_name}"
        _create.__doc__ = f"Create {node_cls.__name__}."
        self._creator_cache[node_name] = _create
        return _create

    def __dir__(self) -> list[str]:
        return sorted(
            set(super().__dir__()) | set(self.available_node_names())
        )

    @staticmethod
    def _normalize_node_name(node_name: str) -> str:
        if not isinstance(node_name, str):
            raise TypeError(f"node_name must be str: {type(node_name)}")

        module_name = _camel_to_snake(node_name)
        if module_name.endswith("_") and keyword.iskeyword(module_name[:-1]):
            module_name = module_name[:-1]

        if not _VALID_MODULE_NAME_PATTERN.fullmatch(module_name):
            raise AttributeError(f"Unsupported node type: {node_name}")
        return module_name


def _read_node_type(code: str) -> str:
    match = _NODE_TYPE_PATTERN.search(code)
    if match is None:
        raise ValueError("NODE_TYPE definition not found.")
    return match.group(1)
