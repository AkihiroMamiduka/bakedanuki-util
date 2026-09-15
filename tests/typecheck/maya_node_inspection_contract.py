"""属性調査APIの公開値型を固定する。"""

from typing import assert_type

from bd_util.maya.node.inspection import (
    ScalarAttributeInfo,
    ScalarAttributeKind,
    inspect_scalar_attributes,
    selected_node_names,
)

assert_type(selected_node_names(), tuple[str, ...])
attributes = inspect_scalar_attributes("transform1")
assert_type(attributes, tuple[ScalarAttributeInfo, ...])
for attribute in attributes:
    assert_type(attribute.name, str)
    assert_type(attribute.path, str)
    assert_type(attribute.nice_name, str)
    assert_type(attribute.kind, ScalarAttributeKind)
    assert_type(attribute.keyable, bool)
    assert_type(attribute.channel_box, bool)
