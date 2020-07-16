from rest_framework import serializers

from common.models import Currency
from common.utils.return_value_or_none import return_value_or_none

class FacilityCoverageDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)
        self.model = str(self.Meta.model.__name__)

        super(FacilityCoverageDataSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'hostFacilityId': representation.get('FacilityIdHost', None),
            'facilityOwner': return_value_or_none(representation.get('BasePartyId', {}), 'BasePartyName'),
            'facilityDescription': return_value_or_none(representation.get('Description1', {}), 'HostValue') if return_value_or_none(representation.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(representation.get('Description1', {}), 'ProposedValue'),
            'currency': Currency.objects.get(CurrencyId=representation['Currency']['HostValue']).Description if representation['Currency'] is not None and Currency.objects.filter(CurrencyId=representation['Currency']['HostValue']).exists() else None,
            'tenor': return_value_or_none(representation.get('TenorOriginal', {}), 'HostValue') if return_value_or_none(representation.get('TenorOriginal', {}), 'ProposedValue') is None else return_value_or_none(representation.get('TenorOriginal', {}), 'ProposedValue'),
            'frequency': return_value_or_none(representation.get('FrequencyTenor', {}), 'HostValue') if return_value_or_none(representation.get('FrequencyTenor', {}), 'ProposedValue') is None else return_value_or_none(representation.get('FrequencyTenor', {}), 'ProposedValue'),
            'facilityLimit': return_value_or_none(representation.get('CommitmentValue', {}), 'HostValue') if return_value_or_none(representation.get('CommitmentValue', {}), 'ProposedValue') is None else return_value_or_none(representation.get('CommitmentValue', {}), 'ProposedValue'),
            'outstandingBalance': return_value_or_none(representation.get('BalanceValue', {}), 'HostValue') if return_value_or_none(representation.get('BalanceValue', {}), 'ProposedValue') is None else return_value_or_none(representation.get('BalanceValue', {}), 'ProposedValue'),
            'proposedLimit': None,
            'totalExposure': return_value_or_none(representation.get('ExposureTotal', {}), 'HostValue') if return_value_or_none(representation.get('ExposureTotal', {}), 'ProposedValue') is None else return_value_or_none(representation.get('ExposureTotal', {}), 'ProposedValue'),
        }

        return to_represent
