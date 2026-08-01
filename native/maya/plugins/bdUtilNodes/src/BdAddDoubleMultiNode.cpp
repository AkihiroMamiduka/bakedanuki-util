#include "bdUtilNodes/BdAddDoubleMultiNode.h"

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/NumericAttribute.h"

const MString BdAddDoubleMultiNode::typeName("bdAddDoubleMulti");
const MTypeId BdAddDoubleMultiNode::typeId(0x0007F007);

MObject BdAddDoubleMultiNode::input;
MObject BdAddDoubleMultiNode::output;

void* BdAddDoubleMultiNode::creator() {
    return new BdAddDoubleMultiNode();
}

MStatus BdAddDoubleMultiNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        input,
        "input",
        "i",
        0.0
    );
    if (!status) {
        return status;
    }

    status = attributeFn.setArray(true);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        output,
        "output",
        "o",
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

    return attributeAffects(input, output);
}

MStatus BdAddDoubleMultiNode::compute(
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
        MDataHandle inputValue = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }

        sum += inputValue.asDouble();

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

MPxNode::SchedulingType BdAddDoubleMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
