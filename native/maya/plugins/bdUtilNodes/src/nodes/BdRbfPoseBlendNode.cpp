#include "bdUtilNodes/nodes/BdRbfPoseBlendNode.h"

#include <array>
#include <unordered_map>
#include <utility>
#include <vector>

#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MEulerRotation.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>
#include <maya/MQuaternion.h>

#include "bdUtilNodes/attributes/Double3Attribute.h"
#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/attributes/RotateAttribute.h"
#include "bdUtilNodes/math/PoseBlend.h"

namespace {

MStatus configureOutputEnumAttribute(MFnEnumAttribute& attributeFn) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setWritable(false);
    if (!status) {
        return status;
    }
    status = attributeFn.setStorable(false);
    if (!status) {
        return status;
    }
    return attributeFn.setKeyable(false);
}

std::array<double, 3> toArray(const double3& value) {
    return {value[0], value[1], value[2]};
}

bool isRequestedOutput(const MObject& attribute) {
    return attribute == BdRbfPoseBlendNode::outputTranslate
        || attribute == BdRbfPoseBlendNode::outputTranslateX
        || attribute == BdRbfPoseBlendNode::outputTranslateY
        || attribute == BdRbfPoseBlendNode::outputTranslateZ
        || attribute == BdRbfPoseBlendNode::outputRotate
        || attribute == BdRbfPoseBlendNode::outputRotateX
        || attribute == BdRbfPoseBlendNode::outputRotateY
        || attribute == BdRbfPoseBlendNode::outputRotateZ
        || attribute == BdRbfPoseBlendNode::outputQuat
        || attribute == BdRbfPoseBlendNode::outputQuatX
        || attribute == BdRbfPoseBlendNode::outputQuatY
        || attribute == BdRbfPoseBlendNode::outputQuatZ
        || attribute == BdRbfPoseBlendNode::outputQuatW
        || attribute == BdRbfPoseBlendNode::outputScale
        || attribute == BdRbfPoseBlendNode::outputScaleX
        || attribute == BdRbfPoseBlendNode::outputScaleY
        || attribute == BdRbfPoseBlendNode::outputScaleZ
        || attribute == BdRbfPoseBlendNode::isValid
        || attribute == BdRbfPoseBlendNode::blendStatus;
}

}  // namespace

const MString BdRbfPoseBlendNode::typeName("bdRbf_PoseBlend");
const MTypeId BdRbfPoseBlendNode::typeId(0x00142714);

MObject BdRbfPoseBlendNode::baseTranslate;
MObject BdRbfPoseBlendNode::baseTranslateX;
MObject BdRbfPoseBlendNode::baseTranslateY;
MObject BdRbfPoseBlendNode::baseTranslateZ;

MObject BdRbfPoseBlendNode::baseRotate;
MObject BdRbfPoseBlendNode::baseRotateX;
MObject BdRbfPoseBlendNode::baseRotateY;
MObject BdRbfPoseBlendNode::baseRotateZ;

MObject BdRbfPoseBlendNode::baseScale;
MObject BdRbfPoseBlendNode::baseScaleX;
MObject BdRbfPoseBlendNode::baseScaleY;
MObject BdRbfPoseBlendNode::baseScaleZ;

MObject BdRbfPoseBlendNode::rotateOrder;

MObject BdRbfPoseBlendNode::pose;
MObject BdRbfPoseBlendNode::poseTranslate;
MObject BdRbfPoseBlendNode::poseTranslateX;
MObject BdRbfPoseBlendNode::poseTranslateY;
MObject BdRbfPoseBlendNode::poseTranslateZ;
MObject BdRbfPoseBlendNode::poseRotate;
MObject BdRbfPoseBlendNode::poseRotateX;
MObject BdRbfPoseBlendNode::poseRotateY;
MObject BdRbfPoseBlendNode::poseRotateZ;
MObject BdRbfPoseBlendNode::poseScale;
MObject BdRbfPoseBlendNode::poseScaleX;
MObject BdRbfPoseBlendNode::poseScaleY;
MObject BdRbfPoseBlendNode::poseScaleZ;
MObject BdRbfPoseBlendNode::enabled;

MObject BdRbfPoseBlendNode::weight;

