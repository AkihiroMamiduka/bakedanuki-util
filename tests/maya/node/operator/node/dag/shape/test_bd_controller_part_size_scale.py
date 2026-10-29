# coding: utf-8
from __future__ import annotations

import pytest

import bd_util as bdu

from test_bd_controller_attachment_contract import (
    _controller,
    _end_bounds,
    _union_bounds,
)
from test_bd_controller_shape import SHAPE_NAMES, _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

NON_ARC_PART_SHAPES = (
    "Line",
    "WideLine",
    "CrossLine",
    "WideCrossLine",
    "CrossLineSwapped",
    "WideCrossLineSwapped",
    "CrossLine3Axis",
    "WideCrossLine3Axis",
    "Square",
    "SquareTemplate",
    "SquareSwapped",
    "SquareTemplateSwapped",
    "Circle",
    "WideCircle",
    "CircleSwapped",
    "WideCircleSwapped",
    "Cube",
    "Sphere",
    "ColorCrossLine3Axis",
    "ColorWideCrossLine3Axis",
    "ColorSphere",
)
SCALE_PAIRS = (
    (1.0, 0.5),
    (1.0, 1.0),
    (1.7, 0.3),
    (0.4, 1.6),
    (0.0, 1.0),
    (1.0, 0.0),
    (0.0, 0.0),
    (-1.0, -0.5),
)


def _set_scales(cmds, shape, primary, other):
    cmds.setAttr(f"{shape}.shapePartPrimarySizeScale", primary)
    cmds.setAttr(f"{shape}.shapePartOtherSizeScale", other)


def _swap_bounds(bounds):
    return bounds[1], bounds[0], -bounds[5], bounds[4], bounds[3], -bounds[2]


@pytest.mark.parametrize(
    "preset,axes",
    (
        ("Line", (0,)),
        ("SquareTemplate", (0, 2)),
        ("SquareSwapped", (0, 2)),
        ("WideCircle", (0, 2)),
        ("WideCrossLine3Axis", (0, 1, 2)),
        ("ColorSphere", (0, 1, 2)),
        ("ColorWideCrossLine3Axis", (0, 1, 2)),
    ),
)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("filled", (False, True))
def test_directional_scales_match_independently_sized_at_end_parts(
    maya_cmds, maya_om, new_scene, preset, axes, part, filled
):
    _load_bd_util_nodes(maya_cmds)
    size = 1.7
    options = dict(
        shapeFill=filled,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=size,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.8,
        shapePartOffset=0.13,
    )
    actual = _controller(maya_cmds, "allEnds", preset, **options)
    reference = _controller(maya_cmds, "oneEnd", preset, **options)
    maya_cmds.setAttr(f"{actual}.shapePartType", 1)
    swapped = preset.endswith("Swapped")
    maya_cmds.setAttr(f"{reference}.shapePart", False)
    body = _bounds(maya_om, reference)
    if swapped:
        body = _swap_bounds(body)
    for primary, other in SCALE_PAIRS:
        _set_scales(maya_cmds, actual, primary, other)
        boxes = [body]
        if primary != 0:
            maya_cmds.setAttr(f"{reference}.shapePart", True)
            maya_cmds.setAttr(f"{reference}.shapePartSize", size * primary)
            box = _bounds(maya_om, reference)
            boxes.append(_swap_bounds(box) if swapped else box)
        if other != 0:
            maya_cmds.setAttr(f"{reference}.shapePart", True)
            maya_cmds.setAttr(f"{reference}.shapePartSize", size * other)
            box = _bounds(maya_om, reference)
            if swapped:
                box = _swap_bounds(box)
            boxes.extend(
                _end_bounds(box, axis, sign)
                for axis in axes
                for sign in (-1, 1)
                if (axis, sign) != (0, 1)
            )
        expected = _union_bounds(boxes)
        if swapped:
            expected = _swap_bounds(expected)
        assert _bounds(maya_om, actual) == pytest.approx(expected, abs=1e-9), (
            preset,
            part,
            filled,
            primary,
            other,
        )


@pytest.mark.parametrize("preset", NON_ARC_PART_SHAPES)
@pytest.mark.parametrize("filled", (False, True))
def test_zero_directional_scales_restore_the_body_fin_and_guide_bounds(
    maya_cmds, maya_om, new_scene, preset, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "zeroParts",
        preset,
        shapeFill=filled,
        shapePartType=1,
        shapePartSize=2.3,
        shapePartLengthScale=0.8,
        shapePartWidthScale=1.4,
        shapePartOffset=0.22,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.7,
        shapeFinWidthScale=1.3,
        shapeGuideLine=True,
    )
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 5)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 0)
    for part in range(11):
        maya_cmds.setAttr(f"{shape}.shapePartShape", part)
        for template in (False, True):
            maya_cmds.setAttr(f"{shape}.shapeGuideLineTemplate", template)
            maya_cmds.setAttr(f"{shape}.shapePart", False)
            expected = _bounds(maya_om, shape)
            maya_cmds.setAttr(f"{shape}.shapePart", True)
            _set_scales(maya_cmds, shape, 0, 0)
            assert _bounds(maya_om, shape) == pytest.approx(
                expected, abs=1e-9
            ), (preset, part, filled, template)
            assert maya_cmds.getAttr(f"{shape}.shapePart")
    _set_scales(maya_cmds, shape, 1.4, 0.8)
    assert _bounds(maya_om, shape) != pytest.approx(expected)


