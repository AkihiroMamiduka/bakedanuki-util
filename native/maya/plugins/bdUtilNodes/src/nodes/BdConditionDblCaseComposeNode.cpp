#include "bdUtilNodes/nodes/BdConditionDblCaseComposeNode.h"

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
#include "bdUtilNodes/nodes/ConditionCompose.h"

const MString BdConditionDblCaseComposeNode::typeName(
    "bdConditionDblCase_Compose"
);
const MTypeId BdConditionDblCaseComposeNode::typeId(0x0007F05D);

MObject BdConditionDblCaseComposeNode::operation;
MObject BdConditionDblCaseComposeNode::compare;
MObject BdConditionDblCaseComposeNode::extra;
MObject BdConditionDblCaseComposeNode::logic;
MObject BdConditionDblCaseComposeNode::comparison;
MObject BdConditionDblCaseComposeNode::compareValue;
MObject BdConditionDblCaseComposeNode::value;
MObject BdConditionDblCaseComposeNode::output;
MObject BdConditionDblCaseComposeNode::outputOperation;
MObject BdConditionDblCaseComposeNode::outputCompare;
MObject BdConditionDblCaseComposeNode::outputExtra;
MObject BdConditionDblCaseComposeNode::outputLogic;
MObject BdConditionDblCaseComposeNode::outputComparison;
MObject BdConditionDblCaseComposeNode::outputCompareValue;
MObject BdConditionDblCaseComposeNode::outputValue;

void* BdConditionDblCaseComposeNode::creator() {
    return new BdConditionDblCaseComposeNode();
}

MStatus BdConditionDblCaseComposeNode::initialize() {
    MFnEnumAttribute enumAttributeFn;
    MStatus status = bd_util_nodes::createComparisonOperationAttribute(
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

    MFnNumericAttribute numericAttributeFn;
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
    status = addAttribute(value);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createComparisonOperationAttribute(
        enumAttributeFn,
        outputOperation,
        "outputOperation",
        "oop"
    );
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setKeyable(false);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        outputCompare,
        "outputCompare",
        "ocmp",
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

    status = bd_util_nodes::createLogicOperationAttribute(
        enumAttributeFn,
        outputLogic,
        "outputLogic",
        "olgc"
    );
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setKeyable(false);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createComparisonOperationAttribute(
        enumAttributeFn,
        outputComparison,
        "outputComparison",
        "ocpr"
    );
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setKeyable(false);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        outputCompareValue,
        "outputCompareValue",
        "ocv",
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

    MFnCompoundAttribute outputExtraAttributeFn;
    outputExtra = outputExtraAttributeFn.create(
        "outputExtra",
        "oex",
        &status
    );
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             outputLogic,
             outputComparison,
             outputCompareValue,
         }) {
        status = outputExtraAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
    }
    status = outputExtraAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = outputExtraAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = outputExtraAttributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = outputExtraAttributeFn.setStorable(false);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createTypedAnyAttribute(
        typedAttributeFn,
        outputValue,
        "outputValue",
        "ov"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputTypedAttribute(typedAttributeFn);
    if (!status) {
        return status;
    }

    output = compoundAttributeFn.create("output", "o", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             outputOperation,
             outputCompare,
             outputExtra,
             outputValue,
         }) {
        status = compoundAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
    }
    status = compoundAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    for (const MObject& inputAttribute : {
             operation,
             compare,
             extra,
             logic,
             comparison,
             compareValue,
             value,
         }) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdConditionDblCaseComposeNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (requestedAttribute != output
        && requestedAttribute != outputOperation
        && requestedAttribute != outputCompare
        && requestedAttribute != outputExtra
        && requestedAttribute != outputLogic
        && requestedAttribute != outputComparison
        && requestedAttribute != outputCompareValue
        && requestedAttribute != outputValue) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle outputHandle = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputHandle.child(outputOperation).setShort(
        dataBlock.inputValue(operation, &status).asShort()
    );
    if (!status) {
        return status;
    }
    outputHandle.child(outputCompare).setDouble(
        dataBlock.inputValue(compare, &status).asDouble()
    );
    if (!status) {
        return status;
    }

    MArrayDataHandle inputExtraHandles = dataBlock.inputArrayValue(
        extra,
        &status
    );
    if (!status) {
        return status;
    }
    MDataHandle outputExtraHandle = outputHandle.child(outputExtra);
    MArrayDataHandle outputExtraHandles(outputExtraHandle, &status);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::copyExtraConditionArray(
        dataBlock,
        inputExtraHandles,
        outputExtraHandles,
        logic,
        comparison,
        compareValue,
        outputExtra,
        outputLogic,
        outputComparison,
        outputCompareValue
    );
    if (!status) {
        return status;
    }

    MDataHandle inputValue = dataBlock.inputValue(value, &status);
    if (!status) {
        return status;
    }
    status = outputHandle.child(outputValue).copy(inputValue);
    if (!status) {
        return status;
    }

    outputHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdConditionDblCaseComposeNode::schedulingType() const {
    return MPxNode::kParallel;
}
