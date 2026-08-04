#include "bdUtilNodes/nodes/BdDblConditionMultiNode.h"

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
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Comparison.h"

namespace {

struct IndexedConditionCase {
    unsigned int logicalIndex;
    short operation;
    double compare;
    double value;
};

}  // namespace

const MString BdDblConditionMultiNode::typeName("bdDbl_ConditionMulti");
const MTypeId BdDblConditionMultiNode::typeId(0x0007F02D);

MObject BdDblConditionMultiNode::input;
MObject BdDblConditionMultiNode::caseArray;
MObject BdDblConditionMultiNode::operation;
MObject BdDblConditionMultiNode::compare;
MObject BdDblConditionMultiNode::value;
MObject BdDblConditionMultiNode::elseValue;
MObject BdDblConditionMultiNode::output;

void* BdDblConditionMultiNode::creator() {
    return new BdDblConditionMultiNode();
}

MStatus BdDblConditionMultiNode::initialize() {
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

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        value,
        "value",
        "v",
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

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        elseValue,
        "elseValue",
        "ev",
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

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        output,
        "output",
        "o",
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

    const std::array<MObject, 6> inputAttributes = {
        input,
        caseArray,
        operation,
        compare,
        value,
        elseValue,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdDblConditionMultiNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    const double inputValue = dataBlock.inputValue(input, &status).asDouble();
    if (!status) {
        return status;
    }
    double selectedValue = dataBlock
                               .inputValue(elseValue, &status)
                               .asDouble();
    if (!status) {
        return status;
    }

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
        cases.push_back({
            logicalIndex,
            caseHandle.child(operation).asShort(),
            caseHandle.child(compare).asDouble(),
            caseHandle.child(value).asDouble(),
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
    outputValue.setDouble(selectedValue);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblConditionMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
