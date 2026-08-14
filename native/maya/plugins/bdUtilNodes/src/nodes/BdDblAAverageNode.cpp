#include "bdUtilNodes/nodes/BdDblAAverageNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/Average.h"

const MString BdDblAAverageNode::typeName("bdDblA_Average");
const MTypeId BdDblAAverageNode::typeId(0x001426FB);

MObject BdDblAAverageNode::input1;
MObject BdDblAAverageNode::input2;
MObject BdDblAAverageNode::output;

void* BdDblAAverageNode::creator() {
    return new BdDblAAverageNode();
}

MStatus BdDblAAverageNode::initialize() {
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

MStatus BdDblAAverageNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    const double input1Value = dataBlock
                                   .inputValue(input1, &status)
                                   .asDouble();
    if (!status) {
        return status;
    }
    const double input2Value = dataBlock
                                   .inputValue(input2, &status)
                                   .asDouble();
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.setDouble(
        bd_util_nodes::average(input1Value, input2Value)
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblAAverageNode::schedulingType() const {
    return MPxNode::kParallel;
}
