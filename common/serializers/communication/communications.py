from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.communication import Communication


class CommunicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        communication_id = representation.get('CommunicationId', None)

        to_represent = {
            "communicationId": communication_id,
            'from': representation.get('AddressFrom', None),
            'subject': representation.get('Subject', None),
            'regarding': return_value_or_none(representation.get('BasePartyId', None), 'BasePartyName'),
            'dateReceive': representation.get('InsertDate', None)
        }

        return to_represent
