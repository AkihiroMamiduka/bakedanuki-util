#include "bdUtilNodes/nodes/BdDblL3SubtractMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

namespace {

struct IndexedDouble3 {
    unsigned int logicalIndex;
    std::array<double, 3> value;
};

}  // namespace

const MString BdDblL3SubtractMultiNode::typeName("bdDblL3_SubtractMulti");
const MTypeId BdDblL3SubtractMultiNode::typeId(0x0007F03E);

MObject BdDblL3SubtractMultiNode::input;
MObject BdDblL3SubtractMultiNode::inputX;
MObject BdDblL3SubtractMultiNode::inputY;
MObject BdDblL3SubtractMultiNode::inputZ;

MObject BdDblL3SubtractMultiNode::output;
MObject BdDblL3SubtractMultiNode::outputX;
MObject BdDblL3SubtractMultiNode::outputY;
MObject BdDblL3SubtractMultiNode::outputZ;

void* BdDblL3SubtractMultiNode::creator() {
    return new BdDblL3SubtractMultiNode();
}

MStatus BdDblL3SubtractMultiNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        input,
        inputX,
        inputY,
        inputZ,
        "input",
        "i",
        "inputX",
        "ix",
        "inputY",
        "iy",
        "inputZ",
        "iz",
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
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

    status = bd_util_nodes::configureOutputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 4> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblL3SubtractMultiNode::compute(
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

    std::vector<IndexedDouble3> values;
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
        const double3& value = inputValue.asDouble3();
        values.push_back({
            logicalIndex,
            {value[0], value[1], value[2]},
        });

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
        [](const IndexedDouble3& left, const IndexedDouble3& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    std::array<double, 3> difference = {0.0, 0.0, 0.0};
    if (!values.empty()) {
        difference = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            difference[0] -= values[index].value[0];
            difference[1] -= values[index].value[1];
            difference[2] -= values[index].value[2];
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        difference[0],
        difference[1],
        difference[2]
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3SubtractMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
