#include "bdUtilNodes/nodes/BdConditionDblExtraComposeNode.h"

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/ComparisonAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdConditionDblExtraComposeNode::typeName(
    "bdConditionDblExtra_Compose"
);
const MTypeId BdConditionDblExtraComposeNode::typeId(0x001426DA);

MObject BdConditionDblExtraComposeNode::logic;
MObject BdConditionDblExtraComposeNode::comparison;
MObject BdConditionDblExtraComposeNode::compareValue;
MObject BdConditionDblExtraComposeNode::output;
MObject BdConditionDblExtraComposeNode::outputLogic;
MObject BdConditionDblExtraComposeNode::outputComparison;
MObject BdConditionDblExtraComposeNode::outputCompareValue;

void* BdConditionDblExtraComposeNode::creator() {
    return new BdConditionDblExtraComposeNode();
}

MStatus BdConditionDblExtraComposeNode::initialize() {
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

    MFnNumericAttribute numericAttributeFn;
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

MStatus BdConditionDblExtraComposeNode::compute(
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
BdConditionDblExtraComposeNode::schedulingType() const {
    return MPxNode::kParallel;
}
