#include "bdUtilNodes/nodes/BdRbfMultiBendTwistFalloffWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
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

const MString BdRbfMultiBendTwistFalloffWeightNode::typeName(
    "bdRbf_MultiBendTwistFalloffWeight"
);
const MTypeId BdRbfMultiBendTwistFalloffWeightNode::typeId(0x0007F09E);

MObject BdRbfMultiBendTwistFalloffWeightNode::source;
MObject BdRbfMultiBendTwistFalloffWeightNode::inputQuat;
MObject BdRbfMultiBendTwistFalloffWeightNode::inputQuatX;
MObject BdRbfMultiBendTwistFalloffWeightNode::inputQuatY;
MObject BdRbfMultiBendTwistFalloffWeightNode::inputQuatZ;
MObject BdRbfMultiBendTwistFalloffWeightNode::inputQuatW;
MObject BdRbfMultiBendTwistFalloffWeightNode::axisQuat;
MObject BdRbfMultiBendTwistFalloffWeightNode::axisQuatX;
MObject BdRbfMultiBendTwistFalloffWeightNode::axisQuatY;
MObject BdRbfMultiBendTwistFalloffWeightNode::axisQuatZ;
MObject BdRbfMultiBendTwistFalloffWeightNode::axisQuatW;
MObject BdRbfMultiBendTwistFalloffWeightNode::order;
MObject BdRbfMultiBendTwistFalloffWeightNode::influence;

MObject BdRbfMultiBendTwistFalloffWeightNode::mode;
MObject BdRbfMultiBendTwistFalloffWeightNode::bendInnerRadius;
MObject BdRbfMultiBendTwistFalloffWeightNode::bendOuterRadius;
MObject BdRbfMultiBendTwistFalloffWeightNode::twistInnerRadius;
MObject BdRbfMultiBendTwistFalloffWeightNode::twistOuterRadius;
MObject BdRbfMultiBendTwistFalloffWeightNode::falloff;

MObject BdRbfMultiBendTwistFalloffWeightNode::pose;
MObject BdRbfMultiBendTwistFalloffWeightNode::sourceQuat;
MObject BdRbfMultiBendTwistFalloffWeightNode::sourceQuatX;
MObject BdRbfMultiBendTwistFalloffWeightNode::sourceQuatY;
MObject BdRbfMultiBendTwistFalloffWeightNode::sourceQuatZ;
MObject BdRbfMultiBendTwistFalloffWeightNode::sourceQuatW;
MObject BdRbfMultiBendTwistFalloffWeightNode::enabled;
MObject BdRbfMultiBendTwistFalloffWeightNode::useRadiusOverride;
MObject BdRbfMultiBendTwistFalloffWeightNode::bendInnerRadiusOverride;
MObject BdRbfMultiBendTwistFalloffWeightNode::bendOuterRadiusOverride;
MObject BdRbfMultiBendTwistFalloffWeightNode::twistInnerRadiusOverride;
MObject BdRbfMultiBendTwistFalloffWeightNode::twistOuterRadiusOverride;

MObject BdRbfMultiBendTwistFalloffWeightNode::outputWeight;
MObject BdRbfMultiBendTwistFalloffWeightNode::isValid;
MObject BdRbfMultiBendTwistFalloffWeightNode::falloffStatus;

namespace {

using SourceDefinition =
    bd_util_nodes::MultiBendTwistFalloffSourceDefinition;
using Sample = bd_util_nodes::MultiBendTwistFalloffSample;

bool haveSameSources(
    const std::vector<SourceDefinition>& first,
    const std::vector<SourceDefinition>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t index = 0; index < first.size(); ++index) {
        if (
            first[index].logicalIndex != second[index].logicalIndex
            || first[index].axisQuaternion
                != second[index].axisQuaternion
            || first[index].order != second[index].order
            || first[index].influence != second[index].influence
        ) {
            return false;
        }
    }
    return true;
}

bool haveSameSamples(
    const std::vector<Sample>& first,
    const std::vector<Sample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t poseIndex = 0; poseIndex < first.size(); ++poseIndex) {
        if (
            first[poseIndex].logicalIndex != second[poseIndex].logicalIndex
            || first[poseIndex].bendInnerRadiusRadians
                != second[poseIndex].bendInnerRadiusRadians
            || first[poseIndex].bendOuterRadiusRadians
                != second[poseIndex].bendOuterRadiusRadians
            || first[poseIndex].twistInnerRadiusRadians
                != second[poseIndex].twistInnerRadiusRadians
            || first[poseIndex].twistOuterRadiusRadians
                != second[poseIndex].twistOuterRadiusRadians
            || first[poseIndex].sourceQuaternions.size()
                != second[poseIndex].sourceQuaternions.size()
        ) {
            return false;
        }
        for (
            std::size_t sourceIndex = 0;
            sourceIndex < first[poseIndex].sourceQuaternions.size();
            ++sourceIndex
        ) {
            const bd_util_nodes::IndexedQuaternion& firstQuaternion =
                first[poseIndex].sourceQuaternions[sourceIndex];
            const bd_util_nodes::IndexedQuaternion& secondQuaternion =
                second[poseIndex].sourceQuaternions[sourceIndex];
            if (
                firstQuaternion.logicalIndex
                    != secondQuaternion.logicalIndex
                || firstQuaternion.quaternion
                    != secondQuaternion.quaternion
            ) {
                return false;
            }
        }
    }
    return true;
}

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

