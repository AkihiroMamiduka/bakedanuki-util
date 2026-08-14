#include "bdUtilNodes/nodes/BdDblLMapRangeNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/MapRange.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblLMapRangeNode::typeName("bdDblL_MapRange");
const MTypeId BdDblLMapRangeNode::typeId(0x001426D2);

MObject BdDblLMapRangeNode::input;
MObject BdDblLMapRangeNode::sourceMinimum;
MObject BdDblLMapRangeNode::sourceMaximum;
MObject BdDblLMapRangeNode::targetMinimum;
MObject BdDblLMapRangeNode::targetMaximum;
MObject BdDblLMapRangeNode::clamp;
MObject BdDblLMapRangeNode::output;

void* BdDblLMapRangeNode::creator() {
    return new BdDblLMapRangeNode();
}

MStatus BdDblLMapRangeNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        sourceMinimum,
        "srcMin",
        "smin",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(sourceMinimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        sourceMaximum,
        "srcMax",
        "smax",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(sourceMaximum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        targetMinimum,
        "dstMin",
        "dmin",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(targetMinimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        targetMaximum,
        "dstMax",
        "dmax",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(targetMaximum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        attributeFn,
        clamp,
        "clamp",
        "c",
        true
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(clamp);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        output,
        "output",
        "o",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 6> inputAttributes = {
        input,
        sourceMinimum,
        sourceMaximum,
        targetMinimum,
        targetMaximum,
        clamp,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblLMapRangeNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (plug.attribute() != output) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputValue = dataBlock.inputValue(input, &status);
    if (!status) {
        return status;
    }
    MDataHandle sourceMinimumValue = dataBlock.inputValue(
        sourceMinimum,
        &status
    );
    if (!status) {
        return status;
    }
    MDataHandle sourceMaximumValue = dataBlock.inputValue(
        sourceMaximum,
        &status
    );
    if (!status) {
        return status;
    }
    MDataHandle targetMinimumValue = dataBlock.inputValue(
        targetMinimum,
        &status
    );
    if (!status) {
        return status;
    }
    MDataHandle targetMaximumValue = dataBlock.inputValue(
        targetMaximum,
        &status
    );
    if (!status) {
        return status;
    }
    MDataHandle clampValue = dataBlock.inputValue(clamp, &status);
    if (!status) {
        return status;
    }
    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.setDouble(
        bd_util_nodes::mapRange(
            inputValue.asDouble(),
            sourceMinimumValue.asDouble(),
            sourceMaximumValue.asDouble(),
            targetMinimumValue.asDouble(),
            targetMaximumValue.asDouble(),
            clampValue.asBool()
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblLMapRangeNode::schedulingType() const {
    return MPxNode::kParallel;
}
