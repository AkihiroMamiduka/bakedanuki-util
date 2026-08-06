#include "bdUtilNodes/nodes/BdConditionDblAExtraComposeNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdConditionDblAExtraComposeNode::typeName(
    "bdConditionDblAExtra_Compose"
);
const MTypeId BdConditionDblAExtraComposeNode::typeId(0x0007F086);

MObject BdConditionDblAExtraComposeNode::logic;
MObject BdConditionDblAExtraComposeNode::comparison;
MObject BdConditionDblAExtraComposeNode::compareValue;
MObject BdConditionDblAExtraComposeNode::output;
MObject BdConditionDblAExtraComposeNode::outputLogic;
MObject BdConditionDblAExtraComposeNode::outputComparison;
MObject BdConditionDblAExtraComposeNode::outputCompareValue;

void* BdConditionDblAExtraComposeNode::creator() {
    return new BdConditionDblAExtraComposeNode();
}

MStatus BdConditionDblAExtraComposeNode::initialize() {
    MFnEnumAttribute enumAttributeFn;
    MStatus status = bd_util_nodes::createLogicOperationAttribute(
        enumAttributeFn,
        logic,
        "logic",
        "lgc"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(logic);
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
    status = addAttribute(comparison);
    if (!status) {
        return status;
    }

    MFnUnitAttribute unitAttributeFn;
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
    status = addAttribute(compareValue);
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

    MFnCompoundAttribute compoundAttributeFn;
    output = compoundAttributeFn.create("output", "o", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             outputLogic,
             outputComparison,
             outputCompareValue,
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
             logic,
             comparison,
             compareValue,
         }) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdConditionDblAExtraComposeNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (requestedAttribute != output && requestedAttribute != outputLogic
        && requestedAttribute != outputComparison
        && requestedAttribute != outputCompareValue) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.child(outputLogic).setShort(
        dataBlock.inputValue(logic, &status).asShort()
    );
    if (!status) {
        return status;
    }
    outputValue.child(outputComparison).setShort(
        dataBlock.inputValue(comparison, &status).asShort()
    );
    if (!status) {
        return status;
    }
    outputValue.child(outputCompareValue).setDouble(
        dataBlock.inputValue(compareValue, &status).asDouble()
    );
    if (!status) {
        return status;
    }

    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdConditionDblAExtraComposeNode::schedulingType() const {
    return MPxNode::kParallel;
}
