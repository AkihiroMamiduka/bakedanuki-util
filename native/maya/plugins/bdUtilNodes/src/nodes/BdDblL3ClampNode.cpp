#include "bdUtilNodes/nodes/BdDblL3ClampNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Clamp.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3ClampNode::typeName("bdDblL3_Clamp");
const MTypeId BdDblL3ClampNode::typeId(0x0007F04C);

MObject BdDblL3ClampNode::input;
MObject BdDblL3ClampNode::inputX;
MObject BdDblL3ClampNode::inputY;
MObject BdDblL3ClampNode::inputZ;

MObject BdDblL3ClampNode::minimum;
MObject BdDblL3ClampNode::minimumX;
MObject BdDblL3ClampNode::minimumY;
MObject BdDblL3ClampNode::minimumZ;

MObject BdDblL3ClampNode::maximum;
MObject BdDblL3ClampNode::maximumX;
MObject BdDblL3ClampNode::maximumY;
MObject BdDblL3ClampNode::maximumZ;

MObject BdDblL3ClampNode::output;
MObject BdDblL3ClampNode::outputX;
MObject BdDblL3ClampNode::outputY;
MObject BdDblL3ClampNode::outputZ;

void* BdDblL3ClampNode::creator() {
    return new BdDblL3ClampNode();
}

MStatus BdDblL3ClampNode::initialize() {
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
        minimum,
        minimumX,
        minimumY,
        minimumZ,
        "min",
        "mn",
        "minX",
        "mnx",
        "minY",
        "mny",
        "minZ",
        "mnz",
        0.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(minimum);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        attributeFn,
        unitAttributeFn,
        maximum,
        maximumX,
        maximumY,
        maximumZ,
        "max",
        "mx",
        "maxX",
        "mxx",
        "maxY",
        "mxy",
        "maxZ",
        "mxz",
        1.0
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureInputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(maximum);
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

    const std::array<MObject, 12> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
        minimum,
        minimumX,
        minimumY,
        minimumZ,
        maximum,
        maximumX,
        maximumY,
        maximumZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblL3ClampNode::compute(
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

    MDataHandle minimumValue = dataBlock.inputValue(minimum, &status);
    if (!status) {
        return status;
    }

    MDataHandle maximumValue = dataBlock.inputValue(maximum, &status);
    if (!status) {
        return status;
    }

    const double3& inputComponents = inputValue.asDouble3();
    const double3& minimumComponents = minimumValue.asDouble3();
    const double3& maximumComponents = maximumValue.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(
        bd_util_nodes::clamp(
            inputComponents[0],
            minimumComponents[0],
            maximumComponents[0]
        ),
        bd_util_nodes::clamp(
            inputComponents[1],
            minimumComponents[1],
            maximumComponents[1]
        ),
        bd_util_nodes::clamp(
            inputComponents[2],
            minimumComponents[2],
            maximumComponents[2]
        )
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3ClampNode::schedulingType() const {
    return MPxNode::kParallel;
}
