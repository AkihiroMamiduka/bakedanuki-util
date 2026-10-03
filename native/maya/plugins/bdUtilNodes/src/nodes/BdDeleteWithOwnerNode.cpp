#include "bdUtilNodes/nodes/BdDeleteWithOwnerNode.h"

#include <vector>

#include <maya/MDGModifier.h>
#include <maya/MFn.h>
#include <maya/MFnDependencyNode.h>
#include <maya/MFnMessageAttribute.h>
#include <maya/MGlobal.h>
#include <maya/MMessage.h>
#include <maya/MNodeMessage.h>
#include <maya/MPlug.h>
#include <maya/MPlugArray.h>

const MString BdDeleteWithOwnerNode::typeName("bdDeleteWithOwner");
const MTypeId BdDeleteWithOwnerNode::typeId(0x0014271E);

MObject BdDeleteWithOwnerNode::owner;
MObject BdDeleteWithOwnerNode::deleteTarget;

namespace {

bool isStandardMessagePlug(const MPlug& plug) {
    MStatus status;
    MFnDependencyNode nodeFn(plug.node(), &status);
    if (!status) {
        return false;
    }
    const MObject message = nodeFn.attribute("message", &status);
    return status && plug.attribute() == message;
}

bool isDeleteTargetDestination(const MPlug& plug) {
    if (plug.attribute() != BdDeleteWithOwnerNode::deleteTarget) {
        return false;
    }
    MStatus status;
    const MFnDependencyNode nodeFn(plug.node(), &status);
    return status && nodeFn.typeId() == BdDeleteWithOwnerNode::typeId;
}

bool hasAnotherOwner(const MPlug& source, const MPlug& requestedDestination) {
    MPlugArray destinations;
    MStatus status;
    source.connectedTo(destinations, false, true, &status);
    if (!status) {
        return true;
    }
    for (unsigned int index = 0; index < destinations.length(); ++index) {
        const MPlug destination = destinations[index];
        const bool sameElement = destination.node() == requestedDestination.node()
            && destination.attribute() == requestedDestination.attribute()
            && destination.logicalIndex() == requestedDestination.logicalIndex();
        if (!sameElement && isDeleteTargetDestination(destination)) {
            return true;
        }
    }
    return false;
}

bool isDeletableTarget(const MObject& node) {
    if (node.hasFn(MFn::kDagNode)) {
        return false;
    }
    MStatus status;
    const MFnDependencyNode nodeFn(node, &status);
    return status
        && nodeFn.typeId() != BdDeleteWithOwnerNode::typeId
        && !nodeFn.isDefaultNode()
        && !nodeFn.isFromReferencedFile()
        && !nodeFn.isLocked();
}

}  // namespace

BdDeleteWithOwnerNode::~BdDeleteWithOwnerNode() {
    removeOwnerCallback();
    if (selfCallbackId_ != 0) {
        MMessage::removeCallback(selfCallbackId_);
    }
}

void* BdDeleteWithOwnerNode::creator() {
    return new BdDeleteWithOwnerNode();
}

MStatus BdDeleteWithOwnerNode::initialize() {
    MFnMessageAttribute attributeFn;
    MStatus status;

    owner = attributeFn.create("owner", "own", &status);
    if (!status) {
        return status;
    }
    attributeFn.setReadable(false);
    attributeFn.setWritable(true);
    status = addAttribute(owner);
    if (!status) {
        return status;
    }

    deleteTarget = attributeFn.create("deleteTarget", "dt", &status);
    if (!status) {
        return status;
    }
    attributeFn.setReadable(false);
    attributeFn.setWritable(true);
    attributeFn.setArray(true);
    return addAttribute(deleteTarget);
}

void BdDeleteWithOwnerNode::postConstructor() {
    MPxNode::postConstructor();
    MStatus status;
    MObject node = thisMObject();
    selfCallbackId_ = MNodeMessage::addNodeAboutToDeleteCallback(
        node, selfAboutToDelete, this, &status
    );
    if (!status) {
        MGlobal::displayError("bdDeleteWithOwner: failed to register deletion callback");
    }
    refreshOwnerCallback();
}

MStatus BdDeleteWithOwnerNode::connectionMade(
    const MPlug& plug,
    const MPlug& otherPlug,
    bool asSrc
) {
    const MStatus status = MPxNode::connectionMade(plug, otherPlug, asSrc);
    if (!asSrc && plug.attribute() == owner) {
        refreshOwnerCallback();
    }
    return status;
}

MStatus BdDeleteWithOwnerNode::connectionBroken(
    const MPlug& plug,
    const MPlug& otherPlug,
    bool asSrc
) {
    if (!asSrc && plug.attribute() == owner) {
        removeOwnerCallback();
    }
    return MPxNode::connectionBroken(plug, otherPlug, asSrc);
}

