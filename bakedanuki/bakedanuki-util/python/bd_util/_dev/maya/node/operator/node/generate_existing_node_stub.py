# coding: utf-8
from __future__ import annotations

import argparse
import ast
import keyword
import re
from dataclasses import dataclass
from pathlib import Path
from typing import cast

_ABSTRACT_NODE_TYPES = frozenset({"baseGeometryVarGroup", "shape"})
_SUPPORTED_MAYA_VERSIONS = (2025, 2026, 2027)


@dataclass(frozen=True)
class NodeDefinition:
    method_name: str
    node_type: str
    class_name: str
    module_name: str

    @property
    def can_import(self) -> bool:
        return all(
            not keyword.iskeyword(part)
            for part in self.module_name.lstrip(".").split(".")
        )

    @property
    def return_type(self) -> str:
        if self.can_import:
            return self.class_name
        return "NodeOperator"


def _find_node_definition(
    path: Path,
    node_dir: Path,
) -> NodeDefinition | None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    definitions: list[NodeDefinition] = []

    for statement in tree.body:
        if not isinstance(statement, ast.ClassDef):
            continue
        if statement.name.startswith("_"):
            continue
        for class_statement in statement.body:
            if not isinstance(class_statement, ast.Assign):
                continue
            if not any(
                isinstance(target, ast.Name) and target.id == "NODE_TYPE"
                for target in class_statement.targets
            ):
                continue
            value = class_statement.value
            if not isinstance(value, ast.Constant) or not isinstance(
                value.value, str
            ):
                continue

            node_type = value.value
            if node_type in _ABSTRACT_NODE_TYPES:
                continue
            method_name = (
                f"{node_type}_" if keyword.iskeyword(node_type) else node_type
            )
            if not method_name.isidentifier():
                raise ValueError(
                    f"nodeType cannot be exposed as a method: {node_type!r}"
                )

            relative_module = path.relative_to(node_dir).with_suffix("")
            module_name = "." + ".".join(relative_module.parts)
            definitions.append(
                NodeDefinition(
                    method_name=method_name,
                    node_type=node_type,
                    class_name=statement.name,
                    module_name=module_name,
                )
            )

    if not definitions:
        return None
    if len(definitions) > 1:
        raise ValueError(f"Multiple node classes found: {path}")
    return definitions[0]


def collect_node_definitions(python_root: Path) -> tuple[NodeDefinition, ...]:
    node_dir = python_root / "bd_util" / "maya" / "node"
    operator_dir = node_dir / "operator" / "node"
    package_dirs = (
        operator_dir / "dg",
        operator_dir / "dag",
        operator_dir / "dag" / "transform",
        operator_dir / "dag" / "shape",
    )

    definitions: list[NodeDefinition] = []
    for package_dir in package_dirs:
        for path in sorted(package_dir.glob("*.py")):
            definition = _find_node_definition(path, node_dir)
            if definition is not None:
                definitions.append(definition)

    definitions.sort(key=lambda definition: definition.method_name)

    method_names = [definition.method_name for definition in definitions]
    if len(method_names) != len(set(method_names)):
        raise ValueError("Duplicate ExistingNode method names found")

    class_names = [definition.class_name for definition in definitions]
    if len(class_names) != len(set(class_names)):
        raise ValueError("Duplicate NodeOperator class names found")

    return tuple(definitions)


def _collect_creatable_node_types(
    python_root: Path,
    *,
    types_filename: str,
    variable_name: str,
) -> frozenset[str]:
    types_path = (
        python_root / "bd_util" / "maya" / "node" / "creator" / types_filename
    )
    tree = ast.parse(
        types_path.read_text(encoding="utf-8"),
        filename=str(types_path),
    )
    node_types: frozenset[str] | None = None
    for statement in tree.body:
        if not isinstance(statement, ast.Assign):
            continue
        if not any(
            isinstance(target, ast.Name) and target.id == variable_name
            for target in statement.targets
        ):
            continue
        value = statement.value
        if (
            not isinstance(value, ast.Call)
            or not isinstance(value.func, ast.Name)
            or value.func.id != "frozenset"
            or len(value.args) != 1
        ):
            break
        literal = cast(object, ast.literal_eval(value.args[0]))
        if not isinstance(literal, set):
            break
        literal_items = cast(set[object], literal)
        if not all(isinstance(item, str) for item in literal_items):
            break
        node_types = frozenset(cast(set[str], literal_items))
        break

    if node_types is None:
        raise ValueError(f"{variable_name} definition not found or invalid")
    return node_types


