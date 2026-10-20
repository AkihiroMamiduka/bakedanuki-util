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
    CustomBoundsAxisRotatePlugOperator,
    CustomBoundsAxisScalePlugOperator,
    CustomBoundsAxisTranslatePlugOperator,
    CustomBoundsRotatePlugOperator,
    CustomBoundsScalePlugOperator,
    CustomBoundsTranslatePlugOperator,
    ShapeAxisRotatePlugOperator,
    ShapeAxisScalePlugOperator,
    ShapeAxisTranslatePlugOperator,
)
from bd_util.maya.node.operator.node.dag.shape._generated.bd_controller_shape import (
    BoundsModeEnumPlugOperator,
    CustomBounds1stAxisEnumPlugOperator,
    CustomBounds2ndAxisEnumPlugOperator,
    CustomBoundsAxisOffsetDirectionEnumPlugOperator,
    Shape1stAxisEnumPlugOperator,
    Shape2ndAxisEnumPlugOperator,
    ShapeAxisOffsetDirectionEnumPlugOperator,
    ShapeEnumPlugOperator,
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
    shape.shape.set(ShapeEnumPlugOperator.GEAR)
    shape.shape.set(ShapeEnumPlugOperator.LINE1ST)
    shape.shape.set(ShapeEnumPlugOperator.LINE2ND)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RD)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST2ND)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST3RD)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE2ND3RD)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXIS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDCUBE)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDCUBEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDOCTAHEDRON)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDOCTAHEDRONFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDSPHERE)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDSPHEREFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDPYRAMID)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDPYRAMIDFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDCONE)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE3AXISENDCONEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST2NDARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST2NDARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST3RDARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST3RDARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE2ND3RDARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE2ND3RDARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST2NDWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST2NDWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST3RDWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE1ST3RDWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE2ND3RDWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.CROSSLINE2ND3RDWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEWIDEARROWATENDS)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEWIDEARROWATENDSFILLED)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXIS)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDCUBE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDCUBEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDOCTAHEDRON)
    shape.shape.set(
        ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDOCTAHEDRONFILLED
    )
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDSPHERE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDSPHEREFILLED)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDPYRAMID)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDPYRAMIDFILLED)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDCONE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCROSSLINE3AXISENDCONEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.TRIANGLEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.SQUAREFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CUBEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.OCTAHEDRONFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CIRCLEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.SPHEREFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CYLINDERFILLED)
    shape.shape.set(ShapeEnumPlugOperator.PYRAMIDFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CONEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.CUBEFINARROW)
    shape.shape.set(ShapeEnumPlugOperator.CYLINDERFINARROW)
    shape.shape.set(ShapeEnumPlugOperator.CIRCLEARROW2D)
    shape.shape.set(ShapeEnumPlugOperator.OCTAHEDRON)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLE)
    shape.shape.set(ShapeEnumPlugOperator.COLORSPHERE)
    shape.shape.set(ShapeEnumPlugOperator.COLORSPHERECROSSLINE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCUBE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCUBEFILLED)
    shape.shape.set(ShapeEnumPlugOperator.COLORCORNERCUBE)
    shape.shape.set(ShapeEnumPlugOperator.COLORCORNERCUBEFILLED)
    assert_type(shape.shape1stAxis, Shape1stAxisEnumPlugOperator)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STARROWATSTART)
    shape.shape.set(ShapeEnumPlugOperator.LINE1STARROWATENDFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDWIDEARROWATSTART)
    shape.shape.set(ShapeEnumPlugOperator.LINE2NDWIDEARROWATENDFILLED)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDARROWATEND)
    shape.shape.set(ShapeEnumPlugOperator.LINE3RDWIDEARROWATSTARTFILLED)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEARROWATSTART)
    shape.shape.set(ShapeEnumPlugOperator.SEMICIRCLEWIDEARROWATENDFILLED)
    assert_type(shape.shape2ndAxis, Shape2ndAxisEnumPlugOperator)
    assert_type(shape.shapeAnimationTransformMatrix, DataMatrixPlugOperator)
    assert_type(shape.shapeAxisOffsetLength, DoubleLinearPlugOperator)
    assert_type(shape.shapePartOffset, DoubleLinearPlugOperator)
    assert_type(shape.shapePartOffsetAngle, DoubleAnglePlugOperator)
    assert_type(shape.spoa, DoubleAnglePlugOperator)
    assert_type(shape.shapePartFinHeight, DoubleLinearPlugOperator)
    assert_type(shape.spfh, DoubleLinearPlugOperator)
    assert_type(shape.shapePartSize, DoublePlugOperator)
    assert_type(shape.shapePartLengthScale, DoublePlugOperator)
    assert_type(shape.shapePartWidthScale, DoublePlugOperator)
    assert_type(shape.sps, DoublePlugOperator)
    shape.shapePartOffset.set(0.1)
    shape.shapePartOffsetAngle.set(30)
    shape.shapePartFinHeight.set(0.75)
    shape.shapePartSize.set(2.0)
    shape.shapePartLengthScale.set(2.0)
    shape.shapePartWidthScale.set(3.0)
    assert_type(shape.shapeAxisOffset, BoolPlugOperator)
    assert_type(
        shape.shapeAxisOffsetDirection,
        ShapeAxisOffsetDirectionEnumPlugOperator,
    )
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
    shape.shapeAxisOffsetLength.set(5.0)
    shape.shapeAxisOffset.set(True)
    shape.shapeAxisOffsetDirection.set(
        ShapeAxisOffsetDirectionEnumPlugOperator.PLUS_1STAXIS
    )
    shape.shapeAxisTranslate.set(1.0, 2.0, 3.0)
    shape.shapeAxisRotate.set(0.0, 0.0, 90.0)
    shape.shapeAxisScale.set(2.0, 1.0, 1.0)
    assert_type(shape.showShapeOffsetLine, BoolPlugOperator)
    assert_type(shape.shapeOffsetLineTemplate, BoolPlugOperator)
    shape.showShapeOffsetLine.set(True)
    shape.shapeOffsetLineTemplate.set(False)


