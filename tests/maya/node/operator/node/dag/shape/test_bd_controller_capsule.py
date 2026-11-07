"""Capsuleの横径由来の半球、専用基準空間、付属形状の契約を検証する。"""

from __future__ import annotations

import math

import pytest

import bd_util as bdu

from test_bd_controller_attachment_contract import _controller, _union_bounds
from test_bd_controller_base_space import _set_base_space
from test_bd_controller_shape import _bounds, _load_bd_util_nodes

pytestmark = pytest.mark.maya

MAIN_LIMITS = (
    (-0.5, 0.5),
    (-2, 2),
    (1, 4),
    (3, 1),
    (0.2, 0.7),
    (0.2, 0.2),
    (1e-8, 2e-8),
    (-0.8, 0.15),
)
TRANSVERSE_CASES = (
    ((-1, 1), (-1, 1)),
    ((-0.2, 0.8), (-0.1, 0.4)),
    ((0, 0), (-1, 1)),
    ((1, -1), (0.8, -0.2)),
    ((0, 0), (0, 0)),
)


def _limits(main, swapped, *, shifted=False):
    limits = [(-0.5, 0.5)] * 3
    if shifted:
        limits = [(-1.3, 0.7), (1, 2), (-2, -0.5)]
    limits[int(swapped)] = main
    return tuple(limits)


def _cap_radius(limits, swapped):
    return (
        sum(
            abs(plus - minus)
            for axis, (minus, plus) in enumerate(limits)
            if axis != int(swapped)
        )
        / 4
    )


def _capsule_bounds(limits, swapped):
    result = [min(pair) for pair in limits] + [max(pair) for pair in limits]
    radius = _cap_radius(limits, swapped)
    result[int(swapped)] -= radius
    result[int(swapped) + 3] += radius
    return tuple(result)


def _smooth_support_bounds(maya_om, limits, swapped, angles, main_scale=1):
    matrix = maya_om.MEulerRotation(
        *(math.radians(angle) for angle in angles)
    ).asMatrix()
    center = maya_om.MPoint(*(sum(pair) / 2 for pair in limits)) * matrix
    axes = [
        maya_om.MVector(*(int(axis == component) for component in range(3)))
        * matrix
        for axis in range(3)
    ]
    main = int(swapped)
    length = abs(limits[main][1] - limits[main][0])
    cylinder_half = length / 2 * abs(main_scale)
    radii = [abs(plus - minus) / 2 for minus, plus in limits]
    radii[main] = _cap_radius(limits, swapped) * abs(main_scale)
    support = tuple(
        cylinder_half * abs(axes[main][world_axis])
        + math.sqrt(
            sum(
                (radii[axis] * axes[axis][world_axis]) ** 2
                for axis in range(3)
            )
        )
        for world_axis in range(3)
    )
    return tuple(center[axis] - support[axis] for axis in range(3)) + tuple(
        center[axis] + support[axis] for axis in range(3)
    )


@pytest.mark.parametrize("main", MAIN_LIMITS)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("filled", (False, True))
def test_capsule_endpoints_are_cap_centers_and_transverse_limits_are_preserved(
    maya_cmds, maya_om, new_scene, main, swapped, filled
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsuleEndpoints",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeFill=filled,
    )
    limits = _limits(main, swapped, shifted=True)
    _set_base_space(maya_cmds, shape, limits)
    assert _bounds(maya_om, shape) == pytest.approx(
        _capsule_bounds(limits, swapped), abs=1e-9
    )