def _collect_creatable_definitions(
    python_root: Path,
    *,
    types_filename: str,
    variable_name: str,
    module_prefix: str,
) -> tuple[NodeDefinition, ...]:
    node_types = _collect_creatable_node_types(
        python_root,
        types_filename=types_filename,
        variable_name=variable_name,
    )

    definitions = tuple(
        definition
        for definition in collect_node_definitions(python_root)
        if definition.node_type in node_types
        and definition.module_name.startswith(module_prefix)
    )
    found_node_types = {definition.node_type for definition in definitions}
    missing_node_types = node_types - found_node_types
    if missing_node_types:
        missing = ", ".join(sorted(missing_node_types))
        raise ValueError(f"Creatable node definitions not found: {missing}")
    return definitions


def collect_creatable_shape_definitions(
    python_root: Path,
) -> tuple[NodeDefinition, ...]:
    return _collect_creatable_definitions(
        python_root,
        types_filename="_shape_types.py",
        variable_name="CREATABLE_SHAPE_NODE_TYPES",
        module_prefix=".operator.node.dag.shape.",
    )


def collect_creatable_transform_definitions(
    python_root: Path,
) -> tuple[NodeDefinition, ...]:
    return _collect_creatable_definitions(
        python_root,
        types_filename="_transform_types.py",
        variable_name="CREATABLE_TRANSFORM_NODE_TYPES",
        module_prefix=".operator.node.dag.transform.",
    )


def _collect_node_type_version_ranges(
    python_root: Path,
) -> dict[str, tuple[tuple[int, int | None], ...]]:
    registry_path = (
        python_root / "bd_util" / "maya" / "node" / "_node_version_registry.py"
    )
    tree = ast.parse(
        registry_path.read_text(encoding="utf-8"),
        filename=str(registry_path),
    )
    for statement in tree.body:
        if not isinstance(statement, ast.AnnAssign):
            continue
        if (
            not isinstance(statement.target, ast.Name)
            or statement.target.id != "NODE_TYPE_VERSION_RANGES"
            or statement.value is None
        ):
            continue
        value = cast(object, ast.literal_eval(statement.value))
        if not isinstance(value, dict):
            break
        return cast(
            dict[str, tuple[tuple[int, int | None], ...]],
            value,
        )
    raise ValueError("NODE_TYPE_VERSION_RANGES definition not found")


def _definition_is_available(
    definition: NodeDefinition,
    maya_version: int,
    version_ranges: dict[str, tuple[tuple[int, int | None], ...]],
) -> bool:
    ranges = version_ranges.get(definition.node_type, ((2025, None),))
    return any(
        maya_version >= minimum and (maximum is None or maya_version < maximum)
        for minimum, maximum in ranges
    )


def _definition_introduced_version(
    definition: NodeDefinition,
    version_ranges: dict[str, tuple[tuple[int, int | None], ...]],
) -> int:
    ranges = version_ranges.get(definition.node_type, ((2025, None),))
    return min(minimum for minimum, _ in ranges)


def _generated_module_name(definition: NodeDefinition) -> str:
    module_name = definition.module_name.rsplit(".", 1)[-1]
    if module_name != "_core":
        return module_name

    node_type = definition.node_type
    node_type = re.sub(
        r"([A-Z]+)([A-Z][a-z])",
        r"\1_\2",
        node_type,
    )
    node_type = re.sub(
        r"([a-z\d])([A-Z])",
        r"\1_\2",
        node_type,
    )
    return node_type.lower().lstrip("_")


def _overlay_module_name(
    definition: NodeDefinition,
    maya_version: int,
) -> str:
    package_name = definition.module_name.rsplit(".", 1)[0]
    return "{}._generated_maya{}.{}".format(
        package_name,
        maya_version,
        _generated_module_name(definition),
    )


def _overlay_path(
    python_root: Path,
    definition: NodeDefinition,
    maya_version: int,
) -> Path:
    node_dir = python_root / "bd_util" / "maya" / "node"
    module_parts = (
        _overlay_module_name(
            definition,
            maya_version,
        )
        .lstrip(".")
        .split(".")
    )
    return node_dir.joinpath(*module_parts).with_suffix(".py")


def _versioned_type_name(
    definition: NodeDefinition,
    maya_version: int,
) -> str:
    return f"_{definition.class_name}Maya{maya_version}"


