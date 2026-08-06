#include "bdUtilNodes/nodes/BdAnyConditionDblANode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnTypedAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/TypedAnyAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/Comparison.h"
#include "bdUtilNodes/nodes/ConditionExtra.h"

const MString BdAnyConditionDblANode::typeName("bdAny_ConditionDblA");
const MTypeId BdAnyConditionDblANode::typeId(0x0007F084);

MObject BdAnyConditionDblANode::input;
MObject BdAnyConditionDblANode::operation;
MObject BdAnyConditionDblANode::compare;
MObject BdAnyConditionDblANode::extra;
MObject BdAnyConditionDblANode::logic;
MObject BdAnyConditionDblANode::comparison;
MObject BdAnyConditionDblANode::compareValue;
MObject BdAnyConditionDblANode::trueValue;
MObject BdAnyConditionDblANode::falseValue;
MObject BdAnyConditionDblANode::output;

void* BdAnyConditionDblANode::creator() {
    return new BdAnyConditionDblANode();
}

MStatus BdAnyConditionDblANode::initialize() {
    MFnUnitAttribute unitAttributeFn;

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
    status = addAttribute(operation);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        compare,
        "compare",
        "cmp",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(compare);
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        compareValue,
        "compareValue",
        "cv",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }

    MFnCompoundAttribute compoundAttributeFn;
    extra = compoundAttributeFn.create("extra", "ex", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {logic, comparison, compareValue}) {
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
    status = addAttribute(extra);
    if (!status) {
        return status;
    }

    MFnTypedAttribute typedAttributeFn;
    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        trueValue,
        "trueValue",
        "tv"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(trueValue);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        falseValue,
        "falseValue",
        "fv"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(falseValue);
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

    const std::array<MObject, 9> inputAttributes = {
        input,
        operation,
        compare,
        extra,
        logic,
        comparison,
        compareValue,
        trueValue,
        falseValue,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdAnyConditionDblANode::compute(
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
    const short operationValue = dataBlock
                                     .inputValue(operation, &status)
                                     .asShort();
    if (!status) {
        return status;
    }
    const double primaryCompareValue = dataBlock
                                           .inputValue(compare, &status)
                                           .asDouble();
    if (!status) {
        return status;
    }

    bool conditionResult = bd_util_nodes::evaluateComparison(
        inputValue,
        operationValue,
        primaryCompareValue
    );

    MArrayDataHandle extraHandles = dataBlock.inputArrayValue(
        extra,
        &status
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::evaluateExtraConditions(
        extraHandles,
        inputValue,
        logic,
        comparison,
        BdAnyConditionDblANode::compareValue,
        conditionResult
    );
    if (!status) {
        return status;
    }

    const MObject& selectedAttribute = conditionResult ? trueValue
                                                       : falseValue;
    MDataHandle selectedValue = dataBlock.inputValue(
        selectedAttribute,
        &status
    );
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    status = outputValue.copy(selectedValue);
    if (!status) {
        return status;
    }
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdAnyConditionDblANode::schedulingType() const {
    return MPxNode::kParallel;
}
