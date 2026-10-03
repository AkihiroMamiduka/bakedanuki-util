#pragma once

#include <maya/MMessage.h>
#include <maya/MObject.h>
#include <maya/MPxNode.h>
#include <maya/MStatus.h>
#include <maya/MString.h>
#include <maya/MTypeId.h>

class MDGModifier;

class BdDeleteWithOwnerNode final : public MPxNode {
public:
    ~BdDeleteWithOwnerNode() override;

    static void* creator();
    static MStatus initialize();

    void postConstructor() override;
    MStatus connectionMade(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus connectionBroken(const MPlug& plug, const MPlug& otherPlug, bool asSrc) override;
    MStatus legalConnection(
        const MPlug& plug,
        const MPlug& otherPlug,
        bool asSrc,
        bool& isLegal
    ) const override;

    static const MString typeName;
    static const MTypeId typeId;
    static MObject owner;
    static MObject deleteTarget;

private:
    static void ownerAboutToDelete(MObject& node, MDGModifier& modifier, void* clientData);
    static void selfAboutToDelete(MObject& node, MDGModifier& modifier, void* clientData);

    void refreshOwnerCallback();
    void removeOwnerCallback();

    MCallbackId selfCallbackId_ = 0;
    MCallbackId ownerCallbackId_ = 0;
    MObject ownerObject_;
};