struct BdRbfMultiBendTwistFalloffWeightNode::Cache {
    bd_util_nodes::MultiBendTwistFalloffStatus evaluate(
        const std::vector<SourceDefinition>& sources,
        const std::vector<Sample>& samples,
        bd_util_nodes::BendTwistFalloffMode requestedMode,
        bd_util_nodes::Falloff requestedFalloff,
        const std::vector<bd_util_nodes::IndexedQuaternion>& inputQuaternions,
        std::vector<bd_util_nodes::BendTwistFalloffWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSources(configuredSources, sources)
            || !haveSameSamples(configuredSamples, samples)
            || mode != requestedMode || falloff != requestedFalloff
        ) {
            configuredSources = sources;
            configuredSamples = samples;
            mode = requestedMode;
            falloff = requestedFalloff;
            configureStatus = evaluator.configure(
                configuredSources,
                configuredSamples,
                mode,
                falloff
            );
            configured = true;
        }

        outputWeights.clear();
        if (
            configureStatus
            != bd_util_nodes::MultiBendTwistFalloffStatus::kSuccess
        ) {
            return configureStatus;
        }
        return evaluator.evaluate(inputQuaternions, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<SourceDefinition> configuredSources;
    std::vector<Sample> configuredSamples;
    bd_util_nodes::BendTwistFalloffMode mode =
        bd_util_nodes::BendTwistFalloffMode::kBendTwist;
    bd_util_nodes::Falloff falloff = bd_util_nodes::Falloff::kQuintic;
    bd_util_nodes::MultiBendTwistFalloffStatus configureStatus =
        bd_util_nodes::MultiBendTwistFalloffStatus::kNoSources;
    bd_util_nodes::MultiBendTwistFalloffEvaluator evaluator;
};

BdRbfMultiBendTwistFalloffWeightNode::
    BdRbfMultiBendTwistFalloffWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfMultiBendTwistFalloffWeightNode::
    ~BdRbfMultiBendTwistFalloffWeightNode() = default;

void* BdRbfMultiBendTwistFalloffWeightNode::creator() {
    return new BdRbfMultiBendTwistFalloffWeightNode();
}

MStatus BdRbfMultiBendTwistFalloffWeightNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;
    MFnCompoundAttribute compoundAttributeFn;

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

