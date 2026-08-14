#include "bdUtilNodes/nodes/BdEulerDecomposeTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdEulerDecomposeTwistNode::typeName(
    "bdEuler_DecomposeTwist"
);
const MTypeId BdEulerDecomposeTwistNode::typeId(0x0014270B);

MObject BdEulerDecomposeTwistNode::inputRotate;
MObject BdEulerDecomposeTwistNode::inputRotateX;
MObject BdEulerDecomposeTwistNode::inputRotateY;
MObject BdEulerDecomposeTwistNode::inputRotateZ;
MObject BdEulerDecomposeTwistNode::inputRotateOrder;

MObject BdEulerDecomposeTwistNode::axisRotate;
MObject BdEulerDecomposeTwistNode::axisRotateX;
MObject BdEulerDecomposeTwistNode::axisRotateY;
MObject BdEulerDecomposeTwistNode::axisRotateZ;
MObject BdEulerDecomposeTwistNode::axisRotateOrder;

MObject BdEulerDecomposeTwistNode::outputTwist;

void* BdEulerDecomposeTwistNode::creator() {
    return new BdEulerDecomposeTwistNode();
}

MStatus BdEulerDecomposeTwistNode::initialize() {
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outputTwist,
        "outputTwist",
        "otw",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(outputTwist);
    if (!status) {
        return status;
    }

    const std::array<MObject, 10> inputs = {
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
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputTwist);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdEulerDecomposeTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != outputTwist) {
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

    MEulerRotation::RotationOrder inputOrder;
    MEulerRotation::RotationOrder axisOrder;
    double result = 0.0;
    if (
        bd_util_nodes::toEulerRotationOrder(
            inputRotateOrderValue,
            inputOrder
        )
        && bd_util_nodes::toEulerRotationOrder(
            axisRotateOrderValue,
            axisOrder
        )
    ) {
        result = bd_util_nodes::decomposeTwist(
            MEulerRotation(
                inputRotateValue[0],
                inputRotateValue[1],
                inputRotateValue[2],
                inputOrder
            ).asQuaternion(),
            MEulerRotation(
                axisRotateValue[0],
                axisRotateValue[1],
                axisRotateValue[2],
                axisOrder
            ).asQuaternion()
        );
    }

    MDataHandle outputValue = dataBlock.outputValue(outputTwist, &status);
    if (!status) {
        return status;
    }
    outputValue.setDouble(result);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdEulerDecomposeTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
