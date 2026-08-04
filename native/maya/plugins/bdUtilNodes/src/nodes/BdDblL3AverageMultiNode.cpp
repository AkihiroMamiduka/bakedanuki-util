#include "bdUtilNodes/nodes/BdDblL3AverageMultiNode.h"

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

const MString BdDblL3AverageMultiNode::typeName("bdDblL3_AverageMulti");
const MTypeId BdDblL3AverageMultiNode::typeId(0x0007F042);

MObject BdDblL3AverageMultiNode::input;
MObject BdDblL3AverageMultiNode::inputX;
MObject BdDblL3AverageMultiNode::inputY;
MObject BdDblL3AverageMultiNode::inputZ;

MObject BdDblL3AverageMultiNode::output;
MObject BdDblL3AverageMultiNode::outputX;
MObject BdDblL3AverageMultiNode::outputY;
MObject BdDblL3AverageMultiNode::outputZ;

void* BdDblL3AverageMultiNode::creator() {
    return new BdDblL3AverageMultiNode();
}

MStatus BdDblL3AverageMultiNode::initialize() {
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

MStatus BdDblL3AverageMultiNode::compute(
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
        values.push_back(
            {logicalIndex, {value[0], value[1], value[2]}}
        );

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

    std::array<double, 3> result = {0.0, 0.0, 0.0};
    if (!values.empty()) {
        result = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            result[0] += values[index].value[0];
            result[1] += values[index].value[1];
            result[2] += values[index].value[2];
        }
        const double inverseCount =
            1.0 / static_cast<double>(values.size());
        result[0] *= inverseCount;
        result[1] *= inverseCount;
        result[2] *= inverseCount;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(result[0], result[1], result[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3AverageMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
