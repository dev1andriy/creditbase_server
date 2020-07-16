from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none, return_deep_value_or_none

from common.models.related_party import RelatedParty


class RelatedPartiesOwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        # fields = ('RelatedPartyId', 'RelatedParty', 'BaseParty1Id', 'RelationType', 'Percent', 'Amount', 'BeginDate')
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'relatedPartyId': representation.get('RelatedPartyId', None),
            'relatedParty': return_value_or_none(representation.get('BaseParty2Id', None), 'BasePartyName'),
            'relationType': return_value_or_none(representation.get('RelationType', {}), 'Description'),
            'percentOwnership': representation.get('PercentOwnership', None),
            'controllingOwner': 'Yes' if representation.get('IsControllingOwner', None) else 'No',
            'relationLegalId': return_value_or_none(representation.get('BaseParty1Id', None), 'PrimaryLegalId'),
            'relationEmail': return_deep_value_or_none(representation.get('BaseParty1Id', None),
                                                       'PrimaryEmailId',
                                                       'EmailFinal'),
            'RelationPhone': return_deep_value_or_none(representation.get('BaseParty1Id', None),
                                                       'PrimaryTelephoneId',
                                                       'TelFormattedFinal'),
            'BeginDate': representation.get('StartDate', None),
        }

        return to_represent
