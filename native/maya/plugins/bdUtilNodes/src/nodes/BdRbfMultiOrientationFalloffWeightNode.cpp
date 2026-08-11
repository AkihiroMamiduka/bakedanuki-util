#include "bdUtilNodes/nodes/BdRbfMultiOrientationFalloffWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
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

#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/QuaternionAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/OrientationFalloff.h"

const MString BdRbfMultiOrientationFalloffWeightNode::typeName(
    "bdRbf_MultiOrientationFalloffWeight"
);
const MTypeId BdRbfMultiOrientationFalloffWeightNode::typeId(0x0007F09C);

MObject BdRbfMultiOrientationFalloffWeightNode::source;
MObject BdRbfMultiOrientationFalloffWeightNode::inputQuat;
MObject BdRbfMultiOrientationFalloffWeightNode::inputQuatX;
MObject BdRbfMultiOrientationFalloffWeightNode::inputQuatY;
MObject BdRbfMultiOrientationFalloffWeightNode::inputQuatZ;
MObject BdRbfMultiOrientationFalloffWeightNode::inputQuatW;
MObject BdRbfMultiOrientationFalloffWeightNode::influence;

MObject BdRbfMultiOrientationFalloffWeightNode::innerRadius;
MObject BdRbfMultiOrientationFalloffWeightNode::outerRadius;
MObject BdRbfMultiOrientationFalloffWeightNode::falloff;

MObject BdRbfMultiOrientationFalloffWeightNode::pose;
MObject BdRbfMultiOrientationFalloffWeightNode::sourceQuat;
MObject BdRbfMultiOrientationFalloffWeightNode::sourceQuatX;
MObject BdRbfMultiOrientationFalloffWeightNode::sourceQuatY;
MObject BdRbfMultiOrientationFalloffWeightNode::sourceQuatZ;
MObject BdRbfMultiOrientationFalloffWeightNode::sourceQuatW;
MObject BdRbfMultiOrientationFalloffWeightNode::enabled;
MObject BdRbfMultiOrientationFalloffWeightNode::useRadiusOverride;
MObject BdRbfMultiOrientationFalloffWeightNode::innerRadiusOverride;
MObject BdRbfMultiOrientationFalloffWeightNode::outerRadiusOverride;

MObject BdRbfMultiOrientationFalloffWeightNode::outputWeight;
MObject BdRbfMultiOrientationFalloffWeightNode::isValid;
MObject BdRbfMultiOrientationFalloffWeightNode::falloffStatus;

namespace {

bool haveSameSources(
    const std::vector<bd_util_nodes::QuaternionSourceDefinition>& first,
    const std::vector<bd_util_nodes::QuaternionSourceDefinition>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t index = 0; index < first.size(); ++index) {
        if (
            first[index].logicalIndex != second[index].logicalIndex
            || first[index].influence != second[index].influence
        ) {
            return false;
        }
    }
    return true;
}

