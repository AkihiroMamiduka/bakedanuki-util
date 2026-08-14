#include "bdUtilNodes/nodes/BdQuatChangeBasisNode.h"

#include <array>
#include <utility>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"

namespace {

enum class BasisDirection : short {
    kApplyAxis = 0,
    kRemoveAxis = 1,
};

}  // namespace

const MString BdQuatChangeBasisNode::typeName("bdQuat_ChangeBasis");
const MTypeId BdQuatChangeBasisNode::typeId(0x00142710);

MObject BdQuatChangeBasisNode::inputQuat;
MObject BdQuatChangeBasisNode::inputQuatX;
MObject BdQuatChangeBasisNode::inputQuatY;
MObject BdQuatChangeBasisNode::inputQuatZ;
MObject BdQuatChangeBasisNode::inputQuatW;

MObject BdQuatChangeBasisNode::axisQuat;
MObject BdQuatChangeBasisNode::axisQuatX;
MObject BdQuatChangeBasisNode::axisQuatY;
MObject BdQuatChangeBasisNode::axisQuatZ;
MObject BdQuatChangeBasisNode::axisQuatW;

MObject BdQuatChangeBasisNode::direction;

MObject BdQuatChangeBasisNode::outputQuat;
MObject BdQuatChangeBasisNode::outputQuatX;
MObject BdQuatChangeBasisNode::outputQuatY;
MObject BdQuatChangeBasisNode::outputQuatZ;
MObject BdQuatChangeBasisNode::outputQuatW;

void* BdQuatChangeBasisNode::creator() {
    return new BdQuatChangeBasisNode();
}

MStatus BdQuatChangeBasisNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
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
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(inputQuat);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        axisQuat,
        axisQuatX,
        axisQuatY,
        axisQuatZ,
        axisQuatW,
        "axisQuat",
        "aq",
        "axisQuatX",
        "aqx",
        "axisQuatY",
        "aqy",
        "axisQuatZ",
        "aqz",
        "axisQuatW",
        "aqw"
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(axisQuat);
    if (!status) {
        return status;
    }

    MFnEnumAttribute enumAttributeFn;
    direction = enumAttributeFn.create(
        "direction",
        "dir",
        static_cast<short>(BasisDirection::kApplyAxis),
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : {
             std::pair<const char*, BasisDirection>{
                 "ApplyAxis",
                 BasisDirection::kApplyAxis,
             },
             std::pair<const char*, BasisDirection>{
                 "RemoveAxis",
                 BasisDirection::kRemoveAxis,
             },
         }) {
        status = enumAttributeFn.addField(
            field.first,
            static_cast<short>(field.second)
        );
        if (!status) {
            return status;
        }
    }
    status = enumAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    status = enumAttributeFn.setKeyable(true);
    if (!status) {
        return status;
    }
    status = addAttribute(direction);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
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
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(outputQuat);
    if (!status) {
        return status;
    }

    const std::array<MObject, 11> inputs = {
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        axisQuat,
        axisQuatX,
        axisQuatY,
        axisQuatZ,
        axisQuatW,
        direction,
    };
    for (const MObject& inputAttribute : inputs) {
        status = attributeAffects(inputAttribute, outputQuat);
        if (!status) {
            return status;
        }
    }
    return MS::kSuccess;
}

MStatus BdQuatChangeBasisNode::compute(
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
    MDataHandle inputHandle = dataBlock.inputValue(inputQuat, &status);
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();
    const MQuaternion input(
        inputValue[0],
        inputValue[1],
        inputValue[2],
        inputValue[3]
    );

    MDataHandle axisHandle = dataBlock.inputValue(axisQuat, &status);
    if (!status) {
        return status;
    }
    const double4& axisValue = axisHandle.asDouble4();
    const MQuaternion axis(
        axisValue[0],
        axisValue[1],
        axisValue[2],
        axisValue[3]
    );
    const MQuaternion inverseAxis = axis.inverse();

    const short directionValue = dataBlock.inputValue(
        direction,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    MQuaternion result;
    switch (static_cast<BasisDirection>(directionValue)) {
        case BasisDirection::kApplyAxis:
            result = inverseAxis * input * axis;
            break;
        case BasisDirection::kRemoveAxis:
            result = axis * input * inverseAxis;
            break;
        default:
            return MS::kInvalidParameter;
    }

    MDataHandle outputValue = dataBlock.outputValue(outputQuat, &status);
    if (!status) {
        return status;
    }
    outputValue.set4Double(result.x, result.y, result.z, result.w);
    outputValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdQuatChangeBasisNode::schedulingType() const {
    return MPxNode::kParallel;
}