def controller_shape_bounds_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape.boundsMode, BoundsModeEnumPlugOperator)
    assert_type(shape.showBoundsPreview, BoolPlugOperator)
    assert_type(shape.customBounds1stAxis, CustomBounds1stAxisEnumPlugOperator)
    assert_type(shape.customBounds2ndAxis, CustomBounds2ndAxisEnumPlugOperator)
    assert_type(shape.customBoundsRootSize, DoublePlugOperator)
    assert_type(shape.customBoundsTranslate, CustomBoundsTranslatePlugOperator)
    assert_type(shape.customBoundsRotate, CustomBoundsRotatePlugOperator)
    assert_type(shape.customBoundsScale, CustomBoundsScalePlugOperator)
    assert_type(shape.customBoundsAxisOffsetLength, DoubleLinearPlugOperator)
    assert_type(shape.customBoundsAxisOffset, BoolPlugOperator)
    assert_type(
        shape.customBoundsAxisOffsetDirection,
        CustomBoundsAxisOffsetDirectionEnumPlugOperator,
    )
    assert_type(
        shape.customBoundsAxisTranslate, CustomBoundsAxisTranslatePlugOperator
    )
    assert_type(
        shape.customBoundsAxisRotate, CustomBoundsAxisRotatePlugOperator
    )
    assert_type(shape.customBoundsAxisScale, CustomBoundsAxisScalePlugOperator)
    assert_type(shape.customBoundsSize, DoublePlugOperator)
    shape.boundsMode.set(BoundsModeEnumPlugOperator.CUSTOM)
    shape.showBoundsPreview.set(True)
    shape.customBounds1stAxis.set(CustomBounds1stAxisEnumPlugOperator.PLUS_X)
    shape.customBounds2ndAxis.set(CustomBounds2ndAxisEnumPlugOperator.PLUS_Y)
    shape.customBoundsAxisOffsetDirection.set(
        CustomBoundsAxisOffsetDirectionEnumPlugOperator.PLUS_1STAXIS
    )
    shape.customBoundsTranslate.set(1.0, 2.0, 3.0)
    shape.customBoundsRotate.set(0.0, 0.0, 45.0)
    shape.customBoundsScale.set(1.0, 2.0, 3.0)
    shape.customBoundsAxisTranslate.set(1.0, 2.0, 3.0)
    shape.customBoundsAxisRotate.set(0.0, 0.0, 45.0)
    shape.customBoundsAxisScale.set(1.0, 2.0, 3.0)


def controller_shape_draw_style_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape.shapeLineWidth, FloatPlugOperator)
    assert_type(shape.shapeTransparency, FloatPlugOperator)
    assert_type(shape.shapeFillTransparency, FloatPlugOperator)
    assert_type(shape.shapeDrawOnTop, BoolPlugOperator)
    shape.shapeLineWidth.set(2.5)
    shape.shapeTransparency.set(0.375)
    shape.shapeFillTransparency.set(0.25)
    shape.shapeDrawOnTop.set(True)
