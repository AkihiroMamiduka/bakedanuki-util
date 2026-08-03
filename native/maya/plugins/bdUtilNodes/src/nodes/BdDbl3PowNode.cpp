#include "bdUtilNodes/nodes/BdDbl3PowNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/SafePower.h"

const MString BdDbl3PowNode::typeName("bdDbl3_Pow");
const MTypeId BdDbl3PowNode::typeId(0x0007F012);

MObject BdDbl3PowNode::input1;
MObject BdDbl3PowNode::input1X;
MObject BdDbl3PowNode::input1Y;
MObject BdDbl3PowNode::input1Z;

MObject BdDbl3PowNode::input2;
MObject BdDbl3PowNode::input2X;
MObject BdDbl3PowNode::input2Y;
MObject BdDbl3PowNode::input2Z;

MObject BdDbl3PowNode::output;
MObject BdDbl3PowNode::outputX;
MObject BdDbl3PowNode::outputY;
MObject BdDbl3PowNode::outputZ;

void* BdDbl3PowNode::creator() {
    return new BdDbl3PowNode();
}

MStatus BdDbl3PowNode::initialize() {
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

MStatus BdDbl3PowNode::compute(
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
        bd_util_nodes::safePower(value1[0], value2[0]),
        bd_util_nodes::safePower(value1[1], value2[1]),
        bd_util_nodes::safePower(value1[2], value2[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDbl3PowNode::schedulingType() const {
    return MPxNode::kParallel;
}
