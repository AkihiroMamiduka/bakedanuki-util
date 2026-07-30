#include "bdUtilNodes/BdDouble3MultNode.h"

#include <array>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnNumericData.h>
#include <maya/MPlug.h>

namespace {

MStatus createDouble3Attribute(
    MFnNumericAttribute& attributeFn,
    MObject& parent,
    MObject& childX,
    MObject& childY,
    MObject& childZ,
    const char* parentLongName,
    const char* parentShortName,
    const char* childXLongName,
    const char* childXShortName,
    const char* childYLongName,
    const char* childYShortName,
    const char* childZLongName,
    const char* childZShortName,
    double defaultValue
) {
    MStatus status;

    childX = attributeFn.create(
        childXLongName,
        childXShortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    if (!status) {
        return status;
    }

    childY = attributeFn.create(
        childYLongName,
        childYShortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    if (!status) {
        return status;
    }

    childZ = attributeFn.create(
        childZLongName,
        childZShortName,
        MFnNumericData::kDouble,
        defaultValue,
        &status
    );
    if (!status) {
        return status;
    }

    parent = attributeFn.create(
        parentLongName,
        parentShortName,
        childX,
        childY,
        childZ,
        &status
    );
    return status;
}

}  // namespace

const MString BdDouble3MultNode::typeName("bdDouble3Mult");
const MTypeId BdDouble3MultNode::typeId(0x0007F001);

MObject BdDouble3MultNode::input;
MObject BdDouble3MultNode::inputX;
MObject BdDouble3MultNode::inputY;
MObject BdDouble3MultNode::inputZ;

MObject BdDouble3MultNode::output;
MObject BdDouble3MultNode::outputX;
MObject BdDouble3MultNode::outputY;
MObject BdDouble3MultNode::outputZ;

void* BdDouble3MultNode::creator() {
    return new BdDouble3MultNode();
}

MStatus BdDouble3MultNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = createDouble3Attribute(
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

    attributeFn.setArray(true);
    attributeFn.setUsesArrayDataBuilder(true);
    attributeFn.setReadable(true);
    attributeFn.setWritable(true);
    attributeFn.setStorable(true);
    attributeFn.setKeyable(true);

    status = addAttribute(input);
    if (!status) {
        return status;
    }

    status = createDouble3Attribute(
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

    attributeFn.setReadable(true);
    attributeFn.setWritable(false);
    attributeFn.setStorable(false);
    attributeFn.setKeyable(false);

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
    const std::array<MObject, 4> outputs = {
        output,
        outputX,
        outputY,
        outputZ,
    };

    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : outputs) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }

    return MS::kSuccess;
}

MStatus BdDouble3MultNode::compute(
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

MPxNode::SchedulingType BdDouble3MultNode::schedulingType() const {
    return MPxNode::kParallel;
}
