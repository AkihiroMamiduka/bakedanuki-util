#include "bdUtilNodes/nodes/BdDblL3DivideMultiNode.h"

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
#include "bdUtilNodes/math/SafeDivision.h"

namespace {

struct IndexedDouble3 {
    unsigned int logicalIndex;
    std::array<double, 3> value;
};

}  // namespace

const MString BdDblL3DivideMultiNode::typeName(
    "bdDblL3_DivideMulti"
);
const MTypeId BdDblL3DivideMultiNode::typeId(0x001426E5);

MObject BdDblL3DivideMultiNode::input;
MObject BdDblL3DivideMultiNode::inputX;
MObject BdDblL3DivideMultiNode::inputY;
MObject BdDblL3DivideMultiNode::inputZ;
MObject BdDblL3DivideMultiNode::factor;
MObject BdDblL3DivideMultiNode::factorX;
MObject BdDblL3DivideMultiNode::factorY;
MObject BdDblL3DivideMultiNode::factorZ;
MObject BdDblL3DivideMultiNode::output;
MObject BdDblL3DivideMultiNode::outputX;
MObject BdDblL3DivideMultiNode::outputY;
MObject BdDblL3DivideMultiNode::outputZ;

void* BdDblL3DivideMultiNode::creator() {
    return new BdDblL3DivideMultiNode();
}

MStatus BdDblL3DivideMultiNode::initialize() {
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

MStatus BdDblL3DivideMultiNode::compute(
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
    std::array<double, 3> quotient = {value[0], value[1], value[2]};
    for (const IndexedDouble3& currentFactor : factors) {
        quotient[0] = bd_util_nodes::safeDivide(
            quotient[0],
            currentFactor.value[0]
        );
        quotient[1] = bd_util_nodes::safeDivide(
            quotient[1],
            currentFactor.value[1]
        );
        quotient[2] = bd_util_nodes::safeDivide(
            quotient[2],
            currentFactor.value[2]
        );
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(quotient[0], quotient[1], quotient[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3DivideMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
