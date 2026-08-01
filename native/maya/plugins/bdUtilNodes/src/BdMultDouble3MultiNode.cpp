#include "bdUtilNodes/BdMultDouble3MultiNode.h"

#include <array>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/Double3Attribute.h"
#include "bdUtilNodes/NumericAttribute.h"

const MString BdMultDouble3MultiNode::typeName("bdMultDouble3Multi");
const MTypeId BdMultDouble3MultiNode::typeId(0x0007F001);

MObject BdMultDouble3MultiNode::input;
MObject BdMultDouble3MultiNode::inputX;
MObject BdMultDouble3MultiNode::inputY;
MObject BdMultDouble3MultiNode::inputZ;

MObject BdMultDouble3MultiNode::output;
MObject BdMultDouble3MultiNode::outputX;
MObject BdMultDouble3MultiNode::outputY;
MObject BdMultDouble3MultiNode::outputZ;

void* BdMultDouble3MultiNode::creator() {
    return new BdMultDouble3MultiNode();
}

MStatus BdMultDouble3MultiNode::initialize() {
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
        1.0
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
        1.0
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

    const std::array<MObject, 4> inputs = {
        input,
        inputX,
        inputY,
        inputZ,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, output);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdMultDouble3MultiNode::compute(
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

    std::array<double, 3> product = {1.0, 1.0, 1.0};
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
        product[0] *= value[0];
        product[1] *= value[1];
        product[2] *= value[2];

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

    outputValue.set3Double(product[0], product[1], product[2]);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdMultDouble3MultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
