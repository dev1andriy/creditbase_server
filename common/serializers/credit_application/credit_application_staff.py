from django.contrib.auth import get_user_model
from rest_framework import serializers
from common.models import CreditApplicationStaff
from common.models.general import *


class CreditApplicationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditApplicationStaff
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            "id": representation["id"],
            "primaryContact": representation["IsPrimaryRelatedStaff"],
            "relationType": representation["RelationType"],
            "relationshipStaffName": representation["StaffId"],
            'relationTypeStringed': RelationType.objects.filter(RelationTypeId=representation['RelationType']).first().Description if RelationType.objects.filter(RelationTypeId=representation['RelationType']).first() else None,
            'relationshipStaffNameStringed': get_user_model().objects.filter(pk=representation['StaffId']).first().first_name + " " + get_user_model().objects.filter(pk=representation['StaffId']).first().last_name if get_user_model().objects.filter(pk=representation['StaffId']).first() else None,
        }

        return to_represent
