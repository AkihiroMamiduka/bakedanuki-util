# coding: utf-8
from __future__ import annotations

import math

import pytest

import bd_util as bdu

from test_bd_controller_attachment_contract import _controller, _union_bounds
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_cage_geometry import _set_faces
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

NEW_ARROWS = (
    "DiamondArrowPlanar",
    "DiamondArrowSpatial",
    "SquareArrowSpatial",
    "CircleArrowSpatial",
)
MAIN_LIMITS = ((-0.5, 0.5), (-1, 3), (2, -1), (0.2, 0.4), (0.2, 0.2))
TRANSVERSE_SPANS = ((1, 1), (2, 0.5), (-2, 0.5), (0, 2), (0, 0))


def _limits(main, swapped, transverse=(1, 1)):
    axis = int(swapped)
    values = [(-0.5, 0.5), (-0.5, 0.5), (-0.5, 0.5)]
    values[axis] = main
    for other, span in zip((1 - axis, 2), transverse):
        values[other] = (0.3 - span / 2, 0.3 + span / 2)
    return values


def _diamond_vertices(limits, swapped):
    axis = int(swapped)
    minus, plus = limits[axis]
    direction = 1 if plus >= minus else -1
    radius = abs(limits[2][1] - limits[2][0]) / 2
    center = [(low + high) / 2 for low, high in limits]
    result = []
    for longitudinal, lateral in (
        (minus + direction * max(abs(plus - minus), radius), center[2]),
        (minus - direction * radius, center[2]),
        (minus, limits[2][0]),
        (minus, limits[2][1]),
    ):
        point = center.copy()
        point[axis], point[2] = longitudinal, lateral
        result.append(point)
    return result


def _solid_frame(limits, swapped):
    axis = int(swapped)
    minus, plus = limits[axis]
    direction = 1 if plus >= minus else -1
    radii = [abs(high - low) / 2 for low, high in limits]
    radius = (radii[1 - axis] + radii[2]) / 2
    radii[axis] = radius
    center = [(low + high) / 2 for low, high in limits]
    center[axis] = minus
    tip = center.copy()
    tip[axis] = minus + direction * max(radius, abs(plus - minus))
    return center, radii, tip, direction


def _point_bounds(points):
    return tuple(
        min(point[axis] for point in points) for axis in range(3)
    ) + tuple(max(point[axis] for point in points) for axis in range(3))


def _rotation(om, angles):
    return om.MEulerRotation(
        *(math.radians(value) for value in angles)
    ).asMatrix()


def _solid_support_bounds(om, preset, limits, swapped, angles, main_scale=1):
    axis = int(swapped)
    center, radii, tip, _ = _solid_frame(limits, swapped)
    pivot = (
        center[axis]
        - _solid_frame(limits, swapped)[3] * radii[axis]
        + tip[axis]
    ) / 2
    center[axis] = pivot + (center[axis] - pivot) * main_scale
    tip[axis] = pivot + (tip[axis] - pivot) * main_scale
    radii[axis] *= abs(main_scale)
    rotation = _rotation(om, angles)
    rotated_center = om.MPoint(*center) * rotation
    rotated_tip = om.MPoint(*tip) * rotation
    directions = [
        om.MVector(*(int(component == index) for component in range(3)))
        * rotation
        for index in range(3)
    ]
    extent = []
    for component in range(3):
        values = [
            abs(radii[index] * directions[index][component])
            for index in range(3)
        ]
        extent.append(
            sum(values)
            if preset == "SquareArrowSpatial"
            else math.sqrt(sum(value**2 for value in values))
        )
    return tuple(
        min(rotated_center[axis] - extent[axis], rotated_tip[axis])
        for axis in range(3)
    ) + tuple(
        max(rotated_center[axis] + extent[axis], rotated_tip[axis])
        for axis in range(3)
    )


def _body_bounds(preset, limits, swapped):
    if preset == "DiamondArrowPlanar":
        return _point_bounds(_diamond_vertices(limits, swapped))
    center, radii, tip, _ = _solid_frame(limits, swapped)
    return tuple(
        min(center[axis] - radii[axis], tip[axis]) for axis in range(3)
    ) + tuple(max(center[axis] + radii[axis], tip[axis]) for axis in range(3))


