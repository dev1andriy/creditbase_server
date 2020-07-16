from rest_framework import serializers

from common.models import Currency
from common.utils.return_value_or_none import return_value_or_none


class CoveragesSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 3

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)
        self.model = str(self.Meta.model.__name__)

        super(CoveragesSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        collateral = representation.get('CollateralId', {})
        facility = representation.get('FacilityId', {})

        to_represent = {
            'coverageId': representation.get('CoverageId'),
            'model': self.model,
            'coverage': return_value_or_none(facility.get('Description1', {}), 'HostValue') if return_value_or_none(facility.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(facility.get('Description1', {}), 'ProposedValue') if representation.get('BindWith') == 'Facility' else return_value_or_none(collateral.get('Description1', {}), 'HostValue') if return_value_or_none(collateral.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('Description1', {}), 'ProposedValue'),
            'basePartyName': return_value_or_none(facility.get('BasePartyId', {}), 'BasePartyName'),
            'facilityDescription': return_value_or_none(facility.get('Description1', {}), 'HostValue') if return_value_or_none(facility.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(facility.get('Description1', {}), 'ProposedValue'),
            'collateralId': collateral.get('CollateralId'),
            'facilityId': facility.get('FacilityId'),
            'bindWith': representation.get('BindWith'),
            'collateralOwner': return_value_or_none(collateral.get('BasePartyId', {}), 'BasePartyName'),
            'collateralDescription': return_value_or_none(collateral.get('Description1', {}), 'HostValue') if return_value_or_none(collateral.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('Description1', {}), 'ProposedValue'),
            'currency': {
                'id': return_value_or_none(collateral.get('Currency', {}), 'HostValue'),
                'title': Currency.objects.get(CurrencyId=collateral['Currency']['HostValue']).Description if collateral['Currency'] is not None and Currency.objects.filter(CurrencyId=collateral['Currency']['HostValue']).exists() else None
            },
            'assignment': representation.get('Assignment', None),
            'lienOrder': representation.get('LienOrder', None),
            'totalExposure': return_value_or_none(collateral.get('ExposureTotal', {}), 'HostValue') if return_value_or_none(collateral.get('ExposureTotal', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('ExposureTotal', {}), 'ProposedValue'),
            'marketValue': return_value_or_none(collateral.get('MarketValue', {}), 'HostValue') if return_value_or_none(collateral.get('MarketValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('MarketValue', {}), 'ProposedValue'),
            'discountFactor': return_value_or_none(collateral.get('DiscountFactor', {}), 'HostValue') if return_value_or_none(collateral.get('DiscountFactor', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('DiscountFactor', {}), 'ProposedValue'),
            'discountedValue': return_value_or_none(collateral.get('DiscountedValue', {}), 'HostValue') if return_value_or_none(collateral.get('DiscountedValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('DiscountedValue', {}), 'ProposedValue'),
            'forcedSaleValue': return_value_or_none(collateral.get('ForcedSaleValue', {}), 'HostValue') if return_value_or_none(collateral.get('ForcedSaleValue', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('ForcedSaleValue', {}), 'ProposedValue'),
            'priorLiens': return_value_or_none(collateral.get('PriorLiens', {}), 'HostValue') if return_value_or_none(collateral.get('PriorLiens', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('PriorLiens', {}), 'ProposedValue')
        }

        return to_represent
