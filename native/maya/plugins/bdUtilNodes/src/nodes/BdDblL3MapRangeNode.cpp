#include "bdUtilNodes/nodes/BdDblL3MapRangeNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/math/MapRange.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3MapRangeNode::typeName("bdDblL3_MapRange");
const MTypeId BdDblL3MapRangeNode::typeId(0x0007F054);

MObject BdDblL3MapRangeNode::input;
MObject BdDblL3MapRangeNode::inputX;
MObject BdDblL3MapRangeNode::inputY;
MObject BdDblL3MapRangeNode::inputZ;

MObject BdDblL3MapRangeNode::sourceMinimum;
MObject BdDblL3MapRangeNode::sourceMinimumX;
MObject BdDblL3MapRangeNode::sourceMinimumY;
MObject BdDblL3MapRangeNode::sourceMinimumZ;

MObject BdDblL3MapRangeNode::sourceMaximum;
MObject BdDblL3MapRangeNode::sourceMaximumX;
MObject BdDblL3MapRangeNode::sourceMaximumY;
MObject BdDblL3MapRangeNode::sourceMaximumZ;

MObject BdDblL3MapRangeNode::targetMinimum;
MObject BdDblL3MapRangeNode::targetMinimumX;
MObject BdDblL3MapRangeNode::targetMinimumY;
MObject BdDblL3MapRangeNode::targetMinimumZ;

MObject BdDblL3MapRangeNode::targetMaximum;
MObject BdDblL3MapRangeNode::targetMaximumX;
MObject BdDblL3MapRangeNode::targetMaximumY;
MObject BdDblL3MapRangeNode::targetMaximumZ;

MObject BdDblL3MapRangeNode::clamp;

MObject BdDblL3MapRangeNode::output;
MObject BdDblL3MapRangeNode::outputX;
MObject BdDblL3MapRangeNode::outputY;
MObject BdDblL3MapRangeNode::outputZ;

void* BdDblL3MapRangeNode::creator() {
    return new BdDblL3MapRangeNode();
}

MStatus BdDblL3MapRangeNode::initialize() {
    MFnNumericAttribute attributeFn;
    MFnUnitAttribute unitAttributeFn;

    MStatus status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        input,
        inputX,
        inputY,
        inputZ,
        "input",
        "i",
        "inputX",
        "ix",
        "inputY",
        "iy",
        "inputZ",
        "iz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        sourceMinimum,
        sourceMinimumX,
        sourceMinimumY,
        sourceMinimumZ,
        "srcMin",
        "smin",
        "srcMinX",
        "sminx",
        "srcMinY",
        "sminy",
        "srcMinZ",
        "sminz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(sourceMinimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        sourceMaximum,
        sourceMaximumX,
        sourceMaximumY,
        sourceMaximumZ,
        "srcMax",
        "smax",
        "srcMaxX",
        "smaxx",
        "srcMaxY",
        "smaxy",
        "srcMaxZ",
        "smaxz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(sourceMaximum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        targetMinimum,
        targetMinimumX,
        targetMinimumY,
        targetMinimumZ,
        "dstMin",
        "dmin",
        "dstMinX",
        "dminx",
        "dstMinY",
        "dminy",
        "dstMinZ",
        "dminz",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(targetMinimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        targetMaximum,
        targetMaximumX,
        targetMaximumY,
        targetMaximumZ,
        "dstMax",
        "dmax",
        "dstMaxX",
        "dmaxx",
        "dstMaxY",
        "dmaxy",
        "dstMaxZ",
        "dmaxz",
        1.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
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
    status = bd_util_nodes::configureOutputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    const std::array<MObject, 21> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
        sourceMinimum,
        sourceMinimumX,
        sourceMinimumY,
        sourceMinimumZ,
        sourceMaximum,
        sourceMaximumX,
        sourceMaximumY,
        sourceMaximumZ,
        targetMinimum,
        targetMinimumX,
        targetMinimumY,
        targetMinimumZ,
        targetMaximum,
        targetMaximumX,
        targetMaximumY,
        targetMaximumZ,
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

MStatus BdDblL3MapRangeNode::compute(
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

    const double3& inputComponents = inputValue.asDouble3();
    const double3& sourceMinimumComponents = sourceMinimumValue.asDouble3();
    const double3& sourceMaximumComponents = sourceMaximumValue.asDouble3();
    const double3& targetMinimumComponents = targetMinimumValue.asDouble3();
    const double3& targetMaximumComponents = targetMaximumValue.asDouble3();
    const bool shouldClamp = clampValue.asBool();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        bd_util_nodes::mapRange(
            inputComponents[0],
            sourceMinimumComponents[0],
            sourceMaximumComponents[0],
            targetMinimumComponents[0],
            targetMaximumComponents[0],
            shouldClamp
        ),
        bd_util_nodes::mapRange(
            inputComponents[1],
            sourceMinimumComponents[1],
            sourceMaximumComponents[1],
            targetMinimumComponents[1],
            targetMaximumComponents[1],
            shouldClamp
        ),
        bd_util_nodes::mapRange(
            inputComponents[2],
            sourceMinimumComponents[2],
            sourceMaximumComponents[2],
            targetMinimumComponents[2],
            targetMaximumComponents[2],
            shouldClamp
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3MapRangeNode::schedulingType() const {
    return MPxNode::kParallel;
}
