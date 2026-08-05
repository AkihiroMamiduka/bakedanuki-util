#include "bdUtilNodes/nodes/BdAnyConditionDblMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/TypedAnyAttribute.h"
#include "bdUtilNodes/math/Comparison.h"
#include "bdUtilNodes/nodes/ConditionExtra.h"

const MString BdAnyConditionDblMultiNode::typeName(
    "bdAny_ConditionDblMulti"
);
const MTypeId BdAnyConditionDblMultiNode::typeId(0x0007F02D);

MObject BdAnyConditionDblMultiNode::input;
MObject BdAnyConditionDblMultiNode::caseArray;
MObject BdAnyConditionDblMultiNode::operation;
MObject BdAnyConditionDblMultiNode::compare;
MObject BdAnyConditionDblMultiNode::extra;
MObject BdAnyConditionDblMultiNode::logic;
MObject BdAnyConditionDblMultiNode::comparison;
MObject BdAnyConditionDblMultiNode::compareValue;
MObject BdAnyConditionDblMultiNode::value;
MObject BdAnyConditionDblMultiNode::elseValue;
MObject BdAnyConditionDblMultiNode::output;

void* BdAnyConditionDblMultiNode::creator() {
    return new BdAnyConditionDblMultiNode();
}

MStatus BdAnyConditionDblMultiNode::initialize() {
    MFnNumericAttribute numericAttributeFn;
    MFnEnumAttribute enumAttributeFn;

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

    status = bd_util_nodes::createLogicOperationAttribute(
        enumAttributeFn,
        logic,
        "logic",
        "lgc"
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createComparisonOperationAttribute(
        enumAttributeFn,
        comparison,
        "comparison",
        "cpr"
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        compareValue,
        "compareValue",
        "cv",
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

    MFnCompoundAttribute extraAttributeFn;
    extra = extraAttributeFn.create("extra", "ex", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {logic, comparison, compareValue}) {
        status = extraAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
    }
    status = extraAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = extraAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = extraAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = extraAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    status = addAttribute(input);
    if (!status) {
        return status;
    }

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

    MFnTypedAttribute typedAttributeFn;
    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        value,
        "value",
        "v"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }

    MFnCompoundAttribute compoundAttributeFn;
    caseArray = compoundAttributeFn.create("case", "cs", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {operation, compare, extra, value}) {
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

    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        elseValue,
        "elseValue",
        "ev"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(elseValue);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        output,
        "output",
        "o"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 10> inputAttributes = {
        input,
        caseArray,
        operation,
        compare,
        extra,
        logic,
        comparison,
        compareValue,
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

MStatus BdAnyConditionDblMultiNode::compute(
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

    std::vector<unsigned int> logicalIndices;
    logicalIndices.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        logicalIndices.push_back(caseHandles.elementIndex(&status));
        if (!status) {
            return status;
        }

        if (index + 1 < elementCount) {
            status = caseHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(logicalIndices.begin(), logicalIndices.end());

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    for (const unsigned int logicalIndex : logicalIndices) {
        status = caseHandles.jumpToElement(logicalIndex);
        if (!status) {
            return status;
        }
        MDataHandle caseHandle = caseHandles.inputValue(&status);
        if (!status) {
            return status;
        }

        bool conditionResult = bd_util_nodes::evaluateComparison(
            inputValue,
            caseHandle.child(operation).asShort(),
            caseHandle.child(compare).asDouble()
        );

        MDataHandle extraDataHandle = caseHandle.child(extra);
        MArrayDataHandle extraHandles(extraDataHandle, &status);
        if (!status) {
            return status;
        }
        status = bd_util_nodes::evaluateExtraConditions(
            extraHandles,
            inputValue,
            logic,
            comparison,
            compareValue,
            conditionResult
        );
        if (!status) {
            return status;
        }

        if (!conditionResult) {
            continue;
        }

        MDataHandle selectedValue = caseHandle.child(value);
        status = outputValue.copy(selectedValue);
        if (!status) {
            return status;
        }
        return dataBlock.setClean(plug);
    }

    MDataHandle selectedValue = dataBlock.inputValue(elseValue, &status);
    if (!status) {
        return status;
    }
    status = outputValue.copy(selectedValue);
    if (!status) {
        return status;
    }
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdAnyConditionDblMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
