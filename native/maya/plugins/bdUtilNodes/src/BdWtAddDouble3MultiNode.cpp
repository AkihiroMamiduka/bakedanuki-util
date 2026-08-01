#include "bdUtilNodes/BdWtAddDouble3MultiNode.h"

#include <array>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdWtAddDouble3MultiNode::typeName("bdWtAddDouble3Multi");
const MTypeId BdWtAddDouble3MultiNode::typeId(0x0007F019);

MObject BdWtAddDouble3MultiNode::input;

MObject BdWtAddDouble3MultiNode::value;
MObject BdWtAddDouble3MultiNode::valueX;
MObject BdWtAddDouble3MultiNode::valueY;
MObject BdWtAddDouble3MultiNode::valueZ;

MObject BdWtAddDouble3MultiNode::weight;

MObject BdWtAddDouble3MultiNode::output;
MObject BdWtAddDouble3MultiNode::outputX;
MObject BdWtAddDouble3MultiNode::outputY;
MObject BdWtAddDouble3MultiNode::outputZ;

void* BdWtAddDouble3MultiNode::creator() {
    return new BdWtAddDouble3MultiNode();
}

MStatus BdWtAddDouble3MultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        value,
        valueX,
        valueY,
        valueZ,
        "value",
        "v",
        "valueX",
        "vx",
        "valueY",
        "vy",
        "valueZ",
        "vz",
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

    const std::array<MObject, 6> inputAttributes = {
        input,
        value,
        valueX,
        valueY,
        valueZ,
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

MStatus BdWtAddDouble3MultiNode::compute(
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
    MArrayDataHandle inputArray = dataBlock.inputArrayValue(input, &status);
    if (!status) {
        return status;
    }

    double sumX = 0.0;
    double sumY = 0.0;
    double sumZ = 0.0;
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

        const double3& weightedValue = inputValue.asDouble3();
        const double elementWeight = inputWeight.asDouble();
        sumX += weightedValue[0] * elementWeight;
        sumY += weightedValue[1] * elementWeight;
        sumZ += weightedValue[2] * elementWeight;

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

    outputValue.set3Double(sumX, sumY, sumZ);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdWtAddDouble3MultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
