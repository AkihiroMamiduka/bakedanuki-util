#include "bdUtilNodes/nodes/BdDblL3AbsNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Absolute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3AbsNode::typeName("bdDblL3_Abs");
const MTypeId BdDblL3AbsNode::typeId(0x0007F04E);

MObject BdDblL3AbsNode::input;
MObject BdDblL3AbsNode::inputX;
MObject BdDblL3AbsNode::inputY;
MObject BdDblL3AbsNode::inputZ;

MObject BdDblL3AbsNode::output;
MObject BdDblL3AbsNode::outputX;
MObject BdDblL3AbsNode::outputY;
MObject BdDblL3AbsNode::outputZ;

void* BdDblL3AbsNode::creator() {
    return new BdDblL3AbsNode();
}

MStatus BdDblL3AbsNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
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

MStatus BdDblL3AbsNode::compute(
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

MPxNode::SchedulingType BdDblL3AbsNode::schedulingType() const {
    return MPxNode::kParallel;
}