MStatus BdDeleteWithOwnerNode::legalConnection(
    const MPlug& plug,
    const MPlug& otherPlug,
    bool asSrc,
    bool& isLegal
) const {
    if (asSrc || (plug.attribute() != owner && plug.attribute() != deleteTarget)) {
        return MPxNode::legalConnection(plug, otherPlug, asSrc, isLegal);
    }

    isLegal = false;
    if (!isStandardMessagePlug(otherPlug) || otherPlug.node() == thisMObject()) {
        return MS::kSuccess;
    }
    if (plug.attribute() == deleteTarget) {
        MStatus status;
        const MPlug ownerSource = MPlug(thisMObject(), owner).source(&status);
        if (!status || (!ownerSource.isNull() && ownerSource.node() == otherPlug.node())) {
            return MS::kSuccess;
        }
        if (!isDeletableTarget(otherPlug.node())
            || hasAnotherOwner(otherPlug, plug)) {
            return MS::kSuccess;
        }
    } else {
        MStatus status;
        const MPlug targets(thisMObject(), deleteTarget);
        const unsigned int count = targets.numConnectedElements(&status);
        if (!status) {
            return MS::kSuccess;
        }
        for (unsigned int index = 0; index < count; ++index) {
            const MPlug target = targets.connectionByPhysicalIndex(index, &status);
            if (!status) {
                return MS::kSuccess;
            }
            const MPlug source = target.source(&status);
            if (!status) {
                return MS::kSuccess;
            }
            if (!source.isNull() && source.node() == otherPlug.node()) {
                return MS::kSuccess;
            }
        }
    }
    isLegal = true;
    return MS::kSuccess;
}

void BdDeleteWithOwnerNode::refreshOwnerCallback() {
    MStatus status;
    const MPlug ownerPlug(thisMObject(), owner);
    const MPlug source = ownerPlug.source(&status);
    if (!status || source.isNull()) {
        removeOwnerCallback();
        return;
    }
    const MObject sourceNode = source.node();
    if (ownerCallbackId_ != 0 && ownerObject_ == sourceNode) {
        return;
    }
    removeOwnerCallback();
    ownerObject_ = sourceNode;
    ownerCallbackId_ = MNodeMessage::addNodeAboutToDeleteCallback(
        ownerObject_, ownerAboutToDelete, this, &status
    );
    if (!status) {
        ownerObject_ = MObject::kNullObj;
        MGlobal::displayError("bdDeleteWithOwner: failed to register owner callback");
    }
}

void BdDeleteWithOwnerNode::removeOwnerCallback() {
    if (ownerCallbackId_ != 0) {
        MMessage::removeCallback(ownerCallbackId_);
        ownerCallbackId_ = 0;
    }
    ownerObject_ = MObject::kNullObj;
}

void BdDeleteWithOwnerNode::ownerAboutToDelete(
    MObject& node,
    MDGModifier& modifier,
    void* clientData
) {
    auto* guard = static_cast<BdDeleteWithOwnerNode*>(clientData);
    if (guard->ownerObject_ != node) {
        return;
    }
    const MStatus status = modifier.deleteNode(guard->thisMObject());
    if (!status) {
        MGlobal::displayWarning("bdDeleteWithOwner: failed to delete owner guard");
    }
}

void BdDeleteWithOwnerNode::selfAboutToDelete(
    MObject& node,
    MDGModifier& modifier,
    void* clientData
) {
    auto* guard = static_cast<BdDeleteWithOwnerNode*>(clientData);
    const MPlug targets(node, deleteTarget);
    MStatus status;
    const unsigned int count = targets.numConnectedElements(&status);
    if (!status) {
        MGlobal::displayWarning("bdDeleteWithOwner: failed to inspect deleteTarget");
        return;
    }

    std::vector<MObject> uniqueTargets;
    uniqueTargets.reserve(count);
    for (unsigned int index = 0; index < count; ++index) {
        const MPlug element = targets.connectionByPhysicalIndex(index, &status);
        if (!status) {
            continue;
        }
        const MPlug source = element.source(&status);
        if (!status || source.isNull()) {
            continue;
        }
        const MObject target = source.node();
        if (target == node || target == guard->ownerObject_
            || !isDeletableTarget(target) || hasAnotherOwner(source, element)) {
            MGlobal::displayWarning("bdDeleteWithOwner: skipped invalid or shared target");
            continue;
        }
        bool found = false;
        for (const MObject& existing : uniqueTargets) {
            if (existing == target) {
                found = true;
                break;
            }
        }
        if (!found) {
            uniqueTargets.push_back(target);
        }
    }

    for (const MObject& target : uniqueTargets) {
        status = modifier.deleteNode(target);
        if (!status) {
            MGlobal::displayWarning("bdDeleteWithOwner: failed to delete target");
        }
    }
}