def _effective_return_type(
    python_root: Path,
    definition: NodeDefinition,
    maya_version: int,
    version_ranges: dict[str, tuple[tuple[int, int | None], ...]],
) -> str:
    if not definition.can_import:
        return "NodeOperator"

    introduced_version = _definition_introduced_version(
        definition,
        version_ranges,
    )
    effective_overlay_versions = [
        version
        for version in _SUPPORTED_MAYA_VERSIONS
        if introduced_version < version <= maya_version
        and _overlay_path(python_root, definition, version).is_file()
    ]
    if effective_overlay_versions:
        return _versioned_type_name(
            definition,
            max(effective_overlay_versions),
        )
    return f"_{definition.class_name}"


def _common_return_type(
    python_root: Path,
    definition: NodeDefinition,
    version_ranges: dict[str, tuple[tuple[int, int | None], ...]],
) -> str:
    return_types = tuple(
        dict.fromkeys(
            _effective_return_type(
                python_root,
                definition,
                maya_version,
                version_ranges,
            )
            for maya_version in _SUPPORTED_MAYA_VERSIONS
        )
    )
    return " | ".join(return_types)


def _collect_creator_definitions(
    python_root: Path,
) -> tuple[NodeDefinition, ...]:
    creatable_dag_node_types = {
        definition.node_type
        for definition in (
            *collect_creatable_transform_definitions(python_root),
            *collect_creatable_shape_definitions(python_root),
        )
    }
    return tuple(
        definition
        for definition in collect_node_definitions(python_root)
        if definition.module_name.startswith(".operator.node.dg.")
        or definition.node_type in creatable_dag_node_types
    )


def _append_existing_accessor_method(
    lines: list[str],
    definition: NodeDefinition,
    return_type: str,
) -> None:
    lines.extend(
        [
            "",
            f"    def {definition.method_name}(",
            "        self,",
            "        node: str | om.MObject,",
            "        auto_add_attr: bool = False,",
            f"    ) -> {return_type}: ...",
        ]
    )


def _append_creator_method(
    lines: list[str],
    definition: NodeDefinition,
    return_type: str,
) -> None:
    lines.extend(
        [
            "",
            f"    def {definition.method_name}(",
            "        self,",
            "        name: str | None = None,",
            ("        auto_add_attr: bool = " "DEFAULT_VALUE_AUTO_ADD_ATTR,"),
        ]
    )
    if definition.module_name.startswith(".operator.node.dag.shape."):
        lines.extend(
            [
                "        *,",
                "        parent: Transform,",
            ]
        )
    elif definition.module_name.startswith(".operator.node.dag.transform."):
        lines.extend(
            [
                "        *,",
                "        parent: DAG | None = None,",
            ]
        )
    lines.append(f"    ) -> {return_type}: ...")


def _append_shape_with_transform_method(
    lines: list[str],
    definition: NodeDefinition,
    return_type: str,
) -> None:
    lines.extend(
        [
            "",
            f"    def {definition.method_name}(",
            "        self,",
            "        name: str | None = None,",
            ("        auto_add_attr: bool = " "DEFAULT_VALUE_AUTO_ADD_ATTR,"),
            "        *,",
            "        shape_name: str | None = None,",
            "        parent: DAG | None = None,",
            f"    ) -> tuple[Transform, {return_type}]: ...",
        ]
    )


def _append_node_types_property(
    lines: list[str],
    class_name: str,
    return_type: str,
) -> None:
    lines.extend(
        [
            "",
            "    @property",
            f"    def {class_name}(self) -> type[{return_type}]: ...",
        ]
    )


def _version_facade_requires_override(
    python_root: Path,
    definition: NodeDefinition,
    maya_version: int,
    common_node_types: set[str],
    version_ranges: dict[str, tuple[tuple[int, int | None], ...]],
) -> bool:
    if definition.node_type not in common_node_types:
        return True
    return _effective_return_type(
        python_root,
        definition,
        maya_version,
        version_ranges,
    ) != _common_return_type(
        python_root,
        definition,
        version_ranges,
    )


def _node_wrapper_class(
    python_root: Path,
    definition: NodeDefinition,
) -> ast.ClassDef | None:
    module_parts = definition.module_name.lstrip(".").split(".")
    wrapper_path = (
        (python_root / "bd_util" / "maya" / "node")
        .joinpath(*module_parts)
        .with_suffix(".py")
    )
    tree = ast.parse(
        wrapper_path.read_text(encoding="utf-8"),
        filename=str(wrapper_path),
    )
    return next(
        (
            statement
            for statement in tree.body
            if isinstance(statement, ast.ClassDef)
            and statement.name == definition.class_name
        ),
        None,
    )


