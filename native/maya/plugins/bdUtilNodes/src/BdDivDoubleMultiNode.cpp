#include "bdUtilNodes/BdDivDoubleMultiNode.h"

#include <algorithm>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/NumericAttribute.h"
#include "bdUtilNodes/SafeDivision.h"

namespace {

struct IndexedDouble {
    unsigned int logicalIndex;
    double value;
};

}  // namespace

const MString BdDivDoubleMultiNode::typeName("bdDivDoubleMulti");
const MTypeId BdDivDoubleMultiNode::typeId(0x0007F00F);

MObject BdDivDoubleMultiNode::input;
MObject BdDivDoubleMultiNode::output;

void* BdDivDoubleMultiNode::creator() {
    return new BdDivDoubleMultiNode();
}

MStatus BdDivDoubleMultiNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        attributeFn,
        input,
        "input",
        "i",
        1.0
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
        1.0
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

MStatus BdDivDoubleMultiNode::compute(
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

    double quotient = 1.0;
    if (!values.empty()) {
        quotient = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            quotient = bd_util_nodes::safeDivide(
                quotient,
                values[index].value
            );
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(quotient);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDivDoubleMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
