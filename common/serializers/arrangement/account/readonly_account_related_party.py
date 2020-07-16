from rest_framework import serializers
from common.models.arrangement import AccountRelatedParty


class ReadOnlyAccountRelatedPartySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountRelatedParty
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "id": representation["AccountRelatedPartyId"],
            "details": {
                "relatedPartyName": representation['RelatedPartyName'],
                "relatedParty": representation["RelatedPartyId"]["BasePartyName"] if "RelatedPartyId" in representation and representation["RelatedPartyId"] is not None else None,
                "accountId": representation["AccountId"]["AccountId"],
                "relationCategory": representation["RelationCategory"]["Description"] if "RelationCategory" in representation and representation["RelationCategory"] is not None else None,
                "relationType": representation["RelationType"]["Description"] if "RelationType" in representation and representation["RelationType"] is not None else None,
                "isPrimaryAccountOwner": representation["IsPrimaryAccountOwner"]["Description"] if "IsPrimaryAccountOwner" in representation and representation["IsPrimaryAccountOwner"] is not None else None,
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
