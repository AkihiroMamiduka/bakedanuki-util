#include "bdUtilNodes/nodes/BdQuatMultiplyMultiNode.h"

#include <algorithm>
#include <array>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"

namespace {

struct IndexedQuaternion {
    unsigned int logicalIndex;
    MQuaternion value;
};

}  // namespace

const MString BdQuatMultiplyMultiNode::typeName("bdQuat_MultiplyMulti");
const MTypeId BdQuatMultiplyMultiNode::typeId(0x0007F088);

MObject BdQuatMultiplyMultiNode::inputQuat;
MObject BdQuatMultiplyMultiNode::inputQuatX;
MObject BdQuatMultiplyMultiNode::inputQuatY;
MObject BdQuatMultiplyMultiNode::inputQuatZ;
MObject BdQuatMultiplyMultiNode::inputQuatW;

MObject BdQuatMultiplyMultiNode::outputQuat;
MObject BdQuatMultiplyMultiNode::outputQuatX;
MObject BdQuatMultiplyMultiNode::outputQuatY;
MObject BdQuatMultiplyMultiNode::outputQuatZ;
MObject BdQuatMultiplyMultiNode::outputQuatW;

void* BdQuatMultiplyMultiNode::creator() {
    return new BdQuatMultiplyMultiNode();
}

MStatus BdQuatMultiplyMultiNode::initialize() {
    MFnNumericAttribute attributeFn;

    MStatus status = bd_util_nodes::createQuaternionAttribute(
        attributeFn,
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        "inputQuat",
        "iq",
        "inputQuatX",
        "iqx",
        "inputQuatY",
        "iqy",
        "inputQuatZ",
        "iqz",
        "inputQuatW",
        "iqw"
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

    status = addAttribute(inputQuat);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createQuaternionAttribute(
        attributeFn,
        outputQuat,
        outputQuatX,
        outputQuatY,
        outputQuatZ,
        outputQuatW,
        "outputQuat",
        "oq",
        "outputQuatX",
        "oqx",
        "outputQuatY",
        "oqy",
        "outputQuatZ",
        "oqz",
        "outputQuatW",
        "oqw"
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::configureOutputNumericAttribute(attributeFn);
    if (!status) {
        return status;
    }

    status = addAttribute(outputQuat);
    if (!status) {
        return status;
    }

    const std::array<MObject, 5> inputs = {
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputQuat);
        if (!status) {
            return status;
        }
    }

    return MS::kSuccess;
}

MStatus BdQuatMultiplyMultiNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputQuat
        && requestedAttribute != outputQuatX
        && requestedAttribute != outputQuatY
        && requestedAttribute != outputQuatZ
        && requestedAttribute != outputQuatW
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MArrayDataHandle inputArray = dataBlock.inputArrayValue(
        inputQuat,
        &status
    );
    if (!status) {
        return status;
    }

    const unsigned int elementCount = inputArray.elementCount(&status);
    if (!status) {
        return status;
    }

    std::vector<IndexedQuaternion> values;
    values.reserve(elementCount);
    for (unsigned int index = 0; index < elementCount; ++index) {
        const unsigned int logicalIndex = inputArray.elementIndex(&status);
        if (!status) {
            return status;
        }

        MDataHandle inputValue = inputArray.inputValue(&status);
        if (!status) {
            return status;
        }

        const double4& value = inputValue.asDouble4();
        values.push_back({
            logicalIndex,
            MQuaternion(value[0], value[1], value[2], value[3]),
        });

        if (index + 1 < elementCount) {
            status = inputArray.next();
            if (!status) {
                return status;
            }
        }
    }

    std::sort(
        values.begin(),
        values.end(),
        [](const IndexedQuaternion& left, const IndexedQuaternion& right) {
            return left.logicalIndex < right.logicalIndex;
        }
    );

    MQuaternion product;
    if (!values.empty()) {
        product = values.front().value;
        for (std::size_t index = 1; index < values.size(); ++index) {
            product *= values[index].value;
        }
    }

    MDataHandle outputValue = dataBlock.outputValue(outputQuat, &status);
    if (!status) {
        return status;
    }

    outputValue.set4Double(product.x, product.y, product.z, product.w);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdQuatMultiplyMultiNode::schedulingType() const {
    return MPxNode::kParallel;
}