MObject BdRbfPoseBlendNode::outputTranslate;
MObject BdRbfPoseBlendNode::outputTranslateX;
MObject BdRbfPoseBlendNode::outputTranslateY;
MObject BdRbfPoseBlendNode::outputTranslateZ;

MObject BdRbfPoseBlendNode::outputRotate;
MObject BdRbfPoseBlendNode::outputRotateX;
MObject BdRbfPoseBlendNode::outputRotateY;
MObject BdRbfPoseBlendNode::outputRotateZ;

MObject BdRbfPoseBlendNode::outputQuat;
MObject BdRbfPoseBlendNode::outputQuatX;
MObject BdRbfPoseBlendNode::outputQuatY;
MObject BdRbfPoseBlendNode::outputQuatZ;
MObject BdRbfPoseBlendNode::outputQuatW;

MObject BdRbfPoseBlendNode::outputScale;
MObject BdRbfPoseBlendNode::outputScaleX;
MObject BdRbfPoseBlendNode::outputScaleY;
MObject BdRbfPoseBlendNode::outputScaleZ;

MObject BdRbfPoseBlendNode::isValid;
MObject BdRbfPoseBlendNode::blendStatus;

void* BdRbfPoseBlendNode::creator() {
    return new BdRbfPoseBlendNode();
}

