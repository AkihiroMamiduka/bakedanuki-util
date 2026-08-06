#include "bdUtilNodes/nodes/BdDblL3MultiplyNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3MultiplyNode::typeName("bdDblL3_Multiply");
const MTypeId BdDblL3MultiplyNode::typeId(0x0007F061);

MObject BdDblL3MultiplyNode::input;
MObject BdDblL3MultiplyNode::inputX;
MObject BdDblL3MultiplyNode::inputY;
MObject BdDblL3MultiplyNode::inputZ;
MObject BdDblL3MultiplyNode::factor;
MObject BdDblL3MultiplyNode::factorX;
MObject BdDblL3MultiplyNode::factorY;
MObject BdDblL3MultiplyNode::factorZ;
MObject BdDblL3MultiplyNode::output;
MObject BdDblL3MultiplyNode::outputX;
MObject BdDblL3MultiplyNode::outputY;
MObject BdDblL3MultiplyNode::outputZ;

void* BdDblL3MultiplyNode::creator() {
    return new BdDblL3MultiplyNode();
}

MStatus BdDblL3MultiplyNode::initialize() {
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        input,
        inputX,
        inputY,
        inputZ,
        "input",
        "i",
        "inputX",
        "ix",
        "inputY",
        "iy",
        "inputZ",
        "iz",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        factor,
        factorX,
        factorY,
        factorZ,
        "factor",
        "f",
        "factorX",
        "fx",
        "factorY",
        "fy",
        "factorZ",
        "fz",
        1.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = addAttribute(factor);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
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

    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 8> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
        factor,
        factorX,
        factorY,
        factorZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblL3MultiplyNode::compute(
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
    MDataHandle inputValue = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }

    MDataHandle factorValue = dataBlock.inputValue(factor, &status);
    if (!status) {
        return status;
    }

    const double3& value = inputValue.asDouble3();
    const double3& scale = factorValue.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        value[0] * scale[0],
        value[1] * scale[1],
        value[2] * scale[2]
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3MultiplyNode::schedulingType() const {
    return MPxNode::kParallel;
}
