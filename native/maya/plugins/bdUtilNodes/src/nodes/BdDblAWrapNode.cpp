#include "bdUtilNodes/nodes/BdDblAWrapNode.h"

#include <array>

#include <maya/MAngle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Angle.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblAWrapNode::typeName("bdDblA_Wrap");
const MTypeId BdDblAWrapNode::typeId(0x0007F080);

MObject BdDblAWrapNode::input;
MObject BdDblAWrapNode::minimum;
MObject BdDblAWrapNode::maximum;
MObject BdDblAWrapNode::output;

void* BdDblAWrapNode::creator() {
    return new BdDblAWrapNode();
}

MStatus BdDblAWrapNode::initialize() {
    MFnUnitAttribute attributeFn;
    const double halfRotationRadians =
        MAngle(180.0, MAngle::kDegrees).asRadians();

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        input,
        "input",
        "i",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        minimum,
        "min",
        "mn",
        -halfRotationRadians
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(minimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        maximum,
        "max",
        "mx",
        halfRotationRadians
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(maximum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 3> inputAttributes = {
        input,
        minimum,
        maximum,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblAWrapNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputValue = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }

    MDataHandle minimumValue = dataBlock.inputValue(minimum, &status);
    if (!status) {
        return status;
    }

    MDataHandle maximumValue = dataBlock.inputValue(maximum, &status);
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        bd_util_nodes::wrapAngle(
            inputValue.asDouble(),
            minimumValue.asDouble(),
            maximumValue.asDouble()
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblAWrapNode::schedulingType() const {
    return MPxNode::kParallel;
}
