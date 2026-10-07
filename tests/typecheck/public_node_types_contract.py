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
)
from bd_util.maya.node.operator.node.dag.transform.joint import Joint


def joint_list_contract() -> None:
    nodes = bdu.Nodes()
    joints: list[bdu.node_types.Joint] = []
    for i in range(10):
        joints.append(nodes.create.joint(name=f"j_{i}"))

    assert_type(joints, list[Joint])
    for joint in joints:
        joint.t.set(1, 2, 3)
        joint.r.set(3, 4, 5)
        joint.s.set(6, 7, 8)
        joint.v.set(False)
        assert_type(joint, Joint)

    other = nodes.create.plusMinusAverage()
    joints.append(other)  # pyright: ignore[reportArgumentType]


def versioned_node_type_list_contract() -> None:
    common_nodes = bdu.Nodes()
    nodes_2025 = bdu.Nodes(typing_maya_version="2025")
    nodes_2026 = bdu.Nodes(typing_maya_version="2026")
    nodes_2027 = bdu.Nodes(typing_maya_version="2027")

    common: list[bdu.node_types.Absolute] = [common_nodes.create.absolute()]
    absolute_2025: list[bdu.node_types.maya2025.Absolute] = [
        nodes_2025.create.absolute()
    ]
    absolute_2026: list[bdu.node_types.maya2026.Absolute] = [
        nodes_2026.create.absolute()
    ]
    absolute_2027: list[bdu.node_types.maya2027.Absolute] = [
        nodes_2027.create.absolute()
    ]

    assert_type(
        common[0].input,
        DoubleLinearPlugOperator | DoublePlugOperator,
    )
    assert_type(absolute_2025[0].input, DoubleLinearPlugOperator)
    assert_type(absolute_2026[0].input, DoublePlugOperator)
    assert_type(absolute_2027[0].input, DoublePlugOperator)

    bdu.node_types.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    bdu.node_types.maya2025.AbsoluteDL  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
    assert_type(
        nodes_2026.create.absoluteDL(),
        bdu.node_types.maya2026.AbsoluteDL,
    )


def controller_shape_offset_line_contract() -> None:
    _, shape = bdu.Nodes().create.controllerShape()
    assert_type(shape, bdu.node_types.BdControllerShape)
    assert_type(shape.shape1stAxis, Shape1stAxisEnumPlugOperator)
    assert_type(shape.shape2ndAxis, Shape2ndAxisEnumPlugOperator)
    assert_type(shape.shapeAnimationTransformMatrix, DataMatrixPlugOperator)
    assert_type(shape.shapeAxisOffsetLength, DoubleLinearPlugOperator)
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
    assert_type(shape.shapeDrawOnTop, BoolPlugOperator)
    shape.shapeLineWidth.set(2.5)
    shape.shapeTransparency.set(0.375)
    shape.shapeDrawOnTop.set(True)
