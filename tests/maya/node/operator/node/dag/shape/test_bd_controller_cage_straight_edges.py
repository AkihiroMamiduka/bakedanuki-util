# coding: utf-8
from __future__ import annotations

import itertools
import math

import pytest

from test_bd_controller_attachment_contract import _controller
from test_bd_controller_cage_geometry import _cage_point, _set_faces
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

LIMITS = ((-0.5, 0.5),) * 3
ANGLES = (17, 31, -23)
FACE_SCALES = (
    {(0, "Plus", 2): 3, (2, "Minus", 0): 0.2},
    {(0, "Minus", 2): 0.1, (2, "Plus", 0): 2.7, (1, "Plus", 2): 1.6},
)
POLYGON_VERTICES = {
    "Triangle": ((0.5, 0, 0), (-0.37, 0, -0.5), (-0.37, 0, 0.5)),
    "Diamond": ((0.5, 0, 0), (0, 0, -0.5), (-0.5, 0, 0), (0, 0, 0.5)),
    "Square": tuple(
        (x, 0, z) for x, z in itertools.product((-0.5, 0.5), repeat=2)
    ),
    "Octahedron": tuple(
        tuple(sign * 0.5 if component == axis else 0 for component in range(3))
        for axis in range(3)
        for sign in (-1, 1)
    ),
}


def _mapped_bounds(maya_om, vertices, scales, swapped):
    rotation = maya_om.MEulerRotation(
        *(math.radians(value) for value in ANGLES)
    ).asQuaternion()
    points = []
    for vertex in vertices:
        point = (vertex[1], vertex[0], -vertex[2]) if swapped else vertex
        points.append(
            maya_om.MVector(*_cage_point(point, scales, LIMITS)).rotateBy(
                rotation
            )
        )
    return tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))


@pytest.mark.parametrize("preset", tuple(POLYGON_VERTICES))
@pytest.mark.parametrize("scales", FACE_SCALES)
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_polygon_bounds_use_only_the_deformed_original_vertices(
    maya_cmds, maya_om, new_scene, preset, scales, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "straightCagePolygon",
        preset,
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shape1stAxis=0,
        shape2ndAxis=2,
    )
    _set_faces(maya_cmds, shape, scales)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *ANGLES)
    assert _bounds(maya_om, shape) == pytest.approx(
        _mapped_bounds(maya_om, POLYGON_VERTICES[preset], scales, swapped),
        abs=1e-8,
    )


@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_cage_circle_preserves_its_original_sixty_four_sample_vertices(
    maya_cmds, maya_om, new_scene, filled, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "sampledCageCircle",
        "Circle",
        shapeFill=filled,
        shapeAxisSwap=swapped,
        shape1stAxis=0,
        shape2ndAxis=2,
    )
    scales = FACE_SCALES[0]
    _set_faces(maya_cmds, shape, scales)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *ANGLES)
    vertices = tuple(
        (
            0.5 * math.cos(2 * math.pi * index / 64),
            0,
            0.5 * math.sin(2 * math.pi * index / 64),
        )
        for index in range(64)
    )
    assert _bounds(maya_om, shape) == pytest.approx(
        _mapped_bounds(maya_om, vertices, scales, swapped), abs=1e-8
    )


@pytest.mark.parametrize(
    "preset", ("Triangle", "Diamond", "Octahedron", "Circle")
)
@pytest.mark.parametrize(
    "rate,inverted", ((0.23, False), (0.71, True), (1, False))
)
@pytest.mark.parametrize("filled", (False, True))
def test_cage_template_boundaries_do_not_change_the_rendered_body_extent(
    maya_cmds, maya_om, new_scene, preset, rate, inverted, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "straightCageTemplate",
        preset,
        shapeFill=filled,
        shape1stAxis=0,
        shape2ndAxis=2,
    )
    _set_faces(maya_cmds, shape, FACE_SCALES[0])
    maya_cmds.setAttr(f"{shape}.shapeRotate", *ANGLES)
    original = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", rate)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLineInvert", inverted)
    maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
    maya_cmds.setAttr(f"{shape}.shapeTemplateFill", filled)
    assert _bounds(maya_om, shape) == pytest.approx(original, abs=1e-8)
