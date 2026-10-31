# coding: utf-8
from __future__ import annotations

import math
import os
from pathlib import Path

import pytest

from controller_shape_cases import (
    SHAPE_NAMES,
    VARIANT_NAMES,
    preset_options,
    set_preset,
)

import bd_util as bdu
from bd_util.maya.node.operator.node.dag.shape._generated.bd_controller_shape import (
    ShapeEnumAttrOperator,
    ShapeEnumPlugOperator,
)

pytestmark = pytest.mark.maya


GUIDE_CASES = {
    "SquareCrossLine": ("Square", False),
    "SquareCrossLineTemplate": ("Square", True),
    "SquareCrossLineSwapped": ("SquareSwapped", False),
    "SquareCrossLineTemplateSwapped": ("SquareSwapped", True),
    "ColorSphereCrossLine": ("ColorSphere", False),
}

PART_SHAPES = (
    "Arrow2D",
    "Arrow3D",
    "Triangle",
    "Square",
    "Diamond",
    "Circle",
    "Cube",
    "Octahedron",
    "Sphere",
    "Pyramid",
    "Cone",
)

PLANAR_BASES = (
    "Gear",
    "Triangle",
    "Square",
    "SquareCrossLine",
    "SquareCrossLineTemplate",
    "SquareTemplate",
    "Diamond",
)

SWAPPED_BASES = (
    *PLANAR_BASES,
    "CrossLine",
    "WideCrossLine",
    "Circle",
    "WideCircle",
)


def _circle_arrow_profile_points(start, depth, half_width):
    root = start + 2 * depth
    low, high = sorted((start, root))
    angles = [start, root] + [
        index * math.pi / 32
        for index in range(
            math.floor(low * 32 / math.pi), math.ceil(high * 32 / math.pi) + 1
        )
        if low < index * math.pi / 32 < high
    ]
    return [
        (0, radius * math.sin(angle), radius * math.cos(angle))
        for angle in angles
        for radius in (
            max(0, 0.5 - half_width * abs((angle - start) / (2 * depth))),
            0.5 + half_width * abs((angle - start) / (2 * depth)),
        )
    ]


def _circle_arrow_outer_extent(depth, half_width):
    return max(
        point[2]
        for point in _circle_arrow_profile_points(0, depth, half_width)
    )


ARC_SHAPES = tuple(name for name in VARIANT_NAMES if "Arc" in name)

PART_UNSUPPORTED = (
    "Gear",
    "GearSwapped",
    "Triangle",
    "TriangleSwapped",
    "Diamond",
    "DiamondSwapped",
    "Octahedron",
    "OctahedronArrow",
    "Cylinder",
    "Arrow",
    "Pyramid",
    "Cone",
    "ColorCube",
    "ColorCornerCube",
)

OPTION_CASE_NAMES = (
    "Gear",
    "Line",
    "LineArrowAtEnd",
    "LineArrowAtEnds",
    "LineWideArrowAtEnd",
    "LineWideArrowAtEnds",
    "LineSquareAtEnd",
    "LineSquareAtEnds",
    "LineDiamondAtEnd",
    "LineDiamondAtEnds",
    "LineCircleAtEnd",
    "LineCircleAtEnds",
    "LineTriangleAtEnd",
    "LineTriangleAtEnds",
    "CrossLine",
    "CrossLineArrowAtEnd",
    "CrossLineArrowAtEnds",
    "CrossLineWideArrowAtEnd",
    "CrossLineWideArrowAtEnds",
    "CrossLineSquareAtEnd",
    "CrossLineSquareAtEnds",
    "CrossLineDiamondAtEnd",
    "CrossLineDiamondAtEnds",
    "CrossLineCircleAtEnd",
    "CrossLineCircleAtEnds",
    "CrossLineTriangleAtEnd",
    "CrossLineTriangleAtEnds",
    "CrossLineSwapped",
    "CrossLineSwappedArrowAtEnd",
    "CrossLineSwappedArrowAtEnds",
    "CrossLineSwappedWideArrowAtEnd",
    "CrossLineSwappedWideArrowAtEnds",
    "CrossLineSwappedSquareAtEnd",
    "CrossLineSwappedSquareAtEnds",
    "CrossLineSwappedDiamondAtEnd",
    "CrossLineSwappedDiamondAtEnds",
    "CrossLineSwappedCircleAtEnd",
    "CrossLineSwappedCircleAtEnds",
    "CrossLineSwappedTriangleAtEnd",
    "CrossLineSwappedTriangleAtEnds",
    "CrossLine3Axis",
    "CrossLine3AxisEndCube",
    "CrossLine3AxisEndOctahedron",
    "CrossLine3AxisEndSphere",
    "CrossLine3AxisEndPyramid",
    "CrossLine3AxisEndCone",
    "Triangle",
    "Square",
    "SquareArrow2D",
    "SquareArrow3D",
    "SquareArrowCrossLine2D",
    "SquareArrowCrossLine3D",
    "SquareArrowCrossLineTemplate2D",
    "SquareArrowCrossLineTemplate3D",
    "SquareArrow4Way2D",
    "SquareArrow4Way3D",
    "SquareTemplateArrow4Way2D",
    "SquareTemplateArrow4Way3D",
    "Diamond",
    "Cube",
    "CubeArrow2D",
    "CubeArrow3D",
    "Octahedron",
    "OctahedronArrow",
    "Arc",
    "ArcArrow2D",
    "ArcArrow3D",
    "Semicircle",
    "SemicircleArrowAtEnd",
    "SemicircleArrowAtEnds",
    "SemicircleWideArrowAtEnd",
    "SemicircleWideArrowAtEnds",
    "SemicircleArrow2D",
    "SemicircleArrow3D",
    "Sphere",
    "SphereArrow2D",
    "SphereArrow3D",
    "Cylinder",
    "Arrow",
    "Pyramid",
    "Cone",
    "ColorCrossLine3Axis",
    "ColorCrossLine3AxisEndCube",
    "ColorCrossLine3AxisEndOctahedron",
    "ColorCrossLine3AxisEndSphere",
    "ColorCrossLine3AxisEndPyramid",
    "ColorCrossLine3AxisEndCone",
    "ColorCube",
    "ColorCornerCube",
    "ColorSphere",
    "ColorSphereArrow2D",
    "ColorSphereArrow3D",
    "ColorSphereCrossLine",
)


# Finの組合せを指定するテストケース名。
FIN_CASES = {
    "CubeFin": ("Cube", 0),
    "CubeFinArrow": ("Cube", 1),
    "CylinderFin": ("Cylinder", 0),
    "CylinderFinArrow": ("Cylinder", 1),
    "OctahedronArrowFin": ("OctahedronArrow", 0),
    "ArrowFin": ("Arrow", 1),
    "PyramidFin": ("Pyramid", 0),
    "ConeFin": ("Cone", 0),
}


# Filled接尾辞は回帰テストのケース名であり、公開shape enumの名前ではない。
SHAPE_VARIANTS = tuple(
    name + suffix
    for name in dict.fromkeys(
        (*VARIANT_NAMES, *GUIDE_CASES, *OPTION_CASE_NAMES, *FIN_CASES)
    )
    for suffix in ("", "Filled")
)


def _case_settings(case_name):
    # 本体と共通オプションの組合せを、テスト用の短縮名から指定する。
    name = case_name.removesuffix("Filled")
    name = {"Arc": "ArcRadial", "CrossArc": "CrossArcRadial"}.get(name, name)
    fin = FIN_CASES.get(name)
    base = fin[0] if fin else name
    settings = {
        "shapeFill": case_name.endswith("Filled"),
        "shapeFin": fin is not None,
        "shapeFinType": fin[1] if fin else 0,
        "shapePart": False,
        "shapePartShape": 0,
        "shapePartType": 0,
        "shapeGuideLine": False,
        "shapeGuideLineTemplate": False,
        "shapeArcAngle": 180 if base.startswith("Semicircle") else 360,
    }
    if base not in VARIANT_NAMES and base not in GUIDE_CASES:
        settings["shapePart"] = base != "Semicircle"
        if base.startswith("Semicircle"):
            settings["shapePartType"] = 1 if base.endswith("AtEnds") else 0
            if base.endswith(("Arrow2D", "Arrow3D")):
                settings["shapePartType"] = 2
                settings["shapePartShape"] = int(base.endswith("Arrow3D"))
            base = "WideArcRadial" if "Wide" in base else "ArcRadial"
        elif "CrossLine3AxisEnd" in base:
            prefix, part = base.split("End")
            settings["shapePartType"] = 1
            settings["shapePartShape"] = PART_SHAPES.index(part)
            base = prefix
        elif base.endswith(("AtEnd", "AtEnds")):
            ending = "AtEnds" if base.endswith("AtEnds") else "AtEnd"
            settings["shapePartType"] = int(ending == "AtEnds")
            body_part = base.removesuffix(ending)
            for part in (
                "WideArrow",
                "Arrow",
                "Triangle",
                "Square",
                "Diamond",
                "Circle",
            ):
                if body_part.endswith(part):
                    base = body_part.removesuffix(part)
                    settings["shapePartShape"] = PART_SHAPES.index(
                        "Arrow2D" if part.endswith("Arrow") else part
                    )
                    if part == "WideArrow":
                        base = "Wide" + base
                    break
        elif base.startswith("Square"):
            settings["shapePartShape"] = int(base.endswith("3D"))
            settings["shapePartType"] = int("4Way" in base)
            if "CrossLineTemplate" in base:
                base = "SquareCrossLineTemplate"
            elif "CrossLine" in base:
                base = "SquareCrossLine"
            elif "Template" in base:
                base = "SquareTemplate"
            else:
                base = "Square"
        elif base.endswith(("Arrow2D", "Arrow3D")):
            settings["shapePartShape"] = int(base.endswith("Arrow3D"))
            base = base[:-7]
            if base == "Arc":
                settings["shapePartType"] = 2
        else:
            raise AssertionError(case_name)
    if base in GUIDE_CASES:
        base, template = GUIDE_CASES[base]
        settings["shapeGuideLine"] = True
        settings["shapeGuideLineTemplate"] = template
    base = {"Arc": "ArcRadial", "CrossArc": "CrossArcRadial"}.get(base, base)
    if "Arc" in base and not base.endswith("Swapped"):
        # 曲面とPart接合の回帰検証は、明示した軸で従来のYZ基準座標へ戻す。
        settings["shape1stAxis"] = 2
        settings["shape2ndAxis"] = 0
    settings.update(preset_options(base))
    return settings


def _shape_index(case_name):
    return _case_settings(case_name)["shape"]


def _set_shape(maya_cmds, shape, case_name):
    for name, value in _case_settings(case_name).items():
        if (
            name == "shapeArcAngle"
            and maya_cmds.currentUnit(query=True, angle=True) == "rad"
        ):
            value = math.radians(value)
        maya_cmds.setAttr(f"{shape}.{name}", value)


def _set_shape_operator(shape, case_name):
    for name, value in _case_settings(case_name).items():
        getattr(shape, name).set(value)


def _load_bd_util_nodes(maya_cmds) -> None:
    default_path = (
        Path(__file__).resolve().parents[7]
        / "bakedanuki"
        / "bakedanuki-util"
        / "plug-ins"
        / "maya2025"
        / "bdUtilNodes.mll"
    )
    plugin_path = Path(
        os.environ.get("BD_UTIL_NODES_PLUGIN_PATH", default_path)
    )
    if not plugin_path.is_file():
        pytest.skip("bdUtilNodes.mll is not built")
    maya_cmds.loadPlugin(str(plugin_path), quiet=True)
    maya_cmds.currentUnit(angle="degree")


def _create_controller(
    maya_cmds,
    *,
    name="controller",
    shape_name="SquareSwapped",
    shape_fill=None,
    bounds_mode=0,
) -> tuple[str, str]:
    # 向きと無関係な既存の変形テストでは、YZ面の四角を基準に使う。
    transform = maya_cmds.createNode("transform", name=name)
    shape = maya_cmds.createNode(
        "bdControllerShape", parent=transform, name=f"{name}Shape"
    )
    if shape_name is not None:
        _set_shape(maya_cmds, shape, shape_name)
    if shape_fill is not None:
        maya_cmds.setAttr(f"{shape}.shapeFill", shape_fill)
    if bounds_mode is not None:
        maya_cmds.setAttr(f"{shape}.boundsMode", bounds_mode)
    return transform, shape


def _bounds(maya_om, shape: str) -> tuple[float, ...]:
    selection = maya_om.MSelectionList()
    selection.add(shape)
    bounds = maya_om.MFnDagNode(selection.getDagPath(0)).boundingBox
    return (
        bounds.min.x,
        bounds.min.y,
        bounds.min.z,
        bounds.max.x,
        bounds.max.y,
        bounds.max.z,
    )


def _three_axis_solid_part_bounds(
    part, offset=0, length=1, width=1, size=1, height=1
):
    # 代表の+X端は等倍、残る5端は半分の寸法で、Offsetの距離は共通にする。
    points = [(0.0, 0.0, 0.0)]
    for axis in range(3):
        for sign in (-1, 1):
            end_size = size * (1.0 if axis == 0 and sign > 0 else 0.5)
            center = 0.5 + offset
            depth = 0.05 * length * end_size
            along = (center - depth, center + depth)
            if part in ("Pyramid", "Cone"):
                along = (center - 2 * depth, center)
            side_axis = 0 if axis == 2 else 2
            up_axis = next(i for i in range(3) if i not in (axis, side_axis))
            side_extent = 0.05 * abs(width * end_size)
            up_extent = 0.05 * abs(height * end_size)
            for coordinate in along:
                for first in (-side_extent, side_extent):
                    for second in (-up_extent, up_extent):
                        point = [0.0, 0.0, 0.0]
                        point[axis] = sign * coordinate
                        point[side_axis] = first
                        point[up_axis] = second
                        points.append(tuple(point))
    return tuple(min(point[i] for point in points) for i in range(3)) + tuple(
        max(point[i] for point in points) for i in range(3)
    )


def test_generated_shape_enum_matches_presets():
    assert len(SHAPE_NAMES) == 24
    assert SHAPE_NAMES.index("Cube") == 12
    assert ShapeEnumAttrOperator.NAME_MAP == dict(enumerate(SHAPE_NAMES))
    assert all(
        getattr(ShapeEnumPlugOperator, name.upper()) == index
        for index, name in enumerate(SHAPE_NAMES)
    )


