# coding: utf-8
from __future__ import annotations

import argparse
import ast
import keyword
from dataclasses import dataclass
from pathlib import Path
from typing import cast

_ABSTRACT_NODE_TYPES = frozenset({"baseGeometryVarGroup", "shape"})


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
    definitions = collect_node_definitions(python_root)
    lines = [
        "# coding: utf-8",
        "# This file is generated by generate_existing_node_stub.py.",
        "from __future__ import annotations",
        "",
        "from maya.api import OpenMaya as om",
        "",
        "from .creator import NodeCreator",
        "from .modifier import ModifierManager",
        "from .node_types import NodeTypes",
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
            "class _ExistingNodeAccessor:",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "",
            "    def __call__(",
            "        self,",
            "        node: str | om.MObject,",
            "        auto_add_attr: bool = False,",
            "    ) -> NodeOperator: ...",
        ]
    )

    for definition in definitions:
        lines.extend(
            [
                "",
                f"    def {definition.method_name}(",
                "        self,",
                "        node: str | om.MObject,",
                "        auto_add_attr: bool = False,",
                f"    ) -> {definition.return_type}: ...",
            ]
        )

    lines.extend(
        [
            "",
            "",
            "class Nodes:",
            "    def __init__(",
            "        self,",
            "        modifier_manager: ModifierManager | None = None,",
            "    ) -> None: ...",
            "",
            "    @property",
            "    def modifier_manager(self) -> ModifierManager: ...",
            "",
            "    @property",
            "    def create(self) -> NodeCreator: ...",
            "",
            "    @property",
            "    def existing(self) -> _ExistingNodeAccessor: ...",
            "",
            "    @property",
            "    def types(self) -> NodeTypes: ...",
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
