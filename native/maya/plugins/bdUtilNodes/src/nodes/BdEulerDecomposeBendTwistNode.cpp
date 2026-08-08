#include "bdUtilNodes/nodes/BdEulerDecomposeBendTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/BendTwistAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdEulerDecomposeBendTwistNode::typeName(
    "bdEuler_DecomposeBendTwist"
);
const MTypeId BdEulerDecomposeBendTwistNode::typeId(0x0007F08D);

MObject BdEulerDecomposeBendTwistNode::inputRotate;
MObject BdEulerDecomposeBendTwistNode::inputRotateX;
MObject BdEulerDecomposeBendTwistNode::inputRotateY;
MObject BdEulerDecomposeBendTwistNode::inputRotateZ;
MObject BdEulerDecomposeBendTwistNode::inputRotateOrder;

MObject BdEulerDecomposeBendTwistNode::axisRotate;
MObject BdEulerDecomposeBendTwistNode::axisRotateX;
MObject BdEulerDecomposeBendTwistNode::axisRotateY;
MObject BdEulerDecomposeBendTwistNode::axisRotateZ;
MObject BdEulerDecomposeBendTwistNode::axisRotateOrder;

MObject BdEulerDecomposeBendTwistNode::order;

MObject BdEulerDecomposeBendTwistNode::output;
MObject BdEulerDecomposeBendTwistNode::outputTwist;
MObject BdEulerDecomposeBendTwistNode::outputBendH;
MObject BdEulerDecomposeBendTwistNode::outputBendV;
MObject BdEulerDecomposeBendTwistNode::bendRatio;

void* BdEulerDecomposeBendTwistNode::creator() {
    return new BdEulerDecomposeBendTwistNode();
}

MStatus BdEulerDecomposeBendTwistNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        inputRotate,
        inputRotateX,
        inputRotateY,
        inputRotateZ,
        "inputRotate",
        "ir",
        "inputRotateX",
        "irx",
        "inputRotateY",
        "iry",
        "inputRotateZ",
        "irz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(inputRotate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateOrderAttribute(
        enumAttributeFn,
        inputRotateOrder,
        "inputRotateOrder",
        "iro"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(inputRotateOrder);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        axisRotate,
        axisRotateX,
        axisRotateY,
        axisRotateZ,
        "axisRotate",
        "ar",
        "axisRotateX",
        "arx",
        "axisRotateY",
        "ary",
        "axisRotateZ",
        "arz"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(axisRotate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateOrderAttribute(
        enumAttributeFn,
        axisRotateOrder,
        "axisRotateOrder",
        "aro"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(axisRotateOrder);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBendTwistOrderAttribute(
        enumAttributeFn,
        order,
        "order",
        "ord"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(order);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBendTwistAttribute(
        numericAttributeFn,
        unitAttributeFn,
        output,
        outputTwist,
        outputBendH,
        outputBendV,
        "output",
        "o",
        "outputTwist",
        "otw",
        "outputBendH",
        "obh",
        "outputBendV",
        "obv"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        bendRatio,
        "bendRatio",
        "br",
        0.0
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMax(1.0);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(bendRatio);
    if (!status) {
        return status;
    }

    const std::array<MObject, 11> inputs = {
        inputRotate,
        inputRotateX,
        inputRotateY,
        inputRotateZ,
        inputRotateOrder,
        axisRotate,
        axisRotateX,
        axisRotateY,
        axisRotateZ,
        axisRotateOrder,
        order,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {output, bendRatio}) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdEulerDecomposeBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != output
        && requestedAttribute != outputTwist
        && requestedAttribute != outputBendH
        && requestedAttribute != outputBendV
        && requestedAttribute != bendRatio
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputRotateHandle = dataBlock.inputValue(
        inputRotate,
        &status
    );
    if (!status) {
        return status;
    }
    const double3& inputRotateValue = inputRotateHandle.asDouble3();

    MDataHandle axisRotateHandle = dataBlock.inputValue(
        axisRotate,
        &status
    );
    if (!status) {
        return status;
    }
    const double3& axisRotateValue = axisRotateHandle.asDouble3();

    const short inputRotateOrderValue = dataBlock.inputValue(
        inputRotateOrder,
        &status
    ).asShort();
    if (!status) {
        return status;
    }
    const short axisRotateOrderValue = dataBlock.inputValue(
        axisRotateOrder,
        &status
    ).asShort();
    if (!status) {
        return status;
    }
    const short orderValue = dataBlock.inputValue(order, &status).asShort();
    if (!status) {
        return status;
    }

    MEulerRotation::RotationOrder inputRotateOrderValueMapped;
    MEulerRotation::RotationOrder axisRotateOrderValueMapped;
    bd_util_nodes::BendTwistComponents result;
    if (
        bd_util_nodes::toEulerRotationOrder(
            inputRotateOrderValue,
            inputRotateOrderValueMapped
        )
        && bd_util_nodes::toEulerRotationOrder(
            axisRotateOrderValue,
            axisRotateOrderValueMapped
        )
    ) {
        result = bd_util_nodes::decomposeBendTwist(
            MEulerRotation(
                inputRotateValue[0],
                inputRotateValue[1],
                inputRotateValue[2],
                inputRotateOrderValueMapped
            ).asQuaternion(),
            MEulerRotation(
                axisRotateValue[0],
                axisRotateValue[1],
                axisRotateValue[2],
                axisRotateOrderValueMapped
            ).asQuaternion(),
            static_cast<bd_util_nodes::BendTwistOrder>(orderValue)
        );
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        result.twist,
        result.bendHorizontal,
        result.bendVertical
    );
    outputValue.setClean();

    MDataHandle bendRatioValue = dataBlock.outputValue(bendRatio, &status);
    if (!status) {
        return status;
    }
    bendRatioValue.setDouble(result.bendRatio);
    bendRatioValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdEulerDecomposeBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