def _node_wrapper_is_schema_only(
    python_root: Path,
    definition: NodeDefinition,
) -> bool:
    wrapper_class = _node_wrapper_class(python_root, definition)
    if wrapper_class is None:
        return False

    for statement in wrapper_class.body:
        if isinstance(statement, ast.Pass):
            continue
        if (
            isinstance(statement, ast.Expr)
            and isinstance(statement.value, ast.Constant)
            and isinstance(statement.value.value, str)
        ):
            continue
        if isinstance(statement, ast.Assign) and all(
            isinstance(target, ast.Name)
            and target.id in {"__slots__", "NODE_TYPE"}
            for target in statement.targets
        ):
            continue
        if (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.target.id in {"__slots__", "NODE_TYPE"}
        ):
            continue
        return False
    return True


def _node_wrapper_mixins(
    python_root: Path, definition: NodeDefinition
) -> tuple[str, ...]:
    wrapper = _node_wrapper_class(python_root, definition)
    generated = f"Generated{definition.class_name}"
    if (
        wrapper is None
        or not wrapper.bases
        or not all(isinstance(base, ast.Name) for base in wrapper.bases)
        or ast.unparse(wrapper.bases[0]) != generated
    ):
        raise ValueError(
            f"Versioned wrapper {definition.class_name} requires a generated base followed by named behavior mixins."
        )
    return tuple(ast.unparse(base) for base in wrapper.bases[1:])