@pytest.mark.parametrize(
    "preset,placement",
    tuple(
        (preset, placement)
        for preset in SHAPE_NAMES
        for placement in range(3)
        if preset not in NON_ARC_PART_SHAPES or placement != 1
    ),
)
@pytest.mark.parametrize("filled", (False, True))
def test_directional_scales_are_ignored_outside_non_arc_at_ends(
    maya_cmds, maya_om, new_scene, preset, placement, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "ignoredScales",
        preset,
        shapeFill=filled,
        shapePart=True,
        shapePartType=placement,
        shapePartSize=2.1,
        shapePartOffset=0.13,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.8,
    )
    for part in (1, 6):
        maya_cmds.setAttr(f"{shape}.shapePartShape", part)
        _set_scales(maya_cmds, shape, 1, 0.5)
        expected = _bounds(maya_om, shape)
        for primary, other in ((0, 0), (2.1, 0.17), (-1, 0.9)):
            _set_scales(maya_cmds, shape, primary, other)
            assert _bounds(maya_om, shape) == pytest.approx(
                expected, abs=1e-9
            ), (preset, placement, part, primary, other)
            assert (
                maya_cmds.getAttr(f"{shape}.shapePartPrimarySizeScale")
                == primary
            )
            assert (
                maya_cmds.getAttr(f"{shape}.shapePartOtherSizeScale") == other
            )


@pytest.mark.parametrize(
    "preset", ("SquareSwapped", "ColorSphere", "WideCrossLine3Axis")
)
def test_size_scale_api_undo_connections_animation_and_scene_reload(
    maya_cmds, maya_om, new_scene, tmp_path, preset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "animatedScales",
        preset,
        shapeFill=True,
        shapePart=True,
        shapePartType=1,
        shapePartShape=6,
        shapePartSize=2,
        shapePartOffset=0.11,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.7,
    )
    maya_cmds.setAttr(f"{shape}.shape1stAxis", 5)
    maya_cmds.setAttr(f"{shape}.shape2ndAxis", 0)
    mod = bdu.ModifierManager()
    bd_nodes = bdu.Nodes(modifier_manager=mod)
    node = bd_nodes.existing(shape)
    default_bounds = _bounds(maya_om, shape)
    node.shapePartPrimarySizeScale.set(1.4)
    node.shapePartOtherSizeScale.set(0.2)
    mod.do_it_dg()
    changed_bounds = _bounds(maya_om, shape)
    assert changed_bounds != pytest.approx(default_bounds)
    mod.undo_it()
    assert _bounds(maya_om, shape) == pytest.approx(default_bounds)
    mod.redo_it()
    assert _bounds(maya_om, shape) == pytest.approx(changed_bounds)
    driver = maya_cmds.createNode("network", name="scaleDriver")
    for attr in ("primary", "other"):
        maya_cmds.addAttr(
            driver, longName=attr, attributeType="double", keyable=True
        )
    node.shapePartPrimarySizeScale.connect_from(f"{driver}.primary")
    node.shapePartOtherSizeScale.connect_from(f"{driver}.other")
    mod.do_it_dg()
    values = ((1.4, 0.2), (0, 1), (0, 0), (1, 0), (0.8, 1.6))
    for time, (primary, other) in enumerate(values, 1):
        maya_cmds.setKeyframe(f"{driver}.primary", time=time, value=primary)
        maya_cmds.setKeyframe(f"{driver}.other", time=time, value=other)
    expected = []
    for time in range(1, len(values) + 1):
        maya_cmds.currentTime(time)
        expected.append(_bounds(maya_om, shape))
    assert len(set(expected)) == len(values)
    scene = tmp_path / "part_size_scales.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    for time, box in enumerate(expected, 1):
        maya_cmds.currentTime(time)
        assert _bounds(maya_om, shape) == pytest.approx(box, abs=1e-9)
    assert maya_cmds.isConnected(
        f"{driver}.primary", f"{shape}.shapePartPrimarySizeScale"
    )
    assert maya_cmds.isConnected(
        f"{driver}.other", f"{shape}.shapePartOtherSizeScale"
    )