def test_node_type_defaults_and_single_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(
        maya_cmds, shape_name=None, bounds_mode=None
    )

    selection = maya_om.MSelectionList()
    selection.add(shape)
    node_fn = maya_om.MFnDependencyNode(selection.getDependNode(0))
    assert node_fn.typeId.id() == 0x0014271F
    assert maya_cmds.nodeType(shape) == "bdControllerShape"
    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert maya_cmds.attributeQuery("shape", node=shape, listEnum=True) == [
        ":".join(SHAPE_NAMES)
    ]
    assert maya_cmds.getAttr(f"{shape}.shape") == _shape_index("Cube")
    assert maya_cmds.attributeQuery("shape", node=shape, listDefault=True) == [
        12
    ]
    for attribute, default in (("shape1stAxis", 0), ("shape2ndAxis", 2)):
        assert maya_cmds.attributeQuery(
            attribute, node=shape, listEnum=True
        ) == ["+X:-X:+Y:-Y:+Z:-Z"]
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
    assert maya_cmds.getAttr(f"{shape}.shapeRootSize") == pytest.approx(1.0)
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix", type=True)
        == "matrix"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAnimationTransformMatrix", node=shape, attributeType=True
        )
        == "typed"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAnimationTransformMatrix", node=shape, shortName=True
        )
        == "satm"
    )
    matrix_data = maya_om.MFnMatrixData(
        node_fn.findPlug("shapeAnimationTransformMatrix", False).asMObject()
    )
    assert list(matrix_data.matrix()) == pytest.approx(list(maya_om.MMatrix()))
    assert maya_cmds.getAttr(f"{shape}.shapeTranslate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeRotate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeScale")[0] == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(
        f"{shape}.shapeAxisOffsetLength"
    ) == pytest.approx(1.0)
    assert (
        maya_cmds.attributeQuery(
            "shapeAxisOffsetLength", node=shape, shortName=True
        )
        == "saol"
    )
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetLength", node=shape, minExists=True
    )
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetLength", node=shape, minimum=True
    ) == [0.0]
    assert not maya_cmds.getAttr(f"{shape}.shapeAxisOffset")
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection") == 0
    assert maya_cmds.attributeQuery(
        "shapeAxisOffsetDirection", node=shape, listEnum=True
    ) == ["+1stAxis:-1stAxis:+2ndAxis:-2ndAxis:+3rdAxis:-3rdAxis"]
    assert (
        maya_cmds.attributeQuery("shapeAxisOffset", node=shape, shortName=True)
        == "sao"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeAxisOffsetDirection", node=shape, shortName=True
        )
        == "saod"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisTranslate")[
        0
    ] == pytest.approx((0.0, 0.0, 0.0))
    assert maya_cmds.getAttr(f"{shape}.shapeAxisRotate")[0] == pytest.approx(
        (0.0, 0.0, 0.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScale")[0] == pytest.approx(
        (1.0, 1.0, 1.0)
    )
    assert maya_cmds.getAttr(f"{shape}.shapeSize") == pytest.approx(1.0)
    for attribute, short_name, kind, default in (
        ("shapePartOffset", "spo", "doubleLinear", 0.0),
        ("shapeFinHeight", "sfnh", "doubleLinear", 0.5),
        ("shapeFinSize", "sfns", "double", 1.0),
        ("shapeFinWidthScale", "sfnws", "double", 1.0),
        ("shapePartSize", "sps", "double", 1.0),
        ("shapePartPrimarySizeScale", "sppss", "double", 1.0),
        ("shapePartOtherSizeScale", "sposs", "double", 0.5),
        ("shapePartLengthScale", "spls", "double", 1.0),
        ("shapePartWidthScale", "spws", "double", 1.0),
        ("shapePartHeightScale", "sphs", "double", 1.0),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == pytest.approx(
            default
        )
        assert maya_cmds.getAttr(f"{shape}.{attribute}", type=True) == kind
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert not maya_cmds.attributeQuery(
            attribute, node=shape, minExists=True
        )
        assert not maya_cmds.attributeQuery(
            attribute, node=shape, maxExists=True
        )
    assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == 180.0
    for attribute, short_name in (
        ("shapeAxisSwap", "sasw"),
        ("shapeWide", "swd"),
        ("shapeTemplateLine", "stl"),
        ("shapeTemplateFill", "stf"),
        ("shapeTemplateLineInvert", "stli"),
        ("shapePartTemplate", "spte"),
        ("shapeFinTemplate", "sft"),
        ("shapeGuideLine", "sgl"),
        ("shapeGuideLineTemplate", "sglt"),
    ):
        assert not maya_cmds.getAttr(f"{shape}.{attribute}")
        assert maya_cmds.getAttr(f"{shape}.{attribute}", type=True) == "bool"
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    assert maya_cmds.getAttr(
        f"{shape}.shapeTemplateLineRate"
    ) == pytest.approx(0.7)
    assert (
        maya_cmds.getAttr(f"{shape}.shapeTemplateLineRate", type=True)
        == "double"
    )
    assert (
        maya_cmds.attributeQuery(
            "shapeTemplateLineRate", node=shape, shortName=True
        )
        == "stlr"
    )
    assert maya_cmds.attributeQuery(
        "shapeTemplateLineRate", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeTemplateLineRate", node=shape, maximum=True
    ) == [1.0]
    assert not maya_cmds.getAttr(f"{shape}.shapePart")
    assert maya_cmds.getAttr(f"{shape}.shapePart", type=True) == "bool"
    for attribute, short_name, names in (
        ("shapePartShape", "spsh", PART_SHAPES),
        ("shapePartType", "sptp", ("AtEnd", "AtEnds", "AtApex")),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == 0
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert maya_cmds.attributeQuery(
            attribute, node=shape, listEnum=True
        ) == [":".join(names)]
    assert (
        maya_cmds.attributeQuery("shapePart", node=shape, shortName=True)
        == "spt"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeWideWidth") == pytest.approx(0.05)
    assert (
        maya_cmds.getAttr(f"{shape}.shapeWideWidth", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.attributeQuery("shapeWideWidth", node=shape, shortName=True)
        == "sww"
    )
    assert maya_cmds.attributeQuery(
        "shapeWideWidth", node=shape, minimum=True
    ) == [0.0]
    assert not maya_cmds.attributeQuery(
        "shapeWideWidth", node=shape, maxExists=True
    )
    for removed in (
        "shapeTransparency",
        "shapePartFinHeight",
        "shapePartOffsetAngle",
        "showShapeOffsetLine",
    ):
        assert not maya_cmds.attributeQuery(removed, node=shape, exists=True)
    assert maya_cmds.getAttr(f"{shape}.shapeFinType") == 0
    assert not maya_cmds.getAttr(f"{shape}.shapeFin")
    assert maya_cmds.getAttr(f"{shape}.shapeFin", type=True) == "bool"
    assert (
        maya_cmds.attributeQuery("shapeFin", node=shape, shortName=True)
        == "sfn"
    )
    assert (
        maya_cmds.attributeQuery("shapeFinType", node=shape, shortName=True)
        == "sfnt"
    )
    assert maya_cmds.attributeQuery(
        "shapeFinType", node=shape, listEnum=True
    ) == ["Standard:Tapered"]
    assert (
        maya_cmds.getAttr(f"{shape}.shapeArcAngle", type=True) == "doubleAngle"
    )
    assert (
        maya_cmds.attributeQuery("shapeArcAngle", node=shape, shortName=True)
        == "saa"
    )
    assert maya_cmds.attributeQuery(
        "shapeArcAngle", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeArcAngle", node=shape, maximum=True
    ) == [360.0]
    assert not maya_cmds.getAttr(f"{shape}.shapeOffsetLine")
    assert not maya_cmds.getAttr(f"{shape}.shapeOffsetLineTemplate")
    assert (
        maya_cmds.attributeQuery(
            "shapeOffsetLineTemplate", node=shape, shortName=True
        )
        == "solt"
    )
    assert not maya_cmds.attributeQuery(
        "shapeOffsetLineSelectable", node=shape, exists=True
    )
    for attribute, short_name, default in (
        ("shapeLineWidth", "slw", 1.0),
        ("shapeLineTransparency", "slt", 0.0),
        ("shapeFill", "sfl", False),
        ("shapeFillTransparency", "sftp", pytest.approx(0.85)),
        ("shapeDrawOnTop", "sdot", False),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
        assert (
            maya_cmds.attributeQuery(attribute, node=shape, shortName=True)
            == short_name
        )
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    assert maya_cmds.getAttr(f"{shape}.shapeLineWidth", type=True) == "float"
    assert (
        maya_cmds.getAttr(f"{shape}.shapeLineTransparency", type=True)
        == "float"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeFillTransparency", type=True)
        == "float"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeDrawOnTop", type=True) == "bool"
    assert maya_cmds.getAttr(f"{shape}.shapeFill", type=True) == "bool"
    assert maya_cmds.attributeQuery(
        "shapeLineWidth", node=shape, minimum=True
    ) == [1.0]
    assert maya_cmds.attributeQuery(
        "shapeLineTransparency", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeLineTransparency", node=shape, maximum=True
    ) == [1.0]
    assert maya_cmds.attributeQuery(
        "shapeFillTransparency", node=shape, minimum=True
    ) == [0.0]
    assert maya_cmds.attributeQuery(
        "shapeFillTransparency", node=shape, maximum=True
    ) == [1.0]
    assert (
        maya_cmds.getAttr(f"{shape}.shapeTranslateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeRotateX", type=True) == "doubleAngle"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeScaleX", type=True) == "double"
    assert not maya_cmds.getAttr(
        f"{shape}.shapeAnimationTransformMatrix", keyable=True
    )
    assert not maya_cmds.getAttr(
        f"{shape}.shapeAnimationTransformMatrix", channelBox=True
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisOffsetLength", type=True)
        == "doubleLinear"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffset", type=True) == "bool"
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection", type=True)
        == "enum"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisTranslateX", type=True)
        == "doubleLinear"
    )
    assert (
        maya_cmds.getAttr(f"{shape}.shapeAxisRotateX", type=True)
        == "doubleAngle"
    )
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScaleX", type=True) == "double"
    for attribute in (
        "shape",
        "shape1stAxis",
        "shape2ndAxis",
        "shapeRootSize",
        "shapeTranslate",
        "shapeTranslateX",
        "shapeTranslateY",
        "shapeTranslateZ",
        "shapeRotate",
        "shapeRotateX",
        "shapeRotateY",
        "shapeRotateZ",
        "shapeScale",
        "shapeScaleX",
        "shapeScaleY",
        "shapeScaleZ",
        "shapeAxisOffsetLength",
        "shapeAxisOffset",
        "shapeAxisOffsetDirection",
        "shapeAxisTranslate",
        "shapeAxisTranslateX",
        "shapeAxisTranslateY",
        "shapeAxisTranslateZ",
        "shapeAxisRotate",
        "shapeAxisRotateX",
        "shapeAxisRotateY",
        "shapeAxisRotateZ",
        "shapeAxisScale",
        "shapeAxisScaleX",
        "shapeAxisScaleY",
        "shapeAxisScaleZ",
        "shapeSize",
        "shapePartOffset",
        "shapeArcAngle",
        "shapeFinHeight",
        "shapePartSize",
        "shapePartPrimarySizeScale",
        "shapePartOtherSizeScale",
        "shapePartLengthScale",
        "shapePartWidthScale",
        "shapeTemplateLineRate",
        "shapeOffsetLine",
        "shapeOffsetLineTemplate",
        "shapeLineWidth",
        "shapeLineTransparency",
        "shapeFill",
        "shapeFillTransparency",
        "shapeDrawOnTop",
    ):
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)

    for attribute in (
        "shapePart",
        "shapePartShape",
        "shapePartType",
        "shapeWideWidth",
        "shapeFin",
        "shapeFinType",
        "shapeFinSize",
        "shapeFinWidthScale",
    ):
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)

    for index in range(1, 17):
        separator = "_" * index
        assert (
            maya_cmds.attributeQuery(separator, node=shape, shortName=True)
            == separator
        )
        assert maya_cmds.attributeQuery(
            separator, node=shape, listEnum=True
        ) == ["-----------------------------------"]
        assert maya_cmds.getAttr(f"{shape}.{separator}", type=True) == "enum"
        assert maya_cmds.getAttr(f"{shape}.{separator}") == 0
        assert maya_cmds.getAttr(f"{shape}.{separator}", lock=True)
        assert not maya_cmds.getAttr(f"{shape}.{separator}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{separator}", channelBox=True)

    channel_order = maya_cmds.listAttr(shape, channelBox=True)
    ordered_attributes = (
        "_",
        "shape1stAxis",
        "shape2ndAxis",
        "shapeAxisSwap",
        "shape",
        "__",
        "shapeDrawOnTop",
        "___",
        "shapeLineWidth",
        "shapeLineTransparency",
        "____",
        "shapeFill",
        "shapeFillTransparency",
        "_____",
        "shapeTemplateLine",
        "shapeTemplateLineRate",
        "shapeTemplateLineInvert",
        "shapeTemplateFill",
        "shapePartTemplate",
        "shapeFinTemplate",
        "shapeGuideLineTemplate",
        "shapeOffsetLineTemplate",
        "______",
        "shapeWide",
        "shapeWideWidth",
        "_______",
        "shapeArcAngle",
        "________",
        "shapePart",
        "shapePartShape",
        "shapePartType",
        "shapePartOffset",
        "shapePartSize",
        "shapePartPrimarySizeScale",
        "shapePartOtherSizeScale",
        "shapePartLengthScale",
        "shapePartWidthScale",
        "shapePartHeightScale",
        "_________",
        "shapeFin",
        "shapeFinType",
        "shapeFinHeight",
        "shapeFinSize",
        "shapeFinWidthScale",
        "__________",
        "shapeGuideLine",
        "___________",
        "shapeOffsetLine",
        "____________",
        "shapeAxisOffset",
        "shapeAxisOffsetDirection",
        "shapeAxisOffsetLength",
        "_____________",
        "shapeRootSize",
        "shapeTranslateX",
        "shapeRotateX",
        "shapeScaleX",
        "shapeAxisTranslateX",
        "shapeAxisRotateX",
        "shapeAxisScaleX",
        "shapeSize",
        "______________",
        "boundsMode",
        "showBoundsPreview",
        "_______________",
        "customBounds1stAxis",
        "customBounds2ndAxis",
        "customBoundsAxisOffset",
        "customBoundsAxisOffsetDirection",
        "customBoundsAxisOffsetLength",
        "________________",
        "customBoundsRootSize",
        "customBoundsTranslateX",
        "customBoundsRotateX",
        "customBoundsScaleX",
        "customBoundsAxisTranslateX",
        "customBoundsAxisRotateX",
        "customBoundsAxisScaleX",
        "customBoundsSize",
    )
    expected_channel_order = tuple(
        child
        for attribute in ordered_attributes
        for child in (
            tuple(attribute[:-1] + component for component in "XYZ")
            if attribute.endswith("X")
            else (attribute,)
        )
    )
    visible_channels = tuple(
        attribute
        for attribute in channel_order
        if not maya_cmds.attributeQuery(
            attribute, node=shape, listChildren=True
        )
    )
    assert visible_channels == expected_channel_order


def test_inherited_locator_channels_are_hidden_only_on_controller_shape(
    maya_cmds, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    locator_shape = maya_cmds.createNode(
        "locator", name="standardLocatorShape"
    )
    inherited_channels = (
        "localPositionX",
        "localPositionY",
        "localPositionZ",
        "localScaleX",
        "localScaleY",
        "localScaleZ",
    )

    def assert_channel_visibility() -> None:
        for attribute in inherited_channels:
            assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
            assert not maya_cmds.getAttr(
                f"{shape}.{attribute}", channelBox=True
            )
            assert maya_cmds.getAttr(
                f"{locator_shape}.{attribute}", channelBox=True
            )

    assert_channel_visibility()

    scene_path = tmp_path / "controller_shape_channels.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert_channel_visibility()


@pytest.mark.parametrize(
    ("shape_name", "expected_bounds"),
    (
        ("Triangle", (-0.37, 0.0, -0.5, 0.5, 0.0, 0.5)),
        (
            "TriangleFilled",
            (-0.37, 0.0, -0.5, 0.5, 0.0, 0.5),
        ),
        ("Square", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("SquareFilled", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("Cube", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        ("CubeFilled", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        ("Octahedron", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            "OctahedronFilled",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        ("Arc", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        ("ArcFilled", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (
            "ArcArrow2D",
            (0.0, -0.5, -0.5, 0.0, 0.625, 0.5),
        ),
        ("Sphere", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        ("SphereFilled", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        ("Cylinder", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            "CylinderFilled",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        ("Pyramid", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (
            "PyramidFilled",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),
        ("Cone", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        ("ConeFilled", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
    ),
)
def test_shape_bounds(
    maya_cmds, maya_om, new_scene, shape_name, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, shape_name)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize("base", PLANAR_BASES)
@pytest.mark.parametrize("filled", (False, True))
def test_planar_base_uses_first_third_plane(
    maya_cmds, maya_om, new_scene, base, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=base, shape_fill=filled
    )
    low = -0.37 if base == "Triangle" else -0.5
    assert _bounds(maya_om, shape) == pytest.approx(
        (low, 0, -0.5, 0.5, 0, 0.5), abs=1e-9
    )


@pytest.mark.parametrize("base", SWAPPED_BASES)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("first_axis,second_axis", ((0, 2), (1, 4), (5, 3)))
@pytest.mark.parametrize(
    "part,placement,fin_type", ((None, 0, 0), (1, 0, 1), (9, 1, 0))
)
def test_swapped_geometry_follows_right_handed_axis_exchange(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    filled,
    first_axis,
    second_axis,
    part,
    placement,
    fin_type,
):
    _load_bd_util_nodes(maya_cmds)
    _, reference = _create_controller(
        maya_cmds, shape_name=base, shape_fill=filled
    )
    _, swapped = _create_controller(
        maya_cmds,
        name="swapped",
        shape_name=base + "Swapped",
        shape_fill=filled,
    )
    for shape in (reference, swapped):
        for name, value in (
            ("shapePart", part is not None),
            ("shapePartShape", part if part is not None else 0),
            ("shapePartType", placement),
            ("shapePartOffset", 0.17),
            ("shapePartLengthScale", -1.3),
            ("shapePartWidthScale", 1.7),
            ("shapeFin", part is not None),
            ("shapeFinType", fin_type),
            ("shapeFinHeight", 0.8),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
        maya_cmds.setAttr(f"{shape}.shapeScale", -2, 0.7, 1.3)
        maya_cmds.setAttr(f"{shape}.shapeRotate", 17, -31, 23)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 0.4, -0.2, 0.6)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.2)
        maya_cmds.setAttr(
            f"{shape}.shapeAnimationTransformMatrix",
            1,
            0.2,
            -0.1,
            0,
            -0.3,
            1,
            0.4,
            0,
            0.1,
            -0.2,
            1,
            0,
            0.3,
            0.5,
            -0.2,
            1,
            type="matrix",
        )
    # 軸を交換すると第3軸も反転し、本体・Part・Finの全頂点が同じ位置へ移る。
    maya_cmds.setAttr(f"{reference}.shape1stAxis", second_axis)
    maya_cmds.setAttr(f"{reference}.shape2ndAxis", first_axis)
    maya_cmds.setAttr(f"{reference}.shapeAxisScale", -3, 2, 1.5)
    maya_cmds.setAttr(f"{reference}.shapeAxisTranslate", -0.1, 0.2, -0.3)
    maya_cmds.setAttr(f"{swapped}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{swapped}.shape2ndAxis", second_axis)
    maya_cmds.setAttr(f"{swapped}.shapeAxisScale", 2, -3, 1.5)
    maya_cmds.setAttr(f"{swapped}.shapeAxisTranslate", 0.2, -0.1, 0.3)
    assert _bounds(maya_om, swapped) == pytest.approx(
        _bounds(maya_om, reference), abs=1e-8
    )


@pytest.mark.parametrize("base", ("Line", "CrossLine", *PLANAR_BASES))
@pytest.mark.parametrize("filled", (False, True))
def test_tapered_fin_narrows_toward_positive_first_axis(
    maya_cmds, maya_om, new_scene, base, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=base, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 1)
    # YへXを加え、Finの高い端が-1st側にあることを範囲から区別する。
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix",
        1,
        1,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        1,
        type="matrix",
    )
    assert _bounds(maya_om, shape)[4] == pytest.approx(1.5)
    maya_cmds.setAttr(f"{shape}.shapeFinType", 1)
    expected = 0.63 if base == "Triangle" else 0.5
    assert _bounds(maya_om, shape)[4] == pytest.approx(expected)


def test_sphere_filled_bounds_include_surface_vertices(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = (
        1.0,
        0.0,
        0.0,
        0.0,
        1.0,
        1.0,
        0.0,
        0.0,
        1.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
    )
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix, type="matrix"
    )
    _set_shape(maya_cmds, shape, "Sphere")
    wire_bounds = _bounds(maya_om, shape)
    _set_shape(maya_cmds, shape, "SphereFilled")
    filled_bounds = _bounds(maya_om, shape)

    assert filled_bounds[3] > wire_bounds[3] + 0.1
    assert filled_bounds[0] < wire_bounds[0] - 0.1


@pytest.mark.parametrize("shape_name", SHAPE_VARIANTS)
def test_every_preset_has_a_drawable_extent(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, shape_name)

    bounds = _bounds(maya_om, shape)
    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert any(bounds[axis + 3] > bounds[axis] for axis in range(3))


@pytest.mark.parametrize(
    "filled_name",
    tuple(name for name in SHAPE_VARIANTS if name.endswith("Filled")),
)
def test_fill_toggle_preserves_default_outline_bounds(
    maya_cmds, maya_om, new_scene, filled_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    base_name = filled_name.removesuffix("Filled")
    _set_shape(maya_cmds, shape, base_name)
    outline_bounds = _bounds(maya_om, shape)
    _set_shape(maya_cmds, shape, filled_name)

    assert _bounds(maya_om, shape) == pytest.approx(outline_bounds, abs=1.0e-9)


@pytest.mark.parametrize("connected", (False, True))
@pytest.mark.parametrize("mode", (0, 1, 2))
def test_fill_toggle_invalidates_bounds_and_keeps_transparency(
    maya_cmds, maya_om, new_scene, connected, mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="Semicircle", bounds_mode=mode
    )
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 120)
    maya_cmds.setAttr(f"{shape}.shapeFillTransparency", 0.42)
    target = f"{shape}.shapeFill"
    if connected:
        source = maya_cmds.createNode("network")
        maya_cmds.addAttr(source, longName="fill", attributeType="bool")
        target = f"{source}.fill"
        maya_cmds.connectAttr(target, f"{shape}.shapeFill")
    z = math.sqrt(3) / 4
    for fill in (False, True, False, True):
        maya_cmds.setAttr(target, fill)
        if mode == 0:
            expected = (0, 0.25, -z, 0, 0.5, z)
        elif mode == 1:
            height = 0.125
            expected = (0, -height, -z, 0, height, z)
        else:
            expected = (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(
            f"{shape}.shapeFillTransparency"
        ) == pytest.approx(0.42)
    set_preset(maya_cmds, shape, "Cube")
    assert maya_cmds.getAttr(f"{shape}.shapeFill")
    set_preset(maya_cmds, shape, "Line")
    assert maya_cmds.getAttr(f"{shape}.shapeFill")


def test_fill_animation_updates_cached_bounds(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Semicircle")
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 120)
    maya_cmds.setKeyframe(shape, attribute="shapeFill", time=1, value=0)
    maya_cmds.setKeyframe(shape, attribute="shapeFill", time=10, value=1)
    for time, minimum in ((1, 0.25), (10, 0.25), (1, 0.25)):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape)[1] == pytest.approx(minimum)


def test_fill_option_connection_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds, shape_name="Semicircle")
    maya_cmds.setAttr(f"{name}.shapeArcAngle", 120)
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="fill", attributeType="bool", defaultValue=True
    )
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shapeFill.set(True)
    shape.shapeFill.connect_from(f"{source}.fill")
    shape.shapeFillTransparency.set(0.37)
    mod.do_it_dg()
    assert _bounds(maya_om, name)[1] == pytest.approx(0.25)
    mod.undo_it()
    assert _bounds(maya_om, name)[1] == pytest.approx(0.25)
    mod.redo_it()
    assert _bounds(maya_om, name)[1] == pytest.approx(0.25)
    path = tmp_path / "shape_fill.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert maya_cmds.getAttr(f"{name}.shapeFill")
    assert maya_cmds.getAttr(f"{name}.shapeFillTransparency") == pytest.approx(
        0.37
    )
    assert maya_cmds.isConnected(f"{source}.fill", f"{name}.shapeFill")
    assert _bounds(maya_om, name)[1] == pytest.approx(0.25)
    maya_cmds.setAttr(f"{source}.fill", False)
    assert _bounds(maya_om, name)[1] == pytest.approx(0.25)


@pytest.mark.parametrize(
    ("shape_name", "expected_bounds"),
    (
        ("Gear", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),  # Gear
        (
            "Line",
            (-0.5, 0.0, 0.0, 0.5, 0.0, 0.0),
        ),  # Line
        (
            "CubeFin",
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CubeFin
        (
            "CubeFinArrow",
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CubeFinArrow
        (
            "OctahedronArrow",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # OctahedronArrow
        (
            "ArcArrow3D",
            (0.0, -0.5, -0.5, 0.0625, 0.625, 0.5),
        ),  # ArcArrow3D
        (
            "Semicircle",
            (0.0, 0.0, -0.5, 0.0, 0.5, 0.5),
        ),  # Semicircle
        (
            "CylinderFinArrow",
            (-0.5, -0.5, -0.5, 0.5, 1.0, 0.5),
        ),  # CylinderFinArrow
        (
            "ColorCrossLine3Axis",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorCrossLine3Axis
        (
            "ColorSphere",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorSphere
        (
            "ColorSphereArrow2D",
            (-0.5, -0.5, -0.5, 0.625, 0.5, 0.5),
        ),  # ColorSphereArrow2D
        (
            "ColorSphereArrow3D",
            (-0.5, -0.5, -0.5, 0.625, 0.5, 0.5),
        ),  # ColorSphereArrow3D
        (
            "ColorSphereCrossLine",
            (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
        ),  # ColorSphereCrossLine
    ),
)
def test_preset_base_and_decoration_bounds(
    maya_cmds, maya_om, new_scene, shape_name, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, shape_name)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_VARIANTS if name.startswith("Line")]
)
@pytest.mark.parametrize(
    "first_axis,second_axis,order,signs",
    (
        (0, 2, (0, 1, 2), (1, 1, 1)),
        (1, 2, (0, 1, 2), (-1, 1, -1)),
        (2, 0, (1, 0, 2), (1, 1, -1)),
        (3, 0, (1, 0, 2), (1, -1, 1)),
        (4, 0, (1, 2, 0), (1, 1, 1)),
        (5, 0, (1, 2, 0), (1, -1, -1)),
    ),
)
def test_line_follows_selected_axis_basis(
    maya_cmds,
    maya_om,
    new_scene,
    shape_name,
    first_axis,
    second_axis,
    order,
    signs,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.5)
    original = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", second_axis)
    low = [
        min(original[axis] * sign, original[axis + 3] * sign)
        for axis, sign in zip(order, signs)
    ]
    high = [
        max(original[axis] * sign, original[axis + 3] * sign)
        for axis, sign in zip(order, signs)
    ]
    assert _bounds(maya_om, shape) == pytest.approx((*low, *high), abs=1e-9)


@pytest.mark.parametrize(
    ("shape_name", "expected"),
    (
        ("CrossLine", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("CrossLineSwapped", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        ("CrossLine3Axis", (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
    ),
)
def test_crossline_uses_named_axis_plane(
    maya_cmds, maya_om, new_scene, shape_name, expected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    ("base_name", "expected"),
    (
        ("Line", (-0.5, 0.0, -0.05, 0.5, 0.0, 0.05)),
        ("CrossLine", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("CrossLineSwapped", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (
            "Semicircle",
            (
                0.0,
                0.0,
                -_circle_arrow_outer_extent(0.1 * math.cos(math.pi / 6), 0.05),
                0.0,
                0.5,
                _circle_arrow_outer_extent(0.1 * math.cos(math.pi / 6), 0.05),
            ),
        ),
    ),
)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("remap_axes", (False, True))
@pytest.mark.parametrize("wide", (False, True))
def test_end_arrow_extent_and_axis_transform(
    maya_cmds,
    maya_om,
    new_scene,
    base_name,
    expected,
    filled,
    remap_axes,
    wide,
):
    _load_bd_util_nodes(maya_cmds)
    shape_name = (
        base_name
        + ("WideArrowAtEnds" if wide else "ArrowAtEnds")
        + ("Filled" if filled else "")
    )
    if wide and base_name == "Semicircle":
        expected = (*expected[:4], 0.525, expected[5])
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    if remap_axes:
        maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)  # +Z
        maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 3.0, 4.0)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.5)
        xmin, ymin, zmin, xmax, ymax, zmax = expected
        expected = (
            1.5 * (1.0 - 2.0 * zmax),
            1.5 * (2.0 + 3.0 * ymin),
            1.5 * (3.0 + 4.0 * xmin),
            1.5 * (1.0 - 2.0 * zmin),
            1.5 * (2.0 + 3.0 * ymax),
            1.5 * (3.0 + 4.0 * xmax),
        )
        if base_name == "Semicircle":
            expected = (
                1.5 * (1.0 + 2.0 * xmin),
                1.5 * (2.0 - 3.0 * zmax),
                1.5 * (3.0 + 4.0 * ymin),
                1.5 * (1.0 + 2.0 * xmax),
                1.5 * (2.0 - 3.0 * zmin),
                1.5 * (3.0 + 4.0 * ymax),
            )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    "end_shape", ("Cube", "Octahedron", "Sphere", "Pyramid", "Cone")
)
@pytest.mark.parametrize("colored", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("remap_axes", (False, True))
def test_crossline_end_solids_extent_and_axis_transform(
    maya_cmds,
    maya_om,
    new_scene,
    end_shape,
    colored,
    filled,
    remap_axes,
):
    _load_bd_util_nodes(maya_cmds)
    shape_name = (
        ("Color" if colored else "")
        + "CrossLine3AxisEnd"
        + end_shape
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    expected = _three_axis_solid_part_bounds(end_shape)
    if remap_axes:
        maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)
        maya_cmds.setAttr(f"{shape}.shapeScale", -2.0, 3.0, 4.0)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0)
        maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.5)
        corners = [
            (
                1.5 * (1 + (2 if colored else -2) * -z),
                1.5 * (2 + 3 * y),
                1.5 * (3 + 4 * x),
            )
            for x in (expected[0], expected[3])
            for y in (expected[1], expected[4])
            for z in (expected[2], expected[5])
        ]
        expected = tuple(
            min(point[i] for point in corners) for i in range(3)
        ) + tuple(max(point[i] for point in corners) for i in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize(
    ("shape_name", "expected_bounds"),
    (
        ("Triangle", (-0.5, 0.0, -0.37, 0.5, 0.0, 0.5)),
        (
            "TriangleFilled",
            (-0.5, 0.0, -0.37, 0.5, 0.0, 0.5),
        ),
        ("Square", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("SquareFilled", (-0.5, 0.0, -0.5, 0.5, 0.0, 0.5)),
        ("Arc", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        ("ArcFilled", (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (
            "ArcArrow2D",
            (0.0, -0.5, -0.5, 0.0, 0.5, 0.625),
        ),
    ),
)
def test_planar_shape_follows_selected_axis_basis(
    maya_cmds, maya_om, new_scene, shape_name, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, shape_name)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 4)  # +Z

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_draw_style_attributes_preserve_focus_bounds_and_scene_values(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape_name, "Cube")
    maya_cmds.setAttr(f"{shape_name}.shapeTranslateX", 3.0)
    maya_cmds.setAttr(f"{shape_name}.shapeOffsetLine", True)
    maya_cmds.setAttr(f"{shape_name}.customBoundsSize", 2.0)
    maya_cmds.setAttr(f"{shape_name}.showBoundsPreview", True)

    expected_bounds = {}
    for mode in range(3):
        maya_cmds.setAttr(f"{shape_name}.boundsMode", mode)
        expected_bounds[mode] = _bounds(maya_om, shape_name)

    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    shape.shapeLineWidth.set(2.5)
    shape.shapeLineTransparency.set(0.375)
    shape.shapeFillTransparency.set(0.25)
    shape.shapeDrawOnTop.set(True)
    mod.do_it_dg()

    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        2.5
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeLineTransparency"
    ) == pytest.approx(0.375)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    for mode, bounds in expected_bounds.items():
        maya_cmds.setAttr(f"{shape_name}.boundsMode", mode)
        assert _bounds(maya_om, shape_name) == pytest.approx(bounds)

    mod.undo_it()
    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        1.0
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeLineTransparency"
    ) == pytest.approx(0.0)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.85)
    assert not maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    mod.redo_it()

    scene_path = tmp_path / "controller_shape_draw_style.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape_name}.shapeLineWidth") == pytest.approx(
        2.5
    )
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeLineTransparency"
    ) == pytest.approx(0.375)
    assert maya_cmds.getAttr(
        f"{shape_name}.shapeFillTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(f"{shape_name}.shapeDrawOnTop")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected_bounds[2])


def test_bounds_modes_and_custom_attribute_defaults(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=None, bounds_mode=None)

    assert maya_cmds.attributeQuery(
        "boundsMode", node=shape, listEnum=True
    ) == ["Shape:ShapeCentered:Custom"]
    assert maya_cmds.getAttr(f"{shape}.boundsMode") == 1
    assert not maya_cmds.getAttr(f"{shape}.showBoundsPreview")
    assert (
        maya_cmds.attributeQuery(
            "showBoundsPreview", node=shape, shortName=True
        )
        == "sbp"
    )
    assert not maya_cmds.attributeQuery(
        "showCustomBoundsPreview", node=shape, exists=True
    )
    for attribute, default in (
        ("customBounds1stAxis", 0),
        ("customBounds2ndAxis", 2),
        ("customBoundsRootSize", 1.0),
        ("customBoundsAxisOffsetLength", 1.0),
        ("customBoundsAxisOffset", False),
        ("customBoundsAxisOffsetDirection", 0),
        ("customBoundsSize", 1.0),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == default
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
    for attribute, expected in (
        ("customBoundsTranslate", (0.0, 0.0, 0.0)),
        ("customBoundsRotate", (0.0, 0.0, 0.0)),
        ("customBoundsScale", (1.0, 1.0, 1.0)),
        ("customBoundsAxisTranslate", (0.0, 0.0, 0.0)),
        ("customBoundsAxisRotate", (0.0, 0.0, 0.0)),
        ("customBoundsAxisScale", (1.0, 1.0, 1.0)),
    ):
        assert maya_cmds.getAttr(f"{shape}.{attribute}")[0] == pytest.approx(
            expected
        )
        assert not maya_cmds.getAttr(f"{shape}.{attribute}", keyable=True)
        assert maya_cmds.getAttr(f"{shape}.{attribute}", channelBox=True)
        for axis in "XYZ":
            child = f"{attribute}{axis}"
            assert not maya_cmds.getAttr(f"{shape}.{child}", keyable=True)
            assert maya_cmds.getAttr(f"{shape}.{child}", channelBox=True)
    assert not maya_cmds.getAttr(f"{shape}.showBoundsPreview", keyable=True)
    assert maya_cmds.getAttr(f"{shape}.showBoundsPreview", channelBox=True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    )


def test_shape_centered_keeps_size_without_position_offsets(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 5.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateY", 7.0)
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-2.5, -0.5, -0.5, 2.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -2.5, -0.5, 0.5, 2.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    assert _bounds(maya_om, shape) != pytest.approx(
        (-0.5, -2.5, -0.5, 0.5, 2.5, 0.5)
    )


def test_shape_centered_asymmetry_and_animation_matrix(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = maya_cmds.createNode("composeMatrix")
    _set_shape(maya_cmds, shape, "ArcArrow2D")
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    maya_cmds.connectAttr(
        f"{matrix}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5625, -0.5, 0.0, 0.5625, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{matrix}.inputTranslateX", 3.0)
    maya_cmds.setAttr(f"{matrix}.inputRotateZ", 90.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.4375, 0.0, -0.5, 3.5625, 0.0, 0.5), abs=1.0e-9
    )


def test_custom_bounds_are_independent_and_preview_does_not_change_focus(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -3.0)
    maya_cmds.setAttr(f"{shape}.customBoundsSize", 2.0)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)

    expected = (-4.0, -1.0, -1.0, -2.0, 1.0, 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)
    maya_cmds.setAttr(f"{shape}.showBoundsPreview", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1.0e-9)
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (10.0, -0.5, -0.5, 10.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -5.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-6.0, -1.0, -1.0, -4.0, 1.0, 1.0), abs=1.0e-9
    )


def test_custom_bounds_transform_and_animation_connection(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    matrix = maya_cmds.createNode("composeMatrix")
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffsetLength", 4.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", 3.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -0.5, -0.5, 7.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.5, -0.5, -0.5, 3.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)

    maya_cmds.connectAttr(
        f"{matrix}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setKeyframe(matrix, attribute="inputTranslateX", time=1, value=0)
    maya_cmds.setKeyframe(
        matrix, attribute="inputTranslateX", time=10, value=5
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (8.0, -0.5, -0.5, 12.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (3.0, -0.5, -0.5, 7.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", False)
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffsetLength", 1.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", 0.0)
    maya_cmds.setAttr(f"{shape}.customBoundsScaleX", 2.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRotateZ", 90.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -1.0, -0.5, 0.5, 1.0, 0.5), abs=1.0e-9
    )


def test_connected_custom_bounds_input_updates_at_keyframes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setKeyframe(
        shape, attribute="customBoundsTranslateX", time=1, value=0
    )
    maya_cmds.setKeyframe(
        shape, attribute="customBoundsTranslateX", time=10, value=5
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, -0.5, -0.5, 5.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )


def test_view_fit_uses_selected_bounds_mode(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 10.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslateX", -3.0)
    maya_cmds.select(transform)

    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert maya_cmds.xform(
        transform, query=True, boundingBox=True, worldSpace=True
    ) == pytest.approx((-3.5, -0.5, -0.5, -2.5, 0.5, 0.5), abs=1.0e-9)
    maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
    assert maya_cmds.xform(
        "front", query=True, translation=True, worldSpace=True
    )[0] == pytest.approx(-3.0, abs=1.0e-9)

    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    maya_cmds.setAttr(f"{shape}.showBoundsPreview", True)
    maya_cmds.viewFit("frontShape", animate=False, noChildren=True)
    assert maya_cmds.xform(
        "front", query=True, translation=True, worldSpace=True
    )[0] == pytest.approx(10.0, abs=1.0e-9)


def test_circle_arrow_uses_one_shape(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "ArcArrow2D")

    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.625, 0.5), abs=1.0e-9
    )


def test_shape_transform_order_and_dirty_bounds(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeRotate", 0.0, 0.0, 90.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 1.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.5)

    assert _bounds(maya_om, shape) == pytest.approx(
        (1.5, 4.0, 4.5, 2.5, 4.0, 7.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.0, 4.0, 3.0, 3.0, 4.0, 9.0), abs=1.0e-9
    )


def test_animation_matrix_connection_updates_bounds_at_keyframes(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("composeMatrix", name="animatedShapeMatrix")
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 2.0)
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setKeyframe(source, attribute="inputTranslateX", time=1, value=0)
    maya_cmds.setKeyframe(
        source, attribute="inputTranslateX", time=10, value=5
    )
    maya_cmds.setKeyframe(source, attribute="inputScaleZ", time=1, value=1)
    maya_cmds.setKeyframe(source, attribute="inputScaleZ", time=10, value=2)

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )

    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (5.0, -0.5, -1.0, 7.0, 0.5, 1.0), abs=1.0e-9
    )

    scene_path = tmp_path / "controller_shape_animation.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (5.0, -0.5, -1.0, 7.0, 0.5, 1.0), abs=1.0e-9
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


def test_animation_matrix_moves_offset_line_endpoint_from_origin(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    source = maya_cmds.createNode("composeMatrix", name="animatedShapeMatrix")
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setAttr(f"{source}.inputTranslateZ", 3.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, 0.0, 0.0, 0.5, 3.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.5, 0.0, 3.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    "end_shape", ("Cube", "Octahedron", "Sphere", "Pyramid", "Cone")
)
@pytest.mark.parametrize("colored", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("offset", "length", "width"),
    (
        (0.1, 2.0, 3.0),
        (-0.2, 0.5, 4.0),
        (0.0, 2.0, 12.0),
        (0.1, -2.0, -3.0),
        (-0.6, 1.0, 1.0),
        (0.1, 0.0, 1.0),
        (0.1, 1.0, 0.0),
    ),
)
def test_part_transform_bounds(
    maya_cmds,
    maya_om,
    new_scene,
    end_shape,
    colored,
    filled,
    offset,
    length,
    width,
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        ("Color" if colored else "")
        + "CrossLine3AxisEnd"
        + end_shape
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", length)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", width)
    expected = _three_axis_solid_part_bounds(end_shape, offset, length, width)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    ("attribute", "value"),
    (
        ("shapePartOffset", 0.2),
        ("shapePartLengthScale", 3.0),
        ("shapePartWidthScale", 14.0),
        ("shapePartHeightScale", 14.0),
        ("shapePartSize", 3.0),
    ),
)
@pytest.mark.parametrize("connected", (False, True))
def test_part_attribute_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, attribute, value, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="ColorCrossLine3AxisEndCubeFilled"
    )
    target = f"{shape}.{attribute}"
    if connected:
        if attribute == "shapePartOffset":
            source = maya_cmds.createNode("addDoubleLinear")
            target = f"{source}.input1"
            maya_cmds.connectAttr(f"{source}.output", f"{shape}.{attribute}")
        else:
            source = maya_cmds.createNode("multiplyDivide")
            target = f"{source}.input1X"
            maya_cmds.setAttr(target, 1.0)
            maya_cmds.setAttr(f"{source}.input2X", 1.0)
            maya_cmds.connectAttr(f"{source}.outputX", f"{shape}.{attribute}")
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds("Cube")
    )
    maya_cmds.setAttr(target, value)
    controls = {"offset": 0, "length": 1, "width": 1, "height": 1, "size": 1}
    controls[
        {
            "shapePartOffset": "offset",
            "shapePartLengthScale": "length",
            "shapePartWidthScale": "width",
            "shapePartHeightScale": "height",
            "shapePartSize": "size",
        }[attribute]
    ] = value
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds("Cube", **controls)
    )
    maya_cmds.setAttr(target, 0.0 if attribute == "shapePartOffset" else 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds("Cube")
    )


@pytest.mark.parametrize("end_shape", ("Cube", "Cone"))
def test_part_animation_updates_bounds(
    maya_cmds, maya_om, new_scene, end_shape
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="ColorCrossLine3AxisEnd" + end_shape + "Filled"
    )
    for attribute, first, last in (
        ("shapePartOffset", 0, 0.1),
        ("shapePartLengthScale", 1, 2),
        ("shapePartWidthScale", 1, 3),
        ("shapePartHeightScale", 1, 2.5),
    ):
        maya_cmds.setKeyframe(shape, attribute=attribute, time=1, value=first)
        maya_cmds.setKeyframe(shape, attribute=attribute, time=10, value=last)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds(end_shape, 0.1, 2, 3, height=2.5)
    )
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds(end_shape)
    )


def test_part_offset_uses_scene_distance_units(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        _, shape = _create_controller(
            maya_cmds, shape_name="CrossLine3AxisEndCube"
        )
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 1.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            _three_axis_solid_part_bounds("Cube", 0.1)
        )
        maya_cmds.currentUnit(linear="cm")
        assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == pytest.approx(
            0.1
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


@pytest.mark.parametrize("mode", (0, 1, 2))
def test_part_transform_bounds_modes(maya_cmds, maya_om, new_scene, mode):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="CrossLine3AxisEndCubeFilled", bounds_mode=mode
    )
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 3.0)
    expected = _three_axis_solid_part_bounds("Cube", 0.1, 2, 3)
    if mode == 0:
        expected = (
            expected[0] + 2,
            *expected[1:3],
            expected[3] + 2,
            *expected[4:],
        )
    elif mode == 1:
        half = tuple((expected[i + 3] - expected[i]) / 2 for i in range(3))
        expected = tuple(-value for value in half) + half
    else:
        expected = (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(expected)


def test_part_transform_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    _set_shape_operator(shape, "ColorCrossLine3AxisEndConeFilled")
    shape.shapePartOffset.set(0.1)
    shape.shapeFinHeight.set(0.75)
    shape.shapePartLengthScale.set(2.0)
    shape.shapePartWidthScale.set(3.0)
    shape.shapePartHeightScale.set(3.0)
    shape.shapePartSize.set(2.0)
    shape.shapeSize.set(2.0)
    shape.shapeRootSize.set(2.0)
    shape.shapeTranslate.set(1.0, 2.0, 3.0)
    mod.do_it_dg()
    expected = (-0.4, 1.6, 3.6, 4.4, 6.4, 8.4)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(
        (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "part_transform.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    for attribute, value in (
        ("shapePartOffset", 0.1),
        ("shapeFinHeight", 0.75),
        ("shapePartLengthScale", 2),
        ("shapePartWidthScale", 3),
        ("shapePartHeightScale", 3),
        ("shapePartSize", 2),
    ):
        assert maya_cmds.getAttr(f"{name}.{attribute}") == pytest.approx(value)


@pytest.mark.parametrize(
    "shape_name",
    (
        "Cube",
        "CrossLine3Axis",
        "ColorSphereFilled",
        "ColorCornerCubeFilled",
    ),
)
def test_part_attributes_leave_plain_shapes_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 4.0)
    maya_cmds.setAttr(f"{shape}.shapePartHeightScale", -2.0)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 2.0)
    assert _bounds(maya_om, shape) == pytest.approx(before)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("shape_name", "expected"),
    (
        ("SquareArrow2D", (-0.5, 0, -0.5, 0.975, 0, 0.5)),
        ("SquareArrow3D", (-0.5, 0, -0.5, 0.975, 0.09375, 0.5)),
        ("SquareArrowCrossLine2D", (-0.5, 0, -0.5, 0.975, 0, 0.5)),
        ("SquareArrowCrossLine3D", (-0.5, 0, -0.5, 0.975, 0.09375, 0.5)),
        ("SquareArrowCrossLineTemplate2D", (-0.5, 0, -0.5, 0.975, 0, 0.5)),
        (
            "SquareArrowCrossLineTemplate3D",
            (-0.5, 0, -0.5, 0.975, 0.09375, 0.5),
        ),
        ("SquareArrow4Way2D", (-0.7875, 0, -0.7875, 0.975, 0, 0.7875)),
        ("SquareArrow4Way3D", (-0.7875, 0, -0.7875, 0.975, 0.09375, 0.7875)),
        ("SquareTemplateArrow4Way2D", (-0.7875, 0, -0.7875, 0.975, 0, 0.7875)),
        (
            "SquareTemplateArrow4Way3D",
            (-0.7875, 0, -0.7875, 0.975, 0.09375, 0.7875),
        ),
        ("CubeArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("CubeArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("ArcArrow2D", (0, -0.5, -0.5, 0, 0.975, 0.5)),
        ("ArcArrow3D", (0, -0.5, -0.5, 0.09375, 0.975, 0.5)),
        ("SemicircleArrow2D", (0, 0, -0.5, 0, 0.975, 0.5)),
        ("SemicircleArrow3D", (0, 0, -0.5, 0.09375, 0.975, 0.5)),
        ("SphereArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("SphereArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("ColorSphereArrow2D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("ColorSphereArrow3D", (-0.5, -0.5, -0.5, 0.975, 0.5, 0.5)),
        ("CubeFin", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CubeFinArrow", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CylinderFin", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("CylinderFinArrow", (-0.75, -0.5, -0.5, 0.75, 1.5, 0.5)),
        ("PyramidFin", (-0.75, -0.5, -0.5, 0.75, 1.0, 0.5)),
        ("ConeFin", (-0.75, -0.5, -0.5, 0.75, 1.0, 0.5)),
        ("Arrow", (-2.4, 0, -0.75, 0.6, 0, 0.75)),
        ("ArrowFin", (-3.3375, 0, -0.75, 1.1625, 1.0, 0.75)),
        ("OctahedronArrow", (-0.5, -0.75, -0.75, 1.6, 0.75, 0.75)),
        ("OctahedronArrowFin", (-1.025, -0.75, -0.75, 2.125, 1.0, 0.75)),
        ("LineArrowAtEnds", (-0.6, 0, -0.075, 0.6, 0, 0.075)),
        ("CrossLineArrowAtEnds", (-0.6, 0, -0.6, 0.6, 0, 0.6)),
        ("CrossLineSwappedArrowAtEnds", (0, -0.6, -0.6, 0, 0.6, 0.6)),
        (
            "SemicircleArrowAtEnds",
            (
                0,
                0,
                -_circle_arrow_outer_extent(
                    0.3 * math.cos(math.pi / 6), 0.075
                ),
                0,
                0.5,
                _circle_arrow_outer_extent(0.3 * math.cos(math.pi / 6), 0.075),
            ),
        ),
        ("LineWideArrowAtEnds", (-0.6, 0, -0.075, 0.6, 0, 0.075)),
        ("CrossLineWideArrowAtEnds", (-0.6, 0, -0.6, 0.6, 0, 0.6)),
        ("CrossLineSwappedWideArrowAtEnds", (0, -0.6, -0.6, 0, 0.6, 0.6)),
        (
            "SemicircleWideArrowAtEnds",
            (
                0,
                0,
                -_circle_arrow_outer_extent(
                    0.3 * math.cos(math.pi / 6), 0.075
                ),
                0,
                0.525,
                _circle_arrow_outer_extent(0.3 * math.cos(math.pi / 6), 0.075),
            ),
        ),
    ),
)
def test_arrow_and_fin_part_size_bounds(
    maya_cmds, maya_om, new_scene, shape_name, expected, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = shape_name + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    # PartとFinの倍率をそれぞれ指定し、同じ積となる設定を比較する。
    maya_cmds.setAttr(f"{shape}.shapeFinSize", 2)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 0.75)
    for attribute, value in (
        ("shapePartOffset", 0.1),
        ("shapePartLengthScale", 1.5),
        ("shapePartWidthScale", 0.75),
        ("shapePartHeightScale", 0.75),
        ("shapePartSize", 2.0),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 1.0)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.5)
    maya_cmds.setAttr(f"{shape}.shapePartHeightScale", 1.5)
    maya_cmds.setAttr(f"{shape}.shapeFinSize", 1)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 1.5)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("fin", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size,expected",
    (
        (0, 1, 1, 1, (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)),
        (0.2, 1, 1, 1, (-0.5, -0.5, -0.5, 0.7, 0.5, 0.5)),
        (0, 2, 1, 1, (-0.5, -0.5, -0.5, 1.0, 0.5, 0.5)),
        (0.1, 1, 0.5, 2, (-0.5, -0.5, -0.5, 1.1, 0.5, 0.5)),
        (0, -2, 1, 1, (-1, -0.5, -0.5, 0, 0.5, 0.5)),
        (0, 1, -2, 1, (-0.5, -1, -1, 0.5, 1, 1)),
        (0, 0, 1, 1, (-0.5, -0.5, -0.5, 0, 0.5, 0.5)),
        (0.2, 1, 1, 0, (-0.5, 0, 0, 0.2, 0, 0)),
    ),
)
def test_octahedron_arrow_tip_uses_central_section(
    maya_cmds,
    maya_om,
    new_scene,
    filled,
    fin,
    offset,
    length,
    width,
    size,
    expected,
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        "OctahedronArrow"
        + ("Fin" if fin else "")
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=name)
    if fin:
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartHeightScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    half_size = tuple((expected[i + 3] - expected[i]) * 0.5 for i in range(3))
    assert _bounds(maya_om, shape) == pytest.approx(
        tuple(-value for value in half_size) + half_size, abs=1e-9
    )


@pytest.mark.parametrize(
    "shape_name",
    [name for name in SHAPE_VARIANTS if "CrossLine3AxisEnd" in name],
)
def test_terminal_part_size_multiplies_both_scales(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2.0)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 3.0)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 2.0)
    part = shape_name.split("End", 1)[1].removesuffix("Filled")
    assert _bounds(maya_om, shape) == pytest.approx(
        _three_axis_solid_part_bounds(part, 0.1, 2, 3, 2)
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    ("fin_name", "body_name", "max_y"),
    (
        ("CubeFin", "Cube", 1.75),
        ("CubeFinArrow", "Cube", 1.75),
        ("CylinderFin", "Cylinder", 1.75),
        ("CylinderFinArrow", "Cylinder", 1.75),
        ("PyramidFin", "Pyramid", 1.25),
        ("ConeFin", "Cone", 1.25),
        ("OctahedronArrowFin", "OctahedronArrow", 1.25),
        ("ArrowFin", "Arrow", 1.25),
    ),
)
def test_fin_height_is_independent_and_zero_keeps_body(
    maya_cmds, maya_om, new_scene, filled, fin_name, body_name, max_y
):
    _load_bd_util_nodes(maya_cmds)
    suffix = "Filled" if filled else ""
    _, shape = _create_controller(maya_cmds, shape_name=fin_name + suffix)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 1.25)
    assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)
    for attribute, value in (
        ("shapePartOffset", 0.3),
        ("shapePartLengthScale", 3),
        ("shapePartWidthScale", 1.5),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    actual = _bounds(maya_om, shape)
    _set_shape(maya_cmds, shape, body_name + suffix)
    assert actual == pytest.approx(_bounds(maya_om, shape))


@pytest.mark.parametrize("connected", (False, True))
def test_fin_height_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="CubeFinFilled")
    target = f"{shape}.shapeFinHeight"
    if connected:
        source = maya_cmds.createNode("addDoubleLinear")
        target = f"{source}.input1"
        maya_cmds.setAttr(target, 0.5)
        maya_cmds.connectAttr(f"{source}.output", f"{shape}.shapeFinHeight")
    for height in (0.5, 0.25, 1, 0):
        maya_cmds.setAttr(target, height)
        assert _bounds(maya_om, shape)[4] == pytest.approx(0.5 + height)


def test_fin_height_size_survives_other_scale_cancellation(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="CubeFinFilled")
    maya_cmds.setAttr(f"{shape}.shapeFinSize", 2)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 0.5)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 0.5)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 0.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 1.5, 0.5)
    )


def test_fin_height_uses_distance_units(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="CubeFinFilled")
    previous = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        assert maya_cmds.getAttr(f"{shape}.shapeFinHeight") == 5
        maya_cmds.setAttr(f"{shape}.shapeFinHeight", 10)
        assert _bounds(maya_om, shape)[4] == pytest.approx(1.5)
    finally:
        maya_cmds.currentUnit(linear=previous)


def test_fin_height_animation_updates_bounds(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="CubeFinFilled")
    for time, height in ((1, 0), (10, 1)):
        maya_cmds.setKeyframe(
            shape, attribute="shapeFinHeight", time=time, value=height
        )
    for time, max_y in ((10, 1.5), (1, 0.5), (10, 1.5)):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape)[4] == pytest.approx(max_y)


def test_fin_part_size_animation_and_bounds_modes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="CubeFinFilled")
    maya_cmds.setKeyframe(shape, attribute="shapeFinSize", time=1, value=1)
    maya_cmds.setKeyframe(shape, attribute="shapeFinSize", time=10, value=2)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1, -0.5, -0.5, 3, 1.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    assert _bounds(maya_om, shape) == pytest.approx((-1, -1, -0.5, 1, 1, 0.5))
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.boundsMode", 0)
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (1.5, -0.5, -0.5, 2.5, 1, 0.5)
    )


@pytest.mark.parametrize("filled", (False, True))
def test_semicircle_wide_part_retains_outer_arc_when_inner_radius_collapses(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleWideArrowAtEnds" + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.1)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 25)
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 1.25)
    extent = _circle_arrow_outer_extent(0.1 * math.cos(math.pi / 6), 1.25)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, 0, -extent, 0, 1.125, extent)
    )


@pytest.mark.parametrize("filled", (False, True))
def test_wide_end_arrow_negative_offset_moves_heads_past_origin(
    maya_cmds, maya_om, new_scene, filled
):
    import math

    _load_bd_util_nodes(maya_cmds)
    name = "LineWideArrowAtEnds" + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", -0.8)
    extent = 0.3 + 0.1 * math.cos(math.pi / 6)
    half_extent = 0.3 + 0.05 * math.cos(math.pi / 6)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, 0, -0.05, half_extent, 0, 0.05)
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (-90, -89.9, -60, -30, 0, 30, 60, 89.9, 90))
def test_semicircle_angle_bounds(maya_cmds, maya_om, new_scene, filled, angle):
    _load_bd_util_nodes(maya_cmds)
    name = "Semicircle" + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 180 + 2 * angle)
    extent = 0.5 if angle >= 0 else 0.5 * math.cos(math.radians(angle))
    low = -0.5 * math.sin(math.radians(angle))
    expected = (
        (0, 0, 0, 0, 0, 0)
        if angle == -90
        else (0, low, -extent, 0, 0.5, extent)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    # 矢印のない円弧は長さ・太さ・直線方向の移動では変えない。
    for attribute, value in (
        ("shapePartOffset", 0.3),
        ("shapePartSize", 2),
        ("shapePartLengthScale", 3),
        ("shapePartWidthScale", 4),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "base_name",
    (
        "SemicircleArrow2D",
        "SemicircleArrow3D",
        "SemicircleArrowAtEnds",
        "SemicircleWideArrowAtEnds",
    ),
)
@pytest.mark.parametrize("angle", (-90, -30, 30, 90))
def test_semicircle_angle_and_part_scales_remain_finite(
    maya_cmds, maya_om, new_scene, filled, base_name, angle
):
    _load_bd_util_nodes(maya_cmds)
    name = base_name + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    for attribute, value in (
        ("shapeArcAngle", 180 + 2 * angle),
        ("shapePartOffset", 0.3),
        ("shapePartSize", 0.5),
        ("shapePartLengthScale", 2),
        ("shapePartWidthScale", 3),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert all(math.isfinite(value) and abs(value) < 2 for value in bounds)
    maya_cmds.setAttr(f"{shape}.shapeFill", False)
    outline_bounds = _bounds(maya_om, shape)
    assert outline_bounds == pytest.approx(bounds)


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_semicircle_angle_moves_wrapped_endpoints_and_ignores_offset(
    maya_cmds, maya_om, new_scene, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        "Semicircle"
        + ("Wide" if wide else "")
        + "ArrowAtEnds"
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 240)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.3)
    extent = max(
        0.525 if wide else 0.5,
        max(
            point[2]
            for point in _circle_arrow_profile_points(
                -math.pi / 6, 0.1 * math.cos(math.pi / 6), 0.05
            )
        ),
    )
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            0,
            -0.25,
            -extent,
            0,
            0.525 if wide else 0.5,
            extent,
        )
    )