def _sites(preset, limits, swapped):
    axis = int(swapped)
    if preset == "DiamondArrowPlanar":
        points = _diamond_vertices(limits, swapped)
        sign = 1 if limits[axis][1] >= limits[axis][0] else -1
        vectors = ((axis, sign), (axis, -sign), (2, -1), (2, 1))
    else:
        center, radii, tip, sign = _solid_frame(limits, swapped)
        points = [tip]
        vectors = [(axis, sign)]
        for component, direction in (
            (axis, -sign),
            (1 - axis, 1),
            (1 - axis, -1),
            (2, 1),
            (2, -1),
        ):
            point = center.copy()
            point[component] += direction * radii[component]
            points.append(point)
            vectors.append((component, direction))
    return tuple(
        (
            point,
            tuple(sign if component == axis else 0 for component in range(3)),
        )
        for point, (axis, sign) in zip(points, vectors)
    )


def _base_radii(preset, limits, swapped):
    axis = int(swapped)
    radii = [
        abs(limits[component][1] - limits[component][0]) / 2
        for component in (1 - axis, 2)
    ]
    if preset == "DiamondArrowPlanar":
        return radii[1], radii[1]
    return sum(radii) / 2, sum(radii) / 2


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
def test_centered_arrow_zero_transverse_radii_keep_reversed_main_part_direction(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "reversedCollapsedArrowPart",
        preset,
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartOffset=2,
    )
    limits = _limits((1, -1), swapped, (0, 0))
    _set_base_space(maya_cmds, shape, limits)
    expected_part = tuple(
        -3.05 if component == axis else 0.25 for component in range(3)
    ) + tuple(-2.95 if component == axis else 0.35 for component in range(3))
    expected = _union_bounds(
        [_body_bounds(preset, limits, swapped), expected_part]
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((-0.2, 2), (1, -1), (0.2, 0.3)))
@pytest.mark.parametrize(
    "minus_scales,plus_scales",
    (
        ((1, 1), (1, 1)),
        ((2, 0.5), (1, 1)),
        ((1, 1), (0.4, 1.6)),
        ((-2, -0.5), (-0.4, -1.6)),
        ((0, 0), (1, 1)),
        ((1, 1), (0, 0)),
    ),
)
def test_centered_arrow_main_face_scales_deform_cage_without_changing_axial_radius(
    maya_cmds,
    maya_om,
    new_scene,
    preset,
    swapped,
    main,
    minus_scales,
    plus_scales,
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "declaredArrowRadii",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits(main, swapped, (1.4, 0.6))
    _set_base_space(maya_cmds, shape, limits)
    _set_faces(
        maya_cmds,
        shape,
        {
            (axis, side, component): value
            for side, scales in (
                ("Minus", minus_scales),
                ("Plus", plus_scales),
            )
            for component, value in zip((1 - axis, 2), scales)
        },
    )
    rear_radius, front_radius = _base_radii(preset, limits, swapped)
    minus, plus = main
    direction = 1 if plus >= minus else -1
    rear = minus - direction * rear_radius
    front = minus + direction * max(abs(plus - minus), front_radius)
    actual = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in actual)
    assert (actual[axis], actual[axis + 3]) == pytest.approx(
        (min(rear, front), max(rear, front)), abs=1e-9
    )
    for attribute in (
        "shapeGuideLine",
        "shapeTemplateLine",
        "shapeTemplateFill",
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", True)
        assert _bounds(maya_om, shape) == pytest.approx(actual, abs=1e-9)


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
@pytest.mark.parametrize("main", MAIN_LIMITS)
def test_diamond_arrow_keeps_four_vertices_and_the_declared_shoulder_center(
    maya_cmds, maya_om, new_scene, swapped, filled, main
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "fixedDiamondRear",
        "DiamondArrowPlanar",
        shapeAxisSwap=swapped,
        shapeFill=filled,
    )
    limits = _limits(main, swapped, (1.4, 1.8))
    _set_base_space(maya_cmds, shape, limits)
    points = _diamond_vertices(limits, swapped)
    assert _bounds(maya_om, shape) == pytest.approx(
        _point_bounds(points), abs=1e-9
    )
    # 斜め姿勢では肩中心と横径由来の後端もboundsに現れる。
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    rotation = _rotation(maya_om, angles)
    posed = [maya_om.MPoint(*point) * rotation for point in points]
    assert _bounds(maya_om, shape) == pytest.approx(
        _point_bounds(posed), abs=1e-9
    )


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", MAIN_LIMITS)
@pytest.mark.parametrize("transverse", TRANSVERSE_SPANS)
def test_solid_arrow_keeps_the_whole_body_and_extends_only_past_its_front(
    maya_cmds, maya_om, new_scene, preset, swapped, main, transverse
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "solidArrowBody", preset, shapeAxisSwap=swapped
    )
    limits = _limits(main, swapped, transverse)
    _set_base_space(maya_cmds, shape, limits)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(
            _body_bounds(preset, limits, swapped), abs=1e-9
        )


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((0.2, 0.4), (-1, 3), (2, -1)))
@pytest.mark.parametrize("transverse", ((1, 1), (2, 0.5)))
def test_solid_arrow_rotated_support_is_the_convex_hull_of_body_and_tip(
    maya_cmds, maya_om, new_scene, preset, swapped, main, transverse
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "solidArrowSupport",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits(main, swapped, transverse)
    _set_base_space(maya_cmds, shape, limits)
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    expected = _solid_support_bounds(maya_om, preset, limits, swapped, angles)
    assert _bounds(maya_om, shape) == pytest.approx(
        expected, abs=1e-9 if preset == "SquareArrowSpatial" else 0.008
    )


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("wide", (False, True))
def test_short_solid_arrow_matches_its_complete_box_or_sphere_and_crosses_threshold_continuously(
    maya_cmds, maya_om, new_scene, preset, swapped, wide
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(shapeAxisSwap=swapped, shapeWide=wide, shapeWideWidth=0.08)
    shape = _controller(maya_cmds, "shortSolidArrow", preset, **options)
    reference = _controller(
        maya_cmds,
        "wholeSolidBody",
        {"SquareArrowSpatial": "Cube", "CircleArrowSpatial": "Sphere"}[preset],
        **options,
    )
    limits = _limits((0.2, 0.4), swapped)
    _set_base_space(maya_cmds, shape, limits)
    reference_limits = limits.copy()
    reference_limits[int(swapped)] = (-0.3, 0.7)
    _set_base_space(maya_cmds, reference, reference_limits)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{reference}.shapeFill", filled)
        # Wideの球の線は極が帯の内部へ隠れるため、Arrow側は完全表面の保守的boundsを使う。
        expected = (
            _body_bounds(preset, limits, swapped)
            if preset == "CircleArrowSpatial" and wide and not filled
            else _bounds(maya_om, reference)
        )
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)
    if not wide:
        for end in (0.7 - 1e-5, 0.7, 0.7 + 1e-5):
            limits[int(swapped)] = (0.2, end)
            _set_base_space(maya_cmds, shape, limits)
            assert _bounds(maya_om, shape) == pytest.approx(
                _body_bounds(preset, limits, swapped), abs=1e-9
            )


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((-0.5, 2), (2, -0.5), (0.2, 0.4)))
@pytest.mark.parametrize("placement", (0, 1, 2))
def test_new_arrow_part_sites_follow_fixed_body_and_front_tip_with_common_size_rules(
    maya_cmds, maya_om, new_scene, preset, swapped, main, placement
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "arrowSites",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
        shapePart=True,
        shapePartShape=6,
        shapePartType=placement,
        shapePartOffset=2,
        shapePartPrimarySizeScale=1.4,
        shapePartOtherSizeScale=0.6,
    )
    limits = _limits(main, swapped, (1.4, 0.6))
    _set_base_space(maya_cmds, shape, limits)
    sites = _sites(preset, limits, swapped)
    if placement != 1:
        sites = sites[:1]
    boxes = [_body_bounds(preset, limits, swapped)]
    for index, (point, along) in enumerate(sites):
        scale = (1.4 if index == 0 else 0.6) if placement == 1 else 1
        center = [point[axis] + 2 * along[axis] for axis in range(3)]
        boxes.append(
            tuple(value - 0.05 * scale for value in center)
            + tuple(value + 0.05 * scale for value in center)
        )
    assert _bounds(maya_om, shape) == pytest.approx(
        _union_bounds(boxes), abs=1e-9
    )


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("wide", (False, True))
def test_new_arrows_generate_every_part_profile_and_restore_the_body(
    maya_cmds, maya_om, new_scene, preset, part, wide
):
    _load_bd_util_nodes(maya_cmds)
    swapped = bool(part % 2)
    shape = _controller(
        maya_cmds,
        "arrowPartProfiles",
        preset,
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapePartShape=part,
        shapePartType=1,
        shapePartOffset=3,
        shapePartSize=1.3,
        shapePartLengthScale=1.7,
        shapePartWidthScale=1.8,
        shapePartHeightScale=0.7,
    )
    _set_base_space(maya_cmds, shape, _limits((-1, 3), swapped))
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        body = _bounds(maya_om, shape)
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        decorated = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in decorated)
        assert decorated != pytest.approx(body)
        attributes = (
            "shapeGuideLine",
            "shapeGuideLineTemplate",
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        )
        for attribute in attributes:
            maya_cmds.setAttr(f"{shape}.{attribute}", True)
            assert _bounds(maya_om, shape) == pytest.approx(
                decorated, abs=1e-9
            )
        for attribute in attributes:
            maya_cmds.setAttr(f"{shape}.{attribute}", False)
        maya_cmds.setAttr(f"{shape}.shapePartPrimarySizeScale", 0)
        maya_cmds.setAttr(f"{shape}.shapePartOtherSizeScale", 0)
        assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        maya_cmds.setAttr(f"{shape}.shapePartPrimarySizeScale", 1)
        maya_cmds.setAttr(f"{shape}.shapePartOtherSizeScale", 0.5)
        assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main_scale", (1.6, -0.7))
