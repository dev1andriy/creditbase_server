from rest_framework import serializers
from common.models import CreditApplication
from common.utils.credit_application_notes_data import generate_credit_applications_notes_data


class CreditApplicationNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditApplication
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        credit_application_id = representation['CreditApplicationId']

        to_represent = {
            "notes": generate_credit_applications_notes_data(credit_application_id, representation['BasePartyId'])
        }

        return to_represent
