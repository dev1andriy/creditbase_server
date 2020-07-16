from rest_framework import serializers

from common.models.related_party import RelatedParty


class RelatedPartyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedParty
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'relatedPartyId': representation.get('RelatedPartyId', None),
            'details': {
                'baseParty': representation.get('BaseParty1Id', None),
                'relationType': representation.get('RelationType', None),
                'relatedParty': representation.get('BaseParty2Id', None),
                'percentOwnership': representation.get('PercentOwnership', None),
                'percentVoting': representation.get('PercentVoting', None),
                'sharesCount': representation.get('SharesCount', None),
                'sharesValue': representation.get('SharesValue', None),
                'startDate': representation.get('StartDate', None),
                'endDate': representation.get('EndDate', None),
                'comment': representation.get('Comment', None),
                'isControllingOwner': representation.get('IsControllingOwner', None),
                'linkFinancials': representation.get('LinkFinancials', None),
                'linkBankingInfo': representation.get('LinkBankingInfo', None),
                'linkApplications': representation.get('LinkApplications', None),
            },
        }

        return to_represent
