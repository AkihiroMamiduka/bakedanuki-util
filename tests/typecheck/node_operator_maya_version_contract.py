from typing import assert_type

import bd_util as bdu
from bd_util.maya.node.operator.attr import (
    CurveKeyframeManager,
    KeyframeManager,
)

from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import (
    DoubleAttrOperator,
    DoublePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.float import (
    FloatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearAttrOperator,
    DoubleLinearPlugOperator,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_area import (
    UfeLightArea,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_cylinder import (
    UfeLightCylinder,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_default import (
    UfeLightDefault,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_directional import (
    UfeLightDirectional,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_disk import (
    UfeLightDisk,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_dome import (
    UfeLightDome,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_sphere import (
    UfeLightSphere,
)
from bd_util.maya.node.operator.node.dag.shape.ufe_light_spot import (
    UfeLightSpot,
)
from bd_util.maya.node.operator.node.dg.absolute import Absolute
from bd_util.maya.node.operator.node.dg.absolute_dl import AbsoluteDL
from bd_util.maya.node.operator.node.dg.add_double_linear import (
    AddDoubleLinear,
)
from bd_util.maya.node.operator.node.dg.bifrost_closure_converter import (
    BifrostClosureConverter,
)
from bd_util.maya.node.operator.node.dg.dga_delta import DgaDelta
from bd_util.maya.node.operator.node.dg.dga_tension import DgaTension
from bd_util.maya.node.operator.node.dg.dga_to_array import DgaToArray
from bd_util.maya.node.operator.node.dg.dga_visualizer import DgaVisualizer
from bd_util.maya.node.operator.node.dg.shot_label import ShotLabel
from bd_util.maya.node.operator.node.dg.usd_default_settings import (
    UsdDefaultSettings,
)

nodes_common = bdu.Nodes()
nodes_2025 = bdu.Nodes(typing_maya_version="2025")
nodes_2026 = bdu.Nodes(typing_maya_version="2026")
nodes_2027 = bdu.Nodes(typing_maya_version="2027")
for version_nodes in (nodes_2025, nodes_2026, nodes_2027):
    curve_candidates = version_nodes.existing.transform(
        "target"
    ).translate.translateX.keyframe.find_anim_curves(
        filter_type=version_nodes.types.AnimCurveTL
    )
    assert_type(curve_candidates[0].keyframe, CurveKeyframeManager)
    layer_keyframe = version_nodes.existing.transform(
        "target"
    ).translate.translateX.keyframe.anim_layer("Correction")
    assert_type(layer_keyframe, KeyframeManager)
    assert_type(layer_keyframe.get_keys(), list[tuple[float, float]])
bdu.Nodes(  # pyright: ignore[reportCallIssue]
    typing_maya_version="2028"  # pyright: ignore[reportArgumentType]
)

absolute_common = nodes_common.create.absolute()
absolute_2025 = nodes_2025.create.absolute()
absolute_2026 = nodes_2026.create.absolute()
absolute_2027 = nodes_2027.create.absolute()

assert_type(absolute_2025, Absolute)
assert_type(
    absolute_common.input, DoubleLinearPlugOperator | DoublePlugOperator
)
assert_type(absolute_2025.input, DoubleLinearPlugOperator)
assert_type(absolute_2026.input, DoublePlugOperator)
assert_type(absolute_2027.input, DoublePlugOperator)
assert isinstance(absolute_common, Absolute)

assert_type(
    nodes_common.types.Absolute.input,
    DoubleLinearAttrOperator | DoubleAttrOperator,
)
assert_type(nodes_2025.types.Absolute.input, DoubleLinearAttrOperator)
assert_type(nodes_2026.types.Absolute.input, DoubleAttrOperator)
assert_type(nodes_2027.types.Absolute.input, DoubleAttrOperator)

assert_type(nodes_2025.create.addDoubleLinear(), AddDoubleLinear)
assert_type(nodes_2026.create.absoluteDL(), AbsoluteDL)
assert_type(nodes_2027.create.absoluteDL(), AbsoluteDL)
assert_type(nodes_2027.create.shotLabel(), ShotLabel)

poly_smart_bevel_2026 = nodes_2026.create.polySmartBevel()
poly_smart_bevel_2027 = nodes_2027.create.polySmartBevel()
assert_type(poly_smart_bevel_2027.cutbackRelaxation, FloatPlugOperator)
poly_smart_bevel_2026.cutbackRelaxation  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

assert_type(
    nodes_2025.existing.addDoubleLinear("existing_add"),
    AddDoubleLinear,
)
assert_type(nodes_2026.existing.absoluteDL("existing_abs"), AbsoluteDL)
assert_type(nodes_2027.existing.shotLabel("existing_shot_label"), ShotLabel)

assert_type(nodes_2026.create.dgaDelta(), DgaDelta)
assert_type(nodes_2026.create.dgaTension(), DgaTension)
assert_type(nodes_2026.create.dgaToArray(), DgaToArray)
assert_type(nodes_2026.create.dgaVisualizer(), DgaVisualizer)
assert_type(nodes_2027.create.dgaDelta(), DgaDelta)

assert_type(nodes_2026.existing.ufeLightArea("ufe_area"), UfeLightArea)
assert_type(
    nodes_2026.existing.ufeLightCylinder("ufe_cylinder"),
    UfeLightCylinder,
)
assert_type(
    nodes_2026.existing.ufeLightDefault("ufe_default"), UfeLightDefault
)
assert_type(
    nodes_2026.existing.ufeLightDirectional("ufe_directional"),
    UfeLightDirectional,
)
assert_type(nodes_2026.existing.ufeLightDisk("ufe_disk"), UfeLightDisk)
assert_type(nodes_2027.existing.ufeLightDome("ufe_dome"), UfeLightDome)
assert_type(nodes_2027.existing.ufeLightSphere("ufe_sphere"), UfeLightSphere)
assert_type(nodes_2027.existing.ufeLightSpot("ufe_spot"), UfeLightSpot)

assert_type(nodes_2026.types.DgaDelta, type[DgaDelta])
assert_type(nodes_2026.types.UfeLightArea, type[UfeLightArea])
assert_type(nodes_2027.types.DgaVisualizer, type[DgaVisualizer])
assert_type(nodes_2027.types.UfeLightSpot, type[UfeLightSpot])

assert_type(
    nodes_2027.create.bifrostClosureConverter(), BifrostClosureConverter
)
assert_type(nodes_2027.create.UsdDefaultSettings(), UsdDefaultSettings)
assert_type(
    nodes_2027.existing.bifrostClosureConverter("closure_converter"),
    BifrostClosureConverter,
)
assert_type(
    nodes_2027.existing.UsdDefaultSettings("usd_defaults"),
    UsdDefaultSettings,
)
assert_type(
    nodes_2027.types.BifrostClosureConverter,
    type[BifrostClosureConverter],
)
assert_type(nodes_2027.types.UsdDefaultSettings, type[UsdDefaultSettings])

nodes_common.create.absoluteDL()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.create.absoluteDL()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.create.addDoubleLinear()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.create.shotLabel()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_common.create.polySmartBevel()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.create.polySmartBevel()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_common.existing.absoluteDL(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2025.existing.absoluteDL(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2026.existing.addDoubleLinear(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)

nodes_common.types.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.types.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.types.AddDoubleLinear  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.types.ShotLabel  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_common.create.dgaDelta()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.create.dgaDelta()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_common.existing.dgaDelta(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2025.existing.dgaDelta(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_common.types.DgaDelta  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.types.DgaDelta  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_common.existing.ufeLightArea(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2025.existing.ufeLightArea(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_common.types.UfeLightArea  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2025.types.UfeLightArea  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_common.create.bifrostClosureConverter()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.create.bifrostClosureConverter()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.existing.bifrostClosureConverter(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2026.types.BifrostClosureConverter  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_common.create.UsdDefaultSettings()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.create.UsdDefaultSettings()  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.existing.UsdDefaultSettings(  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    "node"
)
nodes_2026.types.UsdDefaultSettings  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

nodes_2025.types.StandardSurface.lightDirectionX
nodes_common.types.StandardSurface.lightDirectionX  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2026.types.StandardSurface.lightDirectionX  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
nodes_2027.types.StandardSurface.lightDirectionX  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
