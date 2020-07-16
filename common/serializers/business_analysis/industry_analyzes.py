from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.business_analysis import IndustryAnalysis


class IndustryAnalyzesSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndustryAnalysis
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'industryAnalysisId': representation.get('IndustryAnalysisId', None),
            'industry': return_value_or_none(representation.get('Industry', {}), 'Description'),
            'productServiceSold': representation.get('ProductServiceSold', None),
            'percentTotalRevenue': representation.get('PercentTotalRevenue', None),
            'revenueContribution': representation.get('RevenueContribution', None),
            'percentMarketShare': representation.get('PercentMarketShare', None),
            'growthRate': representation.get('GrowthRate', None),
            'buyerPower': return_value_or_none(representation.get('BuyerPower', {}), 'Description'),
            'supplierPower': return_value_or_none(representation.get('SupplierPower', {}), 'Description'),
            'newEntrantThreat': return_value_or_none(representation.get('NewEntrantThreat', {}), 'Description'),
            'substitutionThreat': return_value_or_none(representation.get('SubstitutionThreat', {}), 'Description'),
            'competitiveRivalry': return_value_or_none(representation.get('CompetitiveRivalry', {}), 'Description'),
            'startDate': representation.get('StartDate', None)
        }

        return to_represent