def generate_versioned_accessors_stub_code(python_root: Path) -> str:
    definitions = collect_node_definitions(python_root)
    definitions_by_type = {
        definition.node_type: definition for definition in definitions
    }
    creator_definitions = _collect_creator_definitions(python_root)
    shape_definitions = collect_creatable_shape_definitions(python_root)
    version_ranges = _collect_node_type_version_ranges(python_root)

    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "from maya.api import OpenMaya as om",
        "",
        "from .modifier import ModifierManager",
        (
            "from .operator.node._core import "
            "DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator"
        ),
        "from .operator.node.dag._core import DAG",
        "from .operator.node.dag.shape._core import Shape",
        "from .operator.node.dag.transform._core import Transform",
        (
            "from .operator.node.dag.transform.base_geometry_var_group "
            "import BaseGeometryVarGroup"
        ),
    ]
    lines.extend(
        "from {} import {} as _{}".format(
            definition.module_name,
            definition.class_name,
            definition.class_name,
        )
        for definition in definitions
        if definition.can_import
    )

    variants: list[tuple[NodeDefinition, int]] = []
    for definition in definitions:
        if not definition.can_import:
            continue
        introduced_version = _definition_introduced_version(
            definition,
            version_ranges,
        )
        for maya_version in _SUPPORTED_MAYA_VERSIONS:
            if (
                introduced_version < maya_version
                and _overlay_path(
                    python_root,
                    definition,
                    maya_version,
                ).is_file()
            ):
                variants.append((definition, maya_version))

    custom_variant_wrappers = sorted(
        {
            definition.class_name
            for definition, _ in variants
            if not _node_wrapper_is_schema_only(python_root, definition)
        }
    )
    if custom_variant_wrappers:
        names = ", ".join(custom_variant_wrappers)
        raise ValueError(
            "Versioned schema wrappers must not define custom members: "
            f"{names}"
        )

    lines.extend(
        "from {} import Generated{} as _Generated{}Maya{}".format(
            _overlay_module_name(definition, maya_version),
            definition.class_name,
            definition.class_name,
            maya_version,
        )
        for definition, maya_version in variants
    )

    mixins_by_type = {
        definition.node_type: _node_wrapper_mixins(python_root, definition)
        for definition, _ in variants
    }
    for definition in definitions:
        for mixin in mixins_by_type.get(definition.node_type, ()):
            lines.append(
                f"from {definition.module_name} import {mixin} as _{definition.class_name}{mixin}"
            )

    for definition, maya_version in variants:
        bases = [f"_Generated{definition.class_name}Maya{maya_version}"]
        bases.extend(
            f"_{definition.class_name}{mixin}"
            for mixin in mixins_by_type[definition.node_type]
        )
        lines.extend(
            [
                "",
                "",
                "class {}(".format(
                    _versioned_type_name(definition, maya_version)
                ),
                "    " + ", ".join(bases),
                "): ...",
            ]
        )

    common_definitions = tuple(
        definition
        for definition in definitions
        if all(
            _definition_is_available(
                definition,
                maya_version,
                version_ranges,
            )
            for maya_version in _SUPPORTED_MAYA_VERSIONS
        )
    )
    common_node_types = {
        definition.node_type for definition in common_definitions
    }

    lines.extend(
        [
            "",
            "",
            "class _ShapeWithTransformCreatorCommon:",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "    def create(",
            "        self,",
            "        node_name: str,",
            "        name: str | None = None,",
            ("        auto_add_attr: bool = " "DEFAULT_VALUE_AUTO_ADD_ATTR,"),
            "        *,",
            "        shape_name: str | None = None,",
            "        parent: DAG | None = None,",
            "    ) -> tuple[Transform, Shape]: ...",
            "    def available_node_names(self) -> tuple[str, ...]: ...",
        ]
    )
    for definition in shape_definitions:
        if definition.node_type not in common_node_types:
            continue
        _append_shape_with_transform_method(
            lines,
            definition,
            _common_return_type(
                python_root,
                definition,
                version_ranges,
            ),
        )

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "",
                "",
                f"class _ShapeWithTransformCreatorMaya{maya_version}(",
                "    _ShapeWithTransformCreatorCommon",
                "):",
            ]
        )
        for definition in shape_definitions:
            if not _definition_is_available(
                definition,
                maya_version,
                version_ranges,
            ):
                continue
            if not _version_facade_requires_override(
                python_root,
                definition,
                maya_version,
                common_node_types,
                version_ranges,
            ):
                continue
            _append_shape_with_transform_method(
                lines,
                definition,
                _effective_return_type(
                    python_root,
                    definition,
                    maya_version,
                    version_ranges,
                ),
            )

    lines.extend(
        [
            "",
            "",
            "class _NodeCreatorCommon:",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "    @property",
            (
                "    def with_transform(self) -> "
                "_ShapeWithTransformCreatorCommon: ..."
            ),
            "    def create(",
            "        self,",
            "        node_name: str,",
            "        name: str | None = None,",
            ("        auto_add_attr: bool = " "DEFAULT_VALUE_AUTO_ADD_ATTR,"),
            "        *,",
            "        parent: DAG | None = None,",
            "    ) -> NodeOperator: ...",
            (
                "    def node_class(self, node_name: str) "
                "-> type[NodeOperator]: ..."
            ),
            "    def available_node_names(self) -> tuple[str, ...]: ...",
        ]
    )
    for definition in creator_definitions:
        if definition.node_type not in common_node_types:
            continue
        _append_creator_method(
            lines,
            definition,
            _common_return_type(
                python_root,
                definition,
                version_ranges,
            ),
        )

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "",
                "",
                f"class _NodeCreatorMaya{maya_version}(_NodeCreatorCommon):",
                "    @property",
                (
                    "    def with_transform(self) -> "
                    f"_ShapeWithTransformCreatorMaya{maya_version}: ..."
                ),
            ]
        )
        for definition in creator_definitions:
            if not _definition_is_available(
                definition,
                maya_version,
                version_ranges,
            ):
                continue
            if not _version_facade_requires_override(
                python_root,
                definition,
                maya_version,
                common_node_types,
                version_ranges,
            ):
                continue
            _append_creator_method(
                lines,
                definition,
                _effective_return_type(
                    python_root,
                    definition,
                    maya_version,
                    version_ranges,
                ),
            )

    lines.extend(
        [
            "",
            "",
            "class _ExistingNodeAccessorCommon:",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "    def __call__(",
            "        self,",
            "        node: str | om.MObject,",
            "        auto_add_attr: bool = False,",
            "    ) -> NodeOperator: ...",
        ]
    )
    for definition in common_definitions:
        _append_existing_accessor_method(
            lines,
            definition,
            _common_return_type(
                python_root,
                definition,
                version_ranges,
            ),
        )

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "",
                "",
                f"class _ExistingNodeAccessorMaya{maya_version}(",
                "    _ExistingNodeAccessorCommon",
                "):",
            ]
        )
        for definition in definitions:
            if not _definition_is_available(
                definition,
                maya_version,
                version_ranges,
            ):
                continue
            if not _version_facade_requires_override(
                python_root,
                definition,
                maya_version,
                common_node_types,
                version_ranges,
            ):
                continue
            _append_existing_accessor_method(
                lines,
                definition,
                _effective_return_type(
                    python_root,
                    definition,
                    maya_version,
                    version_ranges,
                ),
            )

    base_node_types = (
        ("BaseGeometryVarGroup", "BaseGeometryVarGroup"),
        ("DAG", "DAG"),
        ("NodeOperator", "NodeOperator"),
        ("Shape", "Shape"),
    )
    lines.extend(
        [
            "",
            "",
            "class _NodeTypesCommon:",
            "    def resolve(",
            "        self,",
            "        node_type: str,",
            "    ) -> type[NodeOperator]: ...",
            "    def available_class_names(self) -> tuple[str, ...]: ...",
        ]
    )
    for class_name, return_type in base_node_types:
        _append_node_types_property(lines, class_name, return_type)
    for definition in common_definitions:
        _append_node_types_property(
            lines,
            definition.class_name,
            _common_return_type(
                python_root,
                definition,
                version_ranges,
            ),
        )

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "",
                "",
                f"class _NodeTypesMaya{maya_version}(_NodeTypesCommon):",
            ]
        )
        for definition in definitions:
            if not _definition_is_available(
                definition,
                maya_version,
                version_ranges,
            ):
                continue
            if not _version_facade_requires_override(
                python_root,
                definition,
                maya_version,
                common_node_types,
                version_ranges,
            ):
                continue
            _append_node_types_property(
                lines,
                definition.class_name,
                _effective_return_type(
                    python_root,
                    definition,
                    maya_version,
                    version_ranges,
                ),
            )

    missing_versioned_node_types = set(version_ranges) - set(
        definitions_by_type
    )
    if missing_versioned_node_types:
        missing = ", ".join(sorted(missing_versioned_node_types))
        raise ValueError(f"Versioned node definitions not found: {missing}")

    return "\n".join(lines) + "\n"


