#include "bdUtilNodes/nodes/BdDblASubtractNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblASubtractNode::typeName("bdDblA_Subtract");
const MTypeId BdDblASubtractNode::typeId(0x0007F06D);

MObject BdDblASubtractNode::input1;
MObject BdDblASubtractNode::input2;
MObject BdDblASubtractNode::output;

void* BdDblASubtractNode::creator() {
    return new BdDblASubtractNode();
}

MStatus BdDblASubtractNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        input1,
        "input1",
        "i1",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input1);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        input2,
        "input2",
        "i2",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input2);
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

    status = attributeAffects(input1, output);
    if (!status) {
        return status;
    }

    return attributeAffects(input2, output);
}

MStatus BdDblASubtractNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle input1Value = dataBlock.inputValue(input1, &status);
    if (!status) {
        return status;
    }

    MDataHandle input2Value = dataBlock.inputValue(input2, &status);
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        input1Value.asDouble() - input2Value.asDouble()
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblASubtractNode::schedulingType() const {
    return MPxNode::kParallel;
}
