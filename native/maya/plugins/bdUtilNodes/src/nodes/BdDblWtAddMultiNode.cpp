#include "bdUtilNodes/nodes/BdDblWtAddMultiNode.h"

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblWtAddMultiNode::typeName("bdDbl_WtAddMulti");
const MTypeId BdDblWtAddMultiNode::typeId(0x0007F01A);

MObject BdDblWtAddMultiNode::input;
MObject BdDblWtAddMultiNode::value;
MObject BdDblWtAddMultiNode::weight;
MObject BdDblWtAddMultiNode::output;

void* BdDblWtAddMultiNode::creator() {
    return new BdDblWtAddMultiNode();
}

MStatus BdDblWtAddMultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        value,
        "value",
        "v",
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

    status = attributeAffects(value, output);
    if (!status) {
        return status;
    }

    return attributeAffects(weight, output);
}

MStatus BdDblWtAddMultiNode::compute(
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

MPxNode::SchedulingType BdDblWtAddMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