def generate_existing_node_stub_code(python_root: Path) -> str:
    definitions = collect_node_definitions(python_root)
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "from maya.api import OpenMaya as om",
        "",
        "from .modifier import ModifierManager",
        "from .operator.node._core import NodeOperator",
    ]

    lines.extend(
        "from {} import {}".format(
            definition.module_name,
            definition.class_name,
        )
        for definition in definitions
        if definition.can_import
    )
    lines.extend(
        [
            "",
            "",
            "class ExistingNode:",
            "    def __new__(",
            "        cls,",
            "        node: str | om.MObject,",
            "        modifier_manager: ModifierManager | None = None,",
            "        auto_add_attr: bool = False,",
            "    ) -> NodeOperator: ...",
        ]
    )

    for definition in definitions:
        lines.extend(
            [
                "",
                "    @staticmethod",
                f"    def {definition.method_name}(",
                "        node: str | om.MObject,",
                "        modifier_manager: ModifierManager | None = None,",
                "        auto_add_attr: bool = False,",
                f"    ) -> {definition.return_type}: ...",
            ]
        )

    return "\n".join(lines) + "\n"


def generate_nodes_stub_code(python_root: Path) -> str:
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "from typing import Literal, overload",
        "",
        "from .modifier import ModifierManager",
        "from ._versioned_accessors import (",
        "    _ExistingNodeAccessorCommon,",
        "    _ExistingNodeAccessorMaya2025,",
        "    _ExistingNodeAccessorMaya2026,",
        "    _ExistingNodeAccessorMaya2027,",
        "    _NodeCreatorCommon,",
        "    _NodeCreatorMaya2025,",
        "    _NodeCreatorMaya2026,",
        "    _NodeCreatorMaya2027,",
        "    _NodeTypesCommon,",
        "    _NodeTypesMaya2025,",
        "    _NodeTypesMaya2026,",
        "    _NodeTypesMaya2027,",
        ")",
        "",
        "",
        "class Nodes:",
    ]

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "    @overload",
                "    def __new__(",
                "        cls,",
                "        modifier_manager: ModifierManager | None = None,",
                "        *,",
                (
                    "        typing_maya_version: "
                    f'Literal["{maya_version}"],'
                ),
                f"    ) -> _NodesMaya{maya_version}: ...",
                "",
            ]
        )
    lines.extend(
        [
            "    @overload",
            "    def __new__(",
            "        cls,",
            "        modifier_manager: ModifierManager | None = None,",
            "        *,",
            "        typing_maya_version: None = None,",
            "    ) -> Nodes: ...",
            "",
            "    def __init__(",
            "        self,",
            "        modifier_manager: ModifierManager | None = None,",
            "        *,",
            (
                "        typing_maya_version: "
                'Literal["2025", "2026", "2027"] | None = None,'
            ),
            "    ) -> None: ...",
            "",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "",
            "    @property",
            "    def create(self) -> _NodeCreatorCommon: ...",
            "",
            "    @property",
            ("    def existing(self) -> " "_ExistingNodeAccessorCommon: ..."),
            "",
            "    @property",
            "    def types(self) -> _NodeTypesCommon: ...",
        ]
    )

    for maya_version in _SUPPORTED_MAYA_VERSIONS:
        lines.extend(
            [
                "",
                "",
                f"class _NodesMaya{maya_version}(Nodes):",
                "    @property",
                (
                    "    def create(self) -> "
                    f"_NodeCreatorMaya{maya_version}: ..."
                ),
                "",
                "    @property",
                (
                    "    def existing(self) -> "
                    f"_ExistingNodeAccessorMaya{maya_version}: ..."
                ),
                "",
                "    @property",
                (
                    "    def types(self) -> "
                    f"_NodeTypesMaya{maya_version}: ..."
                ),
            ]
        )

    return "\n".join(lines) + "\n"


