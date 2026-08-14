#include "bdUtilNodes/nodes/BdDblLMultiplyNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLMultiplyNode::typeName("bdDblL_Multiply");
const MTypeId BdDblLMultiplyNode::typeId(0x001426DE);

MObject BdDblLMultiplyNode::input;
MObject BdDblLMultiplyNode::factor;
MObject BdDblLMultiplyNode::output;

void* BdDblLMultiplyNode::creator() {
    return new BdDblLMultiplyNode();
}

MStatus BdDblLMultiplyNode::initialize() {
    MFnUnitAttribute unitAttributeFn;
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        input,
        "input",
        "i",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        factor,
        "factor",
        "f",
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    status = attributeAffects(input, output);
    if (!status) {
        return status;
    }

    return attributeAffects(factor, output);
}

MStatus BdDblLMultiplyNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
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

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        inputValue.asDouble() * factorValue.asDouble()
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLMultiplyNode::schedulingType() const {
    return MPxNode::kParallel;
}