@pytest.mark.parametrize("connected", (False, True))
def test_semicircle_angle_invalidates_cached_geometry(
    maya_cmds, maya_om, new_scene, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="SemicircleFilled")
    target = f"{shape}.shapeArcAngle"
    if connected:
        source = maya_cmds.createNode("bdDblA_Value")
        target = f"{source}.value"
        maya_cmds.setAttr(target, 180)
        maya_cmds.connectAttr(target, f"{shape}.shapeArcAngle")
    assert _bounds(maya_om, shape) == pytest.approx((0, 0, -0.5, 0, 0.5, 0.5))
    maya_cmds.setAttr(target, 240)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, -0.25, -0.5, 0, 0.5, 0.5)
    )
    maya_cmds.setAttr(target, 120)
    extent = 0.5 * math.cos(math.pi / 6)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, 0.25, -extent, 0, 0.5, extent)
    )
    if connected:
        # 接続元の角度に制限がなくても、円弧は0–360度の範囲に収める。
        maya_cmds.setAttr(target, 540)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0, -0.5, -0.5, 0, 0.5, 0.5)
        )


def test_semicircle_angle_uses_scene_angle_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, angle=True)
    try:
        maya_cmds.currentUnit(angle="rad")
        _, shape = _create_controller(maya_cmds, shape_name="Semicircle")
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", 4 * math.pi / 3)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0, -0.25, -0.5, 0, 0.5, 0.5)
        )
        maya_cmds.currentUnit(angle="deg")
        assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == pytest.approx(
            240
        )
    finally:
        maya_cmds.currentUnit(angle=previous_unit)


