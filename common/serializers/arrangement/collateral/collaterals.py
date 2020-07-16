from rest_framework import serializers
from django.apps import apps

from common.models import RequestType, Currency
from common.serializers.configs import RequestTypeSerializer
from common.utils.params import generate_params
from common.utils.return_value_or_none import return_value_or_none


class CollateralsSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)
        self.model = str(self.Meta.model.__name__)

        super(CollateralsSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'collateralId': representation.get('CollateralId'),
            'creditApplicationId': representation.get('CreditApplicationId').get('CreditApplicationId', None) if representation.get('CreditApplicationId') is not None else None,
            'basePartyName': representation.get('BasePartyId').get('BasePartyName', None) if representation.get('BasePartyId') is not None else None,
            'model': self.model,
            'collateralParent': representation.get('CollateralIdParent').get('Description1') if representation.get('CollateralIdParent') is not None else None,
            'requestType': representation.get('RequestType').get('Description', None) if representation.get('RequestType') is not None else None,
            'collateral': return_value_or_none(representation.get('Description1', {}), 'HostValue') if return_value_or_none(representation.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(representation.get('Description1', {}), 'ProposedValue'),
            'hostCollateralId': representation.get('CollateralIdHost', None),
            'currency': {
                'id': representation.get('Currency', {}).get('HostValue', None) if representation.get('Currency') is not None else None,
                'title': Currency.objects.get(CurrencyId=representation['Currency']['HostValue']).Description if representation['Currency'] is not None and Currency.objects.filter(CurrencyId=representation['Currency']['HostValue']).exists() else None
            },
            'existingCharge': 100000,
            'marketValue': 100000,
            'forcedSaleValue': 100000,
            'discountFactor': None,
            'discountedValue': 100000,
            'proposedCharge': 100000,
            'parameterSummary': None,
        }

        return to_represent
