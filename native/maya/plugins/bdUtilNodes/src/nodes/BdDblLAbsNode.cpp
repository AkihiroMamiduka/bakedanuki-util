#include "bdUtilNodes/nodes/BdDblLAbsNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Absolute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLAbsNode::typeName("bdDblL_Abs");
const MTypeId BdDblLAbsNode::typeId(0x0007F04D);

MObject BdDblLAbsNode::input;
MObject BdDblLAbsNode::output;

void* BdDblLAbsNode::creator() {
    return new BdDblLAbsNode();
}

MStatus BdDblLAbsNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
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

    return attributeAffects(input, output);
}

MStatus BdDblLAbsNode::compute(
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
    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        bd_util_nodes::absolute(inputValue.asDouble())
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLAbsNode::schedulingType() const {
    return MPxNode::kParallel;
}
