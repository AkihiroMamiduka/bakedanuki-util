# coding: utf-8
from pathlib import Path


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
