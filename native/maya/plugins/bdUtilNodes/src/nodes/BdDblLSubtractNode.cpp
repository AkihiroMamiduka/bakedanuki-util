#include "bdUtilNodes/nodes/BdDblLSubtractNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLSubtractNode::typeName("bdDblL_Subtract");
const MTypeId BdDblLSubtractNode::typeId(0x0007F03B);

MObject BdDblLSubtractNode::input1;
MObject BdDblLSubtractNode::input2;
MObject BdDblLSubtractNode::output;

void* BdDblLSubtractNode::creator() {
    return new BdDblLSubtractNode();
}

MStatus BdDblLSubtractNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = attributeAffects(input1, output);
    if (!status) {
        return status;
    }

    return attributeAffects(input2, output);
}

MStatus BdDblLSubtractNode::compute(
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

MPxNode::SchedulingType BdDblLSubtractNode::schedulingType() const {
    return MPxNode::kParallel;
}
