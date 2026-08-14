#include "bdUtilNodes/nodes/BdEulerLimitBendTwistNode.h"

#include <array>

#include <maya/MAngle.h>
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

const MString BdEulerLimitBendTwistNode::typeName(
    "bdEuler_LimitBendTwist"
);
const MTypeId BdEulerLimitBendTwistNode::typeId(0x00142712);

MObject BdEulerLimitBendTwistNode::inputRotate;
MObject BdEulerLimitBendTwistNode::inputRotateX;
MObject BdEulerLimitBendTwistNode::inputRotateY;
MObject BdEulerLimitBendTwistNode::inputRotateZ;
MObject BdEulerLimitBendTwistNode::inputRotateOrder;

MObject BdEulerLimitBendTwistNode::axisRotate;
MObject BdEulerLimitBendTwistNode::axisRotateX;
MObject BdEulerLimitBendTwistNode::axisRotateY;
MObject BdEulerLimitBendTwistNode::axisRotateZ;
MObject BdEulerLimitBendTwistNode::axisRotateOrder;

MObject BdEulerLimitBendTwistNode::order;
MObject BdEulerLimitBendTwistNode::bendLimitMode;

MObject BdEulerLimitBendTwistNode::minimum;
MObject BdEulerLimitBendTwistNode::minTwist;
MObject BdEulerLimitBendTwistNode::minBendH;
MObject BdEulerLimitBendTwistNode::minBendV;

MObject BdEulerLimitBendTwistNode::maximum;
MObject BdEulerLimitBendTwistNode::maxTwist;
MObject BdEulerLimitBendTwistNode::maxBendH;
MObject BdEulerLimitBendTwistNode::maxBendV;

MObject BdEulerLimitBendTwistNode::output;
MObject BdEulerLimitBendTwistNode::outputTwist;
MObject BdEulerLimitBendTwistNode::outputBendH;
MObject BdEulerLimitBendTwistNode::outputBendV;

MObject BdEulerLimitBendTwistNode::outputRotateOrder;
MObject BdEulerLimitBendTwistNode::outputRotate;
MObject BdEulerLimitBendTwistNode::outputRotateX;
MObject BdEulerLimitBendTwistNode::outputRotateY;
MObject BdEulerLimitBendTwistNode::outputRotateZ;

void* BdEulerLimitBendTwistNode::creator() {
    return new BdEulerLimitBendTwistNode();
}

MStatus BdEulerLimitBendTwistNode::initialize() {
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

    status = bd_util_nodes::createRotateOrderAttribute(
        enumAttributeFn,
        outputRotateOrder,
        "outputRotateOrder",
        "oro"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(outputRotateOrder);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        outputRotate,
        outputRotateX,
        outputRotateY,
        outputRotateZ,
        "outputRotate",
        "ort",
        "outputRotateX",
        "orx",
        "outputRotateY",
        "ory",
        "outputRotateZ",
        "orz"
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
    status = addAttribute(outputRotate);
    if (!status) {
        return status;
    }

    const std::array<MObject, 20> inputs = {
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
        for (const MObject& outputAttribute : {output, outputRotate}) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return attributeAffects(outputRotateOrder, outputRotate);
}

MStatus BdEulerLimitBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != output
        && requestedAttribute != outputTwist
        && requestedAttribute != outputBendH
        && requestedAttribute != outputBendV
        && requestedAttribute != outputRotate
        && requestedAttribute != outputRotateX
        && requestedAttribute != outputRotateY
        && requestedAttribute != outputRotateZ
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
    const short modeValue = dataBlock.inputValue(
        bendLimitMode,
        &status
    ).asShort();
    if (!status) {
        return status;
    }
    const short outputRotateOrderValue = dataBlock.inputValue(
        outputRotateOrder,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    MEulerRotation::RotationOrder inputRotateOrderMapped =
        MEulerRotation::kXYZ;
    MEulerRotation::RotationOrder axisRotateOrderMapped =
        MEulerRotation::kXYZ;
    MEulerRotation::RotationOrder outputRotateOrderMapped =
        MEulerRotation::kXYZ;
    bd_util_nodes::BendTwistLimitResult result;
    const bool validInputOrders = bd_util_nodes::toEulerRotationOrder(
        inputRotateOrderValue,
        inputRotateOrderMapped
    ) && bd_util_nodes::toEulerRotationOrder(
        axisRotateOrderValue,
        axisRotateOrderMapped
    );
    if (validInputOrders) {
        result = bd_util_nodes::limitBendTwist(
            MEulerRotation(
                inputRotateValue[0],
                inputRotateValue[1],
                inputRotateValue[2],
                inputRotateOrderMapped
            ).asQuaternion(),
            MEulerRotation(
                axisRotateValue[0],
                axisRotateValue[1],
                axisRotateValue[2],
                axisRotateOrderMapped
            ).asQuaternion(),
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
    }

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

    MEulerRotation outputRotation;
    if (
        bd_util_nodes::toEulerRotationOrder(
            outputRotateOrderValue,
            outputRotateOrderMapped
        )
    ) {
        outputRotation = result.quaternion.asEulerRotation();
        outputRotation.reorderIt(outputRotateOrderMapped);
    }

    MDataHandle outputRotateValue = dataBlock.outputValue(
        outputRotate,
        &status
    );
    if (!status) {
        return status;
    }
    outputRotateValue.set3Double(
        outputRotation.x,
        outputRotation.y,
        outputRotation.z
    );
    outputRotateValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdEulerLimitBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
