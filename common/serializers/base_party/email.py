from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.base_party import BasePartyEmail


class BasePartyEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyEmail
        fields = ('BasePartyEmailId', 'EmailFinal', 'EmailType', 'PreferenceType', 'AddressType')
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation.get('BasePartyEmailId', None),
            'value': representation.get('EmailFinal', None),
            'emailType': return_value_or_none(representation.get('EmailType'), 'EmailTypeId'),
            'addressType': return_value_or_none(representation.get('AddressType'), 'AddressTypeId'),
            'preferenceType': return_value_or_none(representation.get('PreferenceType'), 'PreferenceTypeId'),

            'addressTypeStringed': return_value_or_none(representation.get('AddressType'), 'Description'),
            'preferenceTypeStringed': return_value_or_none(representation.get('PreferenceType'), 'Description'),
        }

        return to_represent