@pytest.mark.parametrize("mode", (0, 1, 2))
@pytest.mark.parametrize(
    ("angle", "shape_bounds", "centered_bounds"),
    (
        (30, (2, -0.25, -0.5, 2, 0.5, 0.5), (0, -0.375, -0.5, 0, 0.375, 0.5)),
        (
            -30,
            (2, 0.25, -math.sqrt(3) / 4, 2, 0.5, math.sqrt(3) / 4),
            (0, -0.125, -math.sqrt(3) / 4, 0, 0.125, math.sqrt(3) / 4),
        ),
    ),
)
def test_semicircle_angle_animation_and_bounds_modes(
    maya_cmds, maya_om, new_scene, mode, angle, shape_bounds, centered_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="SemicircleFilled", bounds_mode=mode
    )
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2)
    maya_cmds.setKeyframe(shape, attribute="shapeArcAngle", time=1, value=180)
    maya_cmds.setKeyframe(
        shape, attribute="shapeArcAngle", time=10, value=180 + 2 * angle
    )
    maya_cmds.currentTime(10)
    expected = (
        shape_bounds,
        centered_bounds,
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5),
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected[mode])
    maya_cmds.currentTime(1)
    if mode == 0:
        assert _bounds(maya_om, shape) == pytest.approx(
            (2, 0, -0.5, 2, 0.5, 0.5)
        )


def test_semicircle_angle_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    _set_shape_operator(shape, "SemicircleFilled")
    shape.shapeArcAngle.set(240)
    shape.shapeSize.set(2)
    shape.shapeRootSize.set(2)
    shape.shapeTranslate.set(1, 2, 3)
    mod.do_it_dg()
    expected = (2, 3, 4, 2, 6, 8)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(
        (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "semicircle_angle.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert maya_cmds.getAttr(f"{name}.shapeArcAngle") == pytest.approx(240)
    assert _bounds(maya_om, name) == pytest.approx(expected)


@pytest.mark.parametrize(
    "shape_name",
    [
        name
        for name in SHAPE_VARIANTS
        if "Arc" not in name and not name.startswith("Semicircle")
    ],
)
def test_semicircle_angle_leaves_other_shapes_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 30)
    assert _bounds(maya_om, shape) == pytest.approx(before)


def test_animation_matrix_set_uses_modifier_history(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    matrix = maya_om.MMatrix((1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 1))

    shape.shapeAnimationTransformMatrix.set(matrix)
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.do_it_dg()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.undo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    mod.redo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "expected_position"),
    (
        (0, 2, (1.0, 0.0, 0.0)),  # +X, +Y: identity
        (4, 2, (0.0, 0.0, 1.0)),  # +Z, +Y: local +X becomes +Z
        (5, 2, (0.0, 0.0, -1.0)),  # -Z, +Y: local +X becomes -Z
        (2, 0, (0.0, 1.0, 0.0)),  # +Y, +X: local +X becomes +Y
        (2, 3, (0.0, 1.0, 0.0)),  # Invalid: +Y keeps primary, uses +Z
        (4, 5, (0.0, 0.0, 1.0)),  # Invalid: +Z keeps primary, uses +Y
    ),
)
def test_axis_orientation_and_invalid_pair_fallback(
    maya_cmds, maya_om, new_scene, first_axis, second_axis, expected_position
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", second_axis)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_position, *expected_position), abs=1.0e-9
    )


@pytest.mark.parametrize("prefix, mode", (("shape", 0), ("customBounds", 2)))
@pytest.mark.parametrize(
    "first_axis, expected_axes",
    (
        (0, ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))),
        (4, ((0.0, 0.0, 1.0), (0.0, 1.0, 0.0), (-1.0, 0.0, 0.0))),
    ),
)
@pytest.mark.parametrize("component, index", (("X", 0), ("Y", 1), ("Z", 2)))
def test_axis_translation_components_follow_selected_basis(
    maya_cmds,
    maya_om,
    new_scene,
    prefix,
    mode,
    first_axis,
    expected_axes,
    component,
    index,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", mode)
    maya_cmds.setAttr(f"{shape}.{prefix}Size", 0.0)
    maya_cmds.setAttr(f"{shape}.{prefix}1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.{prefix}AxisTranslate{component}", 1.0)

    position = expected_axes[index]
    assert _bounds(maya_om, shape) == pytest.approx(
        (*position, *position), abs=1.0e-9
    )


def test_axis_rotate_x_turns_circle_arrow_around_first_axis(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "ArcArrow2D")
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotateX", 90.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, 0.0, 0.625, 0.5, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize("prefix, mode", (("shape", 0), ("customBounds", 2)))
def test_axis_scale_x_follows_first_axis(
    maya_cmds, maya_om, new_scene, prefix, mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", mode)
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.{prefix}1stAxis", 4)  # +Z
    maya_cmds.setAttr(f"{shape}.{prefix}AxisScaleX", 3.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -1.5, 0.5, 0.5, 1.5), abs=1.0e-9
    )


def test_custom_bounds_third_axis_offset_matches_axis_z(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.boundsMode", 2)
    maya_cmds.setAttr(f"{shape}.customBoundsSize", 0.0)
    maya_cmds.setAttr(f"{shape}.customBounds1stAxis", 4)  # +Z
    maya_cmds.setAttr(
        f"{shape}.customBoundsAxisOffsetDirection", 4
    )  # +3rdAxis
    maya_cmds.setAttr(f"{shape}.customBoundsAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0.0, 0.0, -0.5, 0.0, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("size", "expected_bounds"),
    (
        (1.0, (0.0, -0.5, -0.5, 1.0, 0.5, 0.5)),
        (2.0, (-0.5, -1.0, -1.0, 1.5, 1.0, 1.0)),
    ),
)
def test_cube_axis_offset_is_fixed_after_shape_size(
    maya_cmds, maya_om, new_scene, size, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "Cube")  # Cube
    maya_cmds.setAttr(f"{shape}.shapeSize", size)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("direction", "expected_bounds"),
    (
        (0, (0.0, -0.5, -0.5, 3.0, 0.5, 0.5)),
        (1, (-3.0, -0.5, -0.5, 0.0, 0.5, 0.5)),
        (2, (-0.5, 0.0, -0.5, 0.5, 3.0, 0.5)),
        (3, (-0.5, -3.0, -0.5, 0.5, 0.0, 0.5)),
        (4, (-0.5, -0.5, 0.0, 0.5, 0.5, 3.0)),
        (5, (-0.5, -0.5, -3.0, 0.5, 0.5, 0.0)),
    ),
)
def test_cube_axis_offset_length_anchors_selected_direction(
    maya_cmds, maya_om, new_scene, direction, expected_bounds
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        expected_bounds, abs=1.0e-9
    )


def test_axis_offset_length_requires_offset_and_scales_axis_translation(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 0.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 3.0)

    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.5, 0.0, 0.0, 4.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 4.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 1.0, 0.0, 0.0), abs=1.0e-9
    )


def test_axis_offset_length_accepts_distance_connection_across_scene_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    maya_cmds.currentUnit(linear="m")
    try:
        _, shape = _create_controller(maya_cmds)
        source = maya_cmds.createNode("transform", name="boneLengthSource")
        _set_shape(maya_cmds, shape, "Cube")
        maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
        maya_cmds.connectAttr(
            f"{source}.translateX", f"{shape}.shapeAxisOffsetLength"
        )
        maya_cmds.setAttr(f"{source}.translateX", 2.0)
        assert maya_cmds.getAttr(
            f"{shape}.shapeAxisOffsetLength"
        ) == pytest.approx(2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 200.0, 0.5, 0.5), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", 3.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 300.0, 0.5, 0.5), abs=1.0e-9
        )
        maya_cmds.setAttr(f"{source}.translateX", -2.0)
        assert _bounds(maya_om, shape) == pytest.approx(
            (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
        )
    finally:
        maya_cmds.currentUnit(linear="cm")


def test_axis_offset_length_updates_bounds_after_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    _set_shape(maya_cmds, shape, "Cube")
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 2.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 1.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("first_axis", "second_axis", "direction", "expected_position"),
    (
        (4, 2, 0, (0.0, 0.0, 0.5)),
        (4, 2, 1, (0.0, 0.0, -0.5)),
        (4, 2, 2, (0.0, 0.5, 0.0)),
        (4, 2, 3, (0.0, -0.5, 0.0)),
        (4, 2, 4, (-0.5, 0.0, 0.0)),
        (4, 2, 5, (0.5, 0.0, 0.0)),
        (0, 2, 0, (0.5, 0.0, 0.0)),
        (0, 2, 4, (0.0, 0.0, 0.5)),
        (5, 2, 0, (0.0, 0.0, -0.5)),
        (2, 3, 4, (0.5, 0.0, 0.0)),
    ),
)
def test_axis_offset_uses_selected_basis_and_invalid_pair_fallback(
    maya_cmds,
    maya_om,
    new_scene,
    first_axis,
    second_axis,
    direction,
    expected_position,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", second_axis)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_position, *expected_position), abs=1.0e-9
    )


def test_axis_transform_is_between_outer_and_inner_transform(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)  # +X
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)  # +Y
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1.0, 2.0, 3.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.shapeScale", 2.0, 3.0, 4.0, type="double3")
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisScale", 1.0, 2.0, 1.0, type="double3")

    assert _bounds(maya_om, shape) == pytest.approx(
        (2.0, 0.0, 10.0, 2.0, 8.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 8.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 10.0, 18.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)  # +3rdAxis
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 2.0, 8.0, 22.0), abs=1.0e-9
    )


def test_axis_offset_does_not_move_offset_line_endpoint(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateX", 1.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 1)  # -1stAxis
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)

    assert _bounds(maya_om, shape) == pytest.approx(
        (0.5, 0.0, 0.0, 0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 1.0, 0.0, 0.0), abs=1.0e-9
    )


def test_axis_offset_updates_bounds_after_direct_changes_and_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.5, 0.0, 0.0, 0.5, 0.0, 0.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )

    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
    )
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, 0.0, 0.0, 0.0, 0.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("animated_attribute", "other_attribute", "other_value", "expected_start"),
    (
        ("shapeAxisOffset", "shapeAxisOffsetDirection", 5, (0.0, 0.0, 0.0)),
        ("shapeAxisOffsetDirection", "shapeAxisOffset", 1, (0.5, 0.0, 0.0)),
    ),
)
def test_connected_axis_offset_updates_bounds_at_keyframes(
    maya_cmds,
    maya_om,
    new_scene,
    animated_attribute,
    other_attribute,
    other_value,
    expected_start,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeSize", 0.0)
    maya_cmds.setAttr(f"{shape}.{other_attribute}", other_value)
    maya_cmds.setKeyframe(shape, attribute=animated_attribute, time=1, value=0)
    maya_cmds.setKeyframe(
        shape,
        attribute=animated_attribute,
        time=10,
        value=1 if animated_attribute == "shapeAxisOffset" else 5,
    )

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (*expected_start, *expected_start), abs=1.0e-9
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, 0.0, -0.5, 0.0, 0.0, -0.5), abs=1.0e-9
    )


def test_connected_axis_translation_updates_bounds_at_keyframes(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setKeyframe(
        shape, attribute="shapeAxisTranslateX", time=1, value=0
    )
    maya_cmds.setKeyframe(
        shape, attribute="shapeAxisTranslateX", time=10, value=2
    )

    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5), abs=1.0e-9
    )
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(
        (2.0, -0.5, -0.5, 2.0, 0.5, 0.5), abs=1.0e-9
    )


