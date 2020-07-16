from rest_framework import serializers

from common.models import Currency
from common.utils.return_value_or_none import return_value_or_none


class CollateralLinkageSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 3

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)

        super(CollateralLinkageSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        collateral = representation.get('CollateralId', {})
        facility = representation.get('FacilityId', {})

        to_represent = {
            'id': representation.get('CoverageId'),
            'facilityDescription': return_value_or_none(facility.get('Description1', {}), 'HostValue') if return_value_or_none(facility.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(facility.get('Description1', {}), 'ProposedValue'),
            'collateralId': collateral.get('CollateralId'),
            'collateralOwner': return_value_or_none(collateral.get('BasePartyId', {}), 'BasePartyName'),
            'collateralDescription': return_value_or_none(collateral.get('Description1', {}), 'HostValue') if return_value_or_none(collateral.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('Description1', {}), 'ProposedValue'),
            'currency': Currency.objects.get(CurrencyId=collateral['Currency']['HostValue']).Description if 'Currency' in collateral and collateral['Currency'] is not None and Currency.objects.filter(CurrencyId=collateral['Currency']['HostValue']).exists() else None,
            'assignment': representation.get('Assignment', None),
            'lienOrder': representation.get('LienOrder', None),
            'openMarketValue': return_value_or_none(collateral.get('MarketValue', {}), 'HostValue') if return_value_or_none(collateral.get('MarketValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('MarketValue', {}), 'ProposedValue'),
            'discountFactor': return_value_or_none(collateral.get('DiscountFactor', {}), 'HostValue') if return_value_or_none(collateral.get('DiscountFactor', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('DiscountFactor', {}), 'ProposedValue'),
            'discountedValue': return_value_or_none(collateral.get('DiscountedValue', {}), 'HostValue') if return_value_or_none(collateral.get('DiscountedValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('DiscountedValue', {}), 'ProposedValue'),
            'forcedSaleValue': return_value_or_none(collateral.get('ForcedSaleValue', {}), 'HostValue') if return_value_or_none(collateral.get('ForcedSaleValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('ForcedSaleValue', {}), 'ProposedValue'),
            'priorLiens': return_value_or_none(collateral.get('PriorLiens', {}), 'HostValue') if return_value_or_none(collateral.get('PriorLiens', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('PriorLiens', {}), 'ProposedValue')
        }

        return to_represent
