from rest_framework import serializers
from common.models.arrangement import AccountRelatedParty


class EditAccountRelatedPartySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountRelatedParty
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "id": representation["AccountRelatedPartyId"],
            "details": {
                "relatedPartyName": representation['RelatedPartyName'],
                "relatedParty": representation["RelatedPartyId"],
                "accountId": representation["AccountId"],
                "relationCategory": representation["RelationCategory"],
                "relationType": representation["RelationType"],
                "isPrimaryAccountOwner": representation["IsPrimaryAccountOwner"],
                "comment": representation["Comment"],
                "startDate": representation["StartDate"],
                "endDate": representation["EndDate"],
                "editHostValues": representation["EditHostValuesFlag"],
                "order": representation["OrderingRank"],
                "print": representation["PrintFlag"]
            },
            "audit": {

            }
        }

        return to_represent
