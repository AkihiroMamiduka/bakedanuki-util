#include "bdUtilNodes/BdLerpDouble3PairNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/Lerp.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdLerpDouble3PairNode::typeName("bdLerpDouble3Pair");
const MTypeId BdLerpDouble3PairNode::typeId(0x0007F017);

MObject BdLerpDouble3PairNode::input1;
MObject BdLerpDouble3PairNode::input1X;
MObject BdLerpDouble3PairNode::input1Y;
MObject BdLerpDouble3PairNode::input1Z;

MObject BdLerpDouble3PairNode::input2;
MObject BdLerpDouble3PairNode::input2X;
MObject BdLerpDouble3PairNode::input2Y;
MObject BdLerpDouble3PairNode::input2Z;

MObject BdLerpDouble3PairNode::weight;

MObject BdLerpDouble3PairNode::output;
MObject BdLerpDouble3PairNode::outputX;
MObject BdLerpDouble3PairNode::outputY;
MObject BdLerpDouble3PairNode::outputZ;

void* BdLerpDouble3PairNode::creator() {
    return new BdLerpDouble3PairNode();
}

MStatus BdLerpDouble3PairNode::initialize() {
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
        weight,
        "weight",
        "w",
        0.0
    );
    if (!status) {
        return status;
    }

    status = attributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    status = attributeFn.setMax(1.0);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(weight);
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

    const std::array<MObject, 9> inputAttributes = {
        input1,
        input1X,
        input1Y,
        input1Z,
        input2,
        input2X,
        input2Y,
        input2Z,
        weight,
    };

    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdLerpDouble3PairNode::compute(
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

    MDataHandle weightValue = dataBlock.inputValue(weight, &status);
    if (!status) {
        return status;
    }

    const double3& value1 = input1Value.asDouble3();
    const double3& value2 = input2Value.asDouble3();
    const double blendWeight = weightValue.asDouble();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        bd_util_nodes::clampedLerp(value1[0], value2[0], blendWeight),
        bd_util_nodes::clampedLerp(value1[1], value2[1], blendWeight),
        bd_util_nodes::clampedLerp(value1[2], value2[2], blendWeight)
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdLerpDouble3PairNode::schedulingType() const {
    return MPxNode::kParallel;
}
