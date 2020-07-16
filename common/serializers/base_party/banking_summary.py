from rest_framework import serializers

from common.models.base_party import BasePartyBankingSummary


class BankingSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyBankingSummary
        fields = ('CommitmentTotal', 'CoverageRatiobyMV', 'ExposureTotal', 'ExposureAtRisk',
                  'AssetClassification')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'commitmentTotal': representation.get('CommitmentTotal', None),
            'coverageRatiobyMV': representation.get('CoverageRatiobyMV', None),
            'exposureTotal': representation.get('ExposureTotal', None),
            'exposureAtRisk': representation.get('ExposureAtRisk', None),
            'assetClassification': representation.get('AssetClassification', None)
        }

        return to_represent



