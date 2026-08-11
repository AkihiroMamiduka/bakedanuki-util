#include "bdUtilNodes/nodes/BdRbfBendTwistFalloffWeightNode.h"

#include <array>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

#include <maya/MAngle.h>
#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/BendTwistAttribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/BendTwistFalloff.h"

const MString BdRbfBendTwistFalloffWeightNode::typeName(
    "bdRbf_BendTwistFalloffWeight"
);
const MTypeId BdRbfBendTwistFalloffWeightNode::typeId(0x0007F099);

MObject BdRbfBendTwistFalloffWeightNode::inputQuat;
MObject BdRbfBendTwistFalloffWeightNode::inputQuatX;
MObject BdRbfBendTwistFalloffWeightNode::inputQuatY;
MObject BdRbfBendTwistFalloffWeightNode::inputQuatZ;
MObject BdRbfBendTwistFalloffWeightNode::inputQuatW;

MObject BdRbfBendTwistFalloffWeightNode::axisQuat;
MObject BdRbfBendTwistFalloffWeightNode::axisQuatX;
MObject BdRbfBendTwistFalloffWeightNode::axisQuatY;
MObject BdRbfBendTwistFalloffWeightNode::axisQuatZ;
MObject BdRbfBendTwistFalloffWeightNode::axisQuatW;
MObject BdRbfBendTwistFalloffWeightNode::order;
MObject BdRbfBendTwistFalloffWeightNode::mode;

MObject BdRbfBendTwistFalloffWeightNode::bendInnerRadius;
MObject BdRbfBendTwistFalloffWeightNode::bendOuterRadius;
MObject BdRbfBendTwistFalloffWeightNode::twistInnerRadius;
MObject BdRbfBendTwistFalloffWeightNode::twistOuterRadius;
MObject BdRbfBendTwistFalloffWeightNode::falloff;

MObject BdRbfBendTwistFalloffWeightNode::pose;
MObject BdRbfBendTwistFalloffWeightNode::poseQuat;
MObject BdRbfBendTwistFalloffWeightNode::poseQuatX;
MObject BdRbfBendTwistFalloffWeightNode::poseQuatY;
MObject BdRbfBendTwistFalloffWeightNode::poseQuatZ;
MObject BdRbfBendTwistFalloffWeightNode::poseQuatW;
MObject BdRbfBendTwistFalloffWeightNode::enabled;
MObject BdRbfBendTwistFalloffWeightNode::useRadiusOverride;
MObject BdRbfBendTwistFalloffWeightNode::bendInnerRadiusOverride;
MObject BdRbfBendTwistFalloffWeightNode::bendOuterRadiusOverride;
MObject BdRbfBendTwistFalloffWeightNode::twistInnerRadiusOverride;
MObject BdRbfBendTwistFalloffWeightNode::twistOuterRadiusOverride;

MObject BdRbfBendTwistFalloffWeightNode::outputWeight;
MObject BdRbfBendTwistFalloffWeightNode::isValid;
MObject BdRbfBendTwistFalloffWeightNode::falloffStatus;

namespace {

MStatus configureInputEnumAttribute(MFnEnumAttribute& attributeFn) {
    MStatus status = attributeFn.setReadable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setWritable(true);
    if (!status) {
        return status;
    }
    status = attributeFn.setStorable(true);
    if (!status) {
        return status;
    }
    return attributeFn.setKeyable(true);
}

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

MStatus createInputAngleAttribute(
    MFnUnitAttribute& attributeFn,
    MObject& attribute,
    const char* longName,
    const char* shortName,
    double defaultValue
) {
    MStatus status = bd_util_nodes::createDoubleAngleAttribute(
        attributeFn,
        attribute,
        longName,
        shortName,
        defaultValue
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(attributeFn);
    if (!status) {
        return status;
    }
    return attributeFn.setMin(0.0);
}

}  // namespace

void* BdRbfBendTwistFalloffWeightNode::creator() {
    return new BdRbfBendTwistFalloffWeightNode();
}

MStatus BdRbfBendTwistFalloffWeightNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

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

