# coding: utf-8
from __future__ import annotations

import importlib
import keyword
import re
from collections.abc import Callable
from importlib import resources

from ..modifier import ModifierManager
from ..operator.node._core import DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator

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


class NodeCreater:
    __slots__ = (
        "_modifier_manager",
        "_node_cls_cache",
        "_creator_cache",
        "_node_names_cache",
    )

    _DG_PACKAGE = "bd_util.maya.node.operator.node.dg"

    def __init__(self, modifier_manager: ModifierManager | None = None):
        self._modifier_manager = modifier_manager or ModifierManager()
        self._node_cls_cache: dict[str, type[NodeOperator]] = {}
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
    ) -> NodeOperator:
        node_cls = self.node_class(node_name)
        return node_cls.create(
            self._modifier_manager,
            name=name,
            auto_add_attr=auto_add_attr,
        )

    def node_class(self, node_name: str) -> type[NodeOperator]:
        module_name = self._normalize_node_name(node_name)

        cached = self._node_cls_cache.get(module_name)
        if cached is not None:
            return cached

        module_path = f"{self._DG_PACKAGE}.{module_name}"
        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError as e:
            if e.name == module_path:
                raise AttributeError(
                    f"Unsupported node type: {node_name}"
                ) from e
            raise

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
                f"Multiple NodeOperator classes found in {module_path}: {class_names}"
            )

        node_cls = node_classes[0]
        self._node_cls_cache[module_name] = node_cls
        return node_cls

    def available_node_names(self) -> tuple[str, ...]:
        if self._node_names_cache is not None:
            return self._node_names_cache

        package_files = resources.files(self._DG_PACKAGE)
        names = sorted(
            _node_type_to_creator_name(
                _read_node_type(path.read_text(encoding="utf-8"))
            )
            for path in package_files.iterdir()
            if path.is_file()
            and path.name.endswith(".py")
            and path.name not in {"_core.py", "__init__.py"}
        )
        self._node_names_cache = tuple(names)
        return self._node_names_cache

    def __getattr__(self, node_name: str) -> Callable[..., NodeOperator]:
        if node_name.startswith("_"):
            raise AttributeError(node_name)

        cached = self._creator_cache.get(node_name)
        if cached is not None:
            return cached

        node_cls = self.node_class(node_name)

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
