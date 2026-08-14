#include "bdUtilNodes/nodes/BdDblL3MultiplyMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

namespace {

struct IndexedDouble3 {
    unsigned int logicalIndex;
    std::array<double, 3> value;
};

}  // namespace

const MString BdDblL3MultiplyMultiNode::typeName(
    "bdDblL3_MultiplyMulti"
);
const MTypeId BdDblL3MultiplyMultiNode::typeId(0x001426E1);

MObject BdDblL3MultiplyMultiNode::input;
MObject BdDblL3MultiplyMultiNode::inputX;
MObject BdDblL3MultiplyMultiNode::inputY;
MObject BdDblL3MultiplyMultiNode::inputZ;
MObject BdDblL3MultiplyMultiNode::factor;
MObject BdDblL3MultiplyMultiNode::factorX;
MObject BdDblL3MultiplyMultiNode::factorY;
MObject BdDblL3MultiplyMultiNode::factorZ;
MObject BdDblL3MultiplyMultiNode::output;
MObject BdDblL3MultiplyMultiNode::outputX;
MObject BdDblL3MultiplyMultiNode::outputY;
MObject BdDblL3MultiplyMultiNode::outputZ;

void* BdDblL3MultiplyMultiNode::creator() {
    return new BdDblL3MultiplyMultiNode();
}

MStatus BdDblL3MultiplyMultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
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

    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        factor,
        factorX,
        factorY,
        factorZ,
        "factor",
        "f",
        "factorX",
        "fx",
        "factorY",
        "fy",
        "factorZ",
        "fz",
        1.0
    );
    if (!status) {
        return status;
    }

    status = numericAttributeFn.setArray(true);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }

    status = addAttribute(factor);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
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

    const std::array<MObject, 8> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
        factor,
        factorX,
        factorY,
        factorZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblL3MultiplyMultiNode::compute(
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
    MDataHandle inputValue = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }

    MArrayDataHandle factorArray = dataBlock.inputArrayValue(
        factor,
        &status
    );
    if (!status) {
        return status;
    }

    const unsigned int elementCount = factorArray.elementCount(&status);
    if (!status) {
        return status;
    }

    std::vector<IndexedDouble3> factors;
    factors.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        const unsigned int logicalIndex = factorArray.elementIndex(&status);
        if (!status) {
            return status;
        }

        MDataHandle factorValue = factorArray.inputValue(&status);
        if (!status) {
            return status;
        }
        const double3& value = factorValue.asDouble3();
        factors.push_back({
            logicalIndex,
            {value[0], value[1], value[2]},
        });

        if (index + 1 < elementCount) {
            status = factorArray.next();
            if (!status) {
                return status;
            }
        }
    }

    std::sort(
        factors.begin(),
        factors.end(),
        [](const IndexedDouble3& left, const IndexedDouble3& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    const double3& value = inputValue.asDouble3();
    std::array<double, 3> product = {value[0], value[1], value[2]};
    for (const IndexedDouble3& currentFactor : factors) {
        product[0] *= currentFactor.value[0];
        product[1] *= currentFactor.value[1];
        product[2] *= currentFactor.value[2];
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(product[0], product[1], product[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3MultiplyMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
