#include "bdUtilNodes/nodes/BdDbl3AbsNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Absolute.h"
#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDbl3AbsNode::typeName("bdDbl3_Abs");
const MTypeId BdDbl3AbsNode::typeId(0x0007F027);

MObject BdDbl3AbsNode::input;
MObject BdDbl3AbsNode::inputX;
MObject BdDbl3AbsNode::inputY;
MObject BdDbl3AbsNode::inputZ;

MObject BdDbl3AbsNode::output;
MObject BdDbl3AbsNode::outputX;
MObject BdDbl3AbsNode::outputY;
MObject BdDbl3AbsNode::outputZ;

void* BdDbl3AbsNode::creator() {
    return new BdDbl3AbsNode();
}

MStatus BdDbl3AbsNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
        input,
        inputX,
        inputY,
        inputZ,
        "input",
        "i",
        "inputX",
        "ix",
        "inputY",
        "iy",
        "inputZ",
        "iz",
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
        output,
        outputX,
        outputY,
        outputZ,
        "output",
        "o",
        "outputX",
        "ox",
        "outputY",
        "oy",
        "outputZ",
        "oz",
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

    const std::array<MObject, 4> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDbl3AbsNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != output
        && requestedAttribute != outputX
        && requestedAttribute != outputY
        && requestedAttribute != outputZ
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputValue = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }
    const double3& inputComponents = inputValue.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        bd_util_nodes::absolute(inputComponents[0]),
        bd_util_nodes::absolute(inputComponents[1]),
        bd_util_nodes::absolute(inputComponents[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDbl3AbsNode::schedulingType() const {
    return MPxNode::kParallel;
}