def generate_node_type_registry_code(python_root: Path) -> str:
    definitions = sorted(
        collect_node_definitions(python_root),
        key=lambda definition: definition.class_name,
    )
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "NODE_TYPE_BY_CLASS_NAME: dict[str, str] = {",
    ]
    lines.extend(
        f"    {definition.class_name!r}: {definition.node_type!r},"
        for definition in definitions
    )
    lines.extend(["}", ""])
    return "\n".join(lines)


def generate_node_types_stub_code(python_root: Path) -> str:
    definitions = sorted(
        collect_node_definitions(python_root),
        key=lambda definition: definition.class_name,
    )
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        ("from .operator.node._core import " "NodeOperator as _NodeOperator"),
        "from .operator.node.dag._core import DAG as _DAG",
        ("from .operator.node.dag.shape._core import " "Shape as _Shape"),
        (
            "from .operator.node.dag.transform.base_geometry_var_group "
            "import BaseGeometryVarGroup as _BaseGeometryVarGroup"
        ),
    ]
    lines.extend(
        "from {} import {} as _{}".format(
            definition.module_name,
            definition.class_name,
            definition.class_name,
        )
        for definition in definitions
        if definition.can_import
    )
    lines.extend(
        [
            "",
            "",
            "class NodeTypes:",
            "    def resolve(",
            "        self,",
            "        node_type: str,",
            "    ) -> type[_NodeOperator]: ...",
            "",
            ("    def available_class_names(self) " "-> tuple[str, ...]: ..."),
        ]
    )

    base_classes = (
        ("BaseGeometryVarGroup", "_BaseGeometryVarGroup"),
        ("DAG", "_DAG"),
        ("NodeOperator", "_NodeOperator"),
        ("Shape", "_Shape"),
    )
    node_classes = tuple(
        (
            definition.class_name,
            (
                f"_{definition.class_name}"
                if definition.can_import
                else "_NodeOperator"
            ),
        )
        for definition in definitions
    )
    for class_name, return_type in sorted(base_classes + node_classes):
        lines.extend(
            [
                "",
                "    @property",
                f"    def {class_name}(self) -> type[{return_type}]: ...",
            ]
        )

    return "\n".join(lines) + "\n"


def generate_transform_creator_stub_code(python_root: Path) -> str:
    definitions = collect_creatable_transform_definitions(python_root)
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        ("from ..operator.node._core import " "DEFAULT_VALUE_AUTO_ADD_ATTR"),
    ]
    lines.extend(
        "from .{} import {}".format(
            definition.module_name,
            definition.class_name,
        )
        for definition in definitions
        if definition.can_import
    )
    lines.extend(
        [
            "",
            "",
            "class _TransformNodeCreatorMixin:",
        ]
    )

    for definition in definitions:
        lines.extend(
            [
                "",
                f"    def {definition.method_name}(",
                "        self,",
                "        name: str | None = None,",
                (
                    "        auto_add_attr: bool = "
                    "DEFAULT_VALUE_AUTO_ADD_ATTR,"
                ),
                "        *,",
                "        parent: Transform | None = None,",
                f"    ) -> {definition.return_type}: ...",
            ]
        )

    return "\n".join(lines) + "\n"


