#include "bdUtilNodes/nodes/BdQuatLimitBendTwistNode.h"

#include <array>

#include <maya/MAngle.h>
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

const MString BdQuatLimitBendTwistNode::typeName(
    "bdQuat_LimitBendTwist"
);
const MTypeId BdQuatLimitBendTwistNode::typeId(0x0007F092);

MObject BdQuatLimitBendTwistNode::inputQuat;
MObject BdQuatLimitBendTwistNode::inputQuatX;
MObject BdQuatLimitBendTwistNode::inputQuatY;
MObject BdQuatLimitBendTwistNode::inputQuatZ;
MObject BdQuatLimitBendTwistNode::inputQuatW;

MObject BdQuatLimitBendTwistNode::axisQuat;
MObject BdQuatLimitBendTwistNode::axisQuatX;
MObject BdQuatLimitBendTwistNode::axisQuatY;
MObject BdQuatLimitBendTwistNode::axisQuatZ;
MObject BdQuatLimitBendTwistNode::axisQuatW;

MObject BdQuatLimitBendTwistNode::order;
MObject BdQuatLimitBendTwistNode::bendLimitMode;

MObject BdQuatLimitBendTwistNode::minimum;
MObject BdQuatLimitBendTwistNode::minTwist;
MObject BdQuatLimitBendTwistNode::minBendH;
MObject BdQuatLimitBendTwistNode::minBendV;

MObject BdQuatLimitBendTwistNode::maximum;
MObject BdQuatLimitBendTwistNode::maxTwist;
MObject BdQuatLimitBendTwistNode::maxBendH;
MObject BdQuatLimitBendTwistNode::maxBendV;

MObject BdQuatLimitBendTwistNode::output;
MObject BdQuatLimitBendTwistNode::outputTwist;
MObject BdQuatLimitBendTwistNode::outputBendH;
MObject BdQuatLimitBendTwistNode::outputBendV;

MObject BdQuatLimitBendTwistNode::outputQuat;
MObject BdQuatLimitBendTwistNode::outputQuatX;
MObject BdQuatLimitBendTwistNode::outputQuatY;
MObject BdQuatLimitBendTwistNode::outputQuatZ;
MObject BdQuatLimitBendTwistNode::outputQuatW;

void* BdQuatLimitBendTwistNode::creator() {
    return new BdQuatLimitBendTwistNode();
}

MStatus BdQuatLimitBendTwistNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

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

    status = bd_util_nodes::createBendLimitModeAttribute(
        enumAttributeFn,
        bendLimitMode,
        "bendLimitMode",
        "blm"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(bendLimitMode);
    if (!status) {
        return status;
    }

    const double halfRotationRadians =
        MAngle(180.0, MAngle::kDegrees).asRadians();
    status = bd_util_nodes::createBendTwistAttribute(
        numericAttributeFn,
        unitAttributeFn,
        minimum,
        minTwist,
        minBendH,
        minBendV,
        "min",
        "mn",
        "minTwist",
        "mntw",
        "minBendH",
        "mnbh",
        "minBendV",
        "mnbv",
        -halfRotationRadians,
        -halfRotationRadians,
        -halfRotationRadians
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
    status = addAttribute(minimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBendTwistAttribute(
        numericAttributeFn,
        unitAttributeFn,
        maximum,
        maxTwist,
        maxBendH,
        maxBendV,
        "max",
        "mx",
        "maxTwist",
        "mxtw",
        "maxBendH",
        "mxbh",
        "maxBendV",
        "mxbv",
        halfRotationRadians,
        halfRotationRadians,
        halfRotationRadians
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
    status = addAttribute(maximum);
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

    const std::array<MObject, 20> inputs = {
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
        order,
        bendLimitMode,
        minimum,
        minTwist,
        minBendH,
        minBendV,
        maximum,
        maxTwist,
        maxBendH,
        maxBendV,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {output, outputQuat}) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdQuatLimitBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != output
        && requestedAttribute != outputTwist
        && requestedAttribute != outputBendH
        && requestedAttribute != outputBendV
        && requestedAttribute != outputQuat
        && requestedAttribute != outputQuatX
        && requestedAttribute != outputQuatY
        && requestedAttribute != outputQuatZ
        && requestedAttribute != outputQuatW
    ) {
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

    MDataHandle minimumHandle = dataBlock.inputValue(minimum, &status);
    if (!status) {
        return status;
    }
    const double3& minimumValue = minimumHandle.asDouble3();

    MDataHandle maximumHandle = dataBlock.inputValue(maximum, &status);
    if (!status) {
        return status;
    }
    const double3& maximumValue = maximumHandle.asDouble3();

    const short orderValue = dataBlock.inputValue(order, &status).asShort();
    if (!status) {
        return status;
    }
    const short modeValue = dataBlock.inputValue(
        bendLimitMode,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    const bd_util_nodes::BendTwistLimitResult result =
        bd_util_nodes::limitBendTwist(
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
            ),
            static_cast<bd_util_nodes::BendTwistOrder>(orderValue),
            static_cast<bd_util_nodes::BendLimitMode>(modeValue),
            {
                minimumValue[0],
                minimumValue[1],
                minimumValue[2],
                maximumValue[0],
                maximumValue[1],
                maximumValue[2],
            }
        );

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        result.components.twist,
        result.components.bendHorizontal,
        result.components.bendVertical
    );
    outputValue.setClean();

    MDataHandle outputQuatValue = dataBlock.outputValue(
        outputQuat,
        &status
    );
    if (!status) {
        return status;
    }
    outputQuatValue.set4Double(
        result.quaternion.x,
        result.quaternion.y,
        result.quaternion.z,
        result.quaternion.w
    );
    outputQuatValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdQuatLimitBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
