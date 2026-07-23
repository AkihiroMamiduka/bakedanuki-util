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

    assert all(
        definition.node_type != "shape" for definition in definitions
    )


def test_existing_node_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        existing_node_stub_path,
        generate_existing_node_stub_code,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = existing_node_stub_path(python_root)

    assert output_path.read_text(
        encoding="utf-8"
    ) == generate_existing_node_stub_code(python_root)


def test_nodes_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node.generate_existing_node_stub import (
        generate_nodes_stub_code,
        nodes_stub_path,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = nodes_stub_path(python_root)

    assert output_path.read_text(
        encoding="utf-8"
    ) == generate_nodes_stub_code(python_root)
