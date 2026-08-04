#include "bdUtilNodes/nodes/BdDbl3WeightedAverageMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/WeightedAverage.h"

namespace {

struct IndexedWeightedValue {
    unsigned int logicalIndex;
    std::array<double, 3> value;
    double weight;
};

}  // namespace

const MString BdDbl3WeightedAverageMultiNode::typeName(
    "bdDbl3_WeightedAverageMulti"
);
const MTypeId BdDbl3WeightedAverageMultiNode::typeId(0x0007F033);

MObject BdDbl3WeightedAverageMultiNode::input;

MObject BdDbl3WeightedAverageMultiNode::value;
MObject BdDbl3WeightedAverageMultiNode::valueX;
MObject BdDbl3WeightedAverageMultiNode::valueY;
MObject BdDbl3WeightedAverageMultiNode::valueZ;

MObject BdDbl3WeightedAverageMultiNode::weight;

MObject BdDbl3WeightedAverageMultiNode::output;
MObject BdDbl3WeightedAverageMultiNode::outputX;
MObject BdDbl3WeightedAverageMultiNode::outputY;
MObject BdDbl3WeightedAverageMultiNode::outputZ;

void* BdDbl3WeightedAverageMultiNode::creator() {
    return new BdDbl3WeightedAverageMultiNode();
}

MStatus BdDbl3WeightedAverageMultiNode::initialize() {
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

MStatus BdDbl3WeightedAverageMultiNode::compute(
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
    const unsigned int elementCount = inputArray.elementCount(&status);
    if (!status) {
        return status;
    }

    std::vector<IndexedWeightedValue> values;
    values.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        MDataHandle inputElement = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }
        const double elementWeight = inputElement.child(weight).asDouble();
        if (elementWeight != 0.0) {
            const unsigned int logicalIndex = inputArray.elementIndex(&status);
            if (!status) {
                return status;
            }
            const double3& elementValue = inputElement.child(value).asDouble3();
            values.push_back(
                {
                    logicalIndex,
                    {elementValue[0], elementValue[1], elementValue[2]},
                    elementWeight,
                }
            );
        }

        if (index + 1 < elementCount) {
            status = inputArray.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(
        values.begin(),
        values.end(),
        [](const IndexedWeightedValue& left,
           const IndexedWeightedValue& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    std::array<double, 3> weightedSum = {0.0, 0.0, 0.0};
    double weightSum = 0.0;
    for (const IndexedWeightedValue& current : values) {
        weightedSum[0] += current.value[0] * current.weight;
        weightedSum[1] += current.value[1] * current.weight;
        weightedSum[2] += current.value[2] * current.weight;
        weightSum += current.weight;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        bd_util_nodes::weightedAverage(weightedSum[0], weightSum),
        bd_util_nodes::weightedAverage(weightedSum[1], weightSum),
        bd_util_nodes::weightedAverage(weightedSum[2], weightSum)
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDbl3WeightedAverageMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
