from rest_framework import serializers
from common.models.arrangement import AccountRelatedParty


class AccountRelatedPartiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountRelatedParty
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "id": representation["AccountRelatedPartyId"],
            "relatedPartyName": representation['RelatedPartyName'],
            "relationTypeStringed": representation["RelationType"]["Description"] if "RelationType" in representation and representation["RelationType"] is not None else None,
            "isPrimaryAccountOwnerStringed": representation["IsPrimaryAccountOwner"]["Description"] if "IsPrimaryAccountOwner" in representation and representation["IsPrimaryAccountOwner"] is not None else None,
            "startDate": representation["StartDate"],
            "endDate": representation["EndDate"],
            "print": representation["PrintFlag"]
        }

        return to_represent
