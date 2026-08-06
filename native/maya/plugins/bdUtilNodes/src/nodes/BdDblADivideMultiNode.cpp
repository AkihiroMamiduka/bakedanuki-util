#include "bdUtilNodes/nodes/BdDblADivideMultiNode.h"

#include <algorithm>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/SafeDivision.h"

namespace {

struct IndexedDouble {
    unsigned int logicalIndex;
    double value;
};

}  // namespace

const MString BdDblADivideMultiNode::typeName("bdDblA_DivideMulti");
const MTypeId BdDblADivideMultiNode::typeId(0x0007F074);

MObject BdDblADivideMultiNode::input;
MObject BdDblADivideMultiNode::factor;
MObject BdDblADivideMultiNode::output;

void* BdDblADivideMultiNode::creator() {
    return new BdDblADivideMultiNode();
}

MStatus BdDblADivideMultiNode::initialize() {
    MFnUnitAttribute unitAttributeFn;
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        input,
        "input",
        "i",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        factor,
        "factor",
        "f",
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
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

    return attributeAffects(factor, output);
}

MStatus BdDblADivideMultiNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
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

    std::vector<IndexedDouble> factors;
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
        factors.push_back({logicalIndex, factorValue.asDouble()});

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
        [](const IndexedDouble& left, const IndexedDouble& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    double quotient = inputValue.asDouble();
    for (const IndexedDouble& currentFactor : factors) {
        quotient = bd_util_nodes::safeDivide(
            quotient,
            currentFactor.value
        );
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(quotient);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblADivideMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