def test_shape_offset_line_expands_bounds_and_round_trips(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeTranslateX", 2.0)

    assert _bounds(maya_om, shape) == pytest.approx(
        (4.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeOffsetLineTemplate", True)

    scene_path = tmp_path / "controller_shape_offset_line.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(f"{shape}.shapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape}.shapeOffsetLineTemplate")
    assert _bounds(maya_om, shape) == pytest.approx(
        (0.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )

    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", False)
    assert _bounds(maya_om, shape) == pytest.approx(
        (4.0, -1.0, -1.0, 4.0, 1.0, 1.0), abs=1.0e-9
    )


@pytest.mark.parametrize(
    ("shape_name", "expected"),
    (
        ("ColorCube", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCubeFilled", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCornerCube", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("ColorCornerCubeFilled", (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0)),
        ("LineWideArrowAtEndsFilled", (0.8, 4.0, 5.0, 3.2, 4.0, 7.0)),
        (
            "SemicircleWideArrowAtEndsFilled",
            (
                2
                - 24
                * _circle_arrow_outer_extent(
                    0.1 * math.cos(math.pi / 6), 0.05
                ),
                4.0,
                6.0,
                2
                + 24
                * _circle_arrow_outer_extent(
                    0.1 * math.cos(math.pi / 6), 0.05
                ),
                4.0,
                7.05,
            ),
        ),
        ("CrossLine3AxisEndCubeFilled", (-10.6, -0.2, 4.95, 14.6, 8.2, 7.1)),
        (
            "ColorCrossLine3AxisEndSphereFilled",
            (-2.2, -0.2, 2.85, 6.2, 8.2, 9.3),
        ),
        ("CrossLine3AxisEndPyramidFilled", (-10.0, 0.0, 5.0, 14.0, 8.0, 7.0)),
        (
            "ColorCrossLine3AxisEndConeFilled",
            (-2.0, 0.0, 3.0, 6.0, 8.0, 9.0),
        ),
    ),
)
def test_preset_transform_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name, expected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name_in_scene = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name_in_scene)
    _set_shape_operator(shape, shape_name)
    shape.shape1stAxis.set(4)
    shape.shape2ndAxis.set(2)
    shape.shapeSize.set(2.0)
    shape.shapeAxisScale.set(1.0, 2.0, 3.0)
    shape.shapeScale.set(2.0, 1.0, 0.5)
    shape.shapeTranslate.set(1.0, 2.0, 3.0)
    shape.shapeRootSize.set(2.0)
    shape.shapeLineTransparency.set(0.25)
    shape.shapeFillTransparency.set(0.6)
    mod.do_it_dg()

    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)
    mod.undo_it()
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(
        (0.0, -0.5, -0.5, 0.0, 0.5, 0.5)
    )
    mod.redo_it()
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)

    scene_path = tmp_path / f"{shape_name}.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.getAttr(f"{shape_name_in_scene}.shape") == _shape_index(
        shape_name
    )
    assert _bounds(maya_om, shape_name_in_scene) == pytest.approx(expected)
    assert maya_cmds.getAttr(
        f"{shape_name_in_scene}.shapeLineTransparency"
    ) == pytest.approx(0.25)
    assert maya_cmds.getAttr(
        f"{shape_name_in_scene}.shapeFillTransparency"
    ) == pytest.approx(0.6)
    assert maya_cmds.getAttr(f"{shape_name_in_scene}.shape1stAxis") == 4


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_VARIANTS if name.startswith("Color")]
)
@pytest.mark.parametrize("bounds_mode", (0, 1))
def test_color_shapes_ignore_orientation_attributes(
    maya_cmds, maya_om, new_scene, shape_name, bounds_mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, bounds_mode=bounds_mode
    )
    for attribute, value in (
        ("shapeAxisScale", (0.75, 1.25, 2.0)),
        ("shapeScale", (1.5, 0.8, 2.5)),
        ("shapeTranslate", (0.25, -0.5, 0.75)),
        ("shapeAxisTranslate", (0.1, -0.2, 0.3)),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", *value)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", 1.6)
    part_enabled = maya_cmds.getAttr(f"{shape}.shapePart")
    fin_enabled = maya_cmds.getAttr(f"{shape}.shapeFin")
    maya_cmds.setAttr(f"{shape}.shapePart", False)
    maya_cmds.setAttr(f"{shape}.shapeFin", False)
    expected = _bounds(maya_om, shape)
    for first, second in ((5, 1), (4, 4)):
        maya_cmds.setAttr(f"{shape}.shape1stAxis", first)
        maya_cmds.setAttr(f"{shape}.shape2ndAxis", second)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == first
        assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == second
    maya_cmds.setAttr(f"{shape}.shapePart", part_enabled)
    maya_cmds.setAttr(f"{shape}.shapeFin", fin_enabled)
    expected = _bounds(maya_om, shape)
    for attribute in ("shapeRotate", "shapeAxisRotate"):
        maya_cmds.setAttr(f"{shape}.{attribute}", 23.0, 41.0, -17.0)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.{attribute}")[0] == (
            23.0,
            41.0,
            -17.0,
        )


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_VARIANTS if name.startswith("Color")]
)
@pytest.mark.parametrize(
    "attribute", ("shapeScale", "shapeAxisScale", "shapeSize", "shapeRootSize")
)
def test_color_shapes_use_scale_magnitudes(
    maya_cmds, maya_om, new_scene, shape_name, attribute
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 0.25, -0.5, 0.75)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslate", 0.1, -0.2, 0.3)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeOffsetLine", True)
    vector = attribute in ("shapeScale", "shapeAxisScale")
    positive = (2.0, 3.0, 4.0) if vector else (2.0,)
    negative = (-2.0, 3.0, -4.0) if vector else (-2.0,)
    maya_cmds.setAttr(f"{shape}.{attribute}", *positive)
    expected = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.{attribute}", *negative)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    stored = maya_cmds.getAttr(f"{shape}.{attribute}")
    assert (stored[0] if vector else (stored,)) == negative


@pytest.mark.parametrize(
    "shape_name", [name for name in SHAPE_VARIANTS if name.startswith("Color")]
)
def test_color_shapes_apply_animation_matrix_unchanged(
    maya_cmds, maya_om, new_scene, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    before = _bounds(maya_om, shape)
    matrix = (0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0.5, 0, 4, -5, 6, 1)
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix, type="matrix"
    )
    xmin, ymin, zmin, xmax, ymax, zmax = before
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            3 * ymin + 4,
            2 * xmin - 5,
            0.5 * zmin + 6,
            3 * ymax + 4,
            2 * xmax - 5,
            0.5 * zmax + 6,
        )
    )
    assert (
        tuple(maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix"))
        == matrix
    )


def test_color_matrix_connection_keeps_rotation_shear_and_reflection(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(
        maya_cmds, shape_name="ColorCornerCubeFilled"
    )
    source = maya_cmds.createNode("composeMatrix")
    maya_cmds.connectAttr(
        f"{source}.outputMatrix", f"{shape}.shapeAnimationTransformMatrix"
    )
    maya_cmds.setAttr(f"{source}.inputScale", -2.0, 3.0, 0.5)
    maya_cmds.setAttr(f"{source}.inputShear", 0.25, -0.4, 0.15)
    maya_cmds.setAttr(f"{source}.inputTranslate", 1.0, 2.0, -3.0)
    maya_cmds.setAttr(f"{shape}.shapeRotate", 17.0, 29.0, 43.0)
    for angle in (31.0, -57.0):
        maya_cmds.setAttr(f"{source}.inputRotate", 13.0, 27.0, angle)
        values = maya_cmds.getAttr(f"{source}.outputMatrix")
        matrix = maya_om.MMatrix(values)
        points = [
            maya_om.MPoint(x, y, z) * matrix
            for x in (-0.5, 0.5)
            for y in (-0.5, 0.5)
            for z in (-0.5, 0.5)
        ]
        expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
            max(p[i] for p in points) for i in range(3)
        )
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert (
            maya_cmds.getAttr(f"{shape}.shapeAnimationTransformMatrix")
            == values
        )
    maya_cmds.setAttr(f"{transform}.rotate", 23.0, 37.0, 51.0)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{transform}.rotate")[0] == (23.0, 37.0, 51.0)


def test_color_orientation_connections_survive_shape_switch_and_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="ColorSphereArrow3DFilled"
    )
    driver = maya_cmds.createNode("transform", name="orientationDriver")
    maya_cmds.connectAttr(f"{driver}.rotate", f"{shape}.shapeRotate")
    maya_cmds.connectAttr(f"{driver}.scale", f"{shape}.shapeAxisScale")
    maya_cmds.setAttr(f"{driver}.scale", 2.0, 3.0, 4.0)
    expected = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{driver}.scale", -2.0, 3.0, -4.0)
    maya_cmds.setKeyframe(driver, attribute="rotateZ", time=1, value=0)
    maya_cmds.setKeyframe(driver, attribute="rotateZ", time=10, value=37)
    for time in (1, 10):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
    _set_shape(maya_cmds, shape, "SphereArrow3DFilled")
    normal = _bounds(maya_om, shape)
    assert normal != pytest.approx(expected)
    _set_shape(maya_cmds, shape, "ColorSphereArrow3DFilled")
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    scene_path = tmp_path / "color_orientation.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    maya_cmds.currentTime(10)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.isConnected(f"{driver}.rotate", f"{shape}.shapeRotate")
    assert maya_cmds.isConnected(f"{driver}.scale", f"{shape}.shapeAxisScale")
    assert maya_cmds.getAttr(f"{shape}.shapeRotateZ") == pytest.approx(37)
    assert maya_cmds.getAttr(f"{shape}.shapeAxisScale")[0] == (-2.0, 3.0, -4.0)
    _set_shape(maya_cmds, shape, "SphereArrow3DFilled")
    assert _bounds(maya_om, shape) == pytest.approx(normal)


def test_color_shape_keeps_custom_bounds_transform_independent(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="ColorCornerCubeFilled", bounds_mode=2
    )
    maya_cmds.setAttr(f"{shape}.customBoundsAxisScale", 2.0, 3.0, 4.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRotateZ", 90.0)
    maya_cmds.setAttr(f"{shape}.customBoundsTranslate", 1.0, 2.0, 3.0)
    maya_cmds.setAttr(f"{shape}.customBoundsRootSize", -1.0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-2.5, -3, -5, 0.5, -1, -1)
    )


def test_scene_round_trip_preserves_circle_arrow(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    transform, shape = _create_controller(maya_cmds, name="savedController")
    _set_shape(maya_cmds, shape, "ArcArrow2D")
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)  # +X
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)  # +Y
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", 4)  # +3rdAxis
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslateZ", 2.0)
    maya_cmds.setAttr(f"{shape}.shapeSize", 1.5)

    scene_path = tmp_path / "controller_shape.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)

    assert maya_cmds.listRelatives(transform, shapes=True) == [shape]
    assert maya_cmds.getAttr(f"{shape}.shape") == _shape_index("ArcArrow2D")
    assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffset")
    assert maya_cmds.getAttr(f"{shape}.shapeAxisOffsetDirection") == 4
    assert maya_cmds.getAttr(f"{shape}.shapeAxisTranslateZ") == pytest.approx(
        2.0
    )
    assert maya_cmds.getAttr(f"{shape}.shapeSize") == pytest.approx(1.5)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.75, 0.0, 1.75, 0.9375, 0.0, 3.25), abs=1.0e-9
    )


def test_nodes_controller_shape_helper_supports_undo_redo(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    transform, shape = bd_nodes.create.controllerShape(name="rig_ctrl")
    shape.boundsMode.set(0)
    _set_shape_operator(shape, "ArcArrow2D")
    shape.shape1stAxis.set(0)
    shape.shape2ndAxis.set(2)
    shape.shapeAxisOffset.set(True)
    shape.shapeAxisOffsetDirection.set(0)
    shape.shapeAxisTranslate.set(0.0, 0.0, 2.0)
    shape.shapeSize.set(2.0)
    shape.shapeOffsetLine.set(True)
    shape.shapeOffsetLineTemplate.set(True)
    mod.do_it_dag()
    mod.do_it_dg()

    assert maya_cmds.nodeType(shape.full_path) == "bdControllerShape"
    assert maya_cmds.getAttr(f"{shape.full_path}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape.full_path}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffset")
    assert (
        maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffsetDirection") == 0
    )
    assert maya_cmds.getAttr(
        f"{shape.full_path}.shapeAxisTranslateZ"
    ) == pytest.approx(2.0)
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLineTemplate")

    assert maya_cmds.listRelatives(
        transform.full_path, shapes=True, fullPath=True
    ) == [shape.full_path]
    assert _bounds(maya_om, shape.full_path) == pytest.approx(
        (-0.5, 0.0, 0.0, 1.75, 0.0, 3.0), abs=1.0e-9
    )

    mod.undo_it()
    assert not maya_cmds.objExists("rig_ctrl")
    mod.redo_it()
    assert maya_cmds.objExists(transform.full_path)
    assert maya_cmds.getAttr(f"{shape.full_path}.shape") == _shape_index(
        "ArcArrow2D"
    )
    assert maya_cmds.getAttr(f"{shape.full_path}.shape1stAxis") == 0
    assert maya_cmds.getAttr(f"{shape.full_path}.shape2ndAxis") == 2
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffset")
    assert (
        maya_cmds.getAttr(f"{shape.full_path}.shapeAxisOffsetDirection") == 0
    )
    assert maya_cmds.getAttr(
        f"{shape.full_path}.shapeAxisTranslateZ"
    ) == pytest.approx(2.0)
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLine")
    assert maya_cmds.getAttr(f"{shape.full_path}.shapeOffsetLineTemplate")


@pytest.mark.parametrize("base,axis,side", (("Line", 0, 2),))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size",
    (
        (0, 1, 1, 1),
        (0.2, 1.5, 2, 1),
        (-0.2, 0.5, 1, 2),
        (0.1, -2, -3, 1),
        (-1.2, 1, 1, 1),
        (0.1, 0, 0, 1),
        (0.1, 1, 1, 0),
    ),
)
def test_single_end_line_arrow_keeps_opposite_endpoint(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    axis,
    side,
    wide,
    filled,
    offset,
    length,
    width,
    size,
):
    _load_bd_util_nodes(maya_cmds)
    name = (
        base
        + ("Wide" if wide else "")
        + "ArrowAtEnd"
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=name)
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    tip = 0.5 + offset
    shoulder = tip - 0.1 * math.cos(math.pi / 6) * length * size
    low, high = [0.0] * 3, [0.0] * 3
    low[axis], high[axis] = min(-0.5, tip, shoulder), max(-0.5, tip, shoulder)
    side_extent = max(0.025 if wide else 0, 0.05 * abs(width * size))
    low[side], high[side] = -side_extent, side_extent
    assert _bounds(maya_om, shape) == pytest.approx((*low, *high), abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (-90, -30, 0, 30, 90))
@pytest.mark.parametrize("offset", (0, 0.2))
def test_single_end_semicircle_arrow_wraps_on_the_arc_and_ignores_offset(
    maya_cmds, maya_om, new_scene, filled, angle, offset
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleArrowAtEnd" + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 180 + 2 * angle)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    start, finish = -math.radians(angle), math.pi + math.radians(angle)
    arc_angles = [start, finish] + [
        a
        for a in (0, math.pi / 2, math.pi, 3 * math.pi / 2)
        if start <= a <= finish
    ]
    points = [(0, 0.5 * math.sin(a), 0.5 * math.cos(a)) for a in arc_angles]
    depth = 0.1 * math.cos(math.pi / 6)
    points.extend(_circle_arrow_profile_points(start, depth, 0.05))
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    if angle == -90:
        expected = (0, 0, 0, 0, 0, 0)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("offset", (0, 0.2))
def test_single_end_wide_semicircle_keeps_flat_cap(
    maya_cmds, maya_om, new_scene, filled, offset
):
    _load_bd_util_nodes(maya_cmds)
    name = "SemicircleWideArrowAtEnd" + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
    extent = _circle_arrow_outer_extent(0.1 * math.cos(math.pi / 6), 0.05)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, 0, -0.525, 0, 0.525, extent), abs=1e-9
    )


@pytest.mark.parametrize(
    "preset,part,offset",
    tuple(
        (preset, part, offset)
        for preset in (
            "Arc",
            "WideArcRadial",
            "CrossArc",
            "WideCrossArcRadial",
        )
        for part, offset in ((0, 0), (1, 0.1))
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_long_arrow_follows_radius_and_keeps_its_tip(
    maya_cmds, maya_om, new_scene, preset, part, offset, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    depth = 0.67 * math.cos(math.pi / 6)
    root_angle = 2 * depth
    for attribute, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartType", 0),
        ("shapePartShape", part),
        ("shapePartLengthScale", 6.7),
        ("shapePartOffset", offset),
        ("shapeFill", filled),
        ("shapeRotateX", math.degrees(root_angle)),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    # 根元の半径方向へ投影し、長さを弧長、幅を半径方向として独立に確認する。
    assert bounds[5] == pytest.approx(0.55, abs=1e-9)
    assert bounds[1] == pytest.approx(-0.5 * math.sin(root_angle), abs=1e-9)
    if part == 1 and "Cross" not in preset:
        assert bounds[3] == pytest.approx(0.05, abs=1e-9)


@pytest.mark.parametrize(
    "preset",
    ("Arc", "WideArcRadial", "CrossArc", "WideCrossArcRadial"),
)
@pytest.mark.parametrize("part", (0, 3))
def test_radial_circle_apex_keeps_outward_part_and_original_body(
    maya_cmds, maya_om, new_scene, preset, part
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    for attribute, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartType", 2),
        ("shapePartShape", part),
        ("shapePartLengthScale", 6.7),
        ("shapePartOffset", 0.1),
        ("shapeFill", True),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    radius = 0.525 if "Wide" in preset else 0.5
    cross_radius = radius if "Cross" in preset else 0
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            -cross_radius,
            0,
            -radius,
            cross_radius,
            0.6 + (0.335 if part == 3 else 0.8375),
            radius,
        ),
        abs=1e-9,
    )


@pytest.mark.parametrize("length", (-2, 0, 20))
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_signed_and_long_arrow_lengths_stay_on_the_circle(
    maya_cmds, maya_om, new_scene, length, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Arc")
    for attribute, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartType", 0),
        ("shapePartShape", 0),
        ("shapePartLengthScale", length),
        ("shapePartOffset", 0.2),
        ("shapeFill", filled),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert bounds[0] == bounds[3] == 0
    assert all(-0.55 - 1e-9 <= value <= 0.55 + 1e-9 for value in bounds)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", -0.4)
    assert _bounds(maya_om, shape) == pytest.approx(bounds, abs=1e-9)


@pytest.mark.parametrize(
    "preset",
    ("Arc", "WideArcRadial", "CrossArc", "WideCrossArcRadial"),
)
@pytest.mark.parametrize("part", range(6))
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_wrapped_parts_ignore_offset_and_use_radial_width(
    maya_cmds, maya_om, new_scene, preset, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=filled
    )
    for attribute, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartType", 1),
        ("shapePartShape", part),
        ("shapePartLengthScale", 6.7),
        ("shapePartWidthScale", 4),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    expected = _bounds(maya_om, shape)
    assert all(-0.7 - 1e-9 <= value <= 0.7 + 1e-9 for value in expected)
    if "Cross" not in preset:
        assert expected[0] == 0
        assert expected[3] == pytest.approx(0.05 if part == 1 else 0, abs=1e-9)
    for offset in (-0.4, 0.4):
        maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == offset


@pytest.mark.parametrize("preset", ("Arc", "WideArcRadial"))
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_wide_marker_stops_at_center_without_folding(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=filled
    )
    for attribute, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartType", 0),
        ("shapePartShape", 3),
        ("shapePartLengthScale", 6.7),
        ("shapePartWidthScale", 40),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert bounds[2] == pytest.approx(
        -0.525 if "Wide" in preset else -0.5, abs=1e-9
    )
    assert bounds[5] == pytest.approx(2.5, abs=1e-9)


@pytest.mark.parametrize("preset", ("Arc", "WideCrossArcRadial"))
@pytest.mark.parametrize("part", range(6))
@pytest.mark.parametrize("filled", (False, True))
def test_radial_circle_wrapped_parts_remain_bounded_across_multiple_turns(
    maya_cmds, maya_om, new_scene, preset, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 180)
    baseline = _bounds(maya_om, shape)
    for attribute, value in (
        ("shapePart", True),
        ("shapePartType", 1),
        ("shapePartShape", part),
        ("shapePartLengthScale", 50),
        ("shapePartWidthScale", 4),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert all(
        math.isfinite(value) and abs(value) <= 0.7 + 1e-9 for value in bounds
    )
    assert max(abs(value) for value in bounds) > 0.5
    maya_cmds.setAttr(f"{shape}.shapePartSize", 0)
    assert _bounds(maya_om, shape) == pytest.approx(baseline, abs=1e-9)


def test_radial_circle_wrapping_preserves_connected_offset_and_history(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds, shape_name="Arc", shape_fill=True)
    maya_cmds.setAttr(f"{name}.shapeArcAngle", 180)
    baseline = _bounds(maya_om, name)
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="offset", attributeType="double", defaultValue=0.4
    )
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shapePart.set(True)
    shape.shapePartShape.set(1)
    shape.shapePartLengthScale.set(6.7)
    shape.shapePartOffset.connect_from(f"{source}.offset")
    mod.do_it_dg()
    wrapped = _bounds(maya_om, name)
    assert wrapped != pytest.approx(baseline)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(baseline)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(wrapped)
    maya_cmds.setAttr(f"{source}.offset", 0.8)
    assert _bounds(maya_om, name) == pytest.approx(wrapped)
    maya_cmds.setAttr(f"{name}.shapePartType", 2)
    high = _bounds(maya_om, name)[4]
    maya_cmds.setAttr(f"{source}.offset", 0.4)
    assert _bounds(maya_om, name)[4] == pytest.approx(high - 0.4)
    maya_cmds.setAttr(f"{name}.shapePartType", 0)
    scene_path = tmp_path / "radial_wrapped_offset.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.isConnected(f"{source}.offset", f"{name}.shapePartOffset")
    assert _bounds(maya_om, name) == pytest.approx(wrapped)


@pytest.mark.parametrize(
    "base,axes",
    (
        ("CrossLine", (0, 2)),
        ("CrossLineSwapped", (1, 2)),
    ),
)
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size",
    (
        (0, 1, 1, 1),
        (0.2, 1.5, 2, 1),
        (-0.2, 0.5, 1, 2),
        (0.1, -2, -3, 1),
        (-1.2, 1, 1, 1),
        (0.1, 3, 22, 1),
        (0.1, 0, 1, 1),
        (0.1, 1, 0, 1),
        (0.1, 1, 1, 0),
    ),
)
def test_single_cross_arrow_bounds_follow_only_selected_endpoint(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    axes,
    wide,
    filled,
    offset,
    length,
    width,
    size,
):
    _load_bd_util_nodes(maya_cmds)
    axis = axes[0]
    side = next(value for value in axes if value != axis)
    name = (
        base
        + ("Wide" if wide else "")
        + "ArrowAtEnd"
        + ("Filled" if filled else "")
    )
    _, shape = _create_controller(maya_cmds, shape_name=name)
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    tip = 0.5 + offset
    shoulder = tip - 0.1 * math.cos(math.pi / 6) * length * size
    points = []
    for body_axis in axes:
        body_side = next(value for value in axes if value != body_axis)
        for body_sign in (-1, 1):
            along = body_sign * 0.5
            if body_axis == axis and body_sign > 0:
                along = shoulder if wide else tip
            for transverse_sign in (-1, 1):
                point = [0.0, 0.0, 0.0]
                point[body_axis] = along
                point[body_side] = transverse_sign * 0.025 if wide else 0
                points.append(point)
    points.append([tip if i == axis else 0 for i in range(3)])
    for transverse_sign in (-1, 1):
        point = [0.0, 0.0, 0.0]
        point[axis] = shoulder
        point[side] = transverse_sign * 0.05 * abs(width * size)
        points.append(point)
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.boundsMode", 1)
    extent = [(expected[i + 3] - expected[i]) * 0.5 for i in range(3)]
    assert _bounds(maya_om, shape) == pytest.approx(
        tuple(-value for value in extent) + tuple(extent), abs=1e-9
    )


@pytest.mark.parametrize(
    "shape_name",
    ("CrossLineWideArrowAtEndFilled", "CrossLineSwappedWideArrowAtEndFilled"),
)
def test_single_cross_arrow_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    _set_shape_operator(shape, shape_name)
    shape.shapePartOffset.set(0.2)
    shape.shapePartLengthScale.set(2)
    shape.shapePartWidthScale.set(1.5)
    shape.shape1stAxis.set(4)
    shape.shape2ndAxis.set(0)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    mod.undo_it()
    assert _bounds(maya_om, name) != pytest.approx(expected)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "single_cross_arrow.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shape") == _shape_index(shape_name)


@pytest.mark.parametrize(
    "shape_name",
    [
        name
        for name in SHAPE_VARIANTS
        if name.endswith(("AtEnd", "AtEndFilled"))
    ],
)
@pytest.mark.parametrize("first_axis,sign", ((4, 1), (5, -1)))
def test_representative_endpoint_follows_axis_reorientation(
    maya_cmds, maya_om, new_scene, shape_name, first_axis, sign
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=shape_name)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 1.5)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 2)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 0)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 2)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", first_axis)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 0)
    maya_cmds.setAttr(f"{shape}.shapeScale", -2, 3, 0.5)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", 1, 2, 3)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", 1.5)
    corners = [
        (
            1.5 * (1 - 2 * y),
            1.5 * (2 + 3 * sign * z),
            1.5 * (3 + 0.5 * sign * x),
        )
        for x in (before[0], before[3])
        for y in (before[1], before[4])
        for z in (before[2], before[5])
    ]
    expected = tuple(min(p[i] for p in corners) for i in range(3)) + tuple(
        max(p[i] for p in corners) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_single_end_shape_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    _set_shape_operator(shape, "SemicircleWideArrowAtEndFilled")
    shape.shapePartOffset.set(0.2)
    shape.shapeArcAngle.set(240)
    shape.shapePartLengthScale.set(2)
    shape.shapePartWidthScale.set(1.5)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    mod.undo_it()
    assert _bounds(maya_om, name) != pytest.approx(expected)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "single_end_arrow.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shape") == _shape_index(
        "SemicircleWideArrowAtEndFilled"
    )


