#include "bdUtilNodes/nodes/BdDblAverageNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Average.h"

const MString BdDblAverageNode::typeName("bdDbl_Average");
const MTypeId BdDblAverageNode::typeId(0x001426B1);

MObject BdDblAverageNode::input1;
MObject BdDblAverageNode::input2;
MObject BdDblAverageNode::output;

void* BdDblAverageNode::creator() {
    return new BdDblAverageNode();
}

MStatus BdDblAverageNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        input1,
        "input1",
        "i1",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(input1);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        input2,
        "input2",
        "i2",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(input2);
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

    status = attributeAffects(input1, output);
    if (!status) {
        return status;
    }
    return attributeAffects(input2, output);
}

MStatus BdDblAverageNode::compute(
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

MPxNode::SchedulingType BdDblAverageNode::schedulingType() const {
    return MPxNode::kParallel;
}
