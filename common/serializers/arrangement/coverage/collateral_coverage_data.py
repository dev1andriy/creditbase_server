from rest_framework import serializers

from common.models import Currency
from common.utils.return_value_or_none import return_value_or_none

class CollateralCoverageDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)
        self.model = str(self.Meta.model.__name__)

        super(CollateralCoverageDataSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'collateralOwner': return_value_or_none(representation.get('BasePartyId', {}), 'BasePartyName'),
            'collateralDescription': return_value_or_none(representation.get('Description1', {}), 'HostValue') if return_value_or_none(representation.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(representation.get('Description1', {}), 'ProposedValue'),
            'currency': Currency.objects.get(CurrencyId=representation['Currency']['HostValue']).Description if representation['Currency'] is not None and Currency.objects.filter(CurrencyId=representation['Currency']['HostValue']).exists() else None,
            'openMarketValue': representation.get('ProposedValue'),
            'discountFactor': return_value_or_none(representation.get('DiscountFactor', {}), 'HostValue') if return_value_or_none(representation.get('DiscountFactor', {}), 'ProposedValue') is None else return_value_or_none(representation.get('DiscountFactor', {}), 'ProposedValue'),
            'discountedValue': return_value_or_none(representation.get('DiscountedValue', {}), 'HostValue') if return_value_or_none(representation.get('DiscountedValue', {}), 'ProposedValue') is None else return_value_or_none(representation.get('DiscountedValue', {}), 'ProposedValue'),
            'forcedSaleValue': return_value_or_none(representation.get('ForcedSaleValue', {}), 'HostValue') if return_value_or_none(representation.get('ForcedSaleValue', {}), 'ProposedValue') is None else return_value_or_none(representation.get('ForcedSaleValue', {}), 'ProposedValue'),
            'priorLiens': return_value_or_none(representation.get('PriorLiens', {}), 'HostValue') if return_value_or_none(representation.get('PriorLiens', {}), 'ProposedValue') is None else return_value_or_none(representation.get('PriorLiens', {}), 'ProposedValue')
        }

        return to_represent
