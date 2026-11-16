# coding: utf-8
from __future__ import annotations

import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

CORNER_LIMITS = (
    ((1.0, 5.0), (-3.0, 3.0), (4.0, 5.0)),
    ((1.0, 1.05), (-2.0, 2.0), (4.0, 4.12)),
    ((-0.05, 0.05), (1.0, 1.15), (2.0, 2.2)),
    ((-0.1, 0.1), (-0.1, 0.1), (-0.1, 0.1)),
    ((3.0, 1.0), (2.0, -2.0), (7.0, 4.0)),
    ((1.0, 1.0), (-2.0, 2.0), (4.0, 5.0)),
    ((1.0, 1.0), (2.0, 2.0), (4.0, 5.0)),
    ((1.0, 1.0), (2.0, 2.0), (3.0, 3.0)),
    ((-5e-13, 5e-13), (-1.0, 1.0), (-0.05, 0.05)),
)


@pytest.mark.parametrize("limits", CORNER_LIMITS)
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_color_corner_markers_and_wide_stay_inside_small_or_degenerate_body(
    maya_cmds, maya_om, new_scene, limits, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "clippedCorner",
        "ColorCornerCube",
        shapeFill=filled,
        shapeWide=wide,
        shapeWideWidth=0.3,
    )
    _set_base_space(maya_cmds, shape, limits)
    expected = tuple(min(pair) for pair in limits) + tuple(
        max(pair) for pair in limits
    )
    actual = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in actual)
    assert actual == pytest.approx(expected, abs=1e-9)

    # 本体のTemplate化でも、常時表示するCorner面は本体の端に残る。
    maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", 0.37)
    maya_cmds.setAttr(f"{shape}.shapeTemplateFill", True)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_color_corner_common_transforms_and_animation_keep_the_cube_envelope(
    maya_cmds, maya_om, new_scene, wide, filled
):
    _load_bd_util_nodes(maya_cmds)
    shapes = [
        _controller(
            maya_cmds,
            name,
            preset,
            shapeFill=filled,
            shapeWide=wide,
            shapeWideWidth=0.12,
            shapeSize=1.7,
            shapeRootSize=0.8,
        )
        for name, preset in (
            ("transformedCorner", "ColorCornerCube"),
            ("transformedCube", "Cube"),
        )
    ]
    animation = maya_om.MTransformationMatrix()
    animation.setScale((1.1, 0.7, 1.3), maya_om.MSpace.kTransform)
    animation.setShear((0.2, -0.3, 0.15), maya_om.MSpace.kTransform)
    animation.setTranslation(
        maya_om.MVector(2, -3, 4), maya_om.MSpace.kTransform
    )
    for index, shape in enumerate(shapes):
        _set_base_space(maya_cmds, shape, ((3, 1), (-0.05, 0.05), (7, 4)))
        sign = -1 if index == 0 else 1
        maya_cmds.setAttr(f"{shape}.shapeScale", sign * 1.2, 0.7, sign * 1.5)
        maya_cmds.setAttr(f"{shape}.shapeAxisScale", sign * 0.8, 1.3, 0.6)
        maya_cmds.setAttr(f"{shape}.shapeAxisTranslate", 0.3, -0.2, 0.4)
        maya_cmds.setAttr(f"{shape}.shapeTranslate", -0.7, 0.9, -0.5)
        maya_cmds.setAttr(
            f"{shape}.shapeAnimationTransformMatrix",
            *list(animation.asMatrix()),
            type="matrix",
        )
    assert _bounds(maya_om, shapes[0]) == pytest.approx(
        _bounds(maya_om, shapes[1]), abs=1e-9
    )


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("fin_type", (0, 1))
def test_color_corner_keeps_fixed_xyz_body_and_fin_placement_after_clipping(
    maya_cmds, maya_om, new_scene, wide, fin_type
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(
        shapeFill=True,
        shapeWide=wide,
        shapeWideWidth=0.12,
        shapeFin=True,
        shapeFinType=fin_type,
        shapeFinHeight=0.84,
        shapeFinWidthScale=0.96,
    )
    corner = _controller(maya_cmds, "cornerFin", "ColorCornerCube", **options)
    reference = _controller(maya_cmds, "cubeFin", "ColorCube", **options)
    for shape in (corner, reference):
        _set_base_space(maya_cmds, shape, ((1, 3), (2, 2.1), (4, 7)))
    for first, second in ((0, 2), (2, 0), (5, 1), (3, 4)):
        for shape in (corner, reference):
            maya_cmds.setAttr(f"{shape}.shape1stAxis", first)
            maya_cmds.setAttr(f"{shape}.shape2ndAxis", second)
        maya_cmds.setAttr(f"{corner}.shapeRotate", 17, -29, 43)
        maya_cmds.setAttr(f"{corner}.shapeAxisRotate", -31, 13, 23)
        assert _bounds(maya_om, corner) == pytest.approx(
            _bounds(maya_om, reference), abs=1e-9
        )
