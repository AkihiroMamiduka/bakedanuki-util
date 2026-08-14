#include "bdUtilNodes/nodes/BdQuatDecomposeTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdQuatDecomposeTwistNode::typeName(
    "bdQuat_DecomposeTwist"
);
const MTypeId BdQuatDecomposeTwistNode::typeId(0x0014270A);

MObject BdQuatDecomposeTwistNode::inputQuat;
MObject BdQuatDecomposeTwistNode::inputQuatX;
MObject BdQuatDecomposeTwistNode::inputQuatY;
MObject BdQuatDecomposeTwistNode::inputQuatZ;
MObject BdQuatDecomposeTwistNode::inputQuatW;

MObject BdQuatDecomposeTwistNode::axisQuat;
MObject BdQuatDecomposeTwistNode::axisQuatX;
MObject BdQuatDecomposeTwistNode::axisQuatY;
MObject BdQuatDecomposeTwistNode::axisQuatZ;
MObject BdQuatDecomposeTwistNode::axisQuatW;

MObject BdQuatDecomposeTwistNode::outputTwist;

void* BdQuatDecomposeTwistNode::creator() {
    return new BdQuatDecomposeTwistNode();
}

MStatus BdQuatDecomposeTwistNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        "inputQuat",
        "iq",
        "inputQuatX",
        "iqx",
        "inputQuatY",
        "iqy",
        "inputQuatZ",
        "iqz",
        "inputQuatW",
        "iqw"
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
    status = addAttribute(inputQuat);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        axisQuat,
        axisQuatX,
        axisQuatY,
        axisQuatZ,
        axisQuatW,
        "axisQuat",
        "aq",
        "axisQuatX",
        "aqx",
        "axisQuatY",
        "aqy",
        "axisQuatZ",
        "aqz",
        "axisQuatW",
        "aqw"
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
    status = addAttribute(axisQuat);
    if (!status) {
        return status;
    }

    MFnUnitAttribute unitAttributeFn;
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
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        axisQuat,
        axisQuatX,
        axisQuatY,
        axisQuatZ,
        axisQuatW,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputTwist);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdQuatDecomposeTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != outputTwist) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(inputQuat, &status);
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();

    MDataHandle axisHandle = dataBlock.inputValue(axisQuat, &status);
    if (!status) {
        return status;
    }
    const double4& axisValue = axisHandle.asDouble4();

    const double result = bd_util_nodes::decomposeTwist(
        MQuaternion(
            inputValue[0],
            inputValue[1],
            inputValue[2],
            inputValue[3]
        ),
        MQuaternion(
            axisValue[0],
            axisValue[1],
            axisValue[2],
            axisValue[3]
        )
    );

    MDataHandle twistValue = dataBlock.outputValue(outputTwist, &status);
    if (!status) {
        return status;
    }
    twistValue.setDouble(result);
    twistValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdQuatDecomposeTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
