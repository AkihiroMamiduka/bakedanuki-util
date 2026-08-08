#include "bdUtilNodes/nodes/BdEulerDecomposeTwistNode.h"

#include <array>
#include <utility>

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

namespace {

enum class RotateOrderValue : short {
    kXYZ = 0,
    kYZX = 1,
    kZXY = 2,
    kXZY = 3,
    kYXZ = 4,
    kZYX = 5,
};

MStatus createRotateOrderAttribute(
    MObject& attribute,
    const char* longName,
    const char* shortName
) {
    MStatus status;
    MFnEnumAttribute attributeFn;
    attribute = attributeFn.create(
        longName,
        shortName,
        static_cast<short>(RotateOrderValue::kXYZ),
        &status
    );
    if (!status) {
        return status;
    }

    for (const auto& field : {
             std::pair<const char*, RotateOrderValue>{
                 "xyz",
                 RotateOrderValue::kXYZ,
             },
             std::pair<const char*, RotateOrderValue>{
                 "yzx",
                 RotateOrderValue::kYZX,
             },
             std::pair<const char*, RotateOrderValue>{
                 "zxy",
                 RotateOrderValue::kZXY,
             },
             std::pair<const char*, RotateOrderValue>{
                 "xzy",
                 RotateOrderValue::kXZY,
             },
             std::pair<const char*, RotateOrderValue>{
                 "yxz",
                 RotateOrderValue::kYXZ,
             },
             std::pair<const char*, RotateOrderValue>{
                 "zyx",
                 RotateOrderValue::kZYX,
             },
         }) {
        status = attributeFn.addField(
            field.first,
            static_cast<short>(field.second)
        );
        if (!status) {
            return status;
        }
    }

    status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    return attributeFn.setKeyable(true);
}

bool toEulerRotationOrder(
    short value,
    MEulerRotation::RotationOrder& order
) {
    switch (static_cast<RotateOrderValue>(value)) {
        case RotateOrderValue::kXYZ:
            order = MEulerRotation::kXYZ;
            return true;
        case RotateOrderValue::kYZX:
            order = MEulerRotation::kYZX;
            return true;
        case RotateOrderValue::kZXY:
            order = MEulerRotation::kZXY;
            return true;
        case RotateOrderValue::kXZY:
            order = MEulerRotation::kXZY;
            return true;
        case RotateOrderValue::kYXZ:
            order = MEulerRotation::kYXZ;
            return true;
        case RotateOrderValue::kZYX:
            order = MEulerRotation::kZYX;
            return true;
    }
    return false;
}

}  // namespace

const MString BdEulerDecomposeTwistNode::typeName(
    "bdEuler_DecomposeTwist"
);
const MTypeId BdEulerDecomposeTwistNode::typeId(0x0007F08C);

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

    status = createRotateOrderAttribute(
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

    status = createRotateOrderAttribute(
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
        toEulerRotationOrder(inputRotateOrderValue, inputOrder)
        && toEulerRotationOrder(axisRotateOrderValue, axisOrder)
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
