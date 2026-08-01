#include "bdUtilNodes/BdDouble3DivMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"
#include "bdUtilNodes/SafeDivision.h"

namespace {

struct IndexedDouble3 {
    unsigned int logicalIndex;
    std::array<double, 3> value;
};

}  // namespace

const MString BdDouble3DivMultiNode::typeName("bdDouble3DivMulti");
const MTypeId BdDouble3DivMultiNode::typeId(0x0007F00D);

MObject BdDouble3DivMultiNode::input;
MObject BdDouble3DivMultiNode::inputX;
MObject BdDouble3DivMultiNode::inputY;
MObject BdDouble3DivMultiNode::inputZ;

MObject BdDouble3DivMultiNode::output;
MObject BdDouble3DivMultiNode::outputX;
MObject BdDouble3DivMultiNode::outputY;
MObject BdDouble3DivMultiNode::outputZ;

void* BdDouble3DivMultiNode::creator() {
    return new BdDouble3DivMultiNode();
}

MStatus BdDouble3DivMultiNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

MStatus BdDouble3DivMultiNode::compute(
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

    std::array<double, 3> quotient = {1.0, 1.0, 1.0};
    if (!values.empty()) {
        quotient = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            quotient[0] = bd_util_nodes::safeDivide(
                quotient[0],
                values[index].value[0]
            );
            quotient[1] = bd_util_nodes::safeDivide(
                quotient[1],
                values[index].value[1]
            );
            quotient[2] = bd_util_nodes::safeDivide(
                quotient[2],
                values[index].value[2]
            );
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(quotient[0], quotient[1], quotient[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDouble3DivMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
