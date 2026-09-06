# coding: utf-8
import ast
from pathlib import Path


def test_transform_stub_uses_public_manual_class():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_node_definitions(python_root)
    transform = next(
        definition
        for definition in definitions
        if definition.node_type == "transform"
    )

    assert transform.class_name == "Transform"
    assert transform.module_name.endswith(".dag.transform._core")


def test_transform_stub_includes_concrete_classes():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_node_definitions(python_root)
    definitions_by_type = {
        definition.node_type: definition for definition in definitions
    }

    expected_classes = {
        "aimConstraint": "AimConstraint",
        "airField": "AirField",
        "clipGhostShape": "ClipGhostShape",
        "collisionModel": "CollisionModel",
        "curveVarGroup": "CurveVarGroup",
        "dagContainer": "DagContainer",
        "dragField": "DragField",
        "fluidEmitter": "FluidEmitter",
        "fosterParent": "FosterParent",
        "geometryConstraint": "GeometryConstraint",
        "geometryVarGroup": "GeometryVarGroup",
        "gravityField": "GravityField",
        "hikEffector": "HikEffector",
        "hikFKJoint": "HikFKJoint",
        "hikGroundPlane": "HikGroundPlane",
        "hikHandle": "HikHandle",
        "hikIKEffector": "HikIKEffector",
        "ikEffector": "IkEffector",
        "ikHandle": "IkHandle",
        "instancer": "Instancer",
        "lodGroup": "LodGroup",
        "lookAt": "LookAt",
        "meshVarGroup": "MeshVarGroup",
        "newtonField": "NewtonField",
        "normalConstraint": "NormalConstraint",
        "nucleus": "Nucleus",
        "oldNormalConstraint": "OldNormalConstraint",
        "oldTangentConstraint": "OldTangentConstraint",
        "orientConstraint": "OrientConstraint",
        "parentConstraint": "ParentConstraint",
        "pointConstraint": "PointConstraint",
        "pointEmitter": "PointEmitter",
        "pointOnPolyConstraint": "PointOnPolyConstraint",
        "poleVectorConstraint": "PoleVectorConstraint",
        "place3dTexture": "Place3dTexture",
        "primitiveFalloff": "PrimitiveFalloff",
        "radialField": "RadialField",
        "rigidConstraint": "RigidConstraint",
        "scaleConstraint": "ScaleConstraint",
        "symmetryConstraint": "SymmetryConstraint",
        "subdivSurfaceVarGroup": "SubdivSurfaceVarGroup",
        "surfaceVarGroup": "SurfaceVarGroup",
        "tangentConstraint": "TangentConstraint",
        "textureDeformerHandle": "TextureDeformerHandle",
        "turbulenceField": "TurbulenceField",
        "uniformField": "UniformField",
        "ufeProxyTransform": "UfeProxyTransform",
        "unknownDag": "UnknownDag",
        "unknownTransform": "UnknownTransform",
        "volumeAxisField": "VolumeAxisField",
        "vortexField": "VortexField",
    }

    assert {
        node_type: definitions_by_type[node_type].class_name
        for node_type in expected_classes
    } == expected_classes


def test_stub_excludes_abstract_base_classes():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_node_definitions(python_root)

    assert {definition.node_type for definition in definitions}.isdisjoint(
        {"baseGeometryVarGroup", "shape"}
    )


def test_shape_with_transform_stub_uses_only_creatable_shapes():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_creatable_shape_definitions(
        python_root
    )

    assert len(definitions) == 80
    assert any(definition.node_type == "mesh" for definition in definitions)
    assert all(
        definition.node_type != "SphereLocator" for definition in definitions
    )


def test_transform_creator_stub_uses_only_creatable_transforms():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_creatable_transform_definitions(
        python_root
    )

    assert len(definitions) == 52
    assert any(
        definition.node_type == "ikHandle" for definition in definitions
    )
    assert all(
        definition.node_type != "baseGeometryVarGroup"
        for definition in definitions
    )


def test_underscore_node_type_uses_pascal_case_class_and_exact_method_name():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    definitions = stub_generator.collect_node_definitions(python_root)
    mash_audio = next(
        definition
        for definition in definitions
        if definition.node_type == "MASH_Audio"
    )

    assert mash_audio.class_name == "MASHAudio"
    assert mash_audio.method_name == "MASH_Audio"


