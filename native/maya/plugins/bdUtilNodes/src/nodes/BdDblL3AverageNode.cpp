#include "bdUtilNodes/nodes/BdDblL3AverageNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Average.h"

const MString BdDblL3AverageNode::typeName("bdDblL3_Average");
const MTypeId BdDblL3AverageNode::typeId(0x0007F041);

MObject BdDblL3AverageNode::input1;
MObject BdDblL3AverageNode::input1X;
MObject BdDblL3AverageNode::input1Y;
MObject BdDblL3AverageNode::input1Z;

MObject BdDblL3AverageNode::input2;
MObject BdDblL3AverageNode::input2X;
MObject BdDblL3AverageNode::input2Y;
MObject BdDblL3AverageNode::input2Z;

MObject BdDblL3AverageNode::output;
MObject BdDblL3AverageNode::outputX;
MObject BdDblL3AverageNode::outputY;
MObject BdDblL3AverageNode::outputZ;

void* BdDblL3AverageNode::creator() {
    return new BdDblL3AverageNode();
}

MStatus BdDblL3AverageNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        input1,
        input1X,
        input1Y,
        input1Z,
        "input1",
        "i1",
        "input1X",
        "i1x",
        "input1Y",
        "i1y",
        "input1Z",
        "i1z",
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        input2,
        input2X,
        input2Y,
        input2Z,
        "input2",
        "i2",
        "input2X",
        "i2x",
        "input2Y",
        "i2y",
        "input2Z",
        "i2z",
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

    const std::array<MObject, 8> inputAttributes = {
        input1,
        input1X,
        input1Y,
        input1Z,
        input2,
        input2X,
        input2Y,
        input2Z,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdDblL3AverageNode::compute(
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
    MDataHandle input1Handle = dataBlock.inputValue(input1, &status);
    if (!status) {
        return status;
    }
    MDataHandle input2Handle = dataBlock.inputValue(input2, &status);
    if (!status) {
        return status;
    }
    const double3& input1Value = input1Handle.asDouble3();
    const double3& input2Value = input2Handle.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        bd_util_nodes::average(input1Value[0], input2Value[0]),
        bd_util_nodes::average(input1Value[1], input2Value[1]),
        bd_util_nodes::average(input1Value[2], input2Value[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3AverageNode::schedulingType() const {
    return MPxNode::kParallel;
}
