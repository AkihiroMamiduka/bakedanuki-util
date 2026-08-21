# coding: utf-8
from __future__ import annotations

import pytest

from bd_util.maya.node.existing_node import ExistingNode


def test_existing_node_wraps_existing_dg_node(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

    node = ExistingNode("test_plus_minus_ave")

    assert isinstance(node, PlusMinusAverage)
    assert node.name == "test_plus_minus_ave"


def test_existing_node_can_edit_wrapped_node(new_scene, maya_cmds):
    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")

    node = ExistingNode("test_plus_minus_ave")
    node.input1D[0].set(10.0)
    node.modifier_manager.do_it_dg()

    assert maya_cmds.getAttr("test_plus_minus_ave.input1D[0]") == 10.0


def test_existing_node_uses_passed_modifier_manager(new_scene, maya_cmds):
    import bd_util

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode(
        "test_plus_minus_ave",
        modifier_manager=modifier_manager,
    )

    assert node.modifier_manager is modifier_manager


def test_existing_node_typed_accessor_wraps_existing_node(
    new_scene,
    maya_cmds,
):
    import bd_util
    from bd_util.maya.node.operator.node.dg.decompose_matrix import (
        DecomposeMatrix,
    )

    maya_cmds.createNode("decomposeMatrix", name="test_decompose_matrix")

    node = ExistingNode.decomposeMatrix("test_decompose_matrix")

    assert isinstance(node, DecomposeMatrix)
    assert node.name == "test_decompose_matrix"


def test_existing_node_typed_accessor_uses_passed_modifier_manager(
    new_scene,
    maya_cmds,
):
    import bd_util

    maya_cmds.createNode("decomposeMatrix", name="test_decompose_matrix")
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode.decomposeMatrix(
        "test_decompose_matrix",
        modifier_manager=modifier_manager,
    )

    assert node.modifier_manager is modifier_manager


def test_existing_node_typed_accessor_rejects_different_node_type(
    new_scene,
    maya_cmds,
):
    import bd_util

    maya_cmds.createNode("composeMatrix", name="test_compose_matrix")

    with pytest.raises(
        TypeError,
        match=(
            "Node type mismatch.*expected 'decomposeMatrix'.*"
            "got 'composeMatrix'"
        ),
    ):
        ExistingNode.decomposeMatrix("test_compose_matrix")


def test_existing_node_wraps_m_object(new_scene, maya_cmds, maya_om):
    from bd_util.maya.node.operator.node.dg.plus_minus_average import (
        PlusMinusAverage,
    )

    maya_cmds.createNode("plusMinusAverage", name="test_plus_minus_ave")
    selection = maya_om.MSelectionList()
    selection.add("test_plus_minus_ave")
    m_obj = selection.getDependNode(0)

    node = ExistingNode(m_obj)

    assert isinstance(node, PlusMinusAverage)
    assert node.name == "test_plus_minus_ave"


def test_existing_node_wraps_transform(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dag.transform._core import Transform

    maya_cmds.createNode("transform", name="test_transform")

    node = ExistingNode("test_transform")

    assert isinstance(node, Transform)
    assert node.name == "test_transform"


def test_existing_node_wraps_joint(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    maya_cmds.createNode("joint", name="test_joint")

    node = ExistingNode("test_joint")

    assert isinstance(node, Joint)
    assert node.NODE_TYPE == "joint"
    assert node.name == "test_joint"


def test_existing_node_wraps_ik_handle_and_effector(
    new_scene,
    maya_cmds,
):
    import bd_util
    from bd_util.maya.node.operator.node.dag.transform.ik_effector import (
        IkEffector,
    )
    from bd_util.maya.node.operator.node.dag.transform.ik_handle import (
        IkHandle,
    )

    start_joint = maya_cmds.joint(name="start_joint", position=(0, 0, 0))
    end_joint = maya_cmds.joint(name="end_joint", position=(5, 0, 0))
    handle_name, effector_name = maya_cmds.ikHandle(
        name="test_ik_handle",
        startJoint=start_joint,
        endEffector=end_joint,
    )
    modifier_manager = bd_util.ModifierManager()

    handle = ExistingNode(
        handle_name,
        modifier_manager=modifier_manager,
    )
    effector = ExistingNode(
        effector_name,
        modifier_manager=modifier_manager,
    )

    assert isinstance(handle, IkHandle)
    assert isinstance(effector, IkEffector)
    assert handle.NODE_TYPE == "ikHandle"
    assert effector.NODE_TYPE == "ikEffector"
    assert handle.modifier_manager is modifier_manager
    assert effector.modifier_manager is modifier_manager
    assert handle.ikBlend.long_name == "ikBlend"
    assert effector.hideDisplay.long_name == "hideDisplay"


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    [
        ("aimConstraint", "AimConstraint"),
        ("geometryConstraint", "GeometryConstraint"),
        ("normalConstraint", "NormalConstraint"),
        ("oldNormalConstraint", "OldNormalConstraint"),
        ("oldTangentConstraint", "OldTangentConstraint"),
        ("orientConstraint", "OrientConstraint"),
        ("parentConstraint", "ParentConstraint"),
        ("pointConstraint", "PointConstraint"),
        ("pointOnPolyConstraint", "PointOnPolyConstraint"),
        ("poleVectorConstraint", "PoleVectorConstraint"),
        ("rigidConstraint", "RigidConstraint"),
        ("scaleConstraint", "ScaleConstraint"),
        ("symmetryConstraint", "SymmetryConstraint"),
        ("tangentConstraint", "TangentConstraint"),
    ],
)
def test_existing_node_wraps_constraint_transform(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util

    node_name = maya_cmds.createNode(node_type)
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode(
        node_name,
        modifier_manager=modifier_manager,
    )

    assert type(node).__name__ == class_name
    assert node.NODE_TYPE == node_type
    assert node.modifier_manager is modifier_manager


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    [
        ("airField", "AirField"),
        ("dragField", "DragField"),
        ("fluidEmitter", "FluidEmitter"),
        ("gravityField", "GravityField"),
        ("newtonField", "NewtonField"),
        ("pointEmitter", "PointEmitter"),
        ("radialField", "RadialField"),
        ("turbulenceField", "TurbulenceField"),
        ("uniformField", "UniformField"),
        ("volumeAxisField", "VolumeAxisField"),
        ("vortexField", "VortexField"),
    ],
)
def test_existing_node_wraps_field_and_emitter_transform(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util

    node_name = maya_cmds.createNode(node_type)
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode(
        node_name,
        modifier_manager=modifier_manager,
    )

    assert type(node).__name__ == class_name
    assert node.NODE_TYPE == node_type
    assert node.modifier_manager is modifier_manager


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    [
        ("collisionModel", "CollisionModel"),
        ("instancer", "Instancer"),
        ("nucleus", "Nucleus"),
        ("primitiveFalloff", "PrimitiveFalloff"),
        ("textureDeformerHandle", "TextureDeformerHandle"),
    ],
)
def test_existing_node_wraps_dynamics_and_deformer_transform(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util

    node_name = maya_cmds.createNode(node_type)
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode(
        node_name,
        modifier_manager=modifier_manager,
    )

    assert type(node).__name__ == class_name
    assert node.NODE_TYPE == node_type
    assert node.modifier_manager is modifier_manager


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    [
        ("hikEffector", "HikEffector"),
        ("hikFKJoint", "HikFKJoint"),
        ("hikGroundPlane", "HikGroundPlane"),
        ("hikHandle", "HikHandle"),
        ("hikIKEffector", "HikIKEffector"),
    ],
)
def test_existing_node_wraps_hik_transform(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util

    node_name = maya_cmds.createNode(node_type)
    modifier_manager = bd_util.ModifierManager()

    node = ExistingNode(
        node_name,
        modifier_manager=modifier_manager,
    )

    assert type(node).__name__ == class_name
    assert node.NODE_TYPE == node_type
    assert node.modifier_manager is modifier_manager


def test_existing_node_hik_preserves_concrete_transform_base(
    new_scene,
    maya_cmds,
):
    from bd_util.maya.node.operator.node.dag.transform.hik_fk_joint import (
        HikFKJoint,
    )
    from bd_util.maya.node.operator.node.dag.transform.hik_handle import (
        HikHandle,
    )
    from bd_util.maya.node.operator.node.dag.transform.ik_handle import (
        IkHandle,
    )
    from bd_util.maya.node.operator.node.dag.transform.joint import Joint

    hik_fk_joint = ExistingNode(maya_cmds.createNode("hikFKJoint"))
    hik_handle = ExistingNode(maya_cmds.createNode("hikHandle"))

    assert isinstance(hik_fk_joint, HikFKJoint)
    assert isinstance(hik_fk_joint, Joint)
    assert isinstance(hik_handle, HikHandle)
    assert isinstance(hik_handle, IkHandle)


def test_existing_node_wraps_mesh_shape(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dag.shape.mesh import Mesh

    transform, _ = maya_cmds.polyCube(name="test_mesh")
    shape = maya_cmds.listRelatives(transform, shapes=True)[0]

    node = ExistingNode(shape)

    assert isinstance(node, Mesh)
    assert node.NODE_TYPE == "mesh"
    assert node.name == shape
    assert node.face.long_name == "face"


def test_existing_node_wraps_camera_shape(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dag.shape.camera import Camera

    _, shape = maya_cmds.camera(name="test_camera")

    node = ExistingNode(shape)

    assert isinstance(node, Camera)
    assert node.NODE_TYPE == "camera"
    assert node.name == shape
    assert node.focalLength.long_name == "focalLength"


def test_existing_node_wraps_generated_light_shape(new_scene, maya_cmds):
    from bd_util.maya.node.operator.node.dag.shape.ambient_light import (
        AmbientLight,
    )

    shape = maya_cmds.createNode("ambientLight", name="test_ambient_light")

    node = ExistingNode(shape)

    assert isinstance(node, AmbientLight)
    assert node.NODE_TYPE == "ambientLight"
    assert node.name == shape
    assert node.intensity.long_name == "intensity"


def test_existing_node_unknown_node_raises_value_error(new_scene):
    with pytest.raises(ValueError):
        ExistingNode("not_existing_node")
