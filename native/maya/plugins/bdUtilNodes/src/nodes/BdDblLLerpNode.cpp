#include "bdUtilNodes/nodes/BdDblLLerpNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Lerp.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLLerpNode::typeName("bdDblL_Lerp");
const MTypeId BdDblLLerpNode::typeId(0x0007F051);

MObject BdDblLLerpNode::input1;
MObject BdDblLLerpNode::input2;
MObject BdDblLLerpNode::weight;
MObject BdDblLLerpNode::output;

void* BdDblLLerpNode::creator() {
    return new BdDblLLerpNode();
}

MStatus BdDblLLerpNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        input1,
        "input1",
        "i1",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input1);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        input2,
        "input2",
        "i2",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
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

    status = attributeAffects(input1, output);
    if (!status) {
        return status;
    }

    status = attributeAffects(input2, output);
    if (!status) {
        return status;
    }

    return attributeAffects(weight, output);
}

MStatus BdDblLLerpNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
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

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        bd_util_nodes::clampedLerp(
            input1Value.asDouble(),
            input2Value.asDouble(),
            weightValue.asDouble()
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLLerpNode::schedulingType() const {
    return MPxNode::kParallel;
}