def test_solid_arrow_face_scale_applies_after_mean_radius_and_head_construction(
    maya_cmds, maya_om, new_scene, preset, swapped, main_scale
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "arrowPostBodyScale",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits((-1, 3), swapped, (2, 0.5))
    _set_base_space(maya_cmds, shape, limits)
    _set_faces(
        maya_cmds,
        shape,
        {(1 - axis, side, axis): main_scale for side in ("Minus", "Plus")},
    )
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    expected = _solid_support_bounds(
        maya_om, preset, limits, swapped, angles, main_scale
    )
    assert _bounds(maya_om, shape) == pytest.approx(
        expected, abs=1e-9 if preset == "SquareArrowSpatial" else 0.012
    )


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("wide", (False, True))
def test_new_arrow_nonaffine_cage_fin_and_degenerate_inputs_remain_finite(
    maya_cmds, maya_om, new_scene, preset, swapped, wide
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "deformedArrowOptions",
        preset,
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapeFill=True,
        shapeFin=True,
        shapeFinType=1,
        shapeFinHeight=-1.3,
        shapeFinWidthScale=1.4,
        shapePart=True,
        shapePartShape=1,
        shapePartType=1,
        shapePartOffset=-0.3,
        shapePartLengthScale=-1.2,
    )
    _set_faces(maya_cmds, shape, {(0, "Plus", 1): 1.7, (2, "Minus", 0): -0.6})
    for main, transverse in (((-1, 3), (2, 0.5)), ((0.2, 0.2), (0, 0))):
        _set_base_space(maya_cmds, shape, _limits(main, swapped, transverse))
        original = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in original)
        maya_cmds.setAttr(f"{shape}.shapeSize", 2)
        assert _bounds(maya_om, shape) == pytest.approx(
            tuple(2 * value for value in original), abs=1e-7
        )
        maya_cmds.setAttr(f"{shape}.shapeSize", 1)
        assert _bounds(maya_om, shape) == pytest.approx(original, abs=1e-9)


