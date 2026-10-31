"""本体の種類から独立した向き・Wide・Template設定を検証する。"""

from __future__ import annotations

import math
from time import perf_counter

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
        maya_cmds.setAttr(f"{shape}.shapeTemplateLineInvert", True)
        maya_cmds.setAttr(f"{shape}.shapePartTemplate", True)
        maya_cmds.setAttr(f"{shape}.shapeFinTemplate", True)
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
    maya_cmds.addAttr(driver, longName="flag", attributeType="bool")
    maya_cmds.setAttr(f"{driver}.flag", True)
    mod = bdu.ModifierManager()
    shape = bdu.Nodes(modifier_manager=mod).existing(name)
    values = {
        "shapeAxisSwap": True,
        "shapeWide": True,
        "shapeTemplateLine": True,
        "shapeTemplateFill": True,
        "shapeTemplateLineInvert": True,
        "shapePartTemplate": True,
        "shapeFinTemplate": True,
    }
    for attribute, value in values.items():
        getattr(shape, attribute).set(value)
    shape.shapeTemplateLineRate.connect_from(f"{driver}.output")
    shape.shapePartHeightScale.connect_from(f"{driver}.output")
    connected_flags = (
        "shapeTemplateLineInvert",
        "shapePartTemplate",
        "shapeFinTemplate",
    )
    for attribute in connected_flags:
        getattr(shape, attribute).connect_from(f"{driver}.flag")
    mod.do_it_dg()
    after = _bounds(maya_om, name)
    assert after != pytest.approx(before)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(before)
    assert not maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapeTemplateLineRate"
    )
    assert not maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapePartHeightScale"
    )
    assert maya_cmds.getAttr(f"{name}.shapePartHeightScale") == 1
    for attribute in values:
        assert not maya_cmds.getAttr(f"{name}.{attribute}")
    for attribute in connected_flags:
        assert not maya_cmds.isConnected(
            f"{driver}.flag", f"{name}.{attribute}"
        )
    mod.redo_it()
    assert _bounds(maya_om, name) == pytest.approx(after)
    for preset in ("Cube", "ArcAxial", "Gear", "Square"):
        maya_cmds.setAttr(f"{name}.shape", SHAPE_NAMES.index(preset))
        for attribute, value in values.items():
            assert maya_cmds.getAttr(f"{name}.{attribute}") == value
        assert maya_cmds.getAttr(
            f"{name}.shapeTemplateLineRate"
        ) == pytest.approx(0.35)
        assert maya_cmds.getAttr(
            f"{name}.shapePartHeightScale"
        ) == pytest.approx(0.35)
    scene = tmp_path / "controller_shape_options.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapeTemplateLineRate"
    )
    assert maya_cmds.isConnected(
        f"{driver}.output", f"{name}.shapePartHeightScale"
    )
    assert maya_cmds.getAttr(f"{name}.shapePartHeightScale") == pytest.approx(
        0.35
    )
    for attribute, value in values.items():
        assert maya_cmds.getAttr(f"{name}.{attribute}") == value
    for attribute in connected_flags:
        assert maya_cmds.isConnected(f"{driver}.flag", f"{name}.{attribute}")
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


@pytest.mark.parametrize("preset", ("Line", "ArcRadial", "ArcAxial"))
@pytest.mark.parametrize("part", (0, 2, 3, 4, 5))
@pytest.mark.parametrize("wide", (False, True))
def test_planar_parts_keep_height_without_changing_geometry(
    maya_cmds, maya_om, new_scene, preset, part, wide
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "planarHeight",
        preset,
        shapeWide=wide,
        shapeFill=True,
        shapePart=True,
        shapePartShape=part,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
    )
    expected = _bounds(maya_om, shape)
    for height in (-3, 0, 0.4, 2):
        maya_cmds.setAttr(f"{shape}.shapePartHeightScale", height)
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
        assert maya_cmds.getAttr(f"{shape}.shapePartHeightScale") == height


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_arrow_body_ignores_part_height_with_its_fin_independent(
    maya_cmds, maya_om, new_scene, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "arrowBodyHeight",
        "Arrow",
        shapeWide=wide,
        shapeFill=filled,
        shapePartLengthScale=1.7,
        shapePartWidthScale=2.1,
        shapeFinHeight=0.8,
    )
    for fin in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFin", fin)
        expected = _bounds(maya_om, shape)
        for height in (-3, 0, 0.4, 2):
            maya_cmds.setAttr(f"{shape}.shapePartHeightScale", height)
            assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("part", range(6, 11))
@pytest.mark.parametrize("height", (-3, 0, 0.4, 2))
@pytest.mark.parametrize("filled", (False, True))
def test_solid_part_length_width_and_height_have_independent_local_axes(
    maya_cmds, maya_om, new_scene, part, height, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "solidHeight",
        "Line",
        shapeFill=filled,
        shapePart=True,
        shapePartShape=part,
        shapePartSize=2,
        shapePartOffset=1,
        shapePartLengthScale=1.3,
        shapePartWidthScale=2.1,
        shapePartHeightScale=height,
    )
    maximum_x = 1.5 if part >= 9 else 1.63
    assert _bounds(maya_om, shape) == pytest.approx(
        (-0.5, -0.1 * abs(height), -0.21, maximum_x, 0.1 * abs(height), 0.21),
        abs=1e-9,
    )
    if height < 0:
        reference = _controller(
            maya_cmds,
            "reflectedSolidHeight",
            "Line",
            shapeFill=filled,
            shapePart=True,
            shapePartShape=part,
            shapePartSize=2,
            shapePartOffset=1,
            shapePartLengthScale=1.3,
            shapePartWidthScale=2.1,
            shapePartHeightScale=-height,
        )
        maya_cmds.setAttr(f"{reference}.shapeAxisScaleY", -1)
        for node in (shape, reference):
            maya_cmds.setAttr(f"{node}.shapeRotate", 17, -29, 23)
        assert _bounds(maya_om, shape) == pytest.approx(
            _bounds(maya_om, reference), abs=1e-9
        )