def test_existing_node_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.existing_node_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_existing_node_stub_code(python_root),
    )


def test_nodes_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.nodes_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_nodes_stub_code(python_root),
    )


def test_versioned_accessors_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.versioned_accessors_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_versioned_accessors_stub_code(python_root),
    )


def test_versioned_creator_surfaces_follow_node_availability():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    tree = ast.parse(
        stub_generator.generate_versioned_accessors_stub_code(python_root)
    )
    classes = {
        statement.name: statement
        for statement in tree.body
        if isinstance(statement, ast.ClassDef)
    }

    def method_names(class_name: str) -> set[str]:
        return {
            statement.name
            for statement in classes[class_name].body
            if isinstance(statement, ast.FunctionDef)
        }

    common_names = method_names("_NodeCreatorCommon")
    maya_2025_names = method_names("_NodeCreatorMaya2025")
    maya_2026_names = method_names("_NodeCreatorMaya2026")
    maya_2027_names = method_names("_NodeCreatorMaya2027")

    assert "absolute" in common_names
    assert "__getattr__" not in common_names
    assert {"addDoubleLinear", "absoluteDL", "shotLabel"}.isdisjoint(
        common_names
    )
    assert "addDoubleLinear" in maya_2025_names
    assert "absoluteDL" not in maya_2025_names
    assert "addDoubleLinear" not in maya_2026_names
    assert "absoluteDL" in maya_2026_names
    assert "shotLabel" not in maya_2026_names
    assert {"absoluteDL", "shotLabel"}.issubset(maya_2027_names)

    existing_common_names = method_names("_ExistingNodeAccessorCommon")
    assert "__getattr__" not in existing_common_names

    node_types_common_names = method_names("_NodeTypesCommon")
    node_types_2025_names = method_names("_NodeTypesMaya2025")
    node_types_2026_names = method_names("_NodeTypesMaya2026")
    node_types_2027_names = method_names("_NodeTypesMaya2027")

    assert "Absolute" in node_types_common_names
    assert {"AddDoubleLinear", "AbsoluteDL", "ShotLabel"}.isdisjoint(
        node_types_common_names
    )
    assert "AddDoubleLinear" in node_types_2025_names
    assert "AbsoluteDL" not in node_types_2025_names
    assert "AddDoubleLinear" not in node_types_2026_names
    assert "AbsoluteDL" in node_types_2026_names
    assert "ShotLabel" not in node_types_2026_names
    assert {"AbsoluteDL", "ShotLabel"}.issubset(node_types_2027_names)

    standard_surface_2026 = classes["_StandardSurfaceMaya2026"]
    assert len(standard_surface_2026.bases) == 1
    assert isinstance(standard_surface_2026.bases[0], ast.Name)
    assert (
        standard_surface_2026.bases[0].id
        == "_GeneratedStandardSurfaceMaya2026"
    )


def test_shape_with_transform_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.shape_with_transform_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_shape_with_transform_stub_code(python_root),
    )


def test_transform_creator_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.transform_creator_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_transform_creator_stub_code(python_root),
    )


def test_node_type_registry_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.node_type_registry_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_node_type_registry_code(python_root),
    )


def test_node_types_stub_matches_generated_code():
    import bd_util
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    python_root = Path(bd_util.__file__).resolve().parent.parent
    output_path = stub_generator.node_types_stub_path(python_root)

    assert stub_generator.stub_code_is_current(
        output_path,
        stub_generator.generate_node_types_stub_code(python_root),
    )


def test_stub_code_is_current_ignores_formatting_only(tmp_path):
    from bd_util._dev.maya.node.operator.node import (
        generate_existing_node_stub as stub_generator,
    )

    output_path = tmp_path / "example.pyi"
    output_path.write_text(
        "from example import (\n" "    Example,\n" ")\n",
        encoding="utf-8",
    )

    assert stub_generator.stub_code_is_current(
        output_path,
        "from example import Example\n",
    )
    assert not stub_generator.stub_code_is_current(
        output_path,
        "from example import Other\n",
    )
