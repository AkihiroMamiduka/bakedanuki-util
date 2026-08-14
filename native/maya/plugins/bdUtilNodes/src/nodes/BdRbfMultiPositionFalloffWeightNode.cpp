#include "bdUtilNodes/nodes/BdRbfMultiPositionFalloffWeightNode.h"

#include <algorithm>
#include <array>
#include <mutex>
#include <unordered_map>
#include <utility>
#include <vector>

#include <maya/MArrayDataBuilder.h>
#include <maya/MArrayDataHandle.h>
#include <maya/MDataBlock.h>
#include <maya/MDataHandle.h>
#include <maya/MDistance.h>
#include <maya/MFnCompoundAttribute.h>
#include <maya/MFnEnumAttribute.h>
#include <maya/MFnNumericAttribute.h>
#include <maya/MFnUnitAttribute.h>
#include <maya/MPlug.h>

#include "bdUtilNodes/attributes/DoubleLinear3Attribute.h"
#include "bdUtilNodes/attributes/NumericAttribute.h"
#include "bdUtilNodes/attributes/UnitAttribute.h"
#include "bdUtilNodes/math/PositionFalloff.h"

const MString BdRbfMultiPositionFalloffWeightNode::typeName(
    "bdRbf_MultiPositionFalloffWeight"
);
const MTypeId BdRbfMultiPositionFalloffWeightNode::typeId(0x0014271C);

MObject BdRbfMultiPositionFalloffWeightNode::source;
MObject BdRbfMultiPositionFalloffWeightNode::inputPosition;
MObject BdRbfMultiPositionFalloffWeightNode::inputPositionX;
MObject BdRbfMultiPositionFalloffWeightNode::inputPositionY;
MObject BdRbfMultiPositionFalloffWeightNode::inputPositionZ;
MObject BdRbfMultiPositionFalloffWeightNode::influence;

MObject BdRbfMultiPositionFalloffWeightNode::innerRadius;
MObject BdRbfMultiPositionFalloffWeightNode::outerRadius;
MObject BdRbfMultiPositionFalloffWeightNode::falloff;

MObject BdRbfMultiPositionFalloffWeightNode::pose;
MObject BdRbfMultiPositionFalloffWeightNode::sourcePosition;
MObject BdRbfMultiPositionFalloffWeightNode::sourcePositionX;
MObject BdRbfMultiPositionFalloffWeightNode::sourcePositionY;
MObject BdRbfMultiPositionFalloffWeightNode::sourcePositionZ;
MObject BdRbfMultiPositionFalloffWeightNode::enabled;
MObject BdRbfMultiPositionFalloffWeightNode::useRadiusOverride;
MObject BdRbfMultiPositionFalloffWeightNode::innerRadiusOverride;
MObject BdRbfMultiPositionFalloffWeightNode::outerRadiusOverride;

MObject BdRbfMultiPositionFalloffWeightNode::outputWeight;
MObject BdRbfMultiPositionFalloffWeightNode::isValid;
MObject BdRbfMultiPositionFalloffWeightNode::falloffStatus;