@pytest.mark.parametrize(
    "preset",
    (
        "Line",
        "Square",
        "Circle",
        "ArcRadial",
        "ArcAxial",
        "CrossArcRadial",
        "CrossArcAxial",
    ),
)
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_zero_arrow3d_height_preserves_the_arrow2d_main_plane(
    maya_cmds, maya_om, new_scene, preset, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeWide=wide,
        shapeFill=filled,
        shapePart=True,
        shapePartSize=1.8,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
        shapePartHeightScale=0,
    )
    actual = _controller(
        maya_cmds, "flatArrow3d", preset, shapePartShape=1, **options
    )
    reference = _controller(
        maya_cmds, "arrow2d", preset, shapePartShape=0, **options
    )
    for swapped in (False, True):
        for placement in (0, 1, 2):
            for node in (actual, reference):
                maya_cmds.setAttr(f"{node}.shapeAxisSwap", swapped)
                maya_cmds.setAttr(f"{node}.shapePartType", placement)
            assert _bounds(maya_om, actual) == pytest.approx(
                _bounds(maya_om, reference), abs=1e-9
            ), (swapped, placement)


@pytest.mark.parametrize("preset", ("Line", "ArcRadial"))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_arrow3d_height_is_signed_and_independent_of_its_main_width(
    maya_cmds, maya_om, new_scene, preset, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "signedArrowHeight",
        preset,
        shapeWide=wide,
        shapeFill=filled,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartSize=2,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
    )
    for height in (-3, 0, 2):
        maya_cmds.setAttr(f"{shape}.shapePartHeightScale", height)
        actual = _bounds(maya_om, shape)
        assert (actual[1], actual[4]) == pytest.approx(
            (min(0, 0.1 * height), max(0, 0.1 * height)), abs=1e-9
        )
        maya_cmds.setAttr(f"{shape}.shapePartWidthScale", -1.7)
        assert _bounds(maya_om, shape) == pytest.approx(actual, abs=1e-9)
        maya_cmds.setAttr(f"{shape}.shapePartWidthScale", 1.7)


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_axial_arrow3d_height_offsets_the_radius_with_its_sign(
    maya_cmds, maya_om, new_scene, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "axialSignedHeight",
        "ArcAxial",
        shapeWide=wide,
        shapeFill=filled,
        shapeArcAngle=60,
        shapePart=True,
        shapePartShape=1,
        shapePartSize=2,
        shapePartLengthScale=1.3,
        shapePartWidthScale=1.7,
    )
    root_angle = math.pi / 3 + 2 * 0.1 * math.cos(math.pi / 6) * 2 * 1.3
    for height in (-3, 0, 2):
        maya_cmds.setAttr(f"{shape}.shapePartHeightScale", height)
        actual = _bounds(maya_om, shape)
        assert (actual[1], actual[4]) == pytest.approx((-0.17, 0.17), abs=1e-9)
        if height:
            index = 0 if height < 0 else 3
            assert actual[index] == pytest.approx(
                (0.5 + 0.1 * height) * math.sin(root_angle), abs=1e-9
            )
        else:
            assert (actual[0], actual[3]) == pytest.approx(
                (0.5 * math.cos(math.pi / 6), 0.5), abs=1e-9
            )


@pytest.mark.parametrize("height", (-2, 0, 0.4, 3))
@pytest.mark.parametrize("filled", (False, True))
def test_octahedron_arrow_height_controls_y_and_its_fin_section(
    maya_cmds, maya_om, new_scene, height, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "octahedronBodyHeight",
        "OctahedronArrow",
        shapeFill=filled,
        shapePartSize=1.3,
        shapePartOffset=0.17,
        shapePartLengthScale=1.7,
        shapePartWidthScale=2.1,
        shapePartHeightScale=height,
        shapeGuideLine=True,
        shapeFinHeight=0.6,
    )
    extent_y = 0.65 * abs(height)
    expected = (-0.5, -extent_y, -1.365, 1.275, extent_y, 1.365)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    expected = (*expected[:4], max(extent_y, 0.6), expected[5])
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("filled", (False, True))
def test_wide_gear_recomputes_after_width_change_without_long_stall(
    maya_cmds, maya_om, new_scene, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "responsiveWideGear",
        "Gear",
        shapeWide=True,
        shapeWideWidth=0.05,
        shapeFill=filled,
    )
    started = perf_counter()
    initial = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeWideWidth", 0.051)
    changed = _bounds(maya_om, shape)
    elapsed = perf_counter() - started
    assert initial != pytest.approx(changed, abs=1e-9)
    assert all(math.isfinite(value) for value in changed)
    assert (
        elapsed < 1.0
    ), f"Wide Gearの初回生成と幅変更に{elapsed:.3f}秒かかった"