@pytest.mark.parametrize(
    "main", ((-2, 2), (4, 1), (-0.5, 0.5), (0.2, 0.6), (0.2, 0.2))
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("angles", ((17, -29, 37), (0, 0, 45), (63, 21, -32)))
def test_capsule_rotated_support_keeps_mean_cap_radius_and_only_stretches_the_cylinder(
    maya_cmds, maya_om, new_scene, main, swapped, angles
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsuleSupport",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = list(_limits(main, swapped))
    limits[1 - int(swapped)] = (-0.7, 0.7)
    limits[2] = (-0.35, 0.35)
    _set_base_space(maya_cmds, shape, limits)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    expected = _smooth_support_bounds(maya_om, limits, swapped, angles)
    # 滑らかな形状の支持関数と比較し、離散メッシュの弦による僅かな内側の誤差を許す。
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=0.006)


@pytest.mark.parametrize("main", ((-2, 2), (0.2, 0.6), (3, 1)))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_face_scales_apply_after_caps_and_cylinder_are_constructed(
    maya_cmds, maya_om, new_scene, main, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsulePostCage",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = _limits(main, swapped)
    _set_base_space(maya_cmds, shape, limits)
    normal, component = ("1st", "2nd") if swapped else ("2nd", "1st")
    for side in ("Minus", "Plus"):
        maya_cmds.setAttr(
            f"{shape}.shapeBaseSpace{normal}Axis{side}Scale{component}Axis",
            1.6,
        )
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    expected = _smooth_support_bounds(
        maya_om, limits, swapped, angles, main_scale=1.6
    )
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=0.008)


@pytest.mark.parametrize("transverse", TRANSVERSE_CASES)
@pytest.mark.parametrize("main", ((-1, 2), (0.2, 0.2)))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_transverse_spans_define_cap_radius_and_zero_core_ellipsoid(
    maya_cmds, maya_om, new_scene, transverse, main, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds, "capsuleMeanRadius", "Capsule", shapeAxisSwap=swapped
    )
    limits = list(_limits(main, swapped))
    limits[1 - int(swapped)], limits[2] = transverse
    _set_base_space(maya_cmds, shape, limits)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(
            _capsule_bounds(limits, swapped), abs=1e-9
        )
    angles = (17, -29, 37)
    maya_cmds.setAttr(f"{shape}.shapeRotate", *angles)
    expected = _smooth_support_bounds(maya_om, limits, swapped, angles)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=0.008)


@pytest.mark.parametrize("length", (0, 1e-8, -1e-8, 0.02))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_tiny_core_cage_uses_total_length_and_converges_to_the_matching_zero_core(
    maya_cmds, maya_om, new_scene, length, swapped
):
    _load_bd_util_nodes(maya_cmds)
    options = dict(shapeAxisSwap=swapped, shapeFill=True)
    actual = _controller(maya_cmds, "tinyCapsuleCage", "Capsule", **options)
    zero_core = _controller(maya_cmds, "zeroCapsuleCage", "Capsule", **options)
    _set_base_space(
        maya_cmds, actual, _limits((-length / 2, length / 2), swapped)
    )
    _set_base_space(maya_cmds, zero_core, _limits((0, 0), swapped))
    normal, component = ("2nd", "1st") if swapped else ("1st", "2nd")
    maya_cmds.setAttr(
        f"{actual}.shapeBaseSpace{normal}AxisPlusScale{component}Axis", 2
    )
    reference_side = "Minus" if length < 0 else "Plus"
    maya_cmds.setAttr(
        f"{zero_core}.shapeBaseSpace{normal}Axis{reference_side}Scale{component}Axis",
        2,
    )
    box = _bounds(maya_om, actual)
    assert all(math.isfinite(value) and abs(value) <= 1.02 for value in box)
    # 反転側では端別半径と面倍率も交換したL0を使い、同じ完成表面への連続性を確認する。
    zero_box = _bounds(maya_om, zero_core)
    assert box == pytest.approx(zero_box, abs=1e-8 + 2 * abs(length))


