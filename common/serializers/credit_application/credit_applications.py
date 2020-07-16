from rest_framework import serializers
from common.models import CreditApplication, CreditApplicationBankingSummary
from common.models.general import *
from common.serializers.general import PurposesApplicableSerializer


class CreditApplicationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CreditApplication
        fields = "__all__"
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        banking_summary = CreditApplicationBankingSummary.objects.filter(CreditApplicationId=representation['CreditApplicationId']).first()

        to_represent = {
            'creditApplicationId': representation.get('CreditApplicationId', None),
            'basePartyName': representation['BasePartyId']['BasePartyName'] if 'BasePartyId' in representation and representation['BasePartyId'] is not None else None,
            'basePartyId': representation['BasePartyId']['BasePartyId'],
            'applicationType': representation['ApplicationType']['Description'] if 'ApplicationType' in representation and representation['ApplicationType'] is not None else None,
            'applicationNumber': representation.get('CreditApplicationId', None),
            'applicationPurpose': PurposesApplicableSerializer(Purpose.objects.filter(PurposeId__in=representation['PurposesApplicable']), many=True).data if representation['PurposesApplicable'] is not None else None,
            'applicationStatus': {
                "value": representation['ApplicationStatus']['Description'] if 'ApplicationStatus' in representation and representation['ApplicationStatus'] is not None else None,
                "icon": representation['ApplicationStatus']['Description1'] if 'ApplicationStatus' in representation and representation['ApplicationStatus'] is not None else None,
                "color": representation['ApplicationStatus']['Description2'] if 'ApplicationStatus' in representation and representation['ApplicationStatus'] is not None else None
            },
            'applicationDate': representation['InsertDate'],
            'businessUnit': representation['BusinessUnit']['Description'] if 'BusinessUnit' in representation and  representation['BusinessUnit'] is not None else None,
            'exposure': banking_summary.ProposedExposure,
            'increase': banking_summary.ProposedIncrease,
            'relationshipManager': None,
            'decisionDate': representation['DecisionDate'],
            'archived': representation['IsArchived']
        }

        return to_represent
