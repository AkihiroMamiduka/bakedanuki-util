"""Standardの基準軸と高さ、Taperedの独立した傾斜規約を確認する。"""

import math

import pytest

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_cage_attachments import _set_cage
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya


@pytest.mark.parametrize(
    "preset,base_height",
    (
        ("SquareArrowAxial", 0),
        ("DiamondArrowAxial", 0),
        ("CircleArrowAxial", 0),
        ("ArrowSpatial", 0),
        ("SquareArrowSpatial", 0),
        ("ArrowPlanar", 0),
        ("Cube", 0.5),
        ("Cylinder", 0.5),
    ),
)
@pytest.mark.parametrize("height", (1.0, 0.25, -1.0))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_standard_fin_uses_one_tip_side_height_and_keeps_existing_height_origins(
    maya_cmds, maya_om, new_scene, preset, base_height, height, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "axisAlignedFin",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFinHeight=height,
    )
    body = _bounds(maya_om, shape)
    expected = list(body)
    component = 1 - int(swapped)
    expected[component] = min(body[component], base_height + height)
    expected[component + 3] = max(body[component + 3], base_height + height)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=2e-8)
    for attribute, value in (
        ("shapePartSize", 7),
        ("shapePartOffset", -3),
        ("shapePartLengthScale", 0),
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", value)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=2e-8)
    maya_cmds.setAttr(f"{shape}.shapeFinTemplate", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=2e-8)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    assert _bounds(maya_om, shape) == pytest.approx(body, abs=2e-8)


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_tapered_fin_keeps_the_physical_normal_offset_on_a_sloping_body(
    maya_cmds, maya_om, new_scene, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    height = 1.7
    shape = _controller(
        maya_cmds,
        "taperedSlopingFin",
        "Cube",
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=height,
    )
    attribute = (
        "2ndAxisPlusScale1stAxis" if swapped else "1stAxisPlusScale2ndAxis"
    )
    _set_cage(maya_cmds, shape, attribute, 2)
    offset = height / math.sqrt(5)
    expected = (
        (-1, -0.5 - offset, -0.5, 0.5 + 2 * offset, 0.5, 0.5)
        if swapped
        else (-0.5 - offset, -1, -0.5, 0.5, 0.5 + 2 * offset, 0.5)
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=2e-8)


@pytest.mark.parametrize(
    "preset",
    [name for name in SHAPE_NAMES if "Arc" not in name],
)
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_all_standard_fins_keep_their_main_axis_footprint_after_cage_deformation(
    maya_cmds, maya_om, new_scene, preset, wide, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "standardFinFootprint",
        preset,
        shapeWide=wide,
        shapeAxisSwap=swapped,
        shapeFill=True,
        shapeFinHeight=1.7,
    )
    attribute = (
        "2ndAxisPlusScale1stAxis" if swapped else "1stAxisPlusScale2ndAxis"
    )
    _set_cage(maya_cmds, shape, attribute, 2)
    body = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    actual = _bounds(maya_om, shape)
    axis = int(swapped)
    assert actual[axis] == pytest.approx(body[axis], abs=2e-8)
    assert actual[axis + 3] == pytest.approx(body[axis + 3], abs=2e-8)
    assert actual[2] == pytest.approx(body[2], abs=2e-8)
    assert actual[5] == pytest.approx(body[5], abs=2e-8)
    assert all(math.isfinite(value) for value in actual)


@pytest.mark.parametrize("preset", ("CrossLine3Axis", "ColorCrossLine3Axis"))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_wide_three_axis_standard_fin_measures_height_from_the_center_axis(
    maya_cmds, maya_om, new_scene, preset, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "wideThreeAxisStandardFin",
        preset,
        shapeWide=True,
        shapeWideWidth=0.2,
        shapeAxisSwap=swapped,
        shapeFill=filled,
        shapeFin=True,
        shapeFinHeight=1.7,
    )
    attribute = (
        "2ndAxisPlusScale1stAxis" if swapped else "1stAxisPlusScale2ndAxis"
    )
    _set_cage(maya_cmds, shape, attribute, 2)
    assert _bounds(maya_om, shape)[4 - int(swapped)] == pytest.approx(
        1.7, abs=2e-8
    )
