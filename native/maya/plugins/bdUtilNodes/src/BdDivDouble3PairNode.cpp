#include "bdUtilNodes/BdDivDouble3PairNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"
#include "bdUtilNodes/SafeDivision.h"

const MString BdDivDouble3PairNode::typeName("bdDivDouble3Pair");
const MTypeId BdDivDouble3PairNode::typeId(0x0007F00E);

MObject BdDivDouble3PairNode::input1;
MObject BdDivDouble3PairNode::input1X;
MObject BdDivDouble3PairNode::input1Y;
MObject BdDivDouble3PairNode::input1Z;

MObject BdDivDouble3PairNode::input2;
MObject BdDivDouble3PairNode::input2X;
MObject BdDivDouble3PairNode::input2Y;
MObject BdDivDouble3PairNode::input2Z;

MObject BdDivDouble3PairNode::output;
MObject BdDivDouble3PairNode::outputX;
MObject BdDivDouble3PairNode::outputY;
MObject BdDivDouble3PairNode::outputZ;

void* BdDivDouble3PairNode::creator() {
    return new BdDivDouble3PairNode();
}

MStatus BdDivDouble3PairNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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
        1.0
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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
        1.0
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
        1.0
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

MStatus BdDivDouble3PairNode::compute(
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
    MDataHandle input1Value = dataBlock.inputValue(input1, &status);
    if (!status) {
        return status;
    }

    MDataHandle input2Value = dataBlock.inputValue(input2, &status);
    if (!status) {
        return status;
    }

    const double3& value1 = input1Value.asDouble3();
    const double3& value2 = input2Value.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        bd_util_nodes::safeDivide(value1[0], value2[0]),
        bd_util_nodes::safeDivide(value1[1], value2[1]),
        bd_util_nodes::safeDivide(value1[2], value2[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDivDouble3PairNode::schedulingType() const {
    return MPxNode::kParallel;
}
