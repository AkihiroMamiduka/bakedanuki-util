#include "bdUtilNodes/nodes/BdQuatDecomposeBendTwistNode.h"

#include <array>

#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/BendTwistAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/math/BendTwist.h"

const MString BdQuatDecomposeBendTwistNode::typeName(
    "bdQuat_DecomposeBendTwist"
);
const MTypeId BdQuatDecomposeBendTwistNode::typeId(0x0007F089);

MObject BdQuatDecomposeBendTwistNode::inputQuat;
MObject BdQuatDecomposeBendTwistNode::inputQuatX;
MObject BdQuatDecomposeBendTwistNode::inputQuatY;
MObject BdQuatDecomposeBendTwistNode::inputQuatZ;
MObject BdQuatDecomposeBendTwistNode::inputQuatW;

MObject BdQuatDecomposeBendTwistNode::axisQuat;
MObject BdQuatDecomposeBendTwistNode::axisQuatX;
MObject BdQuatDecomposeBendTwistNode::axisQuatY;
MObject BdQuatDecomposeBendTwistNode::axisQuatZ;
MObject BdQuatDecomposeBendTwistNode::axisQuatW;

MObject BdQuatDecomposeBendTwistNode::order;

MObject BdQuatDecomposeBendTwistNode::output;
MObject BdQuatDecomposeBendTwistNode::outputTwist;
MObject BdQuatDecomposeBendTwistNode::outputBendH;
MObject BdQuatDecomposeBendTwistNode::outputBendV;
MObject BdQuatDecomposeBendTwistNode::bendRatio;

void* BdQuatDecomposeBendTwistNode::creator() {
    return new BdQuatDecomposeBendTwistNode();
}

MStatus BdQuatDecomposeBendTwistNode::initialize() {
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
    status = bd_util_nodes::createBendTwistOrderAttribute(
        enumAttributeFn,
        order,
        "order",
        "ord"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(order);
    if (!status) {
        return status;
    }

    MFnUnitAttribute unitAttributeFn;
    status = bd_util_nodes::createBendTwistAttribute(
        numericAttributeFn,
        unitAttributeFn,
        output,
        outputTwist,
        outputBendH,
        outputBendV,
        "output",
        "o",
        "outputTwist",
        "otw",
        "outputBendH",
        "obh",
        "outputBendV",
        "obv"
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
    status = addAttribute(output);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        bendRatio,
        "bendRatio",
        "br",
        0.0
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setMax(1.0);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureOutputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(bendRatio);
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
        order,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {output, bendRatio}) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdQuatDecomposeBendTwistNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != output
        && requestedAttribute != outputTwist
        && requestedAttribute != outputBendH
        && requestedAttribute != outputBendV
        && requestedAttribute != bendRatio
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(
        inputQuat,
        &status
    );
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();

    MDataHandle axisOrientationHandle = dataBlock.inputValue(
        axisQuat,
        &status
    );
    if (!status) {
        return status;
    }
    const double4& axisOrientationValue =
        axisOrientationHandle.asDouble4();
    const short orderValue = dataBlock.inputValue(order, &status).asShort();
    if (!status) {
        return status;
    }

    const bd_util_nodes::BendTwistComponents result =
        bd_util_nodes::decomposeBendTwist(
            MQuaternion(
                inputValue[0],
                inputValue[1],
                inputValue[2],
                inputValue[3]
            ),
            MQuaternion(
                axisOrientationValue[0],
                axisOrientationValue[1],
                axisOrientationValue[2],
                axisOrientationValue[3]
            ),
            static_cast<bd_util_nodes::BendTwistOrder>(orderValue)
        );

    MDataHandle outputValue = dataBlock.outputValue(output, &status);
    if (!status) {
        return status;
    }
    outputValue.set3Double(
        result.twist,
        result.bendHorizontal,
        result.bendVertical
    );
    outputValue.setClean();

    MDataHandle bendRatioValue = dataBlock.outputValue(bendRatio, &status);
    if (!status) {
        return status;
    }
    bendRatioValue.setDouble(result.bendRatio);
    bendRatioValue.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdQuatDecomposeBendTwistNode::schedulingType() const {
    return MPxNode::kParallel;
}
