#include "bdUtilNodes/nodes/BdDblL3DivideNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/SafeDivision.h"

const MString BdDblL3DivideNode::typeName("bdDblL3_Divide");
const MTypeId BdDblL3DivideNode::typeId(0x001426E4);

MObject BdDblL3DivideNode::input;
MObject BdDblL3DivideNode::inputX;
MObject BdDblL3DivideNode::inputY;
MObject BdDblL3DivideNode::inputZ;
MObject BdDblL3DivideNode::factor;
MObject BdDblL3DivideNode::factorX;
MObject BdDblL3DivideNode::factorY;
MObject BdDblL3DivideNode::factorZ;
MObject BdDblL3DivideNode::output;
MObject BdDblL3DivideNode::outputX;
MObject BdDblL3DivideNode::outputY;
MObject BdDblL3DivideNode::outputZ;

void* BdDblL3DivideNode::creator() {
    return new BdDblL3DivideNode();
}

MStatus BdDblL3DivideNode::initialize() {
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

MStatus BdDblL3DivideNode::compute(
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
    const double3& divisor = factorValue.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        bd_util_nodes::safeDivide(value[0], divisor[0]),
        bd_util_nodes::safeDivide(value[1], divisor[1]),
        bd_util_nodes::safeDivide(value[2], divisor[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3DivideNode::schedulingType() const {
    return MPxNode::kParallel;
}
