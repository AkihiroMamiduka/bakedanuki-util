#include "bdUtilNodes/nodes/BdDblConditionNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Comparison.h"

const MString BdDblConditionNode::typeName("bdDbl_Condition");
const MTypeId BdDblConditionNode::typeId(0x0007F02E);

MObject BdDblConditionNode::input;
MObject BdDblConditionNode::operation;
MObject BdDblConditionNode::compare;
MObject BdDblConditionNode::trueValue;
MObject BdDblConditionNode::falseValue;
MObject BdDblConditionNode::output;

void* BdDblConditionNode::creator() {
    return new BdDblConditionNode();
}

MStatus BdDblConditionNode::initialize() {
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
    status = addAttribute(operation);
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
    status = addAttribute(compare);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        trueValue,
        "trueValue",
        "tv",
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
    status = addAttribute(trueValue);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        falseValue,
        "falseValue",
        "fv",
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
    status = addAttribute(falseValue);
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

    const std::array<MObject, 5> inputAttributes = {
        input,
        operation,
        compare,
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

MStatus BdDblConditionNode::compute(
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
    const double compareValue = dataBlock
                                    .inputValue(compare, &status)
                                    .asDouble();
    if (!status) {
        return status;
    }

    const MObject& selectedAttribute = bd_util_nodes::evaluateComparison(
        inputValue,
        operationValue,
        compareValue
    )
                                         ? trueValue
                                         : falseValue;
    const double selectedValue = dataBlock
                                     .inputValue(selectedAttribute, &status)
                                     .asDouble();
    if (!status) {
        return status;
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.setDouble(selectedValue);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblConditionNode::schedulingType() const {
    return MPxNode::kParallel;
}
