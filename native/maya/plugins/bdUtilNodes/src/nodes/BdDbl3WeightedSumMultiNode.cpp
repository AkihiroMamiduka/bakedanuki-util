#include "bdUtilNodes/nodes/BdDbl3WeightedSumMultiNode.h"

#include <array>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDbl3WeightedSumMultiNode::typeName("bdDbl3_WeightedSumMulti");
const MTypeId BdDbl3WeightedSumMultiNode::typeId(0x0007F019);

MObject BdDbl3WeightedSumMultiNode::input;

MObject BdDbl3WeightedSumMultiNode::value;
MObject BdDbl3WeightedSumMultiNode::valueX;
MObject BdDbl3WeightedSumMultiNode::valueY;
MObject BdDbl3WeightedSumMultiNode::valueZ;

MObject BdDbl3WeightedSumMultiNode::weight;

MObject BdDbl3WeightedSumMultiNode::output;
MObject BdDbl3WeightedSumMultiNode::outputX;
MObject BdDbl3WeightedSumMultiNode::outputY;
MObject BdDbl3WeightedSumMultiNode::outputZ;

void* BdDbl3WeightedSumMultiNode::creator() {
    return new BdDbl3WeightedSumMultiNode();
}

MStatus BdDbl3WeightedSumMultiNode::initialize() {
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

MStatus BdDbl3WeightedSumMultiNode::compute(
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

MPxNode::SchedulingType BdDbl3WeightedSumMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
