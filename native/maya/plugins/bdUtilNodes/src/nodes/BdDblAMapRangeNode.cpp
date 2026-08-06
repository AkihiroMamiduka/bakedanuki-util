#include "bdUtilNodes/nodes/BdDblAMapRangeNode.h"

#include <array>

#include <maya/MAngle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/MapRange.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"

const MString BdDblAMapRangeNode::typeName("bdDblA_MapRange");
const MTypeId BdDblAMapRangeNode::typeId(0x0007F076);

MObject BdDblAMapRangeNode::input;
MObject BdDblAMapRangeNode::sourceMinimum;
MObject BdDblAMapRangeNode::sourceMaximum;
MObject BdDblAMapRangeNode::targetMinimum;
MObject BdDblAMapRangeNode::targetMaximum;
MObject BdDblAMapRangeNode::clamp;
MObject BdDblAMapRangeNode::output;

void* BdDblAMapRangeNode::creator() {
    return new BdDblAMapRangeNode();
}

MStatus BdDblAMapRangeNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;
    const double fullRotationRadians =
        MAngle(360.0, MAngle::kDegrees).asRadians();

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

    status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        sourceMaximum,
        "srcMax",
        "smax",
        fullRotationRadians
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

    status = bd_util_nodes::createDoubleAngleAttribute(
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        targetMaximum,
        "dstMax",
        "dmax",
        fullRotationRadians
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

    status = bd_util_nodes::createDoubleAngleAttribute(
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

MStatus BdDblAMapRangeNode::compute(
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

MPxNode::SchedulingType BdDblAMapRangeNode::schedulingType() const {
    return MPxNode::kParallel;
}
