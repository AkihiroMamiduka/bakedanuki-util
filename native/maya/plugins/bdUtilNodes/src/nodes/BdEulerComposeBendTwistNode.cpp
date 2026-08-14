#include "bdUtilNodes/nodes/BdEulerComposeBendTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/BendTwistAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdEulerComposeBendTwistNode::typeName(
    "bdEuler_ComposeBendTwist"
);
const MTypeId BdEulerComposeBendTwistNode::typeId(0x0014270D);

MObject BdEulerComposeBendTwistNode::input;
MObject BdEulerComposeBendTwistNode::inputTwist;
MObject BdEulerComposeBendTwistNode::inputBendH;
MObject BdEulerComposeBendTwistNode::inputBendV;

MObject BdEulerComposeBendTwistNode::axisRotate;
MObject BdEulerComposeBendTwistNode::axisRotateX;
MObject BdEulerComposeBendTwistNode::axisRotateY;
MObject BdEulerComposeBendTwistNode::axisRotateZ;
MObject BdEulerComposeBendTwistNode::axisRotateOrder;

MObject BdEulerComposeBendTwistNode::order;
MObject BdEulerComposeBendTwistNode::outputRotateOrder;

MObject BdEulerComposeBendTwistNode::outputRotate;
MObject BdEulerComposeBendTwistNode::outputRotateX;
MObject BdEulerComposeBendTwistNode::outputRotateY;
MObject BdEulerComposeBendTwistNode::outputRotateZ;

void* BdEulerComposeBendTwistNode::creator() {
    return new BdEulerComposeBendTwistNode();
}

MStatus BdEulerComposeBendTwistNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

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

    const std::array<MObject, 11> inputs = {
        input,
        inputTwist,
        inputBendH,
        inputBendV,
        axisRotate,
        axisRotateX,
        axisRotateY,
        axisRotateZ,
        axisRotateOrder,
        order,
        outputRotateOrder,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputRotate);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdEulerComposeBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputRotate
        && requestedAttribute != outputRotateX
        && requestedAttribute != outputRotateY
        && requestedAttribute != outputRotateZ
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }
    const double3& inputValue = inputHandle.asDouble3();

    MDataHandle axisRotateHandle = dataBlock.inputValue(
        axisRotate,
        &status
    );
    if (!status) {
        return status;
    }
    const double3& axisRotateValue = axisRotateHandle.asDouble3();

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
    const short outputRotateOrderValue = dataBlock.inputValue(
        outputRotateOrder,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    MEulerRotation::RotationOrder axisRotateOrderValueMapped;
    MEulerRotation::RotationOrder outputRotateOrderValueMapped;
    MEulerRotation result;
    if (
        bd_util_nodes::toEulerRotationOrder(
            axisRotateOrderValue,
            axisRotateOrderValueMapped
        )
        && bd_util_nodes::toEulerRotationOrder(
            outputRotateOrderValue,
            outputRotateOrderValueMapped
        )
    ) {
        const MQuaternion resultQuaternion =
            bd_util_nodes::composeBendTwist(
                inputValue[0],
                inputValue[1],
                inputValue[2],
                MEulerRotation(
                    axisRotateValue[0],
                    axisRotateValue[1],
                    axisRotateValue[2],
                    axisRotateOrderValueMapped
                ).asQuaternion(),
                static_cast<bd_util_nodes::BendTwistOrder>(orderValue)
            );
        result = resultQuaternion.asEulerRotation();
        result.reorderIt(outputRotateOrderValueMapped);
    }

    MDataHandle outputValue = dataBlock.outputValue(
        outputRotate,
        &status
    );
    if (!status) {
        return status;
    }
    outputValue.set3Double(result.x, result.y, result.z);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdEulerComposeBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