@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((-0.2, 2), (1, -1), (0.2, 0.2)))
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
def test_capsule_uses_each_declared_main_face_radius_before_cage_once(
    maya_cmds, maya_om, new_scene, swapped, main, minus_scales, plus_scales
):
    _load_bd_util_nodes(maya_cmds)
    axis = int(swapped)
    shape = _controller(
        maya_cmds,
        "separateCapsuleCaps",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeFill=True,
    )
    limits = list(_limits(main, swapped))
    limits[1 - axis] = (-0.7, 0.7)
    limits[2] = (-0.3, 0.3)
    _set_base_space(maya_cmds, shape, limits)
    for side, scales in (("Minus", minus_scales), ("Plus", plus_scales)):
        for component, scale in zip((1 - axis, 2), scales):
            maya_cmds.setAttr(
                f"{shape}.shapeBaseSpace{('1st', '2nd')[axis]}Axis{side}Scale{('1st', '2nd', '3rd')[component]}Axis",
                scale,
            )
    rear_radius, front_radius = tuple(
        (0.7 * abs(scales[0]) + 0.3 * abs(scales[1])) / 2
        for scales in (minus_scales, plus_scales)
    )
    minus, plus = main
    sign = 1 if plus >= minus else -1
    ends = (minus - sign * rear_radius, plus + sign * front_radius)
    box = _bounds(maya_om, shape)
    assert all(math.isfinite(value) for value in box)
    assert (box[axis], box[axis + 3]) == pytest.approx(
        (min(ends), max(ends)), abs=1e-9
    )


@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_coincident_junctions_preserve_template_and_wide_bounds(
    maya_cmds, maya_om, new_scene, wide, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "coincidentCapsuleJunctions",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
    )
    limits = list(_limits((0.2, 0.2), swapped))
    limits[1 - int(swapped)] = (-0.7, 0.7)
    limits[2] = (-0.35, 0.35)
    _set_base_space(maya_cmds, shape, limits)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{shape}.shapeTemplateLine", False)
        maya_cmds.setAttr(f"{shape}.shapeTemplateFill", False)
        baseline = _bounds(maya_om, shape)
        assert all(math.isfinite(value) for value in baseline)
        maya_cmds.setAttr(f"{shape}.shapeTemplateLine", True)
        maya_cmds.setAttr(f"{shape}.shapeTemplateFill", True)
        for rate in (0, 0.35, 1):
            maya_cmds.setAttr(f"{shape}.shapeTemplateLineRate", rate)
            for invert in (False, True):
                maya_cmds.setAttr(f"{shape}.shapeTemplateLineInvert", invert)
                assert _bounds(maya_om, shape) == pytest.approx(
                    baseline, abs=1e-9
                )


@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_zero_transverse_radius_keeps_its_axis_with_wide_enabled(
    maya_cmds, maya_om, new_scene, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "collapsedWideCapsule",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeWide=True,
        shapeWideWidth=0.2,
    )
    limits = [(0, 0)] * 3
    limits[int(swapped)] = (-1, 2)
    _set_base_space(maya_cmds, shape, limits)
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        assert _bounds(maya_om, shape) == pytest.approx(
            _capsule_bounds(limits, swapped), abs=1e-9
        )


@pytest.mark.parametrize(
    "placement,primary,other",
    (
        (0, 1.7, 0.6),
        (2, 0, 0),
        (1, 1.7, 0.6),
        (1, 0, 0.6),
        (1, 1.7, 0),
        (1, -1.2, -0.8),
    ),
)
@pytest.mark.parametrize("swapped", (False, True))
@pytest.mark.parametrize("main", ((-1, 2), (2, -1)))
def test_capsule_parts_use_only_the_two_tips_and_keep_at_ends_size_rules(
    maya_cmds, maya_om, new_scene, placement, primary, other, swapped, main
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsuleTipParts",
        "Capsule",
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartType=placement,
        shapePartOffset=2,
        shapePartWidthScale=20,
        shapePartHeightScale=30,
        shapePartPrimarySizeScale=primary,
        shapePartOtherSizeScale=other,
    )
    limits = _limits(main, swapped)
    _set_base_space(maya_cmds, shape, limits)
    axis = int(swapped)
    direction = 1 if main[1] >= main[0] else -1
    radius = _cap_radius(limits, swapped)
    boxes = [_capsule_bounds(limits, swapped)]
    sites = (
        (main[1] + direction * radius, direction, primary),
        (main[0] - direction * radius, -direction, other),
    )
    if placement != 1:
        sites = ((main[1] + direction * radius, direction, 1),)
    for endpoint, sign, scale in sites:
        if scale == 0:
            continue
        center = [0, 0, 0]
        center[axis] = endpoint + sign * 2
        half = [1.5 * abs(scale), 1.5 * abs(scale), abs(scale)]
        half[axis] = 0.05 * abs(scale)
        boxes.append(
            tuple(center[i] - half[i] for i in range(3))
            + tuple(center[i] + half[i] for i in range(3))
        )
    assert _bounds(maya_om, shape) == pytest.approx(
        _union_bounds(boxes), abs=1e-9
    )


