#include "bdUtilNodes/nodes/BdDbl3ConditionNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Comparison.h"

const MString BdDbl3ConditionNode::typeName("bdDbl3_Condition");
const MTypeId BdDbl3ConditionNode::typeId(0x0007F02C);

MObject BdDbl3ConditionNode::input;
MObject BdDbl3ConditionNode::operation;
MObject BdDbl3ConditionNode::compare;

MObject BdDbl3ConditionNode::trueValue;
MObject BdDbl3ConditionNode::trueValueX;
MObject BdDbl3ConditionNode::trueValueY;
MObject BdDbl3ConditionNode::trueValueZ;

MObject BdDbl3ConditionNode::falseValue;
MObject BdDbl3ConditionNode::falseValueX;
MObject BdDbl3ConditionNode::falseValueY;
MObject BdDbl3ConditionNode::falseValueZ;

MObject BdDbl3ConditionNode::output;
MObject BdDbl3ConditionNode::outputX;
MObject BdDbl3ConditionNode::outputY;
MObject BdDbl3ConditionNode::outputZ;

void* BdDbl3ConditionNode::creator() {
    return new BdDbl3ConditionNode();
}

MStatus BdDbl3ConditionNode::initialize() {
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

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        trueValue,
        trueValueX,
        trueValueY,
        trueValueZ,
        "trueValue",
        "tv",
        "trueValueX",
        "tvx",
        "trueValueY",
        "tvy",
        "trueValueZ",
        "tvz",
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

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        falseValue,
        falseValueX,
        falseValueY,
        falseValueZ,
        "falseValue",
        "fv",
        "falseValueX",
        "fvx",
        "falseValueY",
        "fvy",
        "falseValueZ",
        "fvz",
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

    const std::array<MObject, 11> inputAttributes = {
        input,
        operation,
        compare,
        trueValue,
        trueValueX,
        trueValueY,
        trueValueZ,
        falseValue,
        falseValueX,
        falseValueY,
        falseValueZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdDbl3ConditionNode::compute(
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
    MDataHandle selectedHandle = dataBlock.inputValue(
        selectedAttribute,
        &status
    );
    if (!status) {
        return status;
    }
    const double3& selectedValue = selectedHandle.asDouble3();

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

MPxNode::SchedulingType BdDbl3ConditionNode::schedulingType() const {
    return MPxNode::kParallel;
}
