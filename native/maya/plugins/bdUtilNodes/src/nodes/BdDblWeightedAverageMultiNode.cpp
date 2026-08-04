#include "bdUtilNodes/nodes/BdDblWeightedAverageMultiNode.h"

#include <algorithm>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/WeightedAverage.h"

namespace {

struct IndexedWeightedValue {
    unsigned int logicalIndex;
    double value;
    double weight;
};

}  // namespace

const MString BdDblWeightedAverageMultiNode::typeName(
    "bdDbl_WeightedAverageMulti"
);
const MTypeId BdDblWeightedAverageMultiNode::typeId(0x0007F034);

MObject BdDblWeightedAverageMultiNode::input;
MObject BdDblWeightedAverageMultiNode::value;
MObject BdDblWeightedAverageMultiNode::weight;
MObject BdDblWeightedAverageMultiNode::output;

void* BdDblWeightedAverageMultiNode::creator() {
    return new BdDblWeightedAverageMultiNode();
}

MStatus BdDblWeightedAverageMultiNode::initialize() {
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

MStatus BdDblWeightedAverageMultiNode::compute(
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
            values.push_back(
                {
                    logicalIndex,
                    inputElement.child(value).asDouble(),
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

    double weightedSum = 0.0;
    double weightSum = 0.0;
    for (const IndexedWeightedValue& current : values) {
        weightedSum += current.value * current.weight;
        weightSum += current.weight;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.setDouble(
        bd_util_nodes::weightedAverage(weightedSum, weightSum)
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblWeightedAverageMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
