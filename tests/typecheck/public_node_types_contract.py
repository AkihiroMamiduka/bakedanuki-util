from typing import assert_type

import bd_util as bdu
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.bool import (
    BoolPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.double import (
    DoublePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.numeric.range.float import (
    FloatPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_linear import (
    DoubleLinearPlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.at.scalar.unit.range.double_angle import (
    DoubleAnglePlugOperator,
)
from bd_util.maya.node.operator.attr.define.std.dt.matrix import (
    DataMatrixPlugOperator,
)
from bd_util.maya.node.operator.attr.define.node_attr.bd_controller_shape import (
    ShapeAxisRotatePlugOperator,
    ShapeAxisScalePlugOperator,
    ShapeAxisTranslatePlugOperator,
)
from bd_util.maya.node.operator.node.dag.shape._generated.bd_controller_shape import (
    BoundsModeEnumPlugOperator,
    Shape1stAxisEnumPlugOperator,
    Shape2ndAxisEnumPlugOperator,
    ShapeEnumPlugOperator,
    ShapeFinTypeEnumPlugOperator,
    ShapePartShapeEnumPlugOperator,
    ShapePartTypeEnumPlugOperator,
)
from bd_util.maya.node.operator.node.dag.transform.joint import Joint


def joint_list_contract() -> None:
    bd_nodes = bdu.Nodes()
    joints: list[bdu.node_types.Joint] = []
    for i in range(10):
        joints.append(bd_nodes.create.joint(name=f"j_{i}"))

    assert_type(joints, list[Joint])
    for joint in joints:
        joint.t.set(1, 2, 3)
        joint.r.set(3, 4, 5)
        joint.s.set(6, 7, 8)
        joint.v.set(False)
        assert_type(joint, Joint)

    other = bd_nodes.create.plusMinusAverage()
    joints.append(other)  # pyright: ignore[reportArgumentType]


def versioned_node_type_list_contract() -> None:
    bd_nodes_common = bdu.Nodes()
    bd_nodes_2025 = bdu.Nodes(typing_maya_version="2025")
    bd_nodes_2026 = bdu.Nodes(typing_maya_version="2026")
    bd_nodes_2027 = bdu.Nodes(typing_maya_version="2027")
    bd_nodes_2025_plus = bdu.Nodes(typing_maya_version="2025+")
    bd_nodes_2026_plus = bdu.Nodes(typing_maya_version="2026+")
    bd_nodes_2027_plus = bdu.Nodes(typing_maya_version="2027+")

    common: list[bdu.node_types.Absolute] = [bd_nodes_common.create.absolute()]
    absolute_2025: list[bdu.node_types.maya2025.Absolute] = [
        bd_nodes_2025.create.absolute()
    ]
    absolute_2026: list[bdu.node_types.maya2026.Absolute] = [
        bd_nodes_2026.create.absolute()
    ]
    absolute_2027: list[bdu.node_types.maya2027.Absolute] = [
        bd_nodes_2027.create.absolute()
    ]
    absolute_2025_plus: list[bdu.node_types.maya2025_plus.Absolute] = [
        bd_nodes_2025_plus.create.absolute()
    ]
    absolute_2026_plus: list[bdu.node_types.maya2026_plus.Absolute] = [
        bd_nodes_2026_plus.create.absolute()
    ]
    absolute_2027_plus: list[bdu.node_types.maya2027_plus.Absolute] = [
        bd_nodes_2027_plus.create.absolute()
    ]

    assert_type(
        common[0].input,
        DoubleLinearPlugOperator | DoublePlugOperator,
    )
    assert_type(absolute_2025[0].input, DoubleLinearPlugOperator)
    assert_type(absolute_2026[0].input, DoublePlugOperator)
    assert_type(absolute_2027[0].input, DoublePlugOperator)
    assert_type(
        absolute_2025_plus[0].input,
        DoubleLinearPlugOperator | DoublePlugOperator,
    )
    assert_type(absolute_2026_plus[0].input, DoublePlugOperator)
    assert_type(absolute_2027_plus[0].input, DoublePlugOperator)

    bevels: list[bdu.node_types.maya2026_plus.PolySmartBevel] = [
        bd_nodes_2026_plus.create.polySmartBevel()
    ]
    bevels.append(bd_nodes_2027.create.polySmartBevel())
    bevel = bevels[0]
    bevel.cutbackRelaxation  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

    _, area_light = bd_nodes_2026_plus.create.with_transform.aiAreaLight()
    assert_type(area_light, bdu.node_types.maya2026_plus.AiAreaLight)

    bdu.node_types.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    bdu.node_types.maya2025.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    bdu.node_types.maya2025_plus.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    bdu.node_types.maya2026_plus.ShotLabel  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    assert_type(
        bd_nodes_2026.create.absoluteDL(),
        bdu.node_types.maya2026.AbsoluteDL,
    )
    assert_type(
        bd_nodes_2026_plus.create.absoluteDL(),
        bdu.node_types.maya2026_plus.AbsoluteDL,
    )


def controller_shape_offset_line_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape, bdu.node_types.BdControllerShape)
    assert_type(shape.shape, ShapeEnumPlugOperator)
    for preset in (
        ShapeEnumPlugOperator.GEAR,
        ShapeEnumPlugOperator.LINE,
        ShapeEnumPlugOperator.CROSSLINE,
        ShapeEnumPlugOperator.TRIANGLE,
        ShapeEnumPlugOperator.SQUARE,
        ShapeEnumPlugOperator.DIAMOND,
        ShapeEnumPlugOperator.CIRCLE,
        ShapeEnumPlugOperator.ARCRADIAL,
        ShapeEnumPlugOperator.ARCAXIAL,
        ShapeEnumPlugOperator.CROSSARCRADIAL,
        ShapeEnumPlugOperator.CROSSARCAXIAL,
        ShapeEnumPlugOperator.CROSSLINE3AXIS,
        ShapeEnumPlugOperator.CUBE,
        ShapeEnumPlugOperator.OCTAHEDRON,
        ShapeEnumPlugOperator.OCTAHEDRONARROW,
        ShapeEnumPlugOperator.SPHERE,
        ShapeEnumPlugOperator.CYLINDER,
        ShapeEnumPlugOperator.ARROW,
        ShapeEnumPlugOperator.PYRAMID,
        ShapeEnumPlugOperator.CONE,
        ShapeEnumPlugOperator.COLORCROSSLINE3AXIS,
        ShapeEnumPlugOperator.COLORCUBE,
        ShapeEnumPlugOperator.COLORCORNERCUBE,
        ShapeEnumPlugOperator.COLORSPHERE,
    ):
        shape.shape.set(preset)
    assert_type(shape.shapeFin, BoolPlugOperator)
    assert_type(shape.shapeAxisSwap, BoolPlugOperator)
    assert_type(shape.sasw, BoolPlugOperator)
    assert_type(shape.shapeWide, BoolPlugOperator)
    assert_type(shape.swd, BoolPlugOperator)
    assert_type(shape.shapeTemplateLine, BoolPlugOperator)
    assert_type(shape.stl, BoolPlugOperator)
    assert_type(shape.shapeTemplateLineRate, DoublePlugOperator)
    assert_type(shape.stlr, DoublePlugOperator)
    assert_type(shape.shapeTemplateFill, BoolPlugOperator)
    assert_type(shape.stf, BoolPlugOperator)
    assert_type(shape.shapeTemplateLineInvert, BoolPlugOperator)
    assert_type(shape.stli, BoolPlugOperator)
    assert_type(shape.shapePartTemplate, BoolPlugOperator)
    assert_type(shape.spte, BoolPlugOperator)
    assert_type(shape.shapeFinTemplate, BoolPlugOperator)
    assert_type(shape.sft, BoolPlugOperator)
    shape.shapeTemplateLineInvert.set(True)
    shape.stli.set(False)
    shape.shapePartTemplate.set(True)
    shape.spte.set(False)
    shape.shapeFinTemplate.set(True)
    shape.sft.set(False)
    shape.shapeAxisSwap.set(True)
    shape.sasw.set(False)
    shape.shapeWide.set(True)
    shape.swd.set(False)
    shape.shapeTemplateLine.set(True)
    shape.stl.set(False)
    shape.shapeTemplateLineRate.set(0.35)
    shape.stlr.set(0.7)
    shape.shapeTemplateFill.set(True)
    shape.stf.set(False)
    assert_type(shape.shapeGuideLine, BoolPlugOperator)
    assert_type(shape.sgl, BoolPlugOperator)
    assert_type(shape.shapeGuideLineTemplate, BoolPlugOperator)
    assert_type(shape.sglt, BoolPlugOperator)
    shape.shapeGuideLine.set(True)
    shape.sgl.set(False)
    shape.shapeGuideLineTemplate.set(True)
    shape.sglt.set(False)
    assert_type(shape.sfn, BoolPlugOperator)
    assert_type(shape.shapeFinType, ShapeFinTypeEnumPlugOperator)
    assert_type(shape.sfnt, ShapeFinTypeEnumPlugOperator)
    shape.shapeFin.set(True)
    shape.shapeFinType.set(ShapeFinTypeEnumPlugOperator.TAPERED)
    shape.sfnt.set(ShapeFinTypeEnumPlugOperator.STANDARD)
    assert_type(shape.shape1stAxis, Shape1stAxisEnumPlugOperator)
    assert_type(shape.shape2ndAxis, Shape2ndAxisEnumPlugOperator)
    assert_type(shape.shapeAnimationTransformMatrix, DataMatrixPlugOperator)
    assert_type(shape.shapeBaseSpace1stAxisMinus, DoubleLinearPlugOperator)
    assert_type(shape.shapeBaseSpace1stAxisPlus, DoubleLinearPlugOperator)
    assert_type(shape.shapeBaseSpace2ndAxisMinus, DoubleLinearPlugOperator)
    assert_type(shape.shapeBaseSpace2ndAxisPlus, DoubleLinearPlugOperator)
    assert_type(shape.shapeBaseSpace3rdAxisMinus, DoubleLinearPlugOperator)
    assert_type(shape.shapeBaseSpace3rdAxisPlus, DoubleLinearPlugOperator)
    shape.shapeBaseSpace1stAxisMinus.set(1.0)
    shape.shapeBaseSpace1stAxisPlus.set(2.0)
    shape.shapeBaseSpace2ndAxisMinus.set(-0.75)
    shape.shapeBaseSpace2ndAxisPlus.set(0.75)
    shape.shapeBaseSpace3rdAxisMinus.set(-1.0)
    shape.shapeBaseSpace3rdAxisPlus.set(1.0)
    assert_type(shape.shapeWideWidth, DoubleLinearPlugOperator)
    assert_type(shape.sww, DoubleLinearPlugOperator)
    assert_type(shape.shapePart, BoolPlugOperator)
    assert_type(shape.spt, BoolPlugOperator)
    assert_type(shape.shapePartShape, ShapePartShapeEnumPlugOperator)
    assert_type(shape.spsh, ShapePartShapeEnumPlugOperator)
    assert_type(shape.shapePartType, ShapePartTypeEnumPlugOperator)
    assert_type(shape.sptp, ShapePartTypeEnumPlugOperator)
    shape.shapePart.set(True)
    shape.spt.set(False)
    for part_shape in (
        ShapePartShapeEnumPlugOperator.ARROW2D,
        ShapePartShapeEnumPlugOperator.ARROW3D,
        ShapePartShapeEnumPlugOperator.TRIANGLE,
        ShapePartShapeEnumPlugOperator.SQUARE,
        ShapePartShapeEnumPlugOperator.DIAMOND,
        ShapePartShapeEnumPlugOperator.CIRCLE,
        ShapePartShapeEnumPlugOperator.CUBE,
        ShapePartShapeEnumPlugOperator.OCTAHEDRON,
        ShapePartShapeEnumPlugOperator.SPHERE,
        ShapePartShapeEnumPlugOperator.PYRAMID,
        ShapePartShapeEnumPlugOperator.CONE,
    ):
        shape.shapePartShape.set(part_shape)
    shape.spsh.set(shape.spsh.CUBE)
    for part_type in (
        ShapePartTypeEnumPlugOperator.ATEND,
        ShapePartTypeEnumPlugOperator.ATENDS,
        ShapePartTypeEnumPlugOperator.ATAPEX,
    ):
        shape.shapePartType.set(part_type)
    shape.sptp.set(shape.sptp.ATENDS)
    shape.shapeWideWidth.set(0.075)
    assert_type(shape.shapePartOffset, DoubleLinearPlugOperator)
    assert_type(shape.shapeArcAngle, DoubleAnglePlugOperator)
    assert_type(shape.saa, DoubleAnglePlugOperator)
    assert_type(shape.shapeFinHeight, DoubleLinearPlugOperator)
    assert_type(shape.sfnh, DoubleLinearPlugOperator)
    assert_type(shape.shapeFinSize, DoublePlugOperator)
    assert_type(shape.sfns, DoublePlugOperator)
    assert_type(shape.shapeFinWidthScale, DoublePlugOperator)
    assert_type(shape.sfnws, DoublePlugOperator)
    shape.shapeFinSize.set(1.25)
    shape.shapeFinWidthScale.set(0.75)
    assert_type(shape.shapePartSize, DoublePlugOperator)
    assert_type(shape.shapePartPrimarySizeScale, DoublePlugOperator)
    assert_type(shape.shapePartOtherSizeScale, DoublePlugOperator)
    assert_type(shape.shapePartLengthScale, DoublePlugOperator)
    assert_type(shape.shapePartWidthScale, DoublePlugOperator)
    assert_type(shape.shapePartHeightScale, DoublePlugOperator)
    assert_type(shape.sphs, DoublePlugOperator)
    assert_type(shape.sps, DoublePlugOperator)
    assert_type(shape.sppss, DoublePlugOperator)
    assert_type(shape.sposs, DoublePlugOperator)
    shape.shapePartOffset.set(0.1)
    shape.shapeArcAngle.set(240)
    shape.saa.set(180)
    shape.shapeFinHeight.set(0.75)
    shape.shapePartSize.set(2.0)
    shape.shapePartPrimarySizeScale.set(1.5)
    shape.shapePartOtherSizeScale.set(0.75)
    shape.sppss.set(1.0)
    shape.sposs.set(0.5)
    shape.shapePartLengthScale.set(2.0)
    shape.shapePartWidthScale.set(3.0)
    shape.shapePartHeightScale.set(0.5)
    shape.sphs.set(1.0)
    assert_type(shape.shapeAxisTranslate, ShapeAxisTranslatePlugOperator)
    assert_type(shape.shapeAxisRotate, ShapeAxisRotatePlugOperator)
    assert_type(shape.shapeAxisScale, ShapeAxisScalePlugOperator)
    shape.shape1stAxis.set(Shape1stAxisEnumPlugOperator.PLUS_X)
    shape.shape2ndAxis.set(Shape2ndAxisEnumPlugOperator.PLUS_Y)
    shape.shapeAnimationTransformMatrix.set(
        (
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
        )
    )
    shape.shapeAxisTranslate.set(1.0, 2.0, 3.0)
    shape.shapeAxisRotate.set(0.0, 0.0, 90.0)
    shape.shapeAxisScale.set(2.0, 1.0, 1.0)
    assert_type(shape.shapeOffsetLine, BoolPlugOperator)
    assert_type(shape.sol, BoolPlugOperator)
    assert_type(shape.shapeOffsetLineTemplate, BoolPlugOperator)
    shape.shapeOffsetLine.set(True)
    shape.shapeOffsetLineTemplate.set(False)


def controller_shape_bounds_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape.boundsMode, BoundsModeEnumPlugOperator)
    assert_type(shape.showBoundsPreview, BoolPlugOperator)
    assert_type(shape.customBoundsBaseSpaceXPlus, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsBaseSpaceXMinus, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsBaseSpaceYPlus, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsBaseSpaceYMinus, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsBaseSpaceZPlus, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsBaseSpaceZMinus, DoubleLinearPlugOperator)
    shape.boundsMode.set(BoundsModeEnumPlugOperator.CUSTOM)
    shape.showBoundsPreview.set(True)
    shape.customBoundsBaseSpaceXPlus.set(2.0)
    shape.customBoundsBaseSpaceXMinus.set(1.0)
    shape.customBoundsBaseSpaceYPlus.set(3.0)
    shape.customBoundsBaseSpaceYMinus.set(-1.0)
    shape.customBoundsBaseSpaceZPlus.set(4.0)
    shape.customBoundsBaseSpaceZMinus.set(-2.0)


def controller_shape_draw_style_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape.shapeLineWidth, FloatPlugOperator)
    assert_type(shape.shapeLineTransparency, FloatPlugOperator)
    assert_type(shape.slt, FloatPlugOperator)
    assert_type(shape.shapeFill, BoolPlugOperator)
    assert_type(shape.sfl, BoolPlugOperator)
    shape.shapeFill.set(True)
    assert_type(shape.shapeFillTransparency, FloatPlugOperator)
    assert_type(shape.shapeDrawOnTop, BoolPlugOperator)
    shape.shapeLineWidth.set(2.5)
    shape.shapeLineTransparency.set(0.375)
    shape.shapeFillTransparency.set(0.25)
    shape.shapeDrawOnTop.set(True)
