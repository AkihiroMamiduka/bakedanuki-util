"""本体の種類から独立した向き・Wide・Template設定を検証する。"""

from __future__ import annotations

import math

import pytest

import bd_util as bdu

from controller_shape_cases import SHAPE_NAMES
from test_bd_controller_attachment_contract import _controller
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya


@pytest.mark.parametrize("preset", SHAPE_NAMES)
@pytest.mark.parametrize("wide", (False, True))
def test_axis_swap_matches_exchanging_the_selected_basis(
    maya_cmds, maya_om, new_scene, preset, wide
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeWide=wide,
        shapeFill=True,
        shapePart=True,
        shapePartShape=1,
        shapePartSize=2.1,
        shapePartOffset=0.17,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=0.9,
    )
    swapped = _controller(maya_cmds, "swapped", preset, **options)
    reference = _controller(maya_cmds, "reference", preset, **options)
    maya_cmds.setAttr(f"{swapped}.shapeAxisSwap", True)
    maya_cmds.setAttr(f"{reference}.shape1stAxis", 2)
    maya_cmds.setAttr(f"{reference}.shape2ndAxis", 0)
    for shape in (swapped, reference):
        maya_cmds.setAttr(f"{shape}.shapeScale", 1.2, 0.7, 1.4)
        maya_cmds.setAttr(f"{shape}.shapeRotate", 13, -29, 23)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", 0.2, -0.3, 0.1)
    assert _bounds(maya_om, swapped) == pytest.approx(
        _bounds(maya_om, reference), abs=1e-8
    )


@pytest.mark.parametrize("preset", SHAPE_NAMES)
@pytest.mark.parametrize("wide", (False, True))
def test_template_options_preserve_geometry_bounds(
    maya_cmds, maya_om, new_scene, preset, wide
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "template",
        preset,
        shapeWide=wide,
        shapeFill=True,
        shapePart=True,
        shapePartShape=6,
        shapePartSize=2.3,
        shapeFin=True,
        shapeFinHeight=0.9,
    )
    expected = _bounds(maya_om, shape)
    for rate in (0.0, 0.35, 0.7, 1.0):
        maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
        maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", rate)
        maya_cmds.setAttr(f"{shape}.shapeTemplateFill", True)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


def test_shape_options_keep_values_connections_and_history_across_presets(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    name = _controller(maya_cmds, "optionHistory", "Square", shapeFill=True)
    before = _bounds(maya_om, name)
    driver = maya_cmds.createNode(
        "multDoubleLinear", name="templateRateDriver"
    )
    maya_cmds.setAttr(f"{driver}.input1", 0.35)
    maya_cmds.setAttr(f"{driver}.input2", 1)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    values = {
        "shapeAxisSwap": True,
        "shapeWide": True,
        "shapeTemplateLine": True,
        "shapeTemplateFill": True,
    }
    for attribute, value in values.items():
        getattr(shape, attribute).set(value)
    shape.shapeTemplateLineRate.connect_from(f"{driver}.output")
    mod.do_it_dg()
    after = _bounds(maya_om, name)
    assert after != pytest.approx(before)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(before)
    assert not maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapeTemplateLineRate"
    )
    for attribute in values:
        assert not maya_cmds.getAttr(f"{name}.{attribute}")
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(after)
    for preset in ("Cube", "ArcAxial", "Gear", "Square"):
        maya_cmds.setAttr(f"{name}.shape", SHAPE_NAMES.index(preset))
        for attribute, value in values.items():
            assert maya_cmds.getAttr(f"{name}.{attribute}") == value
        assert maya_cmds.getAttr(
            f"{name}.shapeTemplateLineRate"
        ) == pytest.approx(0.35)
    scene = tmp_path / "controller_shape_options.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapeTemplateLineRate"
    )
    for attribute, value in values.items():
        assert maya_cmds.getAttr(f"{name}.{attribute}") == value
    assert _bounds(maya_om, name) == pytest.approx(after)


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize(
    "length,width",
    (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (100, 0.001),
        (-100, 0.001),
        (100, -0.001),
        (-100, -0.001),
    ),
)
def test_wide_arrow_degenerate_and_sharp_profiles_keep_bounded_bands(
    maya_cmds, maya_om, new_scene, filled, length, width
):
    _load_bd_util_nodes(maya_cmds)
    wide_width = 0.05
    options = dict(
        shapeFill=filled,
        shapeWideWidth=wide_width,
        shapePartLengthScale=length,
        shapePartWidthScale=width,
        shapePartOffset=0.17,
    )
    plain = _controller(maya_cmds, "plainArrow", "Arrow", **options)
    wide = _controller(
        maya_cmds, "wideArrow", "Arrow", shapeWide=True, **options
    )
    reference = _bounds(maya_om, plain)
    actual = _bounds(maya_om, wide)
    assert all(math.isfinite(value) for value in actual)
    reach = 4 * wide_width / 2
    for axis in range(3):
        assert (
            reference[axis] - reach - 1e-9
            <= actual[axis]
            <= reference[axis] + 1e-9
        )
        assert (
            reference[axis + 3] - 1e-9
            <= actual[axis + 3]
            <= reference[axis + 3] + reach + 1e-9
        )
    assert actual[1] == pytest.approx(0, abs=1e-9)
    assert actual[4] == pytest.approx(0, abs=1e-9)
    if length == 0:
        assert actual[3] - actual[0] >= 0.9 * wide_width
    if width == 0:
        assert actual[5] - actual[2] >= 0.9 * wide_width


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("offset", (0.37, -0.71))
def test_wide_arrow_collapsed_point_keeps_its_offset_position(
    maya_cmds, maya_om, new_scene, filled, swapped, offset
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "pointArrow",
        "Arrow",
        shapeWide=True,
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shapePartLengthScale=0,
        shapePartWidthScale=0,
        shapePartOffset=offset,
    )
    position = (0, 0.5 + offset, 0) if swapped else (0.5 + offset, 0, 0)
    assert _bounds(maya_om, shape) == pytest.approx(
        (*position, *position), abs=1e-9
    )
