#include "bdUtilNodes/nodes/BdQuatComposeBendTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/BendTwistAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdQuatComposeBendTwistNode::typeName(
    "bdQuat_ComposeBendTwist"
);
const MTypeId BdQuatComposeBendTwistNode::typeId(0x0007F08A);

MObject BdQuatComposeBendTwistNode::input;
MObject BdQuatComposeBendTwistNode::inputTwist;
MObject BdQuatComposeBendTwistNode::inputBendH;
MObject BdQuatComposeBendTwistNode::inputBendV;

MObject BdQuatComposeBendTwistNode::axisQuat;
MObject BdQuatComposeBendTwistNode::axisQuatX;
MObject BdQuatComposeBendTwistNode::axisQuatY;
MObject BdQuatComposeBendTwistNode::axisQuatZ;
MObject BdQuatComposeBendTwistNode::axisQuatW;

MObject BdQuatComposeBendTwistNode::order;

MObject BdQuatComposeBendTwistNode::outputQuat;
MObject BdQuatComposeBendTwistNode::outputQuatX;
MObject BdQuatComposeBendTwistNode::outputQuatY;
MObject BdQuatComposeBendTwistNode::outputQuatZ;
MObject BdQuatComposeBendTwistNode::outputQuatW;

void* BdQuatComposeBendTwistNode::creator() {
    return new BdQuatComposeBendTwistNode();
}

MStatus BdQuatComposeBendTwistNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;

    status = bd_util_nodes::createBendTwistAttribute(
        numericAttributeFn,
        unitAttributeFn,
        input,
        inputTwist,
        inputBendH,
        inputBendV,
        "input",
        "i",
        "inputTwist",
        "itw",
        "inputBendH",
        "ibh",
        "inputBendV",
        "ibv"
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
    status = addAttribute(input);
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

    MFnEnumAttribute enumAttributeFn;
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

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        outputQuat,
        outputQuatX,
        outputQuatY,
        outputQuatZ,
        outputQuatW,
        "outputQuat",
        "oq",
        "outputQuatX",
        "oqx",
        "outputQuatY",
        "oqy",
        "outputQuatZ",
        "oqz",
        "outputQuatW",
        "oqw"
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
    status = addAttribute(outputQuat);
    if (!status) {
        return status;
    }

    const std::array<MObject, 10> inputs = {
        input,
        inputTwist,
        inputBendH,
        inputBendV,
        axisQuat,
        axisQuatX,
        axisQuatY,
        axisQuatZ,
        axisQuatW,
        order,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputQuat);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdQuatComposeBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputQuat
        && requestedAttribute != outputQuatX
        && requestedAttribute != outputQuatY
        && requestedAttribute != outputQuatZ
        && requestedAttribute != outputQuatW
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(
        input,
        &status
    );
    if (!status) {
        return status;
    }
    const double3& inputValue = inputHandle.asDouble3();

    MDataHandle axisOrientationHandle = dataBlock.inputValue(
        axisQuat,
        &status
    );
    if (!status) {
        return status;
    }
    const double4& axisOrientationValue =
        axisOrientationHandle.asDouble4();
    const short orderValue = dataBlock.inputValue(order, &status).asShort();
    if (!status) {
        return status;
    }

    const MQuaternion result = bd_util_nodes::composeBendTwist(
        inputValue[0],
        inputValue[1],
        inputValue[2],
        MQuaternion(
            axisOrientationValue[0],
            axisOrientationValue[1],
            axisOrientationValue[2],
            axisOrientationValue[3]
        ),
        static_cast<bd_util_nodes::BendTwistOrder>(orderValue)
    );

    MDataHandle outputValue = dataBlock.outputValue(outputQuat, &status);
    if (!status) {
        return status;
    }
    outputValue.set4Double(
        result.x,
        result.y,
        result.z,
        result.w
    );
    outputValue.setClean();

    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdQuatComposeBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
