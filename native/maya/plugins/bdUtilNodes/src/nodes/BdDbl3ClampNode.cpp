#include "bdUtilNodes/nodes/BdDbl3ClampNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/math/Clamp.h"
#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDbl3ClampNode::typeName("bdDbl3_Clamp");
const MTypeId BdDbl3ClampNode::typeId(0x001426A2);

MObject BdDbl3ClampNode::input;
MObject BdDbl3ClampNode::inputX;
MObject BdDbl3ClampNode::inputY;
MObject BdDbl3ClampNode::inputZ;

MObject BdDbl3ClampNode::minimum;
MObject BdDbl3ClampNode::minimumX;
MObject BdDbl3ClampNode::minimumY;
MObject BdDbl3ClampNode::minimumZ;

MObject BdDbl3ClampNode::maximum;
MObject BdDbl3ClampNode::maximumX;
MObject BdDbl3ClampNode::maximumY;
MObject BdDbl3ClampNode::maximumZ;

MObject BdDbl3ClampNode::output;
MObject BdDbl3ClampNode::outputX;
MObject BdDbl3ClampNode::outputY;
MObject BdDbl3ClampNode::outputZ;

void* BdDbl3ClampNode::creator() {
    return new BdDbl3ClampNode();
}

MStatus BdDbl3ClampNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

    status = bd_util_nodes::createDouble3Attribute(
        attributeFn,
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

MStatus BdDbl3ClampNode::compute(
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

MPxNode::SchedulingType BdDbl3ClampNode::schedulingType() const {
    return MPxNode::kParallel;
}
