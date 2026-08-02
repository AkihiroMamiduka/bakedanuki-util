#include "bdUtilNodes/BdDblClampNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Clamp.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdDblClampNode::typeName("bdDbl_Clamp");
const MTypeId BdDblClampNode::typeId(0x0007F024);

MObject BdDblClampNode::input;
MObject BdDblClampNode::minimum;
MObject BdDblClampNode::maximum;
MObject BdDblClampNode::output;

void* BdDblClampNode::creator() {
    return new BdDblClampNode();
}

MStatus BdDblClampNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        input,
        "input",
        "i",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        minimum,
        "minimum",
        "min",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(minimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        maximum,
        "maximum",
        "max",
        1.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(maximum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputNumericAttribute(attributeFn);
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

MStatus BdDblClampNode::compute(
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

MPxNode::SchedulingType BdDblClampNode::schedulingType() const {
    return MPxNode::kParallel;
}
