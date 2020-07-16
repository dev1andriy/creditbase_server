from rest_framework import serializers
from common.models.business_analysis import IndustryAnalysis


class IndustryAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = IndustryAnalysis
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'industryAnalysisId': representation.get('IndustryAnalysisId', None),
            'details': {
                'industry': representation.get('Industry', None),
                'baseParty': representation.get('BasePartyId', None),
                'productServiceSold': representation.get('ProductServiceSold', None),
                'revenueContribution': representation.get('RevenueContribution', None),
                'percentTotalRevenue': representation.get('PercentTotalRevenue', None),
                'percentMarketShare': representation.get('PercentMarketShare', None),
                'growthRate': representation.get('GrowthRate', None),
                'buyerPower': representation.get('BuyerPower', None),
                'supplierPower': representation.get('SupplierPower', None),
                'newEntrantThreat': representation.get('NewEntrantThreat', None),
                'substitutionThreat': representation.get('SubstitutionThreat', None),
                'competitiveRivalry': representation.get('CompetitiveRivalry', None),
                'startDate': representation.get('StartDate', None),
                'endDate': representation.get('EndDate', None),
                'comment': representation.get('Comment', None),
                'isPrimaryRevenueStream': representation.get('IsPrimaryRevenueStream', None),
            }

        }

        return to_represent
