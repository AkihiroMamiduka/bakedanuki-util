#include "bdUtilNodes/nodes/BdDblLWeightedSumMultiNode.h"

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLWeightedSumMultiNode::typeName("bdDblL_WeightedSumMulti");
const MTypeId BdDblLWeightedSumMultiNode::typeId(0x0007F055);

MObject BdDblLWeightedSumMultiNode::input;
MObject BdDblLWeightedSumMultiNode::value;
MObject BdDblLWeightedSumMultiNode::weight;
MObject BdDblLWeightedSumMultiNode::output;

void* BdDblLWeightedSumMultiNode::creator() {
    return new BdDblLWeightedSumMultiNode();
}

MStatus BdDblLWeightedSumMultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        value,
        "value",
        "v",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        weight,
        "weight",
        "w",
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

    MFnCompoundAttribute compoundAttributeFn;
    input = compoundAttributeFn.create("input", "i", &status);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.addChild(value);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.addChild(weight);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.setArray(true);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }

    status = compoundAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
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

    status = attributeAffects(value, output);
    if (!status) {
        return status;
    }

    return attributeAffects(weight, output);
}

MStatus BdDblLWeightedSumMultiNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MArrayDataHandle inputArray = dataBlock.inputArrayValue(input, &status);
    if (!status) {
        return status;
    }

    double sum = 0.0;
    const unsigned int elementCount = inputArray.elementCount(&status);
    if (!status) {
        return status;
    }

    for (unsigned int index = 0; index < elementCount; ++index) {
        MDataHandle inputElement = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }

        MDataHandle inputValue = inputElement.child(value);
        MDataHandle inputWeight = inputElement.child(weight);

        sum += inputValue.asDouble() * inputWeight.asDouble();

        if (index + 1 < elementCount) {
            status = inputArray.next();
            if (!status) {
                return status;
            }
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(sum);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLWeightedSumMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