@pytest.mark.parametrize("spans", ((2, 2), (2, 0.5), (0, 2), (-2, 0.5)))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_part_tips_follow_the_mean_transverse_radius(
    maya_cmds, maya_om, new_scene, spans, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsuleMeanRadiusParts",
        "Capsule",
        shapeAxisSwap=swapped,
        shapePart=True,
        shapePartShape=6,
        shapePartType=1,
        shapePartOffset=2,
        shapePartPrimarySizeScale=1.7,
        shapePartOtherSizeScale=0.6,
    )
    limits = list(_limits((-1, 2), swapped))
    limits[1 - int(swapped)] = (-spans[0] / 2, spans[0] / 2)
    limits[2] = (-spans[1] / 2, spans[1] / 2)
    _set_base_space(maya_cmds, shape, limits)
    radius = _cap_radius(limits, swapped)
    expected = list(_capsule_bounds(limits, swapped))
    axis = int(swapped)
    expected[axis] = -1 - radius - 2 - 0.03
    expected[axis + 3] = 2 + radius + 2 + 0.085
    for other_axis in range(3):
        if other_axis != axis:
            expected[other_axis] = min(expected[other_axis], -0.085)
            expected[other_axis + 3] = max(expected[other_axis + 3], 0.085)
    assert _bounds(maya_om, shape) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("part", range(11))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_generates_all_part_profiles_and_restores_the_wide_body(
    maya_cmds, maya_om, new_scene, part, wide, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsulePartKinds",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeWideWidth=0.08,
        shapePartShape=part,
        shapePartType=1,
        shapePartOffset=2.5,
        shapePartSize=1.3,
        shapePartLengthScale=1.7,
        shapePartWidthScale=1.8,
        shapePartHeightScale=0.7,
    )
    _set_base_space(maya_cmds, shape, _limits((-1, 2), swapped))
    for filled in (False, True):
        maya_cmds.setAttr(f"{shape}.shapeFill", filled)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        body = _bounds(maya_om, shape)
        maya_cmds.setAttr(f"{shape}.shapePart", True)
        decorated = _bounds(maya_om, shape)
        assert decorated != pytest.approx(body)
        assert all(math.isfinite(value) for value in decorated)
        for attribute in (
            "shapeGuideLine",
            "shapeGuideLineTemplate",
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", True)
            assert _bounds(maya_om, shape) == pytest.approx(
                decorated, abs=1e-9
            )
        for attribute in (
            "shapeGuideLine",
            "shapeGuideLineTemplate",
            "shapePartTemplate",
            "shapeTemplateLine",
            "shapeTemplateFill",
        ):
            maya_cmds.setAttr(f"{shape}.{attribute}", False)
        maya_cmds.setAttr(f"{shape}.shapePart", False)
        assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)


