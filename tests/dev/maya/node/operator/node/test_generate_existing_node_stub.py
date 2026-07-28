# coding: utf-8
from pathlib import Path


def test_transform_stub_uses_public_manual_class():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        collect_node_definitions,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = collect_node_definitions(python_root)
    transform = next(
        definition
        for definition in definitions
        if definition.node_type == "transform"
    )

    assert transform.class_name == "Transform"
    assert transform.module_name.endswith(".dag.transform._core")


def test_shape_stub_excludes_abstract_base_class():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        collect_node_definitions,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = collect_node_definitions(python_root)

    assert all(definition.node_type != "shape" for definition in definitions)


def test_existing_node_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        existing_node_stub_path,
        generate_existing_node_stub_code,
        stub_code_is_current,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = existing_node_stub_path(python_root)

    assert stub_code_is_current(
        output_path,
        generate_existing_node_stub_code(python_root),
    )


def test_nodes_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        generate_nodes_stub_code,
        nodes_stub_path,
        stub_code_is_current,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = nodes_stub_path(python_root)

    assert stub_code_is_current(
        output_path,
        generate_nodes_stub_code(python_root),
    )


def test_stub_code_is_current_ignores_formatting_only(tmp_path):
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        stub_code_is_current,
    )

    output_path = tmp_path / "example.pyi"
    output_path.write_text(
        "from example import (\n" "    Example,\n" ")\n",
        encoding="utf-8",
    )

    assert stub_code_is_current(
        output_path,
        "from example import Example\n",
    )
    assert not stub_code_is_current(
        output_path,
        "from example import Other\n",
    )
