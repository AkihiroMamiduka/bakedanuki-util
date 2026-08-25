# coding: utf-8
import pytest

TRANSFORM_NODE_TYPES_BY_GROUP = {
    "core": (
        "joint",
        "transform",
    ),
    "ik": (
        "ikEffector",
        "ikHandle",
    ),
    "constraint": (
        "aimConstraint",
        "geometryConstraint",
        "normalConstraint",
        "oldNormalConstraint",
        "oldTangentConstraint",
        "orientConstraint",
        "parentConstraint",
        "pointConstraint",
        "pointOnPolyConstraint",
        "poleVectorConstraint",
        "rigidConstraint",
        "scaleConstraint",
        "symmetryConstraint",
        "tangentConstraint",
    ),
    "field_emitter": (
        "airField",
        "dragField",
        "fluidEmitter",
        "gravityField",
        "newtonField",
        "pointEmitter",
        "radialField",
        "turbulenceField",
        "uniformField",
        "volumeAxisField",
        "vortexField",
    ),
    "dynamics_deformer": (
        "collisionModel",
        "instancer",
        "nucleus",
        "primitiveFalloff",
        "textureDeformerHandle",
    ),
    "hik": (
        "hikEffector",
        "hikFKJoint",
        "hikGroundPlane",
        "hikHandle",
        "hikIKEffector",
    ),
    "scene_utility": (
        "clipGhostShape",
        "dagContainer",
        "fosterParent",
        "lodGroup",
        "lookAt",
        "place3dTexture",
    ),
    "var_group": (
        "curveVarGroup",
        "geometryVarGroup",
        "meshVarGroup",
        "subdivSurfaceVarGroup",
        "surfaceVarGroup",
    ),
    "special": (
        "ufeProxyTransform",
        "unknownTransform",
    ),
}

CREATABLE_TRANSFORM_NODE_TYPES = tuple(
    node_type
    for node_types in TRANSFORM_NODE_TYPES_BY_GROUP.values()
    for node_type in node_types
)


def test_transform_creator_allowlist_matches_verified_types(new_scene):
    from bd_util.maya.node.creator._transform_types import (
        CREATABLE_TRANSFORM_NODE_TYPES as allowlisted_types,
    )

    assert len(CREATABLE_TRANSFORM_NODE_TYPES) == 52
    assert allowlisted_types == frozenset(CREATABLE_TRANSFORM_NODE_TYPES)
    assert "baseGeometryVarGroup" not in allowlisted_types


@pytest.mark.parametrize("node_type", CREATABLE_TRANSFORM_NODE_TYPES)
def test_nodes_create_transform_type_supports_parent_and_undo_redo(
    new_scene,
    maya_cmds,
    node_type,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent_name = f"parent_{node_type}"
    node_name = f"created_{node_type}"

    parent = nodes.create.transform(name=parent_name)
    node = getattr(nodes.create, node_type)(
        name=node_name,
        parent=parent,
    )
    node_cls = nodes.types.resolve(node_type)

    assert isinstance(node, node_cls)
    assert node.modifier_manager is mod

    mod.do_it_dag()
    mod.do_it_dg()

    expected_path = f"|{parent_name}|{node_name}"
    assert node.full_path == expected_path
    assert maya_cmds.nodeType(expected_path) == node_type

    mod.undo_it()
    assert not maya_cmds.objExists(parent_name)
    assert not maya_cmds.objExists(node_name)

    mod.redo_it()
    assert node.full_path == expected_path
    assert maya_cmds.nodeType(expected_path) == node_type


def test_generic_create_supports_transform_type(new_scene, maya_cmds):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="parent")
    node = nodes.create.create(
        "ikHandle",
        name="raw_ik_handle",
        parent=parent,
    )

    mod.do_it_dag()
    mod.do_it_dg()

    assert isinstance(node, nodes.types.IkHandle)
    assert node.full_path == "|parent|raw_ik_handle"
    assert maya_cmds.nodeType(node.full_path) == "ikHandle"