    status = bd_util_nodes::createBendTwistOrderAttribute(
        enumAttributeFn,
        order,
        "order",
        "ord"
    );
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAttribute(
        numericAttributeFn,
        influence,
        "influence",
        "inf",
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
    status = numericAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    source = compoundAttributeFn.create("source", "src", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             inputQuat,
             axisQuat,
             order,
             influence,
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
    status = addAttribute(source);
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
        sourceQuat,
        sourceQuatX,
        sourceQuatY,
        sourceQuatZ,
        sourceQuatW,
        "sourceQuat",
        "sq",
        "sourceQuatX",
        "sqx",
        "sourceQuatY",
        "sqy",
        "sourceQuatZ",
        "sqz",
        "sourceQuatW",
        "sqw",
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
    status = numericAttributeFn.setArray(true);
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

    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             sourceQuat,
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
        8,
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 11>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidQuaternion", static_cast<short>(3)},
              {"UnsupportedFalloff", static_cast<short>(4)},
              {"UnsupportedMode", static_cast<short>(5)},
              {"UnsupportedOrder", static_cast<short>(6)},
              {"NumericalFailure", static_cast<short>(7)},
              {"NoSources", static_cast<short>(8)},
              {"InvalidInfluence", static_cast<short>(9)},
              {"IncompletePose", static_cast<short>(10)}}}) {
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

    const std::array<MObject, 31> inputs = {
        source,
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
        influence,
        mode,
        bendInnerRadius,
        bendOuterRadius,
        twistInnerRadius,
        twistOuterRadius,
        falloff,
        pose,
        sourceQuat,
        sourceQuatX,
        sourceQuatY,
        sourceQuatZ,
        sourceQuatW,
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

MStatus BdRbfMultiBendTwistFalloffWeightNode::compute(
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
    std::vector<SourceDefinition> sources;
    std::vector<bd_util_nodes::IndexedQuaternion> inputQuaternions;
    MArrayDataHandle sourceHandles = dataBlock.inputArrayValue(
        source,
        &status
    );
    if (!status) {
        return status;
    }
    const unsigned int sourceCount = sourceHandles.elementCount(&status);
    if (!status) {
        return status;
    }
    sources.reserve(sourceCount);
    inputQuaternions.reserve(sourceCount);
    for (unsigned int index = 0; index < sourceCount; ++index) {
        const unsigned int logicalIndex = sourceHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        MDataHandle sourceHandle = sourceHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        const double4& inputValue = sourceHandle.child(inputQuat).asDouble4();
        const double4& axisValue = sourceHandle.child(axisQuat).asDouble4();
        sources.push_back({
            logicalIndex,
            {
                axisValue[0],
                axisValue[1],
                axisValue[2],
                axisValue[3],
            },
            static_cast<bd_util_nodes::BendTwistOrder>(
                sourceHandle.child(order).asShort()
            ),
            sourceHandle.child(influence).asDouble(),
        });
        inputQuaternions.push_back({
            logicalIndex,
            {
                inputValue[0],
                inputValue[1],
                inputValue[2],
                inputValue[3],
            },
        });
        if (index + 1 < sourceCount) {
            status = sourceHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(
        sources.begin(),
        sources.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );
    std::sort(
        inputQuaternions.begin(),
        inputQuaternions.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

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
    std::vector<Sample> enabledSamples;
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
            Sample sample;
            sample.logicalIndex = logicalIndex;
            const bool useOverride = poseHandle.child(
                useRadiusOverride
            ).asBool();
            sample.bendInnerRadiusRadians = useOverride
                ? poseHandle.child(
                      bendInnerRadiusOverride
                  ).asAngle().asRadians()
                : defaultBendInnerRadius;
            sample.bendOuterRadiusRadians = useOverride
                ? poseHandle.child(
                      bendOuterRadiusOverride
                  ).asAngle().asRadians()
                : defaultBendOuterRadius;
            sample.twistInnerRadiusRadians = useOverride
                ? poseHandle.child(
                      twistInnerRadiusOverride
                  ).asAngle().asRadians()
                : defaultTwistInnerRadius;
            sample.twistOuterRadiusRadians = useOverride
                ? poseHandle.child(
                      twistOuterRadiusOverride
                  ).asAngle().asRadians()
                : defaultTwistOuterRadius;

            MArrayDataHandle sourceQuatHandles(
                poseHandle.child(sourceQuat),
                &status
            );
            if (!status) {
                return status;
            }
            const unsigned int poseSourceCount =
                sourceQuatHandles.elementCount(&status);
            if (!status) {
                return status;
            }
            sample.sourceQuaternions.reserve(poseSourceCount);
            for (
                unsigned int sourceIndex = 0;
                sourceIndex < poseSourceCount;
                ++sourceIndex
            ) {
                const unsigned int sourceLogicalIndex =
                    sourceQuatHandles.elementIndex(&status);
                if (!status) {
                    return status;
                }
                MDataHandle sourceQuatHandle = sourceQuatHandles.inputValue(
                    &status
                );
                if (!status) {
                    return status;
                }
                const double4& poseValue = sourceQuatHandle.asDouble4();
                sample.sourceQuaternions.push_back({
                    sourceLogicalIndex,
                    {
                        poseValue[0],
                        poseValue[1],
                        poseValue[2],
                        poseValue[3],
                    },
                });
                if (sourceIndex + 1 < poseSourceCount) {
                    status = sourceQuatHandles.next();
                    if (!status) {
                        return status;
                    }
                }
            }
            std::sort(
                sample.sourceQuaternions.begin(),
                sample.sourceQuaternions.end(),
                [](const auto& first, const auto& second) {
                    return first.logicalIndex < second.logicalIndex;
                }
            );
            enabledSamples.push_back(std::move(sample));
        }
        if (index + 1 < poseCount) {
            status = poseHandles.next();
            if (!status) {
                return status;
            }
        }
    }
    std::sort(poseIndices.begin(), poseIndices.end());
    std::sort(
        enabledSamples.begin(),
        enabledSamples.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

    std::vector<bd_util_nodes::BendTwistFalloffWeight> falloffWeights;
    const bd_util_nodes::MultiBendTwistFalloffStatus resultStatus =
        cache_->evaluate(
            sources,
            enabledSamples,
            static_cast<bd_util_nodes::BendTwistFalloffMode>(modeValue),
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            inputQuaternions,
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (
        resultStatus
        == bd_util_nodes::MultiBendTwistFalloffStatus::kSuccess
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
        == bd_util_nodes::MultiBendTwistFalloffStatus::kSuccess
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
BdRbfMultiBendTwistFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