bool haveSameSamples(
    const std::vector<bd_util_nodes::MultiOrientationFalloffSample>& first,
    const std::vector<bd_util_nodes::MultiOrientationFalloffSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t poseIndex = 0; poseIndex < first.size(); ++poseIndex) {
        if (
            first[poseIndex].logicalIndex != second[poseIndex].logicalIndex
            || first[poseIndex].innerRadiusRadians
                != second[poseIndex].innerRadiusRadians
            || first[poseIndex].outerRadiusRadians
                != second[poseIndex].outerRadiusRadians
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

}  // namespace

struct BdRbfMultiOrientationFalloffWeightNode::Cache {
    bd_util_nodes::MultiOrientationFalloffStatus evaluate(
        const std::vector<bd_util_nodes::QuaternionSourceDefinition>& sources,
        const std::vector<bd_util_nodes::MultiOrientationFalloffSample>& samples,
        bd_util_nodes::Falloff requestedFalloff,
        const std::vector<bd_util_nodes::IndexedQuaternion>& inputQuaternions,
        std::vector<bd_util_nodes::OrientationFalloffWeight>& outputWeights
    ) {
        const std::lock_guard<std::mutex> lock(mutex);
        if (
            !configured || !haveSameSources(configuredSources, sources)
            || !haveSameSamples(configuredSamples, samples)
            || falloff != requestedFalloff
        ) {
            configuredSources = sources;
            configuredSamples = samples;
            falloff = requestedFalloff;
            configureStatus = evaluator.configure(
                configuredSources,
                configuredSamples,
                falloff
            );
            configured = true;
        }

        outputWeights.clear();
        if (
            configureStatus
            != bd_util_nodes::MultiOrientationFalloffStatus::kSuccess
        ) {
            return configureStatus;
        }
        return evaluator.evaluate(inputQuaternions, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::QuaternionSourceDefinition> configuredSources;
    std::vector<bd_util_nodes::MultiOrientationFalloffSample>
        configuredSamples;
    bd_util_nodes::Falloff falloff = bd_util_nodes::Falloff::kQuintic;
    bd_util_nodes::MultiOrientationFalloffStatus configureStatus =
        bd_util_nodes::MultiOrientationFalloffStatus::kNoSources;
    bd_util_nodes::MultiOrientationFalloffEvaluator evaluator;
};

BdRbfMultiOrientationFalloffWeightNode::
    BdRbfMultiOrientationFalloffWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfMultiOrientationFalloffWeightNode::
    ~BdRbfMultiOrientationFalloffWeightNode() = default;

void* BdRbfMultiOrientationFalloffWeightNode::creator() {
    return new BdRbfMultiOrientationFalloffWeightNode();
}

MStatus BdRbfMultiOrientationFalloffWeightNode::initialize() {
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

    MFnCompoundAttribute compoundAttributeFn;
    source = compoundAttributeFn.create("source", "src", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {inputQuat, influence}) {
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

    const double defaultOuterRadius = MAngle(
        60.0,
        MAngle::kDegrees
    ).asRadians();
    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        innerRadius,
        "innerRadius",
        "inr",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = addAttribute(innerRadius);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outerRadius,
        "outerRadius",
        "outr",
        defaultOuterRadius
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }
    status = addAttribute(outerRadius);
    if (!status) {
        return status;
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

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        innerRadiusOverride,
        "innerRadiusOverride",
        "iro",
        0.0
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    status = bd_util_nodes::createDoubleAngleAttribute(
        unitAttributeFn,
        outerRadiusOverride,
        "outerRadiusOverride",
        "oro",
        defaultOuterRadius
    );
    if (!status) {
        return status;
    }
    status = bd_util_nodes::configureInputUnitAttribute(unitAttributeFn);
    if (!status) {
        return status;
    }
    status = unitAttributeFn.setMin(0.0);
    if (!status) {
        return status;
    }

    pose = compoundAttributeFn.create("pose", "p", &status);
    if (!status) {
        return status;
    }
    for (const MObject& child : {
             sourceQuat,
             enabled,
             useRadiusOverride,
             innerRadiusOverride,
             outerRadiusOverride,
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
        6,
        &status
    );
    if (!status) {
        return status;
    }
    for (const auto& field : std::array<std::pair<const char*, short>, 9>{
             {{"Success", static_cast<short>(0)},
              {"NoPoses", static_cast<short>(1)},
              {"InvalidRadius", static_cast<short>(2)},
              {"InvalidQuaternion", static_cast<short>(3)},
              {"UnsupportedFalloff", static_cast<short>(4)},
              {"NumericalFailure", static_cast<short>(5)},
              {"NoSources", static_cast<short>(6)},
              {"InvalidInfluence", static_cast<short>(7)},
              {"IncompletePose", static_cast<short>(8)}}}) {
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

    const std::array<MObject, 20> inputs = {
        source,
        inputQuat,
        inputQuatX,
        inputQuatY,
        inputQuatZ,
        inputQuatW,
        influence,
        innerRadius,
        outerRadius,
        falloff,
        pose,
        sourceQuat,
        sourceQuatX,
        sourceQuatY,
        sourceQuatZ,
        sourceQuatW,
        enabled,
        useRadiusOverride,
        innerRadiusOverride,
        outerRadiusOverride,
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

MStatus BdRbfMultiOrientationFalloffWeightNode::compute(
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
    std::vector<bd_util_nodes::QuaternionSourceDefinition> sources;
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
        sources.push_back({
            logicalIndex,
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

    const double defaultInnerRadius = dataBlock.inputValue(
        innerRadius,
        &status
    ).asAngle().asRadians();
    if (!status) {
        return status;
    }
    const double defaultOuterRadius = dataBlock.inputValue(
        outerRadius,
        &status
    ).asAngle().asRadians();
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

    std::vector<unsigned int> poseIndices;
    std::vector<bd_util_nodes::MultiOrientationFalloffSample> enabledSamples;
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
            bd_util_nodes::MultiOrientationFalloffSample sample;
            sample.logicalIndex = logicalIndex;
            const bool useOverride = poseHandle.child(
                useRadiusOverride
            ).asBool();
            sample.innerRadiusRadians = useOverride
                ? poseHandle.child(innerRadiusOverride).asAngle().asRadians()
                : defaultInnerRadius;
            sample.outerRadiusRadians = useOverride
                ? poseHandle.child(outerRadiusOverride).asAngle().asRadians()
                : defaultOuterRadius;

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

    std::vector<bd_util_nodes::OrientationFalloffWeight> falloffWeights;
    const bd_util_nodes::MultiOrientationFalloffStatus resultStatus =
        cache_->evaluate(
            sources,
            enabledSamples,
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            inputQuaternions,
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (
        resultStatus
        == bd_util_nodes::MultiOrientationFalloffStatus::kSuccess
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
        == bd_util_nodes::MultiOrientationFalloffStatus::kSuccess
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
BdRbfMultiOrientationFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