    mode = enumAttributeFn.create("mode", "md", 0, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 2>{
             {{"BendTwist", static_cast<short>(0)},
              {"BendOnly", static_cast<short>(1)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureInputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(mode);
    if (!status) {
        return status;
    }

    const double defaultOuterRadius = MAngle(
        60.0,
        MAngle::kDegrees
    ).asRadians();
    for (const auto& definition : {
             std::tuple<MObject*, const char*, const char*, double>{
                 &bendInnerRadius,
                 "bendInnerRadius",
                 "bir",
                 0.0,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &bendOuterRadius,
                 "bendOuterRadius",
                 "bor",
                 defaultOuterRadius,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &twistInnerRadius,
                 "twistInnerRadius",
                 "tir",
                 0.0,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &twistOuterRadius,
                 "twistOuterRadius",
                 "tor",
                 defaultOuterRadius,
             },
         }) {
        MObject* attribute;
        const char* longName;
        const char* shortName;
        double defaultValue;
        std::tie(attribute, longName, shortName, defaultValue) = definition;
        status = createInputAngleAttribute(
            unitAttributeFn,
            *attribute,
            longName,
            shortName,
            defaultValue
        );
        if (!status) {
            return status;
        }
        status = addAttribute(*attribute);
        if (!status) {
            return status;
        }
    }

    falloff = enumAttributeFn.create("falloff", "fo", 2, &status);
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 3>{
             {{"Linear", static_cast<short>(0)},
              {"CompactCubic", static_cast<short>(1)},
              {"CompactQuintic", static_cast<short>(2)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureInputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(falloff);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createQuaternionAttribute(
        numericAttributeFn,
        poseQuat,
        poseQuatX,
        poseQuatY,
        poseQuatZ,
        poseQuatW,
        "poseQuat",
        "pq",
        "poseQuatX",
        "pqx",
        "poseQuatY",
        "pqy",
        "poseQuatZ",
        "pqz",
        "poseQuatW",
        "pqw",
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

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        useRadiusOverride,
        "useRadiusOverride",
        "uro",
        false
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

    for (const auto& definition : {
             std::tuple<MObject*, const char*, const char*, double>{
                 &bendInnerRadiusOverride,
                 "bendInnerRadiusOverride",
                 "biro",
                 0.0,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &bendOuterRadiusOverride,
                 "bendOuterRadiusOverride",
                 "boro",
                 defaultOuterRadius,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &twistInnerRadiusOverride,
                 "twistInnerRadiusOverride",
                 "tiro",
                 0.0,
             },
             std::tuple<MObject*, const char*, const char*, double>{
                 &twistOuterRadiusOverride,
                 "twistOuterRadiusOverride",
                 "toro",
                 defaultOuterRadius,
             },
         }) {
        MObject* attribute;
        const char* longName;
        const char* shortName;
        double defaultValue;
        std::tie(attribute, longName, shortName, defaultValue) = definition;
        status = createInputAngleAttribute(
            unitAttributeFn,
            *attribute,
            longName,
            shortName,
            defaultValue
        );
        if (!status) {
            return status;
        }
    }

    MFnCompoundAttribute compoundAttributeFn;
    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             poseQuat,
             enabled,
             useRadiusOverride,
             bendInnerRadiusOverride,
             bendOuterRadiusOverride,
             twistInnerRadiusOverride,
             twistOuterRadiusOverride,
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
        outputWeight,
        "outputWeight",
        "ow",
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
    status = numericAttributeFn.setArray(true);
    if (!status) {
        return status;
    }
    status = numericAttributeFn.setUsesArrayDataBuilder(true);
    if (!status) {
        return status;
    }
    status = addAttribute(outputWeight);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createBooleanAttribute(
        numericAttributeFn,
        isValid,
        "isValid",
        "iv",
        false
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

    falloffStatus = enumAttributeFn.create(
        "falloffStatus",
        "fs",
        1,
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 8>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidQuaternion", static_cast<short>(3)},
              {"UnsupportedFalloff", static_cast<short>(4)},
              {"UnsupportedMode", static_cast<short>(5)},
              {"UnsupportedOrder", static_cast<short>(6)},
              {"NumericalFailure", static_cast<short>(7)}}}) {
        status = enumAttributeFn.addField(field.first, field.second);
        if (!status) {
            return status;
        }
    }
    status = configureOutputEnumAttribute(enumAttributeFn);
    if (!status) {
        return status;
    }
    status = addAttribute(falloffStatus);
    if (!status) {
        return status;
    }

    const std::array<MObject, 29> inputs = {
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
        mode,
        bendInnerRadius,
        bendOuterRadius,
        twistInnerRadius,
        twistOuterRadius,
        falloff,
        pose,
        poseQuat,
        poseQuatX,
        poseQuatY,
        poseQuatZ,
        poseQuatW,
        enabled,
        useRadiusOverride,
        bendInnerRadiusOverride,
        bendOuterRadiusOverride,
        twistInnerRadiusOverride,
        twistOuterRadiusOverride,
    };
    for (const MObject& inputAttribute : inputs) {
        for (const MObject& outputAttribute : {
                 outputWeight,
                 isValid,
                 falloffStatus,
             }) {
            status = attributeAffects(inputAttribute, outputAttribute);
            if (!status) {
                return status;
            }
        }
    }
    return MS::kSuccess;
}

MStatus BdRbfBendTwistFalloffWeightNode::compute(
    const MPlug& plug,
    MDataBlock& dataBlock
) {
    const MObject requestedAttribute = plug.attribute();
    if (
        requestedAttribute != outputWeight
        && requestedAttribute != isValid
        && requestedAttribute != falloffStatus
    ) {
        return MS::kUnknownParameter;
    }

    MStatus status;
    MDataHandle inputHandle = dataBlock.inputValue(inputQuat, &status);
    if (!status) {
        return status;
    }
    const double4& inputValue = inputHandle.asDouble4();
    const std::array<double, 4> input = {
        inputValue[0],
        inputValue[1],
        inputValue[2],
        inputValue[3],
    };

    MDataHandle axisHandle = dataBlock.inputValue(axisQuat, &status);
    if (!status) {
        return status;
    }
    const double4& axisValue = axisHandle.asDouble4();
    const std::array<double, 4> axis = {
        axisValue[0],
        axisValue[1],
        axisValue[2],
        axisValue[3],
    };

    const short orderValue = dataBlock.inputValue(order, &status).asShort();
    if (!status) {
        return status;
    }
    const short modeValue = dataBlock.inputValue(mode, &status).asShort();
    if (!status) {
        return status;
    }
    const short falloffValue = dataBlock.inputValue(
        falloff,
        &status
    ).asShort();
    if (!status) {
        return status;
    }

    const double defaultBendInnerRadius = dataBlock.inputValue(
        bendInnerRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }
    const double defaultBendOuterRadius = dataBlock.inputValue(
        bendOuterRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }
    const double defaultTwistInnerRadius = dataBlock.inputValue(
        twistInnerRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }
    const double defaultTwistOuterRadius = dataBlock.inputValue(
        twistOuterRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::BendTwistFalloffSample> enabledSamples;
    MArrayDataHandle poseHandles = dataBlock.inputArrayValue(pose, &status);
    if (!status) {
        return status;
    }
    const unsigned int poseCount = poseHandles.elementCount(&status);
    if (!status) {
        return status;
    }
    poseIndices.reserve(poseCount);
    enabledSamples.reserve(poseCount);
    for (unsigned int index = 0; index < poseCount; ++index) {
        const unsigned int logicalIndex = poseHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        poseIndices.push_back(logicalIndex);

        MDataHandle poseHandle = poseHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        if (poseHandle.child(enabled).asBool()) {
            const double4& poseValue = poseHandle.child(
                poseQuat
            ).asDouble4();
            double resolvedBendInnerRadius = defaultBendInnerRadius;
            double resolvedBendOuterRadius = defaultBendOuterRadius;
            double resolvedTwistInnerRadius = defaultTwistInnerRadius;
            double resolvedTwistOuterRadius = defaultTwistOuterRadius;
            if (poseHandle.child(useRadiusOverride).asBool()) {
                resolvedBendInnerRadius = poseHandle.child(
                    bendInnerRadiusOverride
                ).asAngle().asRadians();
                resolvedBendOuterRadius = poseHandle.child(
                    bendOuterRadiusOverride
                ).asAngle().asRadians();
                resolvedTwistInnerRadius = poseHandle.child(
                    twistInnerRadiusOverride
                ).asAngle().asRadians();
                resolvedTwistOuterRadius = poseHandle.child(
                    twistOuterRadiusOverride
                ).asAngle().asRadians();
            }
            enabledSamples.push_back({
                logicalIndex,
                {
                    poseValue[0],
                    poseValue[1],
                    poseValue[2],
                    poseValue[3],
                },
                resolvedBendInnerRadius,
                resolvedBendOuterRadius,
                resolvedTwistInnerRadius,
                resolvedTwistOuterRadius,
            });
        }

        if (index + 1 < poseCount) {
            status = poseHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::vector<bd_util_nodes::BendTwistFalloffWeight> falloffWeights;
    const bd_util_nodes::BendTwistFalloffStatus resultStatus =
        bd_util_nodes::evaluateBendTwistFalloff(
            input,
            axis,
            enabledSamples,
            static_cast<bd_util_nodes::BendTwistOrder>(orderValue),
            static_cast<bd_util_nodes::BendTwistFalloffMode>(modeValue),
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (
        resultStatus
        == bd_util_nodes::BendTwistFalloffStatus::kSuccess
    ) {
        weightByIndex.reserve(falloffWeights.size());
        for (const auto& falloffWeight : falloffWeights) {
            weightByIndex.emplace(
                falloffWeight.logicalIndex,
                falloffWeight.weight
            );
        }
    }

    MArrayDataHandle outputHandles = dataBlock.outputArrayValue(
        outputWeight,
        &status
    );
    if (!status) {
        return status;
    }
    MArrayDataBuilder outputBuilder(
        &dataBlock,
        outputWeight,
        static_cast<unsigned int>(poseIndices.size()),
        &status
    );
    if (!status) {
        return status;
    }
    for (const unsigned int logicalIndex : poseIndices) {
        MDataHandle outputHandle = outputBuilder.addElement(
            logicalIndex,
            &status
        );
        if (!status) {
            return status;
        }
        const auto foundWeight = weightByIndex.find(logicalIndex);
        outputHandle.setDouble(
            foundWeight == weightByIndex.end() ? 0.0 : foundWeight->second
        );
    }
    status = outputHandles.set(outputBuilder);
    if (!status) {
        return status;
    }
    status = outputHandles.setAllClean();
    if (!status) {
        return status;
    }

    MDataHandle isValidHandle = dataBlock.outputValue(isValid, &status);
    if (!status) {
        return status;
    }
    isValidHandle.setBool(
        resultStatus
        == bd_util_nodes::BendTwistFalloffStatus::kSuccess
    );
    isValidHandle.setClean();

    MDataHandle statusHandle = dataBlock.outputValue(falloffStatus, &status);
    if (!status) {
        return status;
    }
    statusHandle.setShort(static_cast<short>(resultStatus));
    statusHandle.setClean();
    return dataBlock.setClean(plug);
}

MPxNode::SchedulingType
BdRbfBendTwistFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
