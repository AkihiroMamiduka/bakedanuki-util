#include "bdUtilNodes/nodes/BdDbl3RatioDblL3Node.h"

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

const MString BdDbl3RatioDblL3Node::typeName("bdDbl3_RatioDblL3");
const MTypeId BdDbl3RatioDblL3Node::typeId(0x0007F068);

MObject BdDbl3RatioDblL3Node::input;
MObject BdDbl3RatioDblL3Node::inputX;
MObject BdDbl3RatioDblL3Node::inputY;
MObject BdDbl3RatioDblL3Node::inputZ;
MObject BdDbl3RatioDblL3Node::base;
MObject BdDbl3RatioDblL3Node::baseX;
MObject BdDbl3RatioDblL3Node::baseY;
MObject BdDbl3RatioDblL3Node::baseZ;
MObject BdDbl3RatioDblL3Node::output;
MObject BdDbl3RatioDblL3Node::outputX;
MObject BdDbl3RatioDblL3Node::outputY;
MObject BdDbl3RatioDblL3Node::outputZ;

void* BdDbl3RatioDblL3Node::creator() {
    return new BdDbl3RatioDblL3Node();
}

MStatus BdDbl3RatioDblL3Node::initialize() {
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        base,
        baseX,
        baseY,
        baseZ,
        "base",
        "b",
        "baseX",
        "bx",
        "baseY",
        "by",
        "baseZ",
        "bz",
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

    status = addAttribute(base);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
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
        base,
        baseX,
        baseY,
        baseZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDbl3RatioDblL3Node::compute(
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

    MDataHandle baseValue = dataBlock.inputValue(base, &status);
    if (!status) {
        return status;
    }

    const double3& value = inputValue.asDouble3();
    const double3& divisor = baseValue.asDouble3();

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

MPxNode::SchedulingType BdDbl3RatioDblL3Node::schedulingType() const {
    return MPxNode::kParallel;
}
