#include "bdUtilNodes/nodes/BdDblRatioDblANode.h"

#include <maya/MAngle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/SafeDivision.h"

const MString BdDblRatioDblANode::typeName("bdDbl_RatioDblA");
const MTypeId BdDblRatioDblANode::typeId(0x0007F083);

MObject BdDblRatioDblANode::input;
MObject BdDblRatioDblANode::base;
MObject BdDblRatioDblANode::output;

void* BdDblRatioDblANode::creator() {
    return new BdDblRatioDblANode();
}

MStatus BdDblRatioDblANode::initialize() {
    MFnUnitAttribute unitAttributeFn;
    const double fullRotationRadians =
        MAngle(360.0, MAngle::kDegrees).asRadians();
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        base,
        "base",
        "b",
        fullRotationRadians
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(base);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        output,
        "output",
        "o",
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

    status = attributeAffects(input, output);
    if (!status) {
        return status;
    }

    return attributeAffects(base, output);
}

MStatus BdDblRatioDblANode::compute(
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

    MDataHandle baseValue = dataBlock.inputValue(base, &status);
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        bd_util_nodes::safeDivide(
            inputValue.asDouble(),
            baseValue.asDouble()
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblRatioDblANode::schedulingType() const {
    return MPxNode::kParallel;
}