MStatus BdRbfPoseBlendNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        baseTranslate,
        baseTranslateX,
        baseTranslateY,
        baseTranslateZ,
        "baseTranslate",
        "bt",
        "baseTranslateX",
        "btx",
        "baseTranslateY",
        "bty",
        "baseTranslateZ",
        "btz",
        0.0
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
    status = addAttribute(baseTranslate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        baseRotate,
        baseRotateX,
        baseRotateY,
        baseRotateZ,
        "baseRotate",
        "br",
        "baseRotateX",
        "brx",
        "baseRotateY",
        "bry",
        "baseRotateZ",
        "brz"
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
    status = addAttribute(baseRotate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        baseScale,
        baseScaleX,
        baseScaleY,
        baseScaleZ,
        "baseScale",
        "bsc",
        "baseScaleX",
        "bscx",
        "baseScaleY",
        "bscy",
        "baseScaleZ",
        "bscz",
        1.0
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
    status = addAttribute(baseScale);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateOrderAttribute(
        enumAttributeFn,
        rotateOrder,
        "rotateOrder",
        "ro"
    );
    if (!status) {
        return status;
    }
    status = addAttribute(rotateOrder);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        poseTranslate,
        poseTranslateX,
        poseTranslateY,
        poseTranslateZ,
        "translate",
        "pt",
        "translateX",
        "ptx",
        "translateY",
        "pty",
        "translateZ",
        "ptz",
        0.0
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

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        poseRotate,
        poseRotateX,
        poseRotateY,
        poseRotateZ,
        "rotate",
        "pr",
        "rotateX",
        "prx",
        "rotateY",
        "pry",
        "rotateZ",
        "prz"
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

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        poseScale,
        poseScaleX,
        poseScaleY,
        poseScaleZ,
        "scale",
        "ps",
        "scaleX",
        "psx",
        "scaleY",
        "psy",
        "scaleZ",
        "psz",
        1.0
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

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        enabled,
        "enabled",
        "en",
        true
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

    MFnCompoundAttribute compoundAttributeFn;
    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             poseTranslate,
             poseRotate,
             poseScale,
             enabled,
         }) {
        status = compoundAttributeFn.addChild(child);
        if (!status) {
            return status;
        }
    }
    status = compoundAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = compoundAttributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    status = addAttribute(pose);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        weight,
        "weight",
        "w",
        0.0
    );
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputNumericAttribute(
        numericAttributeFn
    );
    if (!status) {
        return status;
    }
    status = addAttribute(weight);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        outputTranslate,
        outputTranslateX,
        outputTranslateY,
        outputTranslateZ,
        "outputTranslate",
        "ot",
        "outputTranslateX",
        "otx",
        "outputTranslateY",
        "oty",
        "outputTranslateZ",
        "otz",
        0.0
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
    status = addAttribute(outputTranslate);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createRotateAttribute(
        numericAttributeFn,
        unitAttributeFn,
        outputRotate,
        outputRotateX,
        outputRotateY,
        outputRotateZ,
        "outputRotate",
        "ort",
        "outputRotateX",
        "orx",
        "outputRotateY",
        "ory",
        "outputRotateZ",
        "orz"
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
    status = addAttribute(outputRotate);
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

    status = bd_util_nodes::createDouble3Attribute(
        numericAttributeFn,
        outputScale,
        outputScaleX,
        outputScaleY,
        outputScaleZ,
        "outputScale",
        "os",
        "outputScaleX",
        "osx",
        "outputScaleY",
        "osy",
        "outputScaleZ",
        "osz",
        1.0
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
    status = addAttribute(outputScale);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        isValid,
        "isValid",
        "iv",
        true
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
    status = addAttribute(isValid);
    if (!status) {
        return status;
    }

    blendStatus = enumAttributeFn.create("blendStatus", "bst", 0, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 7>{
             {{"Success", static_cast<short>(0)},
              {"InvalidWeight", static_cast<short>(1)},
              {"InvalidTranslate", static_cast<short>(2)},
              {"InvalidRotate", static_cast<short>(3)},
              {"InvalidScale", static_cast<short>(4)},
              {"UnsupportedRotateOrder", static_cast<short>(5)},
              {"NumericalFailure", static_cast<short>(6)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureOutputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(blendStatus);
    if (!status) {
        return status;
    }

    const std::array<MObject, 28> inputAttributes = {
        baseTranslate,
        baseTranslateX,
        baseTranslateY,
        baseTranslateZ,
        baseRotate,
        baseRotateX,
        baseRotateY,
        baseRotateZ,
        baseScale,
        baseScaleX,
        baseScaleY,
        baseScaleZ,
        rotateOrder,
        pose,
        poseTranslate,
        poseTranslateX,
        poseTranslateY,
        poseTranslateZ,
        poseRotate,
        poseRotateX,
        poseRotateY,
        poseRotateZ,
        poseScale,
        poseScaleX,
        poseScaleY,
        poseScaleZ,
        enabled,
        weight,
    };
    for (const MObject& inputAttribute : inputAttributes) {
        for (const MObject& outputAttribute : {
                 outputTranslate,
                 outputRotate,
                 outputQuat,
                 outputScale,
                 isValid,
                 blendStatus,
             }) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdRbfPoseBlendNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    if (!isRequestedOutput(plug.attribute())) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    const double3& baseTranslateValue = dataBlock.inputValue(
        baseTranslate,
        &status
    ).asDouble3();
    if (!status) {
        return status;
    }
    const double3& baseRotateValue = dataBlock.inputValue(
        baseRotate,
        &status
    ).asDouble3();
    if (!status) {
        return status;
    }
    const double3& baseScaleValue = dataBlock.inputValue(
        baseScale,
        &status
    ).asDouble3();
    if (!status) {
        return status;
    }
    const short rotateOrderValue = dataBlock.inputValue(
        rotateOrder,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    bd_util_nodes::PoseBlendResult result;
    bd_util_nodes::PoseBlendStatus poseBlendStatus =
        bd_util_nodes::PoseBlendStatus::kUnsupportedRotateOrder;
    MEulerRotation::RotationOrder mappedRotateOrder;
    const bool hasSupportedRotateOrder =
        bd_util_nodes::toEulerRotationOrder(
            rotateOrderValue,
            mappedRotateOrder
        );

    if (hasSupportedRotateOrder) {
        MArrayDataHandle weightHandles = dataBlock.inputArrayValue(
            weight,
            &status
        );
        if (!status) {
            return status;
        }
        const unsigned int weightCount = weightHandles.elementCount(&status);
        if (!status) {
            return status;
        }

        std::unordered_map<unsigned int, double> weights;
        weights.reserve(weightCount);
        for (unsigned int index = 0; index < weightCount; ++index) {
            const unsigned int logicalIndex = weightHandles.elementIndex(
                &status
            );
            if (!status) {
                return status;
            }
            weights[logicalIndex] = weightHandles.inputValue(
                &status
            ).asDouble();
            if (!status) {
                return status;
            }
            if (index + 1 < weightCount) {
                status = weightHandles.next();
                if (!status) {
                    return status;
                }
            }
        }

        MArrayDataHandle poseHandles = dataBlock.inputArrayValue(
            pose,
            &status
        );
        if (!status) {
            return status;
        }
        const unsigned int poseCount = poseHandles.elementCount(&status);
        if (!status) {
            return status;
        }

        std::vector<bd_util_nodes::WeightedPoseValue> weightedPoses;
        weightedPoses.reserve(poseCount);
        for (unsigned int index = 0; index < poseCount; ++index) {
            const unsigned int logicalIndex = poseHandles.elementIndex(
                &status
            );
            if (!status) {
                return status;
            }
            MDataHandle poseHandle = poseHandles.inputValue(&status);
            if (!status) {
                return status;
            }

            const auto weightIterator = weights.find(logicalIndex);
            if (
                poseHandle.child(enabled).asBool()
                && weightIterator != weights.end()
                && weightIterator->second != 0.0
            ) {
                const double3& translateValue = poseHandle.child(
                    poseTranslate
                ).asDouble3();
                const double3& rotateValue = poseHandle.child(
                    poseRotate
                ).asDouble3();
                const double3& scaleValue = poseHandle.child(
                    poseScale
                ).asDouble3();
                weightedPoses.push_back({
                    logicalIndex,
                    toArray(translateValue),
                    MEulerRotation(
                        rotateValue[0],
                        rotateValue[1],
                        rotateValue[2],
                        mappedRotateOrder
                    ).asQuaternion(),
                    toArray(scaleValue),
                    weightIterator->second,
                });
            }

            if (index + 1 < poseCount) {
                status = poseHandles.next();
                if (!status) {
                    return status;
                }
            }
        }

        poseBlendStatus = bd_util_nodes::blendPose(
            toArray(baseTranslateValue),
            MEulerRotation(
                baseRotateValue[0],
                baseRotateValue[1],
                baseRotateValue[2],
                mappedRotateOrder
            ).asQuaternion(),
            toArray(baseScaleValue),
            weightedPoses,
            result
        );
    }

    MEulerRotation outputEuler;
    if (hasSupportedRotateOrder) {
        outputEuler = result.rotate.asEulerRotation();
        outputEuler.reorderIt(mappedRotateOrder);
    }

    MDataHandle outputTranslateHandle = dataBlock.outputValue(
        outputTranslate,
        &status
    );
    if (!status) {
        return status;
    }
    outputTranslateHandle.set3Double(
        result.translate[0],
        result.translate[1],
        result.translate[2]
    );
    outputTranslateHandle.setClean();

    MDataHandle outputRotateHandle = dataBlock.outputValue(
        outputRotate,
        &status
    );
    if (!status) {
        return status;
    }
    outputRotateHandle.set3Double(
        outputEuler.x,
        outputEuler.y,
        outputEuler.z
    );
    outputRotateHandle.setClean();

    MDataHandle outputQuatHandle = dataBlock.outputValue(
        outputQuat,
        &status
    );
    if (!status) {
        return status;
    }
    outputQuatHandle.set4Double(
        result.rotate.x,
        result.rotate.y,
        result.rotate.z,
        result.rotate.w
    );
    outputQuatHandle.setClean();

    MDataHandle outputScaleHandle = dataBlock.outputValue(
        outputScale,
        &status
    );
    if (!status) {
        return status;
    }
    outputScaleHandle.set3Double(
        result.scale[0],
        result.scale[1],
        result.scale[2]
    );
    outputScaleHandle.setClean();

    MDataHandle isValidHandle = dataBlock.outputValue(isValid, &status);
    if (!status) {
        return status;
    }
    isValidHandle.setBool(
        poseBlendStatus == bd_util_nodes::PoseBlendStatus::kSuccess
    );
    isValidHandle.setClean();

    MDataHandle blendStatusHandle = dataBlock.outputValue(
        blendStatus,
        &status
    );
    if (!status) {
        return status;
    }
    blendStatusHandle.setShort(static_cast<short>(poseBlendStatus));
    blendStatusHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType BdRbfPoseBlendNode::schedulingType() const {
    return MPxNode::kParallel;
}
