from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.base_party import BasePartyAddress


class BasePartyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyAddress
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation.get('BasePartyAddressId', None),
            'street1': representation.get('Street1', None),
            'street2': representation.get('Street2', None),
            'countryAndPostCode': {
                'postCode': representation.get('PostCode', None),
                'country': return_value_or_none(representation.get('Country', None), 'CountryId')
            },
            'cityAndState': {
                'location1': representation.get('Level1Location', None),
                'location2': representation.get('Level2Location', None),
                'location3': representation.get('Level3Location', None)
            },
            'value': representation.get('AddressFinal', None),
            'addressType': return_value_or_none(representation.get('AddressType'), 'AddressTypeId'),
            'preferenceType': return_value_or_none(representation.get('PreferenceType'), 'PreferenceTypeId'),

            'addressTypeStringed': return_value_or_none(representation.get('AddressType'), 'Description'),
            'preferenceTypeStringed': return_value_or_none(representation.get('PreferenceType'), 'Description'),
        }

        return to_represent
