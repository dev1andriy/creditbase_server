from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.base_party import BasePartyIdentifier


class BasePartyIdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyIdentifier
        fields = ('BasePartyIdentifierId', 'Identifier', 'IdentifierCategory', 'IdentifierType')
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'id': representation.get('BasePartyIdentifierId', None),
            'identifier': representation.get('Identifier', None),
            'identifierCategory': return_value_or_none(representation.get('IdentifierCategory', {}), 'IdentifierCategoryId'),
            'identifierType': return_value_or_none(representation.get('IdentifierType', {}), 'IdentifierTypeId'),

            'identifierCategoryStringed': return_value_or_none(representation.get('IdentifierCategory', {}), 'Description'),
            'identifierTypeStringed': return_value_or_none(representation.get('IdentifierType', {}), 'Description'),
        }

        return to_represent
