#include "bdUtilNodes/nodes/BdDbl3ConditionMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Comparison.h"

namespace {

struct IndexedConditionCase {
    unsigned int logicalIndex;
    short operation;
    double compare;
    std::array<double, 3> value;
};

}  // namespace

const MString BdDbl3ConditionMultiNode::typeName("bdDbl3_ConditionMulti");
const MTypeId BdDbl3ConditionMultiNode::typeId(0x0007F02B);

MObject BdDbl3ConditionMultiNode::input;
MObject BdDbl3ConditionMultiNode::caseArray;
MObject BdDbl3ConditionMultiNode::operation;
MObject BdDbl3ConditionMultiNode::compare;

MObject BdDbl3ConditionMultiNode::value;
MObject BdDbl3ConditionMultiNode::valueX;
MObject BdDbl3ConditionMultiNode::valueY;
MObject BdDbl3ConditionMultiNode::valueZ;

MObject BdDbl3ConditionMultiNode::elseValue;
MObject BdDbl3ConditionMultiNode::elseValueX;
MObject BdDbl3ConditionMultiNode::elseValueY;
MObject BdDbl3ConditionMultiNode::elseValueZ;

MObject BdDbl3ConditionMultiNode::output;
MObject BdDbl3ConditionMultiNode::outputX;
MObject BdDbl3ConditionMultiNode::outputY;
MObject BdDbl3ConditionMultiNode::outputZ;

void* BdDbl3ConditionMultiNode::creator() {
    return new BdDbl3ConditionMultiNode();
}

MStatus BdDbl3ConditionMultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;

    MStatus status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        input,
        "input",
        "i",
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

    MFnEnumAttribute enumAttributeFn;
    status = bd_util_nodes::createComparisonOperationAttribute(
        enumAttributeFn,
        operation,
        "operation",
        "op"
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        compare,
        "compare",
        "cmp",
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

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        value,
        valueX,
        valueY,
        valueZ,
        "value",
        "v",
        "valueX",
        "vx",
        "valueY",
        "vy",
        "valueZ",
        "vz",
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
    caseArray = compoundAttributeFn.create("case", "cs", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {operation, compare, value}) {
        status = compoundAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
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
    status = addAttribute(caseArray);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        elseValue,
        elseValueX,
        elseValueY,
        elseValueZ,
        "elseValue",
        "ev",
        "elseValueX",
        "evx",
        "elseValueY",
        "evy",
        "elseValueZ",
        "evz",
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
    status = addAttribute(elseValue);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
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

    const std::array<MObject, 12> inputAttributes = {
        input,
        caseArray,
        operation,
        compare,
        value,
        valueX,
        valueY,
        valueZ,
        elseValue,
        elseValueX,
        elseValueY,
        elseValueZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdDbl3ConditionMultiNode::compute(
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
    const double inputValue = dataBlock.inputValue(input, &status).asDouble();
    if (!status) {
        return status;
    }
    MDataHandle elseValueHandle = dataBlock.inputValue(elseValue, &status);
    if (!status) {
        return status;
    }
    const double3& defaultValue = elseValueHandle.asDouble3();
    std::array<double, 3> selectedValue = {
        defaultValue[0],
        defaultValue[1],
        defaultValue[2],
    };

    MArrayDataHandle caseHandles = dataBlock.inputArrayValue(
        caseArray,
        &status
    );
    if (!status) {
        return status;
    }
    const unsigned int elementCount = caseHandles.elementCount(&status);
    if (!status) {
        return status;
    }

    std::vector<IndexedConditionCase> cases;
    cases.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        const unsigned int logicalIndex = caseHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        MDataHandle caseHandle = caseHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        const double3& currentValue = caseHandle.child(value).asDouble3();
        cases.push_back({
            logicalIndex,
            caseHandle.child(operation).asShort(),
            caseHandle.child(compare).asDouble(),
            {currentValue[0], currentValue[1], currentValue[2]},
        });

        if (index + 1 < elementCount) {
            status = caseHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(
        cases.begin(),
        cases.end(),
        [](const IndexedConditionCase& left,
           const IndexedConditionCase& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    for (const IndexedConditionCase& currentCase : cases) {
        if (
            bd_util_nodes::evaluateComparison(
                inputValue,
                currentCase.operation,
                currentCase.compare
            )
        ) {
            selectedValue = currentCase.value;
            break;
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        selectedValue[0],
        selectedValue[1],
        selectedValue[2]
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDbl3ConditionMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
