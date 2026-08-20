# coding: utf-8
from __future__ import annotations

import pytest


def test_shape_common_attributes_are_generated_on_shape_base():
    from bd_util.maya.node.operator.node.dag.shape._generated.camera import (
        GeneratedCamera,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.locator import (
        GeneratedLocator,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.mesh import (
        GeneratedMesh,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.nurbs_curve import (
        GeneratedNurbsCurve,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.nurbs_surface import (
        GeneratedNurbsSurface,
    )
    from bd_util.maya.node.operator.node.dag.shape._generated.shape import (
        GeneratedShape,
    )

    assert "visibility" in vars(GeneratedShape)
    for node_cls in (
        GeneratedCamera,
        GeneratedLocator,
        GeneratedMesh,
        GeneratedNurbsCurve,
        GeneratedNurbsSurface,
    ):
        assert "visibility" not in vars(node_cls)
        assert node_cls.visibility.long_name == "visibility"


@pytest.mark.parametrize(
    ("node_type", "class_name"),
    (
        ("ambientLight", "AmbientLight"),
        ("angleDimension", "AngleDimension"),
        ("annotationShape", "AnnotationShape"),
        ("arcLengthDimension", "ArcLengthDimension"),
        ("areaLight", "AreaLight"),
        ("baseLattice", "BaseLattice"),
        ("bezierCurve", "BezierCurve"),
        ("camera", "Camera"),
        ("clusterFlexorShape", "ClusterFlexorShape"),
        ("clusterHandle", "ClusterHandle"),
        ("deformBend", "DeformBend"),
        ("deformFlare", "DeformFlare"),
        ("deformSine", "DeformSine"),
        ("deformSquash", "DeformSquash"),
        ("deformTwist", "DeformTwist"),
        ("deformWave", "DeformWave"),
        ("directedDisc", "DirectedDisc"),
        ("directionalLight", "DirectionalLight"),
        ("distanceDimShape", "DistanceDimShape"),
        ("dropoffLocator", "DropoffLocator"),
        ("environmentFog", "EnvironmentFog"),
        ("flexorShape", "FlexorShape"),
        ("fluidTexture2D", "FluidTexture2D"),
        ("fluidTexture3D", "FluidTexture3D"),
        ("geoConnectable", "GeoConnectable"),
        ("greasePlane", "GreasePlane"),
        ("greasePlaneRenderShape", "GreasePlaneRenderShape"),
        ("heightField", "HeightField"),
        ("hikFloorContactMarker", "HikFloorContactMarker"),
        ("imagePlane", "ImagePlane"),
        ("implicitBox", "ImplicitBox"),
        ("implicitCone", "ImplicitCone"),
        ("implicitSphere", "ImplicitSphere"),
        ("lattice", "Lattice"),
        ("lineModifier", "LineModifier"),
        ("locator", "Locator"),
        ("mesh", "Mesh"),
        ("motionTrailShape", "MotionTrailShape"),
        ("nurbsCurve", "NurbsCurve"),
        ("nurbsSurface", "NurbsSurface"),
        ("orientationMarker", "OrientationMarker"),
        ("paramDimension", "ParamDimension"),
        ("pfxHair", "PfxHair"),
        ("pfxToon", "PfxToon"),
        ("pointLight", "PointLight"),
        ("positionMarker", "PositionMarker"),
        ("renderBox", "RenderBox"),
        ("renderCone", "RenderCone"),
        ("renderRect", "RenderRect"),
        ("renderSphere", "RenderSphere"),
        ("sketchPlane", "SketchPlane"),
        ("snapshotShape", "SnapshotShape"),
        ("softModHandle", "SoftModHandle"),
        ("spotLight", "SpotLight"),
        ("stereoRigCamera", "StereoRigCamera"),
        ("stroke", "Stroke"),
        ("subdiv", "Subdiv"),
        ("volumeLight", "VolumeLight"),
    ),
)
def test_nodes_create_opted_in_shape(
    new_scene,
    maya_cmds,
    node_type,
    class_name,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name=f"{node_type}_parent")
    shape = getattr(nodes.create, node_type)(
        name=f"{node_type}Shape",
        parent=parent,
    )

    assert shape.full_path == ""
    mod.do_it_dag()

    assert type(shape).__name__ == class_name
    assert shape.modifier_manager is mod
    assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
    assert maya_cmds.nodeType(shape.full_path) == node_type
    assert maya_cmds.listRelatives(
        parent.full_path,
        shapes=True,
        fullPath=True,
    ) == [shape.full_path]
    assert shape.parent is not None
    assert shape.parent.m_obj == parent.m_obj


def test_nodes_create_shapes_in_one_modifier_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="shape_parent")
    shapes = [
        nodes.create.camera(name="cameraShape", parent=parent),
        nodes.create.locator(name="locatorShape", parent=parent),
        nodes.create.mesh(name="meshShape", parent=parent),
        nodes.create.nurbsCurve(name="curveShape", parent=parent),
        nodes.create.nurbsSurface(name="surfaceShape", parent=parent),
    ]

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    assert (
        maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        )
        == expected_paths
    )

    mod.undo_it()
    assert not maya_cmds.objExists("shape_parent")

    mod.redo_it()
    assert maya_cmds.objExists("shape_parent")
    assert [shape.full_path for shape in shapes] == expected_paths


def test_nodes_create_geometry_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "baseLattice",
        "bezierCurve",
        "lattice",
        "subdiv",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_primitive_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "implicitBox",
        "implicitCone",
        "implicitSphere",
        "renderBox",
        "renderCone",
        "renderRect",
        "renderSphere",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_measurement_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "angleDimension",
        "annotationShape",
        "arcLengthDimension",
        "distanceDimShape",
        "paramDimension",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_helper_locator_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "clusterHandle",
        "directedDisc",
        "dropoffLocator",
        "hikFloorContactMarker",
        "motionTrailShape",
        "orientationMarker",
        "positionMarker",
        "softModHandle",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_deformation_connection_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "clusterFlexorShape",
        "flexorShape",
        "geoConnectable",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_nonlinear_deformer_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "deformBend",
        "deformFlare",
        "deformSine",
        "deformSquash",
        "deformTwist",
        "deformWave",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_environment_render_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "environmentFog",
        "fluidTexture2D",
        "fluidTexture3D",
        "heightField",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_scene_display_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "imagePlane",
        "sketchPlane",
        "snapshotShape",
        "stereoRigCamera",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_paint_effects_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    shape_types = (
        "greasePlane",
        "greasePlaneRenderShape",
        "lineModifier",
        "pfxHair",
        "pfxToon",
        "stroke",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_nodes_create_standard_lights_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    light_types = (
        "ambientLight",
        "areaLight",
        "directionalLight",
        "pointLight",
        "spotLight",
        "volumeLight",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    lights = []
    for node_type in light_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        light = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        lights.append(light)

    mod.do_it_dag()

    expected_paths = [light.full_path for light in lights]
    for node_type, parent, light in zip(light_types, parents, lights):
        assert light.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(light.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [light.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in light_types
    )

    mod.redo_it()
    assert [light.full_path for light in lights] == expected_paths
    assert [maya_cmds.nodeType(light.full_path) for light in lights] == list(
        light_types
    )


@pytest.mark.filterwarnings(
    r"ignore:invalid escape sequence.*:DeprecationWarning",
    r"ignore:find_module\(\) is deprecated.*:DeprecationWarning",
    r"ignore:FileFinder\.find_loader\(\) is deprecated.*:DeprecationWarning",
    r"ignore:the load_module\(\) method is deprecated.*:DeprecationWarning",
)
def test_nodes_create_standard_light_exposes_arnold_attribute_when_mtoa_loaded(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    try:
        maya_cmds.loadPlugin("mtoa", quiet=True)
    except Exception as exc:
        pytest.skip(f"mtoa is unavailable: {exc}")

    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parent = nodes.create.transform(name="area_light")
    area_light = nodes.create.areaLight(
        name="area_lightShape",
        parent=parent,
    )
    mod.do_it_dag()

    assert maya_cmds.attributeQuery(
        "aiExposure",
        node=area_light.full_path,
        exists=True,
    )
    assert area_light.aiExposure.name == "aiExposure"


@pytest.mark.filterwarnings(
    r"ignore:invalid escape sequence.*:DeprecationWarning",
    r"ignore:find_module\(\) is deprecated.*:DeprecationWarning",
    r"ignore:FileFinder\.find_loader\(\) is deprecated.*:DeprecationWarning",
    r"ignore:the load_module\(\) method is deprecated.*:DeprecationWarning",
)
def test_nodes_create_arnold_lights_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    try:
        maya_cmds.loadPlugin("mtoa", quiet=True)
    except Exception as exc:
        pytest.skip(f"mtoa is unavailable: {exc}")

    light_types = (
        "aiAreaLight",
        "aiLightPortal",
        "aiMeshLight",
        "aiPhotometricLight",
        "aiSkyDomeLight",
    )
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    lights = []
    for node_type in light_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        light = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        lights.append(light)

    mod.do_it_dag()

    expected_paths = [light.full_path for light in lights]
    for node_type, parent, light in zip(light_types, parents, lights):
        assert light.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(light.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [light.full_path]

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in light_types
    )

    mod.redo_it()
    assert [light.full_path for light in lights] == expected_paths
    assert [maya_cmds.nodeType(light.full_path) for light in lights] == list(
        light_types
    )


@pytest.mark.filterwarnings(
    r"ignore:invalid escape sequence.*:DeprecationWarning",
    r"ignore:find_module\(\) is deprecated.*:DeprecationWarning",
    r"ignore:FileFinder\.find_loader\(\) is deprecated.*:DeprecationWarning",
    r"ignore:the load_module\(\) method is deprecated.*:DeprecationWarning",
)
def test_nodes_create_arnold_non_light_shapes_supports_undo_redo(
    new_scene,
    maya_cmds,
):
    import bd_util as bdu

    try:
        maya_cmds.loadPlugin("mtoa", quiet=True)
    except Exception as exc:
        pytest.skip(f"mtoa is unavailable: {exc}")

    shape_types = (
        "aiCurveCollector",
        "aiLightBlocker",
        "aiStandIn",
        "aiVolume",
    )
    required_attrs = {
        "aiCurveCollector": "visibility",
        "aiLightBlocker": "shader",
        "aiStandIn": "dso",
        "aiVolume": "filename",
    }
    mod = bdu.ModifierManager()
    nodes = bdu.Nodes(modifier_manager=mod)
    parents = []
    shapes = []
    for node_type in shape_types:
        parent = nodes.create.transform(name=f"{node_type}_parent")
        shape = getattr(nodes.create, node_type)(
            name=f"{node_type}Shape",
            parent=parent,
        )
        parents.append(parent)
        shapes.append(shape)

    mod.do_it_dag()

    expected_paths = [shape.full_path for shape in shapes]
    for node_type, parent, shape in zip(shape_types, parents, shapes):
        assert shape.full_path == (f"|{node_type}_parent|{node_type}Shape")
        assert maya_cmds.nodeType(shape.full_path) == node_type
        assert maya_cmds.listRelatives(
            parent.full_path,
            shapes=True,
            fullPath=True,
        ) == [shape.full_path]
        assert maya_cmds.attributeQuery(
            required_attrs[node_type],
            node=shape.full_path,
            exists=True,
        )

    mod.undo_it()
    assert all(
        not maya_cmds.objExists(f"{node_type}_parent")
        for node_type in shape_types
    )

    mod.redo_it()
    assert [shape.full_path for shape in shapes] == expected_paths
    assert [maya_cmds.nodeType(shape.full_path) for shape in shapes] == list(
        shape_types
    )


def test_generic_create_supports_opted_in_shape(new_scene, maya_cmds):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape.nurbs_surface import (
        NurbsSurface,
    )

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="surface_parent")
    surface = nodes.create.create(
        "nurbsSurface",
        name="surfaceShape",
        parent=parent,
    )
    nodes.modifier_manager.do_it_dag()

    assert isinstance(surface, NurbsSurface)
    assert surface.full_path == "|surface_parent|surfaceShape"
    assert maya_cmds.nodeType(surface.full_path) == "nurbsSurface"


def test_shape_parent_must_be_transform(new_scene):
    import bd_util as bdu

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="parent")
    mesh = nodes.create.mesh(name="meshShape", parent=parent)

    with pytest.raises(TypeError, match="parent must be a transform"):
        nodes.create.camera(name="cameraShape", parent=mesh)


def test_uncommitted_shape_parent_must_share_modifier_manager(new_scene):
    import bd_util as bdu

    first_nodes = bdu.Nodes()
    second_nodes = bdu.Nodes()
    parent = first_nodes.create.transform(name="parent")

    with pytest.raises(
        ValueError,
        match="must share the same ModifierManager",
    ):
        second_nodes.create.mesh(name="meshShape", parent=parent)


def test_abstract_shape_is_not_creatable(new_scene):
    import bd_util as bdu
    from bd_util.maya.node.operator.node.dag.shape._core import Shape

    nodes = bdu.Nodes()
    parent = nodes.create.transform(name="parent")

    with pytest.raises(AttributeError, match="Unsupported node type"):
        nodes.create.shape()
    with pytest.raises(AttributeError, match="Unsupported node type"):
        nodes.create.create("shape")
    with pytest.raises(TypeError, match="abstract NodeOperator base class"):
        Shape.create(nodes.modifier_manager, parent=parent)
