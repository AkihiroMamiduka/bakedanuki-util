#include "bdUtilNodes/nodes/BdConditionDblACaseComposeNode.h"

#include <maya/MArrayDataHandle.h>
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
#include "bdUtilNodes/nodes/ConditionCompose.h"

const MString BdConditionDblACaseComposeNode::typeName(
    "bdConditionDblACase_Compose"
);
const MTypeId BdConditionDblACaseComposeNode::typeId(0x0007F087);

MObject BdConditionDblACaseComposeNode::operation;
MObject BdConditionDblACaseComposeNode::compare;
MObject BdConditionDblACaseComposeNode::extra;
MObject BdConditionDblACaseComposeNode::logic;
MObject BdConditionDblACaseComposeNode::comparison;
MObject BdConditionDblACaseComposeNode::compareValue;
MObject BdConditionDblACaseComposeNode::value;
MObject BdConditionDblACaseComposeNode::output;
MObject BdConditionDblACaseComposeNode::outputOperation;
MObject BdConditionDblACaseComposeNode::outputCompare;
MObject BdConditionDblACaseComposeNode::outputExtra;
MObject BdConditionDblACaseComposeNode::outputLogic;
MObject BdConditionDblACaseComposeNode::outputComparison;
MObject BdConditionDblACaseComposeNode::outputCompareValue;
MObject BdConditionDblACaseComposeNode::outputValue;

void* BdConditionDblACaseComposeNode::creator() {
    return new BdConditionDblACaseComposeNode();
}

MStatus BdConditionDblACaseComposeNode::initialize() {
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

    MFnUnitAttribute unitAttributeFn;
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outputCompare,
        "outputCompare",
        "ocmp",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outputCompareValue,
        "outputCompareValue",
        "ocv",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
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

MStatus BdConditionDblACaseComposeNode::compute(
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
BdConditionDblACaseComposeNode::schedulingType() const {
    return MPxNode::kParallel;
}