@pytest.mark.parametrize(
    "preset", ("SquareArrowSpatial", "CircleArrowSpatial")
)
@pytest.mark.parametrize("swapped", (False, True))
def test_short_solid_arrow_cage_uses_the_complete_body_frame_at_zero_and_tiny_lengths(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "stableShortArrowCage",
        preset,
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    _set_faces(
        maya_cmds,
        shape,
        {(axis, "Plus", 1 - axis): 1.7, (axis, "Minus", 2): 0.4},
    )
    expected = None
    for length in (0, 1e-8, 0.2):
        _set_base_space(
            maya_cmds, shape, _limits((0.2, 0.2 + length), swapped, (1.4, 0.6))
        )
        box = _bounds(maya_om, shape)
        assert all(math.isfinite(value) and abs(value) < 3 for value in box)
        if expected is None:
            expected = box
        else:
            assert box == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("preset", NEW_ARROWS)
@pytest.mark.parametrize("swapped", (False, True))
def test_new_arrow_zero_spans_keep_the_physical_part_dimensions_and_fin_height(
    maya_cmds, maya_om, new_scene, preset, swapped
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    side = 1 - axis
    shape = _controller(
        maya_cmds,
        "collapsedArrowAttachments",
        preset,
        shapeAxisSwap=swapped,
        shapePartShape=6,
        shapePartOffset=2,
        shapeFinHeight=-1.3,
    )
    # Finは幅のある主軸区間を使い、横方向の退化で局所高さまで失われないことを確認する。
    limits = _limits((0.2, 1.2), swapped, (0, 0))
    _set_base_space(maya_cmds, shape, limits)
    body = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    assert _bounds(maya_om, shape)[side] == pytest.approx(-1, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeFin", False)
    _set_base_space(maya_cmds, shape, _limits((0.2, 0.2), swapped, (0, 0)))
    body = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapePart", True)
    expected = tuple(
        2.15 if component == axis else 0.25 for component in range(3)
    ) + tuple(2.25 if component == axis else 0.35 for component in range(3))
    # 本体が完全に潰れても、PartのOffsetと局所寸法は残す。
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize(
    "preset,enum",
    (
        ("DiamondArrowPlanar", 23),
        ("SquareArrowSpatial", 29),
        ("CircleArrowSpatial", 31),
    ),
)
def test_new_arrow_public_enum_connections_history_and_reload(
    maya_cmds, maya_om, new_scene, tmp_path, preset, enum
):
    _load_bd_util_nodes(maya_cmds)
    name = _controller(maya_cmds, "animatedNewArrow", preset)
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(name)
    assert getattr(node.shape, preset.upper()) == enum
    driver = maya_cmds.createNode("network", name="newArrowDriver")
    maya_cmds.addAttr(
        driver,
        longName="end",
        attributeType="doubleLinear",
        defaultValue=3,
        keyable=True,
    )
    before = _bounds(maya_om, name)
    node.shapeBaseSpace1stAxisPlus.connect_from(f"{driver}.end")
    mod.do_it_dg()
    assert _bounds(maya_om, name)[3] == pytest.approx(3)
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(before, abs=1e-9)
    mod.redo_it()
    values = ((1, 3), (5, 0.2), (10, -2))
    for frame, end in values:
        maya_cmds.setKeyframe(driver, attribute="end", time=frame, value=end)
    expected = []
    for frame, end in values:
        maya_cmds.currentTime(frame)
        limits = ((-0.5, end), (-0.5, 0.5), (-0.5, 0.5))
        box = _body_bounds(preset, limits, False)
        assert _bounds(maya_om, name) == pytest.approx(box, abs=1e-9)
        expected.append(box)
    scene = tmp_path / "new_arrow.ma"
    maya_cmds.file(rename=str(scene))
    maya_cmds.file(save=True, type="mayaAscii", force=True)
    maya_cmds.file(new=True, force=True)
    maya_cmds.file(str(scene), open=True, force=True)
    assert maya_cmds.isConnected(
        f"{driver}.end", f"{name}.shapeBaseSpace1stAxisPlus"
    )
    for (frame, _), box in zip(values, expected):
        maya_cmds.currentTime(frame)
        assert _bounds(maya_om, name) == pytest.approx(box, abs=1e-9)