def generate_shape_with_transform_stub_code(python_root: Path) -> str:
    definitions = collect_creatable_shape_definitions(python_root)
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "from collections.abc import Callable",
        "",
        "from ..modifier import ModifierManager",
        (
            "from ..operator.node._core import "
            "DEFAULT_VALUE_AUTO_ADD_ATTR, NodeOperator"
        ),
        "from ..operator.node.dag._core import DAG",
        "from ..operator.node.dag.shape._core import Shape",
        "from ..operator.node.dag.transform._core import Transform",
    ]
    lines.extend(
        "from .{} import {}".format(
            definition.module_name,
            definition.class_name,
        )
        for definition in definitions
        if definition.can_import
    )
    lines.extend(
        [
            "",
            "",
            "class ShapeWithTransformCreator:",
            "    def __init__(",
            "        self,",
            "        modifier_manager: ModifierManager,",
            (
                "        node_class_resolver: "
                "Callable[[str], type[NodeOperator]],"
            ),
            "    ) -> None: ...",
            "",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "",
            "    def create(",
            "        self,",
            "        node_name: str,",
            "        name: str | None = None,",
            ("        auto_add_attr: bool = " "DEFAULT_VALUE_AUTO_ADD_ATTR,"),
            "        *,",
            "        shape_name: str | None = None,",
            "        parent: DAG | None = None,",
            "    ) -> tuple[Transform, Shape]: ...",
            "",
            "    def available_node_names(self) -> tuple[str, ...]: ...",
            "",
            "    def __getattr__(",
            "        self,",
            "        node_name: str,",
            "    ) -> Callable[..., tuple[Transform, Shape]]: ...",
        ]
    )

    for definition in definitions:
        lines.extend(
            [
                "",
                f"    def {definition.method_name}(",
                "        self,",
                "        name: str | None = None,",
                (
                    "        auto_add_attr: bool = "
                    "DEFAULT_VALUE_AUTO_ADD_ATTR,"
                ),
                "        *,",
                "        shape_name: str | None = None,",
                "        parent: DAG | None = None,",
                (
                    "    ) -> tuple[Transform, "
                    f"{definition.return_type}]: ..."
                ),
            ]
        )

    return "\n".join(lines) + "\n"


def existing_node_stub_path(python_root: Path) -> Path:
    return python_root / "bd_util" / "maya" / "node" / "existing_node.pyi"


def nodes_stub_path(python_root: Path) -> Path:
    return python_root / "bd_util" / "maya" / "node" / "nodes.pyi"


def versioned_accessors_stub_path(python_root: Path) -> Path:
    return (
        python_root / "bd_util" / "maya" / "node" / "_versioned_accessors.pyi"
    )


def shape_with_transform_stub_path(python_root: Path) -> Path:
    return (
        python_root
        / "bd_util"
        / "maya"
        / "node"
        / "creator"
        / "_shape_with_transform.pyi"
    )


def transform_creator_stub_path(python_root: Path) -> Path:
    return (
        python_root
        / "bd_util"
        / "maya"
        / "node"
        / "creator"
        / "_transform_creator.pyi"
    )


def node_type_registry_path(python_root: Path) -> Path:
    return python_root / "bd_util" / "maya" / "node" / "_node_type_registry.py"


def node_types_stub_path(python_root: Path) -> Path:
    return python_root / "bd_util" / "maya" / "node" / "node_types.pyi"


def stub_code_is_current(
    output_path: Path,
    generated_code: str,
) -> bool:
    if not output_path.is_file():
        return False

    current_tree = ast.parse(
        output_path.read_text(encoding="utf-8"),
        filename=str(output_path),
    )
    generated_tree = ast.parse(
        generated_code,
        filename=f"{output_path} (generated)",
    )
    return ast.dump(current_tree) == ast.dump(generated_tree)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    python_root = Path(__file__).resolve().parents[6]
    outputs = (
        (
            existing_node_stub_path(python_root),
            generate_existing_node_stub_code(python_root),
        ),
        (
            nodes_stub_path(python_root),
            generate_nodes_stub_code(python_root),
        ),
        (
            versioned_accessors_stub_path(python_root),
            generate_versioned_accessors_stub_code(python_root),
        ),
        (
            shape_with_transform_stub_path(python_root),
            generate_shape_with_transform_stub_code(python_root),
        ),
        (
            transform_creator_stub_path(python_root),
            generate_transform_creator_stub_code(python_root),
        ),
        (
            node_type_registry_path(python_root),
            generate_node_type_registry_code(python_root),
        ),
        (
            node_types_stub_path(python_root),
            generate_node_types_stub_code(python_root),
        ),
    )

    if args.check:
        outdated_paths = [
            output_path
            for output_path, code in outputs
            if not stub_code_is_current(output_path, code)
        ]
        if outdated_paths:
            paths = ", ".join(str(path) for path in outdated_paths)
            raise SystemExit(f"Node access stub is out of date: {paths}")
        return

    for output_path, code in outputs:
        output_path.write_text(code, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
