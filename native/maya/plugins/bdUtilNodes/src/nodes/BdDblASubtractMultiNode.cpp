#include "bdUtilNodes/nodes/BdDblASubtractMultiNode.h"

#include <algorithm>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/UnitAttribute.h"

namespace {

struct IndexedDouble {
    unsigned int logicalIndex;
    double value;
};

}  // namespace

const MString BdDblASubtractMultiNode::typeName("bdDblA_SubtractMulti");
const MTypeId BdDblASubtractMultiNode::typeId(0x0007F06E);

MObject BdDblASubtractMultiNode::input;
MObject BdDblASubtractMultiNode::output;

void* BdDblASubtractMultiNode::creator() {
    return new BdDblASubtractMultiNode();
}

MStatus BdDblASubtractMultiNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    return attributeAffects(input, output);
}

MStatus BdDblASubtractMultiNode::compute(
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

    std::vector<IndexedDouble> values;
    values.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        const unsigned int logicalIndex = inputArray.elementIndex(&status);
        if (!status) {
            return status;
        }

        MDataHandle inputValue = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }
        values.push_back({logicalIndex, inputValue.asDouble()});

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
        [](const IndexedDouble& left, const IndexedDouble& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    double difference = 0.0;
    if (!values.empty()) {
        difference = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            difference -= values[index].value;
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(difference);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblASubtractMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
