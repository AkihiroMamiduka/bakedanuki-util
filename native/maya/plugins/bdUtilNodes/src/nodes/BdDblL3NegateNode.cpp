#include "bdUtilNodes/nodes/BdDblL3NegateNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/math/Negate.h"

const MString BdDblL3NegateNode::typeName("bdDblL3_Negate");
const MTypeId BdDblL3NegateNode::typeId(0x0007F050);

MObject BdDblL3NegateNode::input;
MObject BdDblL3NegateNode::inputX;
MObject BdDblL3NegateNode::inputY;
MObject BdDblL3NegateNode::inputZ;

MObject BdDblL3NegateNode::output;
MObject BdDblL3NegateNode::outputX;
MObject BdDblL3NegateNode::outputY;
MObject BdDblL3NegateNode::outputZ;

void* BdDblL3NegateNode::creator() {
    return new BdDblL3NegateNode();
}

MStatus BdDblL3NegateNode::initialize() {
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

    const std::array<MObject, 4> inputAttributes = {
        input,
        inputX,
        inputY,
        inputZ,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdDblL3NegateNode::compute(
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
    const double3& inputComponents = inputValue.asDouble3();

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        bd_util_nodes::negate(inputComponents[0]),
        bd_util_nodes::negate(inputComponents[1]),
        bd_util_nodes::negate(inputComponents[2])
    );
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3NegateNode::schedulingType() const {
    return MPxNode::kParallel;
}
