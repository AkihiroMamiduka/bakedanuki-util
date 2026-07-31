#include "bdUtilNodes/BdDouble3MultNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"

const MString BdDouble3MultNode::typeName("bdDouble3Mult");
const MTypeId BdDouble3MultNode::typeId(0x0007F002);

MObject BdDouble3MultNode::input1;
MObject BdDouble3MultNode::input1X;
MObject BdDouble3MultNode::input1Y;
MObject BdDouble3MultNode::input1Z;

MObject BdDouble3MultNode::input2;
MObject BdDouble3MultNode::input2X;
MObject BdDouble3MultNode::input2Y;
MObject BdDouble3MultNode::input2Z;

MObject BdDouble3MultNode::output;
MObject BdDouble3MultNode::outputX;
MObject BdDouble3MultNode::outputY;
MObject BdDouble3MultNode::outputZ;

void* BdDouble3MultNode::creator() {
    return new BdDouble3MultNode();
}

MStatus BdDouble3MultNode::initialize() {
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

    attributeFn.setReadable(true);
    attributeFn.setWritable(true);
    attributeFn.setStorable(true);
    attributeFn.setKeyable(true);

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

    attributeFn.setReadable(true);
    attributeFn.setWritable(true);
    attributeFn.setStorable(true);
    attributeFn.setKeyable(true);

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

    attributeFn.setReadable(true);
    attributeFn.setWritable(false);
    attributeFn.setStorable(false);
    attributeFn.setKeyable(false);

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 8> inputs = {
        input1,
        input1X,
        input1Y,
        input1Z,
        input2,
        input2X,
        input2Y,
        input2Z,
    };
    const std::array<MObject, 4> outputs = {
        output,
        outputX,
        outputY,
        outputZ,
    };

    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : outputs) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }

    return MS::kSuccess;
}

MStatus BdDouble3MultNode::compute(
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
        value1[0] * value2[0],
        value1[1] * value2[1],
        value1[2] * value2[2]
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDouble3MultNode::schedulingType() const {
    return MPxNode::kParallel;
}