namespace {

bool haveSameSources(
    const std::vector<bd_util_nodes::PositionSourceDefinition>& first,
    const std::vector<bd_util_nodes::PositionSourceDefinition>& second
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
    const std::vector<bd_util_nodes::MultiPositionFalloffSample>& first,
    const std::vector<bd_util_nodes::MultiPositionFalloffSample>& second
) {
    if (first.size() != second.size()) {
        return false;
    }
    for (std::size_t poseIndex = 0; poseIndex < first.size(); ++poseIndex) {
        if (
            first[poseIndex].logicalIndex != second[poseIndex].logicalIndex
            || first[poseIndex].innerRadius != second[poseIndex].innerRadius
            || first[poseIndex].outerRadius != second[poseIndex].outerRadius
            || first[poseIndex].sourcePositions.size()
                != second[poseIndex].sourcePositions.size()
        ) {
            return false;
        }
        for (
            std::size_t sourceIndex = 0;
            sourceIndex < first[poseIndex].sourcePositions.size();
            ++sourceIndex
        ) {
            const bd_util_nodes::IndexedPosition& firstPosition =
                first[poseIndex].sourcePositions[sourceIndex];
            const bd_util_nodes::IndexedPosition& secondPosition =
                second[poseIndex].sourcePositions[sourceIndex];
            if (
                firstPosition.logicalIndex != secondPosition.logicalIndex
                || firstPosition.position != secondPosition.position
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

struct BdRbfMultiPositionFalloffWeightNode::Cache {
    bd_util_nodes::MultiPositionFalloffStatus evaluate(
        const std::vector<bd_util_nodes::PositionSourceDefinition>& sources,
        const std::vector<bd_util_nodes::MultiPositionFalloffSample>& samples,
        bd_util_nodes::Falloff requestedFalloff,
        const std::vector<bd_util_nodes::IndexedPosition>& inputPositions,
        std::vector<bd_util_nodes::PositionFalloffWeight>& outputWeights
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
            != bd_util_nodes::MultiPositionFalloffStatus::kSuccess
        ) {
            return configureStatus;
        }
        return evaluator.evaluate(inputPositions, outputWeights);
    }

    std::mutex mutex;
    bool configured = false;
    std::vector<bd_util_nodes::PositionSourceDefinition> configuredSources;
    std::vector<bd_util_nodes::MultiPositionFalloffSample> configuredSamples;
    bd_util_nodes::Falloff falloff = bd_util_nodes::Falloff::kQuintic;
    bd_util_nodes::MultiPositionFalloffStatus configureStatus =
        bd_util_nodes::MultiPositionFalloffStatus::kNoSources;
    bd_util_nodes::MultiPositionFalloffEvaluator evaluator;
};

BdRbfMultiPositionFalloffWeightNode::BdRbfMultiPositionFalloffWeightNode()
    : cache_(std::make_unique<Cache>()) {}

BdRbfMultiPositionFalloffWeightNode::~BdRbfMultiPositionFalloffWeightNode() =
    default;

void* BdRbfMultiPositionFalloffWeightNode::creator() {
    return new BdRbfMultiPositionFalloffWeightNode();
}

MStatus BdRbfMultiPositionFalloffWeightNode::initialize() {
    MStatus status;
    MFnNumericAttribute numericAttributeFn;
    MFnUnitAttribute unitAttributeFn;
    MFnEnumAttribute enumAttributeFn;

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        "inputPosition",
        "ip",
        "inputPositionX",
        "ipx",
        "inputPositionY",
        "ipy",
        "inputPositionZ",
        "ipz",
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
    for (const MObject& child : {inputPosition, influence}) {
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

    status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        outerRadius,
        "outerRadius",
        "outr",
        1.0
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

    status = bd_util_nodes::createDoubleLinear3Attribute(
        numericAttributeFn,
        unitAttributeFn,
        sourcePosition,
        sourcePositionX,
        sourcePositionY,
        sourcePositionZ,
        "sourcePosition",
        "sp",
        "sourcePositionX",
        "spx",
        "sourcePositionY",
        "spy",
        "sourcePositionZ",
        "spz",
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

    status = bd_util_nodes::createDoubleLinearAttribute(
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

    status = bd_util_nodes::createDoubleLinearAttribute(
        unitAttributeFn,
        outerRadiusOverride,
        "outerRadiusOverride",
        "oro",
        1.0
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
             sourcePosition,
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
              {"InvalidPosition", static_cast<short>(3)},
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

    const std::array<MObject, 18> inputs = {
        source,
        inputPosition,
        inputPositionX,
        inputPositionY,
        inputPositionZ,
        influence,
        innerRadius,
        outerRadius,
        falloff,
        pose,
        sourcePosition,
        sourcePositionX,
        sourcePositionY,
        sourcePositionZ,
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

MStatus BdRbfMultiPositionFalloffWeightNode::compute(
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
    std::vector<bd_util_nodes::PositionSourceDefinition> sources;
    std::vector<bd_util_nodes::IndexedPosition> inputPositions;
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
    inputPositions.reserve(sourceCount);
    for (unsigned int index = 0; index < sourceCount; ++index) {
        const unsigned int logicalIndex = sourceHandles.elementIndex(&status);
        if (!status) {
            return status;
        }
        MDataHandle sourceHandle = sourceHandles.inputValue(&status);
        if (!status) {
            return status;
        }
        const double3& inputValue = sourceHandle.child(
            inputPosition
        ).asDouble3();
        sources.push_back({
            logicalIndex,
            sourceHandle.child(influence).asDouble(),
        });
        inputPositions.push_back({
            logicalIndex,
            {inputValue[0], inputValue[1], inputValue[2]},
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
        inputPositions.begin(),
        inputPositions.end(),
        [](const auto& first, const auto& second) {
            return first.logicalIndex < second.logicalIndex;
        }
    );

    const double defaultInnerRadius = dataBlock.inputValue(
        innerRadius,
        &status
    ).asDistance().asCentimeters();
    if (!status) {
        return status;
    }
    const double defaultOuterRadius = dataBlock.inputValue(
        outerRadius,
        &status
    ).asDistance().asCentimeters();
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
    std::vector<bd_util_nodes::MultiPositionFalloffSample> enabledSamples;
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
            bd_util_nodes::MultiPositionFalloffSample sample;
            sample.logicalIndex = logicalIndex;
            const bool useOverride = poseHandle.child(
                useRadiusOverride
            ).asBool();
            sample.innerRadius = useOverride
                ? poseHandle.child(innerRadiusOverride)
                    .asDistance()
                    .asCentimeters()
                : defaultInnerRadius;
            sample.outerRadius = useOverride
                ? poseHandle.child(outerRadiusOverride)
                    .asDistance()
                    .asCentimeters()
                : defaultOuterRadius;

            MArrayDataHandle sourcePositionHandles(
                poseHandle.child(sourcePosition),
                &status
            );
            if (!status) {
                return status;
            }
            const unsigned int poseSourceCount =
                sourcePositionHandles.elementCount(&status);
            if (!status) {
                return status;
            }
            sample.sourcePositions.reserve(poseSourceCount);
            for (
                unsigned int sourceIndex = 0;
                sourceIndex < poseSourceCount;
                ++sourceIndex
            ) {
                const unsigned int sourceLogicalIndex =
                    sourcePositionHandles.elementIndex(&status);
                if (!status) {
                    return status;
                }
                MDataHandle sourcePositionHandle =
                    sourcePositionHandles.inputValue(&status);
                if (!status) {
                    return status;
                }
                const double3& positionValue =
                    sourcePositionHandle.asDouble3();
                sample.sourcePositions.push_back({
                    sourceLogicalIndex,
                    {
                        positionValue[0],
                        positionValue[1],
                        positionValue[2],
                    },
                });
                if (sourceIndex + 1 < poseSourceCount) {
                    status = sourcePositionHandles.next();
                    if (!status) {
                        return status;
                    }
                }
            }
            std::sort(
                sample.sourcePositions.begin(),
                sample.sourcePositions.end(),
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

    std::vector<bd_util_nodes::PositionFalloffWeight> falloffWeights;
    const bd_util_nodes::MultiPositionFalloffStatus resultStatus =
        cache_->evaluate(
            sources,
            enabledSamples,
            static_cast<bd_util_nodes::Falloff>(falloffValue),
            inputPositions,
            falloffWeights
        );

    std::unordered_map<unsigned int, double> weightByIndex;
    if (
        resultStatus == bd_util_nodes::MultiPositionFalloffStatus::kSuccess
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
        resultStatus == bd_util_nodes::MultiPositionFalloffStatus::kSuccess
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
BdRbfMultiPositionFalloffWeightNode::schedulingType() const {
    return MPxNode::kParallel;
}
