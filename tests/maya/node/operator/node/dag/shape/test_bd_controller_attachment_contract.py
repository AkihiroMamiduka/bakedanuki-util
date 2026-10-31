# coding: utf-8
from __future__ import annotations

import itertools

import pytest

from controller_shape_cases import set_preset

from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

COLOR_PAIRS = (
    ("ColorCrossLine3Axis", "CrossLine3Axis"),
    ("ColorWideCrossLine3Axis", "WideCrossLine3Axis"),
    ("ColorCube", "Cube"),
    ("ColorCornerCube", "Cube"),
    ("ColorSphere", "Sphere"),
)
COLOR_PART_PAIRS = (COLOR_PAIRS[0], COLOR_PAIRS[1], COLOR_PAIRS[4])
AXIS_PAIRS = tuple(itertools.product(range(6), repeat=2))
PART_AXIS_PAIRS = ((0, 2), (2, 0), (5, 1), (3, 4), (4, 5))


def _controller(cmds, name, preset, **values):
    transform = cmds.createNode("transform", name=name)
    shape = cmds.createNode(
        "bdControllerShape", parent=transform, name=f"{name}Shape"
    )
    set_preset(cmds, shape, preset)
    cmds.setAttr(f"{shape}.boundsMode", 0)
    for attribute, value in values.items():
        cmds.setAttr(f"{shape}.{attribute}", value)
    return shape


def _set_axes(cmds, shape, first, second):
    cmds.setAttr(f"{shape}.shape1stAxis", first)
    cmds.setAttr(f"{shape}.shape2ndAxis", second)


def _union_bounds(bounds):
    return tuple(min(box[i] for box in bounds) for i in range(3)) + tuple(
        max(box[i + 3] for box in bounds) for i in range(3)
    )


def _end_bounds(bounds, axis, sign):
    # 各端の主面と立ち上がりを保つ、右手系の90度単位の回転。
    first = [0, 0, 0]
    first[axis] = sign
    second = [0, 0, 0]
    second[0 if axis == 1 else 1] = 1
    third = (
        first[1] * second[2] - first[2] * second[1],
        first[2] * second[0] - first[0] * second[2],
        first[0] * second[1] - first[1] * second[0],
    )
    points = [
        tuple(first[i] * x + second[i] * y + third[i] * z for i in range(3))
        for x in (bounds[0], bounds[3])
        for y in (bounds[1], bounds[4])
        for z in (bounds[2], bounds[5])
    ]
    return tuple(min(p[i] for p in points) for i in range(3)) + tuple(
        max(p[i] for p in points) for i in range(3)
    )


@pytest.mark.parametrize("preset,plain", COLOR_PAIRS)
@pytest.mark.parametrize("filled", (False, True))
def test_color_body_keeps_fixed_axes_without_attachments(
    maya_cmds, maya_om, new_scene, preset, plain, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(maya_cmds, "colorBody", preset, shapeFill=filled)
    maya_cmds.setAttr(f"{shape}.shapeScale", 1.3, 0.7, 1.1)
    maya_cmds.setAttr(f"{shape}.shapeAxisScale", 0.8, 1.2, 1.5)
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslate", 0.13, -0.21, 0.09)
    expected = _bounds(maya_om, shape)
    for first, second in AXIS_PAIRS:
        _set_axes(maya_cmds, shape, first, second)
        maya_cmds.setAttr(f"{shape}.shapeRotate", 17, -29, 43)
        maya_cmds.setAttr(f"{shape}.shapeAxisRotate", -31, 13, 23)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(f"{shape}.shape1stAxis") == first
        assert maya_cmds.getAttr(f"{shape}.shape2ndAxis") == second


@pytest.mark.parametrize("preset,plain", COLOR_PART_PAIRS)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_color_parts_follow_selected_axes_like_the_plain_body(
    maya_cmds, maya_om, new_scene, preset, plain, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=filled,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=2.1,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
        shapePartHeightScale=-0.8,
        shapePartOffset=0.13,
    )
    color = _controller(maya_cmds, "colorPart", preset, **options)
    reference = _controller(maya_cmds, "plainPart", plain, **options)
    for shape in (color, reference):
        maya_cmds.setAttr(f"{shape}.shapeScale", 1.2, 0.7, 1.5)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 0.1, -0.2, 0.3)
    # Colorの回転制約は、付属形状にも従来どおり適用する。
    maya_cmds.setAttr(f"{color}.shapeRotate", 19, -13, 31)
    maya_cmds.setAttr(f"{color}.shapeAxisRotate", -17, 29, 11)
    for first, second in PART_AXIS_PAIRS:
        for placement in range(3):
            for shape in (color, reference):
                _set_axes(maya_cmds, shape, first, second)
                maya_cmds.setAttr(f"{shape}.shapePartType", placement)
            assert _bounds(maya_om, color) == pytest.approx(
                _bounds(maya_om, reference), abs=1e-9
            ), (preset, part, placement, first, second)


@pytest.mark.parametrize("preset,plain", COLOR_PAIRS)
@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("filled", (False, True))
def test_color_fin_follows_selected_axes_with_its_body_fixed(
    maya_cmds, maya_om, new_scene, preset, plain, fin_type, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=filled,
        shapeFin=True,
        shapeFinType=fin_type,
        shapeFinHeight=0.9,
        shapeFinSize=1.3,
        shapeFinWidthScale=1.2,
    )
    color = _controller(maya_cmds, "colorFin", preset, **options)
    reference = _controller(maya_cmds, "plainFin", plain, **options)
    for first, second in AXIS_PAIRS:
        for shape in (color, reference):
            _set_axes(maya_cmds, shape, first, second)
        assert _bounds(maya_om, color) == pytest.approx(
            _bounds(maya_om, reference), abs=1e-9
        ), (preset, fin_type, first, second)


