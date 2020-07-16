from rest_framework import serializers

from common.models.base_party import BasePartyFinancialsSummary


class FinancialsSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePartyFinancialsSummary
        fields = ('FinancialModel', 'FiscalYearEnd', 'RecentStatementDate', 'StatementHistory',
                  'TotalRevenue', 'TotalAssets', 'RetainedEarnings', 'TotalEquity', 'DSCR')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'financialModel': representation.get('FinancialModel', None),
            'fiscalYearEnd': representation.get('FiscalYearEnd', None),
            'recentStatementDate': representation.get('RecentStatementDate', None),
            'statementHistory': representation.get('StatementHistory', None),
            'totalRevenue': representation.get('TotalRevenue', None),
            'totalAssets': representation.get('TotalAssets', None),
            'retainedEarnings': representation.get('RetainedEarnings', None),
            'totalEquity': representation.get('TotalEquity', None),
            'DSCR': representation.get('DSCR', None)
        }

        return to_represent
