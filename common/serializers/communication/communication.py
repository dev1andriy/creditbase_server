from rest_framework import serializers
from common.models.communication import Communication, CommunicationAttachment
from common.serializers.communication.communication_attachment import CommunicationAttachmentSerializer


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        communication_id = representation.get('CommunicationId', None)

        to_represent = {
            "communicationId": communication_id,
            "email": {
                "from": representation.get('AddressFrom', None),
                "to": representation.get('AddressTo', None),
                "CC": representation.get('AddressCC', None),
                "regarding": representation.get('BasePartyId', None),
                "subject": representation.get('Subject', None),
                "emailBody": representation.get('Body', None)
            },
            "attachments": CommunicationAttachmentSerializer(CommunicationAttachment.objects.filter(CommunicationId=communication_id), many=True).data,
        }

        return to_represent
