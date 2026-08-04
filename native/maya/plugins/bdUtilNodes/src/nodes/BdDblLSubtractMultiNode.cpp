#include "bdUtilNodes/nodes/BdDblLSubtractMultiNode.h"

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

const MString BdDblLSubtractMultiNode::typeName("bdDblL_SubtractMulti");
const MTypeId BdDblLSubtractMultiNode::typeId(0x0007F03C);

MObject BdDblLSubtractMultiNode::input;
MObject BdDblLSubtractMultiNode::output;

void* BdDblLSubtractMultiNode::creator() {
    return new BdDblLSubtractMultiNode();
}

MStatus BdDblLSubtractMultiNode::initialize() {
    MFnUnitAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
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

MStatus BdDblLSubtractMultiNode::compute(
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

MPxNode::SchedulingType BdDblLSubtractMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
