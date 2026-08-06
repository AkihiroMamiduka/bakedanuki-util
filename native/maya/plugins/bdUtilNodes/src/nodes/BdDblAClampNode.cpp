#include "bdUtilNodes/nodes/BdDblAClampNode.h"

#include <array>

#include <maya/MAngle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Clamp.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblAClampNode::typeName("bdDblA_Clamp");
const MTypeId BdDblAClampNode::typeId(0x0007F075);

MObject BdDblAClampNode::input;
MObject BdDblAClampNode::minimum;
MObject BdDblAClampNode::maximum;
MObject BdDblAClampNode::output;

void* BdDblAClampNode::creator() {
    return new BdDblAClampNode();
}

MStatus BdDblAClampNode::initialize() {
    MFnUnitAttribute attributeFn;
    const double fullRotationRadians =
        MAngle(360.0, MAngle::kDegrees).asRadians();

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
        0.0
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
        fullRotationRadians
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

MStatus BdDblAClampNode::compute(
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
        bd_util_nodes::clamp(
            inputValue.asDouble(),
            minimumValue.asDouble(),
            maximumValue.asDouble()
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblAClampNode::schedulingType() const {
    return MPxNode::kParallel;
}