@pytest.mark.parametrize("fin_type", (0, 1))
@pytest.mark.parametrize("wide", (False, True))
@pytest.mark.parametrize("swapped", (False, True))
def test_capsule_fin_is_independent_and_zero_height_restores_the_body(
    maya_cmds, maya_om, new_scene, fin_type, wide, swapped
):
    _load_bd_util_nodes(maya_cmds)
    shape = _controller(
        maya_cmds,
        "capsuleFin",
        "Capsule",
        shapeAxisSwap=swapped,
        shapeWide=wide,
        shapeFill=True,
        shapeFinType=fin_type,
        shapeFinHeight=1.3,
        shapeFinWidthScale=1.4,
    )
    _set_base_space(maya_cmds, shape, _limits((-1, 2), swapped))
    body = _bounds(maya_om, shape)
    maya_cmds.setAttr(f"{shape}.shapeFin", True)
    decorated = _bounds(maya_om, shape)
    assert decorated != pytest.approx(body)
    assert all(math.isfinite(value) for value in decorated)
    for axis in range(3):
        assert decorated[axis] <= body[axis] + 1e-9
        assert decorated[axis + 3] >= body[axis + 3] - 1e-9
    for attribute in (
        "shapeGuideLine",
        "shapeGuideLineTemplate",
        "shapeFinTemplate",
    ):
        maya_cmds.setAttr(f"{shape}.{attribute}", True)
        assert _bounds(maya_om, shape) == pytest.approx(decorated, abs=1e-9)
    maya_cmds.setAttr(f"{shape}.shapeFinHeight", 0)
    assert _bounds(maya_om, shape) == pytest.approx(body, abs=1e-9)


def test_capsule_mean_cap_radius_respects_scene_distance_units(
    maya_cmds, maya_om, new_scene
):
    _load_bd_util_nodes(maya_cmds)
    previous = maya_cmds.currentUnit(query=True, linear=True)
    try:
        maya_cmds.currentUnit(linear="mm")
        shape = _controller(
            maya_cmds, "millimeterCapsule", "Capsule", shapeFill=True
        )
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisMinus", -10)
        maya_cmds.setAttr(f"{shape}.shapeBaseSpace1stAxisPlus", 50)
        maya_cmds.setAttr(f"{shape}.shapeRotateZ", 45)
        expected = _smooth_support_bounds(
            maya_om, ((1, 5), (-0.5, 0.5), (-0.5, 0.5)), False, (0, 0, 45)
        )
        assert _bounds(maya_om, shape) == pytest.approx(expected, abs=0.006)
    finally:
        maya_cmds.currentUnit(linear=previous)


def test_capsule_public_enum_connections_history_and_reload_update_the_body(
    maya_cmds, maya_om, new_scene, tmp_path
):
    _load_bd_util_nodes(maya_cmds)
    name = _controller(maya_cmds, "animatedCapsule", "Capsule")
    mod = bdu.ModifierManager()
    node = bdu.Nodes(modifier_manager=mod).existing(name)
    assert node.shape.CAPSULE == 20
    driver = maya_cmds.createNode("network", name="capsuleLengthDriver")
    maya_cmds.addAttr(
        driver,
        longName="end",
        attributeType="doubleLinear",
        defaultValue=4,
        keyable=True,
    )
    node.shape.set(node.shape.CAPSULE)
    node.shapeBaseSpace1stAxisPlus.connect_from(f"{driver}.end")
    mod.do_it_dg()
    assert _bounds(maya_om, name) == pytest.approx(
        (-1, -0.5, -0.5, 4.5, 0.5, 0.5), abs=1e-9
    )
    mod.undo_it()
    assert _bounds(maya_om, name) == pytest.approx(
        (-1, -0.5, -0.5, 1, 0.5, 0.5), abs=1e-9
    )
    mod.redo_it()
    values = ((1, 4), (5, 0.3), (10, -1))
    for frame, end in values:
        maya_cmds.setKeyframe(driver, attribute="end", time=frame, value=end)
    expected = []
    for frame, end in values:
        maya_cmds.currentTime(frame)
        box = (
            min(-0.5, end) - 0.5,
            -0.5,
            -0.5,
            max(-0.5, end) + 0.5,
            0.5,
            0.5,
        )
        assert _bounds(maya_om, name) == pytest.approx(box, abs=1e-9)
        expected.append(box)
    scene = tmp_path / "capsule.ma"
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