@pytest.mark.parametrize("preset,plain", COLOR_PAIRS)
@pytest.mark.parametrize("filled", (False, True))
def test_color_attachments_keep_fixed_xyz_transform_and_offset_meanings(
    maya_cmds, maya_om, new_scene, preset, plain, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "colorTransform",
        preset,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartSize=2.3,
        shapePartOffset=0.17,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.9,
    )
    _set_axes(maya_cmds, shape, 2, 4)
    baseline = _bounds(maya_om, shape)
    size, root = 1.3, 1.1
    axis_scale = (0.8, 1.2, 1.5)
    scale = (1.1, 0.7, 1.2)
    axis_translate = (0.13, -0.21, 0.09)
    translate = (0.1, 0.2, -0.3)
    maya_cmds.setAttr(f"{shape}.shapeSize", -size)
    maya_cmds.setAttr(f"{shape}.shapeRootSize", -root)
    maya_cmds.setAttr(f"{shape}.shapeScale", -scale[0], scale[1], -scale[2])
    maya_cmds.setAttr(
        f"{shape}.shapeAxisScale",
        -axis_scale[0],
        axis_scale[1],
        -axis_scale[2],
    )
    maya_cmds.setAttr(f"{shape}.shapeAxisTranslate", *axis_translate)
    maya_cmds.setAttr(f"{shape}.shapeTranslate", *translate)
    maya_cmds.setAttr(f"{shape}.shapeRotate", 17, -29, 43)
    maya_cmds.setAttr(f"{shape}.shapeAxisRotate", -31, 13, 23)
    maya_cmds.setAttr(f"{shape}.shapeAxisOffset", True)
    for direction in range(6):
        axis, negative = divmod(direction, 2)
        maya_cmds.setAttr(f"{shape}.shapeAxisOffsetDirection", direction)
        for length in (0.7, 2.3):
            maya_cmds.setAttr(f"{shape}.shapeAxisOffsetLength", length)
            expected = []
            for index in range(6):
                component = index % 3
                local = (
                    baseline[index] * size * axis_scale[component]
                    + axis_translate[component]
                )
                if component == axis:
                    local = (local + (-0.5 if negative else 0.5)) * length
                expected.append(
                    root * (translate[component] + local * scale[component])
                )
            assert _bounds(maya_om, shape) == pytest.approx(
                expected, abs=1e-9
            ), (preset, direction, length)


@pytest.mark.parametrize(
    "preset,axes",
    (
        ("Line", (0,)),
        ("Square", (0, 2)),
        ("SquareTemplate", (0, 2)),
        ("Circle", (0, 2)),
        ("WideCircle", (0, 2)),
        ("CrossLine3Axis", (0, 1, 2)),
        ("WideCrossLine3Axis", (0, 1, 2)),
        ("Cube", (0, 1, 2)),
        ("Sphere", (0, 1, 2)),
    ),
)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_at_ends_matches_one_standard_and_other_half_size_at_end_parts(
    maya_cmds, maya_om, new_scene, preset, axes, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=filled,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=1.7,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.8,
        shapePartHeightScale=1.8,
        shapePartOffset=0.13,
    )
    actual = _controller(maya_cmds, "allEnds", preset, **options)
    reference = _controller(maya_cmds, "oneEnd", preset, **options)
    maya_cmds.setAttr(f"{actual}.shapePartType", 1)
    representative = _bounds(maya_om, reference)
    maya_cmds.setAttr(f"{reference}.shapePartSize", 0.85)
    half_size = _bounds(maya_om, reference)
    expected = _union_bounds(
        [representative]
        + [
            _end_bounds(half_size, axis, sign)
            for axis in axes
            for sign in (-1, 1)
            if (axis, sign) != (0, 1)
        ]
    )
    assert _bounds(maya_om, actual) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{actual}.shapePartType", 2)
    assert _bounds(maya_om, actual) == pytest.approx(representative, abs=1e-9)


def test_color_attachment_axis_connections_update_and_survive_reload(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=True,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartSize=2,
        shapePartOffset=0.11,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.9,
    )
    color = _controller(maya_cmds, "colorAnimated", "ColorSphere", **options)
    reference = _controller(maya_cmds, "plainAnimated", "Sphere", **options)
    driver = maya_cmds.createNode("network", name="axisDriver")
    for attr, target in (
        ("first", "shape1stAxis"),
        ("second", "shape2ndAxis"),
    ):
        maya_cmds.addAttr(
            driver, longName=attr, attributeType="long", keyable=True
        )
        for shape in (color, reference):
            maya_cmds.connectAttr(f"{driver}.{attr}", f"{shape}.{target}")
    for time, first, second in ((1, 0, 2), (2, 5, 0), (3, 2, 1)):
        maya_cmds.setKeyframe(f"{driver}.first", time=time, value=first)
        maya_cmds.setKeyframe(f"{driver}.second", time=time, value=second)
    expected = []
    for time in (1, 2, 3):
        maya_cmds.currentTime(time)
        box = _bounds(maya_om, color)
        assert box == pytest.approx(_bounds(maya_om, reference), abs=1e-9)
        expected.append(box)
    assert len(set(expected)) == 3
    scene = tmp_path / "color_attachment_axes.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    for time, box in enumerate(expected, 1):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, color) == pytest.approx(box, abs=1e-9)