@pytest.mark.parametrize("filled", (False, True))
def test_diamond_fits_square_midpoints(maya_cmds, maya_om, new_scene, filled):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="Diamond" + ("Filled" if filled else "")
    )
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, 0, -0.5, 0.5, 0, 0.5), abs=1e-9
    )
    maya_cmds.setAttr(f"{shape}.shapeRotateY", 45)
    extent = math.sqrt(0.125)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, 0, -extent, extent, 0, extent), abs=1e-9
    )
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 3)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent, 0, -extent, extent, 0, extent), abs=1e-9
    )


@pytest.mark.parametrize(
    "preset,normal",
    (
        ("Line", 1),
        ("WideLine", 1),
        ("CrossLine", 1),
        ("WideCrossLine", 1),
        ("CrossLineSwapped", 0),
        ("WideCrossLineSwapped", 0),
        ("Arc", 0),
        ("WideArcRadial", 0),
    ),
)
@pytest.mark.parametrize("all_ends", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_arrow3d_part_uses_positive_normal_at_every_endpoint(
    maya_cmds, maya_om, new_scene, preset, normal, all_ends, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=filled
    )
    for attribute, value in (
        ("shapePart", True),
        ("shapePartShape", 1),
        ("shapePartType", int(all_ends)),
        ("shapeArcAngle", 240),
        ("shapePartOffset", 0.2),
        ("shapePartWidthScale", 2),
        ("shapePartHeightScale", 2),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    bounds = _bounds(maya_om, shape)
    assert bounds[normal] == pytest.approx(0, abs=1e-9)
    assert bounds[normal + 3] == pytest.approx(0.1, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeScale", -1, -1, -1)
    reflected = _bounds(maya_om, shape)
    assert reflected[normal] == pytest.approx(-0.1, abs=1e-9)
    assert reflected[normal + 3] == pytest.approx(0, abs=1e-9)


@pytest.mark.parametrize("base", ("CrossLine3Axis", "ColorCrossLine3Axis"))
@pytest.mark.parametrize("part", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_three_axis_end_arrows_use_direction_specific_planes(
    maya_cmds, maya_om, new_scene, base, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=base, shape_fill=filled
    )
    for name, value in (
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartType", 1),
        ("shapePartOffset", 0.3),
        ("shapePartWidthScale", 7),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    matrix_values = (
        1.1,
        1,
        0.2,
        0,
        1,
        1.1,
        1,
        0,
        0.1,
        0.15,
        1.1,
        0,
        0,
        0,
        0,
        1,
    )
    maya_cmds.setAttr(
        f"{shape}.shapeAnimationTransformMatrix", *matrix_values, type="matrix"
    )
    matrix = maya_om.MMatrix(matrix_values)
    points = []
    # 主面はX/Z方向でXZ、Y方向でYZ。追加面はそれぞれ+Y、+Xへ立てる。
    for along, side, up in ((0, 2, 1), (1, 2, 0), (2, 0, 1)):
        for sign in (-1, 1):
            factor = 1.0 if along == 0 and sign > 0 else 0.5
            shoulder = 0.8 - 0.1 * math.cos(math.pi / 6) * factor
            tip = [0.0, 0.0, 0.0]
            tip[along] = sign * 0.8
            points.append(maya_om.MPoint(*tip) * matrix)
            for width in (-0.35 * factor, 0.35 * factor):
                wing = [0.0, 0.0, 0.0]
                wing[along] = sign * shoulder
                wing[side] = width
                points.append(maya_om.MPoint(*wing) * matrix)
            if part == 1:
                crest = [0.0, 0.0, 0.0]
                crest[along] = sign * shoulder
                crest[up] = 0.05 * factor
                points.append(maya_om.MPoint(*crest) * matrix)
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "base,axes,side",
    (
        ("Line", (0,), 2),
        ("CrossLine", (0, 2), None),
        ("CrossLineSwapped", (1, 2), None),
    ),
)
@pytest.mark.parametrize("all_ends", (False, True))
@pytest.mark.parametrize("part", ("Square", "Diamond", "Circle", "Triangle"))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "offset,length,width,size",
    (
        (0, 1, 1, 1),
        (0.2, 2, 3, 1),
        (-0.2, 0.5, 1, 2),
        (0.1, -2, -3, 1),
        (-0.5, 1, 1, 1),
        (-0.7, 1, 1, 1),
        (0.1, 0, 1, 1),
        (0.1, 1, 0, 1),
        (0.1, 1, 1, 0),
    ),
)
def test_planar_end_shape_bounds_follow_part_controls(
    maya_cmds,
    maya_om,
    new_scene,
    base,
    axes,
    side,
    all_ends,
    part,
    filled,
    offset,
    length,
    width,
    size,
):
    _load_bd_util_nodes(maya_cmds)
    placement = "Ends" if all_ends else "End"
    name = base + part + "At" + placement + ("Filled" if filled else "")
    _, shape = _create_controller(maya_cmds, shape_name=name)
    for attribute, value in (
        ("shapePartOffset", offset),
        ("shapePartLengthScale", length),
        ("shapePartWidthScale", width),
        ("shapePartSize", size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    points = [] if base == "Line" else [[0.0, 0.0, 0.0]]
    for axis in axes:
        other = (
            side
            if side is not None
            else next(value for value in axes if value != axis)
        )
        for sign in (-1, 1):
            if not all_ends and (axis != axes[0] or sign < 0):
                point = [0.0, 0.0, 0.0]
                point[axis] = 0.5 * sign
                points.append(point)
                continue
            factor = 0.5 if all_ends and (axis != axes[0] or sign < 0) else 1.0
            end_size = size * factor
            center = 0.5 + offset
            if part == "Triangle":
                center -= 0.05 * length * end_size
            along = (
                center - 0.05 * length * end_size,
                center + 0.05 * length * end_size,
            )
            transverse = 0.05 * abs(width * end_size)
            for coordinate in along:
                for width_sign in (-1, 1):
                    point = [0.0, 0.0, 0.0]
                    point[axis] = coordinate * sign
                    point[other] = transverse * width_sign
                    points.append(point)
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    if not all_ends:
        maya_cmds.setAttr(f"{shape}.boundsMode", 1)
        extent = [(expected[i + 3] - expected[i]) * 0.5 for i in range(3)]
        assert _bounds(maya_om, shape) == pytest.approx(
            tuple(-value for value in extent) + tuple(extent), abs=1e-9
        )


@pytest.mark.parametrize(
    "shape_name",
    (
        "LineSquareAtEndFilled",
        "LineDiamondAtEndFilled",
        "LineCircleAtEndFilled",
        "CrossLineSquareAtEndFilled",
        "CrossLineSwappedDiamondAtEndFilled",
        "CrossLineCircleAtEndsFilled",
    ),
)
def test_planar_end_controls_connections_and_history(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds)
    source = maya_cmds.createNode("multDoubleLinear")
    maya_cmds.setAttr(f"{source}.input1", 0.1)
    maya_cmds.setAttr(f"{source}.input2", 2)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    shape = bd_nodes.existing(name)
    _set_shape_operator(shape, shape_name)
    shape.shapePartOffset.connect_from(f"{source}.output")
    shape.shapePartLengthScale.set(2)
    shape.shapePartWidthScale.set(1.5)
    shape.shapePartSize.set(2)
    shape.shape1stAxis.set(4)
    shape.shape2ndAxis.set(0)
    mod.do_it_dg()
    expected = _bounds(maya_om, name)
    mod.undo_it()
    assert _bounds(maya_om, name) != pytest.approx(expected)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(expected)
    path = tmp_path / "planar_end_shape.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert _bounds(maya_om, name) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{name}.shape") == _shape_index(shape_name)
    assert maya_cmds.isConnected(f"{source}.output", f"{name}.shapePartOffset")
    maya_cmds.setAttr(f"{source}.input1", 0.2)
    assert _bounds(maya_om, name) != pytest.approx(expected)


@pytest.mark.parametrize("placement", ("End", "Ends"))
def test_planar_end_offset_uses_scene_distance_units(
    maya_cmds, maya_om, new_scene, placement
):
    _load_bd_util_nodes(maya_cmds)
    previous_unit = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        _, shape = _create_controller(
            maya_cmds, shape_name="LineDiamondAt" + placement + "Filled"
        )
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 2)
        assert _bounds(maya_om, shape) == pytest.approx(
            (
                -0.5 if placement == "End" else -0.725,
                0,
                -0.05,
                0.75,
                0,
                0.05,
            ),
            abs=1e-9,
        )
        maya_cmds.currentUnit(linear="cm")
        assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == pytest.approx(
            0.2
        )
    finally:
        maya_cmds.currentUnit(linear=previous_unit)


def test_custom_bounds_node_operator_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds, bounds_mode=None)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    shape.boundsMode.set(2)
    shape.customBoundsSize.set(4.0)
    shape.customBoundsTranslate.set(2.0, 0.0, 0.0)
    shape.showBoundsPreview.set(True)
    mod.do_it_dg()

    expected = (0.0, -2.0, -2.0, 4.0, 2.0, 2.0)
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)
    mod.undo_it()
    assert maya_cmds.getAttr(f"{shape_name}.boundsMode") == 1
    assert not maya_cmds.getAttr(f"{shape_name}.showBoundsPreview")
    mod.redo_it()
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)

    scene_path = tmp_path / "controller_shape_custom_bounds.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape_name}.boundsMode") == 2
    assert maya_cmds.getAttr(f"{shape_name}.showBoundsPreview")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected, abs=1.0e-9)


@pytest.mark.parametrize("shape_name", VARIANT_NAMES)
@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_fin_option_all_shapes(
    maya_cmds, maya_om, new_scene, shape_name, fin_type, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=filled
    )
    base = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeFinType", fin_type)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 1.5)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    actual = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in actual)
    if shape_name in ARC_SHAPES:
        assert actual == pytest.approx(base)
    else:
        assert actual != pytest.approx(base)
    for axis in range(3):
        assert actual[axis] <= base[axis] + 1e-9
        assert actual[axis + 3] >= base[axis + 3] - 1e-9
    maya_cmds.setAttr(f"{shape}.shapeFin", False)
    assert _bounds(maya_om, shape) == pytest.approx(base)
    assert maya_cmds.getAttr(f"{shape}.shapeFinType") == fin_type
    assert maya_cmds.getAttr(f"{shape}.shapeFinHeight") == pytest.approx(1.5)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    assert _bounds(maya_om, shape) == pytest.approx(actual)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    assert _bounds(maya_om, shape) == pytest.approx(base)


@pytest.mark.parametrize("bounds_mode", (0, 1, 2))
@pytest.mark.parametrize("connected", (False, True))
def test_fin_option_updates_bounds(
    maya_cmds, maya_om, new_scene, bounds_mode, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="Pyramid", bounds_mode=bounds_mode
    )
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.75)
    base = _bounds(maya_om, shape)
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(source, longName="fin", attributeType="bool")
    maya_cmds.addAttr(source, longName="finType", attributeType="long")
    if connected:
        for attr in ("fin", "finType"):
            maya_cmds.connectAttr(
                f"{source}.{attr}",
                f"{shape}.shape{attr[0].upper() + attr[1:]}",
            )
    fin = f"{source}.fin" if connected else f"{shape}.shapeFin"
    kind = f"{source}.finType" if connected else f"{shape}.shapeFinType"
    for enabled, fin_type, maximum in (
        (True, 0, 0.75),
        (True, 1, 1.25),
        (False, 1, 0.5),
        (True, 0, 0.75),
    ):
        maya_cmds.setAttr(fin, enabled)
        maya_cmds.setAttr(kind, fin_type)
        actual = _bounds(maya_om, shape)
        if bounds_mode == 2:
            assert actual == pytest.approx(base)
        elif bounds_mode == 0:
            assert actual[4] == pytest.approx(maximum)
        else:
            assert actual[4] == pytest.approx((maximum + 0.5) / 2)


