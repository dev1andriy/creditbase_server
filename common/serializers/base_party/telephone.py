from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.base_party import BasePartyTelephone


class BasePartyTelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyTelephone
        fields = ('BasePartyTelephoneId', 'PreferenceType', 'TelFormattedFinal', 'TelephoneType')
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation.get('BasePartyTelephoneId', None),
            'value': representation.get('TelFormattedFinal', None),
            'telephoneType': return_value_or_none(representation.get('TelephoneType'), 'TelephoneTypeId'),
            'preferenceType': return_value_or_none(representation.get('PreferenceType'), 'PreferenceTypeId'),

            'telephoneTypeStringed': return_value_or_none(representation.get('TelephoneType'), 'Description'),
            'preferenceTypeStringed': return_value_or_none(representation.get('PreferenceType'), 'Description'),
        }

        return to_represent
