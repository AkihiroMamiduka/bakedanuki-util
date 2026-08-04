#include "bdUtilNodes/nodes/BdDblL3MaxMultiNode.h"

#include <array>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/math/MinMax.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"

const MString BdDblL3MaxMultiNode::typeName("bdDblL3_MaxMulti");
const MTypeId BdDblL3MaxMultiNode::typeId(0x0007F04A);

MObject BdDblL3MaxMultiNode::input;
MObject BdDblL3MaxMultiNode::inputX;
MObject BdDblL3MaxMultiNode::inputY;
MObject BdDblL3MaxMultiNode::inputZ;

MObject BdDblL3MaxMultiNode::output;
MObject BdDblL3MaxMultiNode::outputX;
MObject BdDblL3MaxMultiNode::outputY;
MObject BdDblL3MaxMultiNode::outputZ;

void* BdDblL3MaxMultiNode::creator() {
    return new BdDblL3MaxMultiNode();
}

MStatus BdDblL3MaxMultiNode::initialize() {
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

    status = attributeFn.setArray(true);
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

MStatus BdDblL3MaxMultiNode::compute(
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
    MArrayDataHandle inputArray = dataBlock.inputArrayValue(input, &status);
    if (!status) {
        return status;
    }

    std::array<double, 3> result = {0.0, 0.0, 0.0};
    const unsigned int elementCount = inputArray.elementCount(&status);
    if (!status) {
        return status;
    }

    for (unsigned int index = 0; index < elementCount; ++index) {
        MDataHandle inputValue = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }

        const double3& value = inputValue.asDouble3();
        if (index == 0) {
            result = {value[0], value[1], value[2]};
        } else {
            result[0] = bd_util_nodes::maximum(result[0], value[0]);
            result[1] = bd_util_nodes::maximum(result[1], value[1]);
            result[2] = bd_util_nodes::maximum(result[2], value[2]);
        }

        if (index + 1 < elementCount) {
            status = inputArray.next();
            if (!status) {
                return status;
            }
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }

    outputValue.set3Double(result[0], result[1], result[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdDblL3MaxMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
