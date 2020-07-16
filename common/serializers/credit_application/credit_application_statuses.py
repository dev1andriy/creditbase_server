from rest_framework import serializers
from common.models import CreditApplication
from common.utils.credit_application_sections import get_credit_application_sections_statues


class CreditApplicationStatusesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditApplication
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        statuses = get_credit_application_sections_statues(representation['CreditApplicationId'])

        to_represent = {
            "applicationSectionsStatuses": statuses['application_sections_statuses'],
            "creditApplicationStatus": statuses['credit_application_status']
        }

        return to_represent