@pytest.mark.parametrize(
    "shape_name,height_axis,width_axis,low",
    (
        ("Gear", 1, 0, -0.5),
        ("Triangle", 1, 0, -0.37),
        ("SquareArrow3D", 1, 0, -0.5),
        ("Diamond", 1, 0, -0.5),
        ("CrossLine", 1, 0, -0.5),
        ("CrossLineSwapped", 0, 1, -0.5),
    ),
)
@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_planar_fin_perpendicular_bounds(
    maya_cmds,
    maya_om,
    new_scene,
    shape_name,
    height_axis,
    width_axis,
    low,
    fin_type,
    filled,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinType", fin_type)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 1.25)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 2)
    # 本体の部品変形も含む範囲へ、独立したFinの幅・高さを加える。
    maya_cmds.setAttr(f"{shape}.shapeFin", False)
    base = list(_bounds(maya_om, shape))
    expected = base.copy()
    pivot = (low + 0.5) / 2
    expected[width_axis] = min(expected[width_axis], pivot + (low - pivot) * 2)
    expected[width_axis + 3] = max(
        expected[width_axis + 3], pivot + (0.5 - pivot) * 2
    )
    expected[height_axis + 3] = max(expected[height_axis + 3], 1.25)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", -1.25)
    expected[height_axis + 3] = max(base[height_axis + 3], 0)
    expected[height_axis] = min(expected[height_axis], -1.25)
    assert _bounds(maya_om, shape) == pytest.approx(expected)


@pytest.mark.parametrize("shape_name", ARC_SHAPES)
@pytest.mark.parametrize("connected", (False, True))
@pytest.mark.parametrize("bounds_mode", (0, 1, 2))
@pytest.mark.parametrize("filled", (False, True))
def test_circle_fin_controls_are_ignored_and_retained(
    maya_cmds, maya_om, new_scene, shape_name, connected, bounds_mode, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds,
        shape_name=shape_name,
        shape_fill=filled,
        bounds_mode=bounds_mode,
    )
    values = {
        "shapeFin": True,
        "shapeFinType": 1,
        "shapeFinHeight": 3.0,
        "shapeFinSize": 2.0,
        "shapeFinWidthScale": -4.0,
    }
    source = maya_cmds.createNode("network")
    for name, value in values.items():
        target = f"{shape}.{name}"
        if connected:
            maya_cmds.addAttr(
                source,
                longName=name,
                attributeType=(
                    "bool"
                    if name == "shapeFin"
                    else "long" if name == "shapeFinType" else "double"
                ),
            )
            maya_cmds.connectAttr(f"{source}.{name}", target)
            target = f"{source}.{name}"
        maya_cmds.setAttr(target, value)
    for angle in (0, 90, 180, 360):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        baseline = _bounds(maya_om, shape)
        for enabled in (False, True):
            maya_cmds.setAttr(
                f"{source if connected else shape}.shapeFin", enabled
            )
            assert _bounds(maya_om, shape) == pytest.approx(baseline)
    for name, value in values.items():
        assert maya_cmds.getAttr(f"{shape}.{name}") == pytest.approx(value)
        if connected:
            assert maya_cmds.isConnected(f"{source}.{name}", f"{shape}.{name}")
    set_preset(maya_cmds, shape, "Line")
    with_fin = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{source if connected else shape}.shapeFin", False)
    if bounds_mode != 2:
        assert _bounds(maya_om, shape) != pytest.approx(with_fin)


@pytest.mark.parametrize("fin_type", (0, 1))
def test_arrow_fin_type_and_body_following(
    maya_cmds, maya_om, new_scene, fin_type
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Arrow")
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinType", fin_type)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    maya_cmds.setAttr(f"{shape}.shapePartLengthScale", 2)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 0)
    assert _bounds(maya_om, shape) == pytest.approx((-1.3, 0, 0, 0.7, 0.5, 0))


def test_fin_option_axis_mapping(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Line")
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 2)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 4)
    assert _bounds(maya_om, shape) == pytest.approx((0, -0.5, 0, 0, 0.5, 0.5))


@pytest.mark.parametrize(
    "shape_name",
    ("ColorCube", "ColorCornerCube", "ColorSphere", "ColorCrossLine3Axis"),
)
@pytest.mark.parametrize("fin_type", (0, 1))
def test_fin_option_color_constraints(
    maya_cmds, maya_om, new_scene, shape_name, fin_type
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=True
    )
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinType", fin_type)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 5)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 1)
    # 本体の軸色は固定し、Finだけを主軸-Z・補助軸-Xの基底へ向ける。
    expected = (
        -before[4],
        before[2],
        -before[3],
        -before[1],
        before[5],
        -before[0],
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    maya_cmds.setAttr(f"{shape}.shapeRotate", 30, 60, 90)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotate", 90, 60, 30)
    maya_cmds.setAttr(f"{shape}.shapeScale", -1, -1, -1)
    maya_cmds.setAttr(f"{shape}.shapeAxisScale", -1, -1, -1)
    assert _bounds(maya_om, shape) == pytest.approx(expected)


def test_fin_option_animation(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Pyramid")
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.75)
    for frame, enabled, fin_type in (
        (1, False, 0),
        (10, True, 0),
        (20, True, 1),
    ):
        maya_cmds.setKeyframe(
            shape, attribute="shapeFin", time=frame, value=enabled
        )
        maya_cmds.setKeyframe(
            shape, attribute="shapeFinType", time=frame, value=fin_type
        )
    for frame, maximum in ((1, 0.5), (10, 0.75), (20, 1.25), (1, 0.5)):
        maya_cmds.currentTime(frame)
        assert _bounds(maya_om, shape)[4] == pytest.approx(maximum)


def test_fin_option_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(maya_cmds, shape_name="Pyramid")
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="kind", attributeType="long", defaultValue=1
    )
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    shape.shapeFin.set(True)
    shape.shapeFinType.connect_from(f"{source}.kind")
    shape.shapeFinHeight.set(0.75)
    mod.do_it_dg()
    assert _bounds(maya_om, name)[4] == pytest.approx(1.25)
    mod.undo_it()
    assert _bounds(maya_om, name)[4] == pytest.approx(0.5)
    mod.redo_it()
    assert _bounds(maya_om, name)[4] == pytest.approx(1.25)
    scene_path = tmp_path / "shape_fin.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    assert maya_cmds.getAttr(f"{name}.shapeFin")
    assert maya_cmds.isConnected(f"{source}.kind", f"{name}.shapeFinType")
    assert _bounds(maya_om, name)[4] == pytest.approx(1.25)
    maya_cmds.setAttr(f"{source}.kind", 0)
    assert _bounds(maya_om, name)[4] == pytest.approx(0.75)


@pytest.mark.parametrize("shape_name", VARIANT_NAMES)
@pytest.mark.parametrize("part_name", PART_SHAPES)
@pytest.mark.parametrize("placement", (0, 1, 2))
def test_common_part_combinations_are_finite_and_reversible(
    maya_cmds, maya_om, new_scene, shape_name, part_name, placement
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=True
    )
    for attribute, value in (
        ("shapePartOffset", 0.2),
        ("shapePartSize", 1.5),
        ("shapePartLengthScale", 0.75),
        ("shapePartWidthScale", 1.25),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    baseline = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePartShape", PART_SHAPES.index(part_name))
    maya_cmds.setAttr(f"{shape}.shapePartType", placement)
    assert _bounds(maya_om, shape) == pytest.approx(baseline)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    decorated = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in decorated)
    assert all(decorated[i] <= decorated[i + 3] for i in range(3))
    if shape_name in PART_UNSUPPORTED:
        assert decorated == pytest.approx(baseline)
    maya_cmds.setAttr(f"{shape}.shapePart", False)
    assert _bounds(maya_om, shape) == pytest.approx(baseline)
    assert maya_cmds.getAttr(f"{shape}.shapePartShape") == PART_SHAPES.index(
        part_name
    )
    assert maya_cmds.getAttr(f"{shape}.shapePartType") == placement
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    assert _bounds(maya_om, shape) == pytest.approx(decorated)


@pytest.mark.parametrize("shape_name", ARC_SHAPES)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("angle", (0, 45, 90, 180, 270, 360))
def test_circle_total_angle_bounds(
    maya_cmds, maya_om, new_scene, shape_name, filled, angle
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
    shape_name = shape_name.removesuffix("Swapped")
    if angle == 0:
        expected = (0, 0, 0, 0, 0, 0)
    else:
        wide = shape_name.startswith("Wide") and shape_name.endswith("Radial")
        axial = shape_name.startswith("Wide") and shape_name.endswith("Axial")
        outer = 0.525 if wide else 0.5
        half = math.radians(angle / 2)
        lower_radius = 0.475 if wide and angle < 180 else outer
        minimum = lower_radius * math.cos(half)
        side = outer * math.sin(half) if angle < 180 else outer
        depth = 0.025 if axial else 0
        expected = (-depth, minimum, -side, depth, outer, side)
        if "CrossArc" in shape_name:
            side = max(side, depth)
            expected = (-side, minimum, -side, side, outer, side)
        if shape_name == "WideCrossArcAxial":
            top = math.sqrt(0.25 - depth * depth)
            expected = (
                -side,
                -top if angle == 360 else minimum,
                -side,
                side,
                top,
                side,
            )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_fin_scales_are_independent_of_part_scales(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="Line", shape_fill=True
    )
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    baseline = _bounds(maya_om, shape)
    for attribute, value in (
        ("shapePartSize", 9),
        ("shapePartWidthScale", -4),
        ("shapePartLengthScale", 0),
        ("shapePartOffset", 5),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(baseline)
    maya_cmds.setAttr(f"{shape}.shapeFinSize", 2)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 3)
    assert _bounds(maya_om, shape) == pytest.approx((-3, 0, 0, 3, 1, 0))


@pytest.mark.parametrize("connected", (False, True))
@pytest.mark.parametrize("bounds_mode", (0, 1, 2))
def test_common_part_controls_update_cached_bounds(
    maya_cmds, maya_om, new_scene, connected, bounds_mode
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="Line", bounds_mode=bounds_mode
    )
    targets = {
        name: f"{shape}.{name}"
        for name in ("shapePart", "shapePartShape", "shapePartType")
    }
    if connected:
        source = maya_cmds.createNode("network")
        for name in targets:
            maya_cmds.addAttr(
                source,
                longName=name,
                attributeType="bool" if name == "shapePart" else "long",
            )
            maya_cmds.connectAttr(f"{source}.{name}", targets[name])
            targets[name] = f"{source}.{name}"
    for enabled, kind, placement, expected in (
        (False, 6, 0, (-0.5, 0, 0, 0.5, 0, 0)),
        (True, 6, 0, (-0.5, -0.05, -0.05, 0.55, 0.05, 0.05)),
        (True, 6, 1, (-0.525, -0.05, -0.05, 0.55, 0.05, 0.05)),
        (True, 1, 0, (-0.5, 0, -0.05, 0.5, 0.05, 0.05)),
        (False, 1, 1, (-0.5, 0, 0, 0.5, 0, 0)),
    ):
        for name, value in zip(targets, (enabled, kind, placement)):
            maya_cmds.setAttr(targets[name], value)
        if bounds_mode == 1:
            half = tuple((expected[i + 3] - expected[i]) / 2 for i in range(3))
            expected = tuple(-value for value in half) + half
        elif bounds_mode == 2:
            expected = (-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_common_part_option_animation(maya_cmds, maya_om, new_scene):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Line")
    for frame, enabled, kind, placement in (
        (1, False, 6, 0),
        (10, True, 6, 1),
        (20, True, 1, 0),
    ):
        for attribute, value in (
            ("shapePart", enabled),
            ("shapePartShape", kind),
            ("shapePartType", placement),
        ):
            maya_cmds.setKeyframe(
                shape, attribute=attribute, time=frame, value=value
            )
    for frame, expected in (
        (10, (-0.525, -0.05, -0.05, 0.55, 0.05, 0.05)),
        (20, (-0.5, 0, -0.05, 0.5, 0.05, 0.05)),
        (1, (-0.5, 0, 0, 0.5, 0, 0)),
    ):
        maya_cmds.currentTime(frame)
        assert _bounds(maya_om, shape) == pytest.approx(expected)


@pytest.mark.parametrize("shape_name", ARC_SHAPES)
def test_common_options_history_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, shape_name
):
    _load_bd_util_nodes(maya_cmds)
    _, name = _create_controller(
        maya_cmds, shape_name=shape_name, shape_fill=True
    )
    before = _bounds(maya_om, name)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    values = {
        "shapePart": True,
        "shapePartShape": 6,
        "shapePartType": 1,
        "shapePartPrimarySizeScale": 1.5,
        "shapePartOtherSizeScale": 0.25,
        "shapeWideWidth": 0.2,
        "shapeArcAngle": 240,
        "shapeFin": True,
        "shapeFinSize": 1.5,
        "shapeFinWidthScale": 2,
        "shapeFinHeight": 0.75,
    }
    for attribute, value in values.items():
        getattr(shape, attribute).set(value)
    mod.do_it_dg()
    after = _bounds(maya_om, name)
    assert after != pytest.approx(before)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(before)
    assert maya_cmds.getAttr(
        f"{name}.shapePartPrimarySizeScale"
    ) == pytest.approx(1.0)
    assert maya_cmds.getAttr(
        f"{name}.shapePartOtherSizeScale"
    ) == pytest.approx(0.5)
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(after)
    assert maya_cmds.getAttr(
        f"{name}.shapePartPrimarySizeScale"
    ) == pytest.approx(1.5)
    assert maya_cmds.getAttr(
        f"{name}.shapePartOtherSizeScale"
    ) == pytest.approx(0.25)
    scene_path = tmp_path / "common_shape_options.ma"
    maya_cmds.file(rename=str(scene_path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene_path), open=True, force=True)
    for attribute, value in values.items():
        assert maya_cmds.getAttr(f"{name}.{attribute}") == pytest.approx(value)
    assert _bounds(maya_om, name) == pytest.approx(after)


@pytest.mark.parametrize(
    "wide_name,base_name",
    (
        ("WideLine", "Line"),
        ("WideCrossLine", "CrossLine"),
        ("WideCrossLineSwapped", "CrossLineSwapped"),
        ("WideCircle", "Circle"),
        ("WideCircleSwapped", "CircleSwapped"),
        ("WideCrossLine3Axis", "CrossLine3Axis"),
        ("ColorWideCrossLine3Axis", "ColorCrossLine3Axis"),
        ("WideArcRadial", "ArcRadial"),
        ("WideArcAxial", "ArcAxial"),
        ("WideCrossArcRadial", "CrossArcRadial"),
        ("WideCrossArcAxial", "CrossArcAxial"),
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_zero_wide_width_keeps_the_base_outline(
    maya_cmds, maya_om, new_scene, wide_name, base_name, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=wide_name, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0)
    actual = _bounds(maya_om, shape)
    _set_shape(maya_cmds, shape, base_name)
    maya_cmds.setAttr(f"{shape}.shapeFill", filled)
    assert actual == pytest.approx(_bounds(maya_om, shape), abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "base,part_name,placement,expected",
    (
        ("Line", "Cube", 0, (-0.5, -0.05, -0.05, 0.55, 0.05, 0.05)),
        ("Square", "Cube", 0, (-0.5, -0.05, -0.5, 0.55, 0.05, 0.5)),
        ("Square", "Cube", 1, (-0.525, -0.05, -0.525, 0.55, 0.05, 0.525)),
        ("Cube", "Triangle", 0, (-0.5, -0.5, -0.5, 0.6, 0.5, 0.5)),
        ("Cube", "Cone", 1, (-0.55, -0.55, -0.55, 0.6, 0.55, 0.55)),
    ),
)
def test_common_parts_combine_planar_and_solid_shapes(
    maya_cmds, maya_om, new_scene, filled, base, part_name, placement, expected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=base, shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    maya_cmds.setAttr(f"{shape}.shapePartShape", PART_SHAPES.index(part_name))
    maya_cmds.setAttr(f"{shape}.shapePartType", placement)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("angle", (45, 90, 180, 240, 360))
@pytest.mark.parametrize("all_ends", (False, True))
@pytest.mark.parametrize("part", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("offset,part_size", ((0, 1), (0.4, 1), (0.4, 2)))
def test_axial_circle_arrow_frame_follows_the_surface(
    maya_cmds,
    maya_om,
    new_scene,
    angle,
    all_ends,
    part,
    filled,
    offset,
    part_size,
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for attribute, value in (
        ("shapeArcAngle", angle),
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartType", int(all_ends)),
        ("shapePartOffset", offset),
        ("shapePartSize", part_size),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    sweep = math.radians(angle)
    start, end = (math.pi - sweep) / 2, (math.pi + sweep) / 2
    sample_angles = [start, end] + [
        index * math.pi / 2
        for index in range(-2, 5)
        if start < index * math.pi / 2 < end
    ]
    points = [
        (x, 0.5 * math.sin(a), 0.5 * math.cos(a))
        for a in sample_angles
        for x in (-0.025, 0.025)
    ]
    depth = 0.1 * math.cos(math.pi / 6) * part_size
    half_width = 0.05 * part_size
    for angle, sign in ((start, 1), (end, -1)) if all_ends else ((start, 1),):
        root = angle + sign * 2 * depth
        points.extend(
            (width, 0.5 * math.sin(root), 0.5 * math.cos(root))
            for width in (-half_width, half_width)
        )
        if part == 1:
            low, high = sorted((angle, root))
            # 径方向の稜線は根元で最大となり、円周上の先端へ高さを落とす。
            crest_angles = [
                angle,
                root,
                angle + sign * 2 * depth * 0.025 / half_width,
            ]
            crest_angles.extend(
                index * math.pi / 32
                for index in range(
                    math.floor(low * 32 / math.pi),
                    math.ceil(high * 32 / math.pi) + 1,
                )
                if low < index * math.pi / 32 < high
            )
            for sample in crest_angles:
                radius = 0.5 + half_width * abs(sample - angle) / (2 * depth)
                points.append(
                    (0, radius * math.sin(sample), radius * math.cos(sample))
                )
    expected = tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_apex_keeps_outward_direction_and_axial_width(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for attribute, value in (
        ("shapeArcAngle", 1),
        ("shapePart", True),
        ("shapePartType", 2),
        ("shapePartShape", 1),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    half = math.radians(0.5)
    expected = (
        -0.075,
        0.5 * math.cos(half),
        -0.5 * math.sin(half),
        0.075,
        0.625,
        0.0625,
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("fin_type", (0, 1))
def test_axial_circle_fin_does_not_change_width_or_apex(
    maya_cmds, maya_om, new_scene, fin_type
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="WideArcAxial")
    for attribute, value in (
        ("shapeWideWidth", 0.2),
        ("shapeFin", True),
        ("shapeFinType", fin_type),
        ("shapeFinSize", 2),
        ("shapeFinWidthScale", 3),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.1, -0.5, -0.5, 0.1, 0.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, -0.5, -0.5, 0, 0.5, 0.5)
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0.2)
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 0)
    assert _bounds(maya_om, shape) == pytest.approx((0,) * 6)


@pytest.mark.parametrize("connected", (False, True))
def test_axial_circle_width_updates_cached_geometry(
    maya_cmds, maya_om, new_scene, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="WideArcAxial")
    target = f"{shape}.shapeWideWidth"
    if connected:
        source = maya_cmds.createNode("network")
        maya_cmds.addAttr(
            source, longName="width", attributeType="doubleLinear"
        )
        maya_cmds.connectAttr(f"{source}.width", target)
        target = f"{source}.width"
    for width in (0.2, 0, 0.05):
        maya_cmds.setAttr(target, width)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-width / 2, -0.5, -0.5, width / 2, 0.5, 0.5)
        )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("all_ends", (False, True))
@pytest.mark.parametrize("part", (0, 1, 2))
def test_axial_circle_pointed_part_base_stays_on_the_circle(
    maya_cmds, maya_om, new_scene, filled, all_ends, part
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for name, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartType", int(all_ends)),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    depth = 0.1 * (math.cos(math.pi / 6) if part <= 1 else 1)
    shoulder = 0.05 if part == 1 else 0
    maximum = max(0.5, (0.5 + shoulder) * math.cos(2 * depth))
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.05, 0, -maximum if all_ends else -0.5, 0.05, 0.5, maximum),
        abs=1e-9,
    )
    # 弧長で置いた根元を+Zへ回し、円筒からの膨らみと稜線の高さを確認する。
    maya_cmds.setAttr(f"{shape}.shapeRotateX", math.degrees(2 * depth))
    assert _bounds(maya_om, shape)[5] == pytest.approx(
        0.5 + shoulder, abs=1e-9
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("all_ends", (False, True))
@pytest.mark.parametrize("offset", (0, 0.2))
def test_axial_circle_large_sphere_keeps_its_center_and_radius(
    maya_cmds, maya_om, new_scene, filled, all_ends, offset
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for name, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartShape", PART_SHAPES.index("Sphere")),
        ("shapePartType", int(all_ends)),
        ("shapePartSize", 4),
        ("shapePartOffset", offset),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    radius = 0.2
    assert _bounds(maya_om, shape) == pytest.approx(
        (
            -radius,
            -offset - radius,
            -0.5 - radius if all_ends else -0.5,
            radius,
            0.5,
            0.5 + radius,
        ),
        abs=1e-9,
    )


@pytest.mark.parametrize(
    "part_name",
    (
        "Cube",
        "Octahedron",
        "Sphere",
        "Pyramid",
        "Cone",
    ),
)
@pytest.mark.parametrize("length_scale", (1, 1.5))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_large_part_chord_frame_preserves_anchor_and_dimensions(
    maya_cmds, maya_om, new_scene, part_name, length_scale, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    half_length, half_width = 0.3 * length_scale, 0.3
    band_width = 0.1
    if part_name == "Sphere" and length_scale == 1:
        depth = 0
    elif part_name == "Sphere":
        # 輪郭の頂点を通る断面を選び、円の分割数による近似誤差を避ける。
        band_width = 2 * half_width * math.sin(math.pi / 4)
        depth = half_length * math.cos(math.pi / 4)
    elif part_name == "Octahedron":
        depth = half_length * (1 - band_width / (2 * half_width))
    elif part_name in ("Pyramid", "Cone"):
        depth = 2 * half_length
    else:
        depth = half_length
    for name, value in (
        ("shapeArcAngle", 180),
        ("shapePart", True),
        ("shapePartShape", PART_SHAPES.index(part_name)),
        ("shapePartSize", 6),
        ("shapePartLengthScale", length_scale),
        ("shapeWideWidth", band_width),
        ("shapeRotateX", math.degrees(math.asin(depth))),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    # Aim後の長さ軸を-Yへ揃え、固定した中心・先端と元の寸法を同時に確認する。
    anchor_y = -depth / 2
    anchor_z = math.sqrt(1 - depth * depth) / 2
    # 回転後の円弧も64分割の頂点から描かれ、連続円の極値には一致しない。
    arc_maximum_y = max(
        0.5 * math.sin(index * math.pi / 32 - math.asin(depth))
        for index in range(33)
    )
    pointed = part_name in ("Pyramid", "Cone")
    solid = part_name in ("Cube", "Octahedron", "Sphere", "Pyramid", "Cone")
    actual = _bounds(maya_om, shape)
    assert actual == pytest.approx(
        (
            -half_width,
            anchor_y if pointed else anchor_y - half_length,
            -anchor_z,
            half_width,
            arc_maximum_y,
            anchor_z + half_width if solid else anchor_z,
        ),
        abs=1e-9,
    )


@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_large_part_fallback_and_apex_keep_offset_and_history(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    for part_name in (
        "Cube",
        "Octahedron",
        "Sphere",
        "Pyramid",
        "Cone",
    ):
        _, name = _create_controller(
            maya_cmds, shape_name="WideArcAxial", shape_fill=filled
        )
        for attribute, value in (
            ("shapeArcAngle", 180),
            ("shapePart", True),
            ("shapePartShape", PART_SHAPES.index(part_name)),
            ("shapePartSize", 4),
            ("shapePartOffset", 1),
        ):
            maya_cmds.setAttr(f"{name}.{attribute}", value)
        pointed = part_name in ("Pyramid", "Cone")
        solid = part_name in (
            "Cube",
            "Octahedron",
            "Sphere",
            "Pyramid",
            "Cone",
        )
        # 円弧へ届かないOffsetでは元の接線姿勢と中心・先端位置を維持する。
        fallback = (
            -0.2,
            -1 if pointed else -1.2,
            -0.5,
            0.2,
            0.5,
            0.7 if solid else 0.5,
        )
        assert _bounds(maya_om, name) == pytest.approx(fallback), part_name
        mod = bdu.ModifierManager()
        shape = bdu.Nodes(modifier_manager=mod).existing(name)
        shape.shapePartType.set(2)
        shape.shapePartOffset.set(0.2)
        mod.do_it_dg()
        apex = (-0.2, 0, -0.5, 0.2, 1.1 if pointed else 0.9, 0.5)
        assert _bounds(maya_om, name) == pytest.approx(apex), part_name
        mod.undo_it()
        assert _bounds(maya_om, name) == pytest.approx(fallback), part_name
        mod.redo_it()
        assert _bounds(maya_om, name) == pytest.approx(apex), part_name


@pytest.mark.parametrize("part", (3, 4, 5))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_wrapped_centered_part_uses_arc_length_and_axial_width(
    maya_cmds, maya_om, new_scene, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for name, value in (
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartSize", 6),
        ("shapePartOffset", 1),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    for angle in (90, 180):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        start = math.radians((180 - angle) / 2)
        for length_scale in (1, 1.5):
            maya_cmds.setAttr(f"{shape}.shapePartLengthScale", length_scale)
            front = start - 0.6 * length_scale
            expected = (
                -0.3,
                0.5 * math.sin(front),
                -0.5 * math.cos(start),
                0.3,
                0.5,
                0.5 if front <= 0 else 0.5 * math.cos(front),
            )
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("part", range(6))
@pytest.mark.parametrize("connected", (False, True))
def test_axial_circle_wrapped_part_ignores_offset_but_preserves_its_value(
    maya_cmds, maya_om, new_scene, part, connected
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=True
    )
    for name, value in (
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartSize", 4),
        ("shapeArcAngle", 240),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    target = f"{shape}.shapePartOffset"
    if connected:
        source = maya_cmds.createNode("network")
        maya_cmds.addAttr(
            source, longName="offset", attributeType="doubleLinear"
        )
        maya_cmds.connectAttr(f"{source}.offset", target)
        target = f"{source}.offset"
    for placement in (0, 1):
        maya_cmds.setAttr(f"{shape}.shapePartType", placement)
        baseline = _bounds(maya_om, shape)
        for offset in (0, 0.4, -0.8, 2):
            maya_cmds.setAttr(target, offset)
            assert _bounds(maya_om, shape) == pytest.approx(baseline, abs=1e-9)
            assert maya_cmds.getAttr(
                f"{shape}.shapePartOffset"
            ) == pytest.approx(offset)
    maya_cmds.setAttr(f"{shape}.shapePartType", 2)
    assert _bounds(maya_om, shape) != pytest.approx(baseline)
    assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == pytest.approx(2)


@pytest.mark.parametrize("part", (3, 4, 5))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_planar_apex_preserves_the_circular_body(
    maya_cmds, maya_om, new_scene, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideArcAxial", shape_fill=filled
    )
    for name, value in (
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartType", 2),
        ("shapePartSize", 6),
        ("shapeRotateX", 33.75),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    # Partの投影より外側にある円弧の頂点を、回転して+Zの極値に置く。
    for width in (0, 0.1):
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
        assert _bounds(maya_om, shape)[5] == pytest.approx(0.5, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeRotateX", 0)
    maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    assert _bounds(maya_om, shape)[4] == pytest.approx(1.0, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapePartType", 0)
    assert _bounds(maya_om, shape)[4] == pytest.approx(0.5, abs=1e-9)
    assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == pytest.approx(0.2)


@pytest.mark.parametrize("filled", (False, True))
def test_axial_circle_wrapped_degenerate_and_periodic_parts_stay_bounded(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    for part in range(6):
        _, shape = _create_controller(
            maya_cmds, shape_name="WideArcAxial", shape_fill=filled
        )
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        maya_cmds.setAttr(f"{shape}.shapePartShape", part)
        maya_cmds.setAttr(f"{shape}.shapePartType", 1)
        maya_cmds.setAttr(f"{shape}.shapePartSize", 2)
        for length, width, band_width, angle in (
            (0, 1, 0.05, 180),
            (1, 0, 0, 180),
            (-1, -1, 0.05, 90),
            (50, 1, 0.05, 360),
        ):
            for name, value in (
                ("shapePartLengthScale", length),
                ("shapePartWidthScale", width),
                ("shapeWideWidth", band_width),
                ("shapeArcAngle", angle),
            ):
                maya_cmds.setAttr(f"{shape}.{name}", value)
            bounds = _bounds(maya_om, shape)
            assert all(math.isfinite(value) for value in bounds)
            half_width = max(band_width / 2, 0.1 * abs(width))
            assert (bounds[0], bounds[3]) == pytest.approx(
                (-half_width, half_width), abs=1e-9
            ), (part, length, width)
            radius = 0.5 + (0.1 if part == 1 else 0)
            for index in (1, 2, 4, 5):
                assert abs(bounds[index]) <= radius + 1e-9
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", 0)
        assert _bounds(maya_om, shape) == pytest.approx((0,) * 6)


def test_axial_circle_wrapped_part_is_independent_of_disabled_fin(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    for part in (1, 3):
        _, shape = _create_controller(
            maya_cmds, shape_name="WideArcAxial", shape_fill=True
        )
        for name, value in (
            ("shapePart", True),
            ("shapePartShape", part),
            ("shapePartSize", 6),
            ("shapeArcAngle", 90),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
        baseline = _bounds(maya_om, shape)
        if part == 1:
            assert baseline[4] > 0.5
        else:
            assert baseline[4] == pytest.approx(0.5, abs=1e-9)
        maya_cmds.setAttr(f"{shape}.shapeFin", True)
        assert _bounds(maya_om, shape) == pytest.approx(baseline, abs=1e-9)
        for offset in (-1, 1):
            maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
            assert _bounds(maya_om, shape) == pytest.approx(baseline, abs=1e-9)


@pytest.mark.parametrize(
    "base,cross",
    tuple(
        (base + suffix, cross + suffix)
        for base, cross in (
            ("ArcRadial", "CrossArcRadial"),
            ("ArcAxial", "CrossArcAxial"),
            ("WideArcRadial", "WideCrossArcRadial"),
            ("WideArcAxial", "WideCrossArcAxial"),
        )
        for suffix in ("", "Swapped")
    ),
)
@pytest.mark.parametrize("placement", (0, 1, 2))
@pytest.mark.parametrize("part", (0, 1, 3, 6))
@pytest.mark.parametrize("filled", (False, True))
def test_cross_circle_matches_perpendicular_circle_components(
    maya_cmds, maya_om, new_scene, base, cross, placement, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    shapes = [
        _create_controller(
            maya_cmds,
            name=f"circleComponent{index}",
            shape_name=name,
            shape_fill=filled,
        )[1]
        for index, name in enumerate((cross, base, base))
    ]
    for index, shape in enumerate(shapes):
        for name, value in (
            ("shapePart", index != 2 or placement == 1),
            ("shapePartShape", part),
            ("shapePartType", placement),
            ("shapePartSize", 3),
            ("shapePartOffset", 0.2),
            ("shapeWideWidth", 0.15),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
    maya_cmds.setAttr(f"{shapes[2]}.shapeRotateY", 90)
    join_height = math.sqrt(0.25 - 0.075**2)
    if cross.removesuffix("Swapped") == "WideCrossArcAxial" and placement == 2:
        maya_cmds.setAttr(
            f"{shapes[1]}.shapePartOffset", 0.2 + join_height - 0.5
        )
    for angle in (90, 180, 360):
        for shape in shapes:
            maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        first, second = [_bounds(maya_om, shape) for shape in shapes[1:]]
        expected = tuple(min(first[i], second[i]) for i in range(3)) + tuple(
            max(first[i], second[i]) for i in range(3, 6)
        )
        actual = _bounds(maya_om, shapes[0])
        if cross.removesuffix("Swapped") == "WideCrossArcAxial":
            # 交差部の接合は上下方向だけを変え、各円とPartの横方向寸法を保つ。
            indices = (0, 2, 3, 5)
            assert tuple(actual[i] for i in indices) == pytest.approx(
                tuple(expected[i] for i in indices), abs=1e-8
            )
            if placement == 2:
                assert actual[1] == pytest.approx(
                    -join_height if angle == 360 else expected[1], abs=1e-8
                )
                assert actual[4] == pytest.approx(expected[4], abs=1e-8)
        else:
            assert actual == pytest.approx(expected, abs=1e-8)


@pytest.mark.parametrize("part", range(6))
@pytest.mark.parametrize("placement", (0, 1))
def test_cross_circle_axial_wrapped_offset_is_ignored(
    maya_cmds, maya_om, new_scene, part, placement
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="WideCrossArcAxial")
    for name, value in (
        ("shapePart", True),
        ("shapePartShape", part),
        ("shapePartType", placement),
        ("shapePartSize", 6),
        ("shapeArcAngle", 180),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    baseline = _bounds(maya_om, shape)
    for offset in (-2, 2):
        maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
        assert _bounds(maya_om, shape) == pytest.approx(baseline)
    assert maya_cmds.getAttr(f"{shape}.shapePartOffset") == 2


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("width", (0.2, 0.6))
def test_cross_circle_axial_joined_body_bounds(
    maya_cmds, maya_om, new_scene, filled, width
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideCrossArcAxial", shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
    height = math.sqrt(0.25 - (width / 2) ** 2)
    for angle in (90, 180, 360):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        side = 0.5 * math.sin(math.radians(angle / 2)) if angle < 180 else 0.5
        minimum = (
            -height
            if angle == 360
            else 0.5 * math.cos(math.radians(angle / 2))
        )
        assert _bounds(maya_om, shape) == pytest.approx(
            (-side, minimum, -side, side, height, side), abs=1e-9
        )
    maya_cmds.setAttr(f"{shape}.shapeArcAngle", 0)
    assert _bounds(maya_om, shape) == pytest.approx((0,) * 6)


@pytest.mark.parametrize("filled", (False, True))
def test_cross_circle_axial_join_preserves_short_arcs_and_lower_opening(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideCrossArcAxial", shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0.2)
    for angle in (10, 350):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        side = (
            max(0.1, 0.5 * math.sin(math.radians(angle / 2)))
            if angle < 180
            else 0.5
        )
        maximum = 0.5 if angle == 10 else math.sqrt(0.24)
        assert _bounds(maya_om, shape) == pytest.approx(
            (
                -side,
                0.5 * math.cos(math.radians(angle / 2)),
                -side,
                side,
                maximum,
                side,
            ),
            abs=1e-9,
        )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("width", (0, 1, 1.2))
def test_cross_circle_axial_join_width_fallback_keeps_both_cylinders(
    maya_cmds, maya_om, new_scene, filled, width
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideCrossArcAxial", shape_fill=filled
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
    for angle in (90, 360):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        side = max(width / 2, math.sqrt(0.125) if angle == 90 else 0.5)
        minimum = math.sqrt(0.125) if angle == 90 else -0.5
        assert _bounds(maya_om, shape) == pytest.approx(
            (-side, minimum, -side, side, 0.5, side), abs=1e-9
        )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("part", range(len(PART_SHAPES)))
def test_cross_circle_axial_apex_follows_the_joined_plane(
    maya_cmds, maya_om, new_scene, filled, part
):
    _load_bd_util_nodes(maya_cmds)
    shapes = [
        _create_controller(
            maya_cmds,
            name=f"joinedApex{index}",
            shape_name=name,
            shape_fill=filled,
        )[1]
        for index, name in enumerate(("WideCrossArcAxial", "WideArcAxial"))
    ]
    for shape in shapes:
        for name, value in (
            ("shapePart", True),
            ("shapePartShape", part),
            ("shapePartType", 2),
            ("shapePartSize", 2),
            ("shapeWideWidth", 0.2),
            ("shapeArcAngle", 180),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
    height = math.sqrt(0.24)
    for offset in (0, 0.2):
        maya_cmds.setAttr(f"{shapes[0]}.shapePartOffset", offset)
        maya_cmds.setAttr(
            f"{shapes[1]}.shapePartOffset", offset + height - 0.5
        )
        expected = _bounds(maya_om, shapes[1])
        actual = _bounds(maya_om, shapes[0])
        assert actual == pytest.approx(
            (-0.5, expected[1], expected[2], 0.5, expected[4], expected[5]),
            abs=1e-9,
        )
        assert maya_cmds.getAttr(
            f"{shapes[0]}.shapePartOffset"
        ) == pytest.approx(offset)
    # 交点がそろわない短い円弧では、AtApexも元の円頂部へ戻る。
    for shape in shapes:
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", 10)
        maya_cmds.setAttr(f"{shape}.shapePartOffset", 0.2)
    assert _bounds(maya_om, shapes[0])[4] == pytest.approx(
        _bounds(maya_om, shapes[1])[4], abs=1e-9
    )


@pytest.mark.parametrize("filled", (False, True))
def test_cross_circle_axial_join_updates_from_connected_width_and_history(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name="WideCrossArcAxial", shape_fill=filled
    )
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(source, longName="width", attributeType="doubleLinear")
    maya_cmds.connectAttr(f"{source}.width", f"{shape}.shapeWideWidth")
    for width in (0.2, 0.6, 1, 0):
        maya_cmds.setAttr(f"{source}.width", width)
        height = math.sqrt(0.25 - (width / 2) ** 2) if 0 < width < 1 else 0.5
        assert _bounds(maya_om, shape) == pytest.approx(
            (-0.5, -height, -0.5, 0.5, height, 0.5), abs=1e-9
        )
    maya_cmds.setAttr(f"{source}.width", 0.2)
    before = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{source}.width", 0.6)
    after = _bounds(maya_om, shape)
    maya_cmds.undo()
    assert _bounds(maya_om, shape) == pytest.approx(before, abs=1e-9)
    maya_cmds.redo()
    assert _bounds(maya_om, shape) == pytest.approx(after, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("part", (6, 7, 8))
@pytest.mark.parametrize(
    "size,length_scale,width_scale,placement",
    (
        pytest.param(0.1, 0, 1, 1, id="zero_length_strokes"),
        pytest.param(6, 1, 0.01, 0, id="long_narrow_at_end"),
        pytest.param(6, 1, 1, 1, id="large_solid_at_ends"),
    ),
)
def test_cross_circle_axial_solid_preserves_the_lower_curve_and_part(
    maya_cmds,
    maya_om,
    new_scene,
    filled,
    part,
    size,
    length_scale,
    width_scale,
    placement,
):
    _load_bd_util_nodes(maya_cmds)
    shapes = [
        _create_controller(
            maya_cmds,
            name=f"lowerPoleReference{index}",
            shape_name=name,
            shape_fill=filled,
        )[1]
        for index, name in enumerate(
            ("WideCrossArcAxial", "WideArcAxial", "WideArcAxial")
        )
    ]
    for index, shape in enumerate(shapes):
        for name, value in (
            ("shapeWideWidth", 0.2),
            ("shapeArcAngle", 360),
            ("shapePart", index != 2 or placement == 1),
            ("shapePartShape", part),
            ("shapePartType", placement),
            ("shapePartSize", size),
            ("shapePartLengthScale", length_scale),
            ("shapePartWidthScale", width_scale),
            ("shapePartHeightScale", width_scale),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
    maya_cmds.setAttr(f"{shapes[2]}.shapeRotateY", 90)
    expected_minimum = min(_bounds(maya_om, shape)[1] for shape in shapes[1:])
    actual = _bounds(maya_om, shapes[0])
    assert actual[1] == pytest.approx(expected_minimum, abs=1e-9)
    assert actual[4] == pytest.approx(math.sqrt(0.24), abs=1e-9)
    if length_scale == 0:
        assert expected_minimum == pytest.approx(-0.505, abs=1e-9)

    # 下部の線形Partが範囲を覆い隠さない方向から、残る円筒リムを確認する。
    angle = math.degrees(math.atan2(0.1, 0.5))
    for shape in shapes:
        maya_cmds.setAttr(f"{shape}.shapeRotateZ", angle)
    expected_minimum = min(_bounds(maya_om, shape)[1] for shape in shapes[1:])
    if length_scale == 0 or placement == 0:
        assert expected_minimum == pytest.approx(
            -math.hypot(0.5, 0.1), abs=1e-9
        )
    assert _bounds(maya_om, shapes[0])[1] == pytest.approx(
        expected_minimum, abs=1e-9
    )


PLANAR_CIRCLE_SHAPES = (
    "Circle",
    "WideCircle",
    "CircleSwapped",
    "WideCircleSwapped",
)


@pytest.mark.parametrize("preset", PLANAR_CIRCLE_SHAPES)
def test_planar_circle_angle_input_is_ignored_and_retained(
    maya_cmds, maya_om, new_scene, preset
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=True
    )
    for name, value in (
        ("shapePart", True),
        ("shapePartType", 1),
        ("shapePartShape", 1),
        ("shapePartOffset", 0.1),
        ("shapeFin", True),
        ("shapeFinHeight", 0.3),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    expected = _bounds(maya_om, shape)
    for angle in (0, 180, 270):
        maya_cmds.setAttr(f"{shape}.shapeArcAngle", angle)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
        assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == pytest.approx(
            angle
        )
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="angle", attributeType="doubleAngle", keyable=True
    )
    maya_cmds.connectAttr(f"{source}.angle", f"{shape}.shapeArcAngle")
    for frame, angle in ((1, 0), (10, 240)):
        maya_cmds.setKeyframe(
            source, attribute="angle", time=frame, value=angle
        )
    for frame in (1, 5, 10):
        maya_cmds.currentTime(frame)
        assert _bounds(maya_om, shape) == pytest.approx(expected)
    assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == pytest.approx(240)
    set_preset(maya_cmds, shape, "Arc")
    assert _bounds(maya_om, shape) != pytest.approx(expected)
    maya_cmds.currentTime(1)
    assert _bounds(maya_om, shape) == pytest.approx((0,) * 6)
    assert maya_cmds.isConnected(f"{source}.angle", f"{shape}.shapeArcAngle")


@pytest.mark.parametrize("preset", PLANAR_CIRCLE_SHAPES)
@pytest.mark.parametrize("placement", (0, 1, 2))
@pytest.mark.parametrize("part", (0, 1))
def test_planar_circle_parts_follow_square_directions(
    maya_cmds, maya_om, new_scene, preset, placement, part
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    for name, value in (
        ("shapeWideWidth", 0.2),
        ("shapePart", True),
        ("shapePartType", placement),
        ("shapePartShape", part),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    radius = 0.6 if preset.startswith("Wide") else 0.5
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        for offset in (0, 0.15, -0.05):
            maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
            other = radius + 0.0625 + offset if placement == 1 else radius
            expected = (
                -other,
                0,
                -other,
                radius + 0.125 + offset,
                0.0625 if part == 1 else 0,
                other,
            )
            if preset.endswith("Swapped"):
                expected = (
                    expected[1],
                    expected[0],
                    -expected[5],
                    expected[4],
                    expected[3],
                    -expected[2],
                )
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", ("WideCircle", "WideCircleSwapped"))
@pytest.mark.parametrize("width", (0, 0.2, 1.25))
def test_wide_planar_circle_width_and_fin_use_outer_radius(
    maya_cmds, maya_om, new_scene, preset, width
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(
        maya_cmds, shape_name=preset, shape_fill=True
    )
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
    radius = 0.5 + width * 0.5
    expected = (-radius, 0, -radius, radius, 0, radius)
    if preset.endswith("Swapped"):
        expected = (0, -radius, -radius, 0, radius, radius)
    assert _bounds(maya_om, shape) == pytest.approx(expected)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0.3)
    maya_cmds.setAttr(f"{shape}.shapeFinWidthScale", 1.5)
    expected = (-radius * 1.5, 0, -radius, radius * 1.5, 0.3, radius)
    if preset.endswith("Swapped"):
        expected = (
            expected[1],
            expected[0],
            -expected[5],
            expected[4],
            expected[3],
            -expected[2],
        )
    assert _bounds(maya_om, shape) == pytest.approx(expected)


@pytest.mark.parametrize(
    "preset", ("WideCrossLine3Axis", "ColorWideCrossLine3Axis")
)
@pytest.mark.parametrize("width", (0, 0.2, 1, 1.25))
def test_wide_three_axis_width_preserves_solid_extent(
    maya_cmds, maya_om, new_scene, preset, width
):
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
    extent = max(0.5, width * 0.5)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(
            (-extent,) * 3 + (extent,) * 3
        )
    maya_cmds.setAttr(f"{shape}.shapePartSize", 7)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 4)
    assert _bounds(maya_om, shape) == pytest.approx(
        (-extent,) * 3 + (extent,) * 3
    )


@pytest.mark.parametrize(
    "preset,reference_preset",
    (
        ("WideCrossLine3Axis", "CrossLine3Axis"),
        ("ColorWideCrossLine3Axis", "ColorCrossLine3Axis"),
    ),
)
@pytest.mark.parametrize("fin_type", (0, 1))
def test_wide_three_axis_fin_reaches_the_same_height_as_cross_line(
    maya_cmds, maya_om, new_scene, preset, reference_preset, fin_type
):
    """断面幅をFinの到達高さへ加算せず、正負の高さとSizeを維持する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    _, reference = _create_controller(
        maya_cmds, name="finHeightReference", shape_name=reference_preset
    )
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(source, longName="width", attributeType="doubleLinear")
    maya_cmds.connectAttr(f"{source}.width", f"{shape}.shapeWideWidth")
    for target in (shape, reference):
        maya_cmds.setAttr(f"{target}.shapeFin", True)
        maya_cmds.setAttr(f"{target}.shapeFinType", fin_type)
    for width, height, size in (
        (0, 1, 0.75),
        (0.2, 0.8, 1.5),
        (0.2, -0.8, 1.5),
        (1.25, 0.8, -1.5),
        (1.25, -0.8, -1.5),
        (-0.2, 1, 0.75),
    ):
        maya_cmds.setAttr(f"{source}.width", width)
        for filled in (False, True):
            for target in (shape, reference):
                maya_cmds.setAttr(f"{target}.shapeFinHeight", height)
                maya_cmds.setAttr(f"{target}.shapeFinSize", size)
                maya_cmds.setAttr(f"{target}.shapeFill", filled)
            reach = height * size
            extent = max(0.5, max(0, width) * 0.5)
            actual = _bounds(maya_om, shape)
            expected = _bounds(maya_om, reference)
            reached_side = 4 if reach > 0 else 1
            assert actual[reached_side] == pytest.approx(reach, abs=1e-9)
            assert actual[reached_side] == pytest.approx(
                expected[reached_side], abs=1e-9
            )
            assert (actual[1], actual[4]) == pytest.approx(
                (min(-extent, reach), max(extent, reach)), abs=1e-9
            )


@pytest.mark.parametrize("preset", VARIANT_NAMES)
def test_guide_options_do_not_expand_shape_bounds(
    maya_cmds, maya_om, new_scene, preset
):
    """ガイドの表示とTemplate切替でも本体と付属形状の範囲を保つ。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    for name, value in (
        ("shapePart", True),
        ("shapePartType", 1),
        ("shapePartShape", 1),
        ("shapePartSize", 1.4),
        ("shapePartLengthScale", 1.7),
        ("shapePartWidthScale", 1.3),
        ("shapePartOffset", 0.15),
        ("shapeFin", True),
        ("shapeFinHeight", 0.3),
    ):
        maya_cmds.setAttr(f"{shape}.{name}", value)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
        maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", False)
        expected = _bounds(maya_om, shape)
        for guide, template in ((True, False), (True, True), (False, True)):
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", guide)
            maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", template)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "preset",
    (
        "WideLine",
        "WideCrossLine",
        "WideCrossLineSwapped",
        "WideCrossLine3Axis",
        "ColorWideCrossLine3Axis",
    ),
)
@pytest.mark.parametrize("part_shape", (0, 1, 6))
def test_wide_guides_follow_retracted_body(
    maya_cmds, maya_om, new_scene, preset, part_shape
):
    """内向きPartや幅ゼロでもガイドを短縮後の本体内に収める。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    maya_cmds.setAttr(f"{shape}.shapePartShape", part_shape)
    for width, offset, part_type in (
        (0, -0.4, 0),
        (0.05, -0.4, 0),
        (0.2, -2, 0),
        (0.2, -0.6, 1),
        (1.4, -2, 1),
    ):
        maya_cmds.setAttr(f"{shape}.shapeWideWidth", width)
        maya_cmds.setAttr(f"{shape}.shapePartOffset", offset)
        maya_cmds.setAttr(f"{shape}.shapePartType", part_type)
        for filled in (False, True):
            maya_cmds.setAttr(f"{shape}.shapeFill", filled)
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
            expected = _bounds(maya_om, shape)
            for template in (False, True):
                maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
                maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", template)
                assert _bounds(maya_om, shape) == pytest.approx(
                    expected, abs=1e-9
                )


@pytest.mark.parametrize(
    "preset",
    (
        "WideLine",
        "WideCrossLine",
        "WideCrossLineSwapped",
        "Circle",
        "CircleSwapped",
    ),
)
@pytest.mark.parametrize("part_shape", (0, 1))
def test_arrow_tip_guides_preserve_shape_bounds(
    maya_cmds, maya_om, new_scene, preset, part_shape
):
    """先端へつなぐガイドを、変形した本体とPartの範囲に収める。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=preset)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    maya_cmds.setAttr(f"{shape}.shapePartShape", part_shape)
    maya_cmds.setAttr(f"{shape}.shapePartSize", 1.4)
    maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.2)
    for offset, length, width, part_type in (
        (0.35, 1.7, 0.2, 0),
        (-0.4, 0.5, 0.05, 0),
        (-1.5, 1.4, 0.2, 0),
        (0.2, 1.4, 0, 1),
        (-2, 1.4, 1.4, 1),
    ):
        for name, value in (
            ("shapePartOffset", offset),
            ("shapePartLengthScale", length),
            ("shapeWideWidth", width),
            ("shapePartType", part_type),
        ):
            maya_cmds.setAttr(f"{shape}.{name}", value)
        for filled in (False, True):
            maya_cmds.setAttr(f"{shape}.shapeFill", filled)
            maya_cmds.setAttr(f"{shape}.shapeGuideLine", False)
            expected = _bounds(maya_om, shape)
            for template in (False, True):
                maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
                maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", template)
                assert _bounds(maya_om, shape) == pytest.approx(
                    expected, abs=1e-9
                )


def test_arc_default_draws_a_half_circle_without_case_overrides(
    maya_cmds, maya_om, new_scene
):
    """テスト用の角度指定を通さず、Arcの初期円弧を確認する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name=None)
    set_preset(maya_cmds, shape, "Arc")
    assert maya_cmds.getAttr(f"{shape}.shapeArcAngle") == pytest.approx(180)
    assert _bounds(maya_om, shape) == pytest.approx(
        (0, 0, -0.5, 0.5, 0, 0.5), abs=1e-9
    )


def test_guide_options_preserve_history_and_scene_values(
    maya_cmds, maya_om, new_scene, tmp_path
):
    """ガイドの値を履歴・本体切替・シーン再読込で保持する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape_name = _create_controller(maya_cmds, shape_name="Square")
    expected = _bounds(maya_om, shape_name)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(shape_name)
    shape.shapeGuideLine.set(True)
    shape.shapeGuideLineTemplate.set(True)
    mod.do_it_dg()
    assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLine")
    assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLineTemplate")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected)
    mod.undo_it()
    assert not maya_cmds.getAttr(f"{shape_name}.shapeGuideLine")
    assert not maya_cmds.getAttr(f"{shape_name}.shapeGuideLineTemplate")
    mod.redo_it()
    for preset in ("Line", "Arc", "ColorSphere", "SquareTemplate", "Square"):
        set_preset(maya_cmds, shape_name, preset)
        assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLine")
        assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLineTemplate")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected)
    path = tmp_path / "controller_guide_options.ma"
    maya_cmds.file(rename=str(path))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(path), open=True, force=True)
    assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLine")
    assert maya_cmds.getAttr(f"{shape_name}.shapeGuideLineTemplate")
    assert _bounds(maya_om, shape_name) == pytest.approx(expected)


@pytest.mark.parametrize(
    "attribute", ("shapeGuideLine", "shapeGuideLineTemplate")
)
def test_guide_option_connected_animation_is_retained(
    maya_cmds, maya_om, new_scene, attribute
):
    """対象外でもガイドの接続と明示キーを保持する。"""
    _load_bd_util_nodes(maya_cmds)
    _, shape = _create_controller(maya_cmds, shape_name="Square")
    expected = _bounds(maya_om, shape)
    if attribute == "shapeGuideLineTemplate":
        maya_cmds.setAttr(f"{shape}.shapeGuideLine", True)
    source = maya_cmds.createNode("network")
    maya_cmds.addAttr(
        source, longName="enabled", attributeType="bool", keyable=True
    )
    maya_cmds.connectAttr(f"{source}.enabled", f"{shape}.{attribute}")
    for frame, value in ((1, False), (10, True)):
        maya_cmds.setKeyframe(
            source, attribute="enabled", time=frame, value=value
        )
    for frame, value in ((1, False), (10, True), (1, False), (10, True)):
        maya_cmds.currentTime(frame)
        assert maya_cmds.getAttr(f"{shape}.{attribute}") == value
        assert _bounds(maya_om, shape) == pytest.approx(expected)
    set_preset(maya_cmds, shape, "Line")
    assert maya_cmds.getAttr(f"{shape}.{attribute}")
    assert maya_cmds.isConnected(f"{source}.enabled", f"{shape}.{attribute}")
    set_preset(maya_cmds, shape, "Square")
    assert _bounds(maya_om, shape) == pytest.approx(expected)
