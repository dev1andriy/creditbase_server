from rest_framework import serializers

from common.models import Currency
from common.utils.return_value_or_none import return_value_or_none


class CoverageCollateralSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        depth = 3

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)
        self.model = str(self.Meta.model.__name__)

        super(CoverageCollateralSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        collateral = representation.get('CollateralId', {})
        facility = representation.get('FacilityId', {})

        to_represent = {
            'model': self.model,
            'bindWith': representation.get('BindWith', None),
            'collateralId': collateral.get('CollateralId'),
            'collateralDescription': return_value_or_none(collateral.get('Description1', {}), 'HostValue') if return_value_or_none(collateral.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(collateral.get('Description1', {}), 'ProposedValue'),
            'facilityId': facility.get('FacilityId'),
            'hostFacilityId': facility.get('FacilityIdHost', None),
            'facilityOwner': return_value_or_none(facility.get('BasePartyId', {}), 'BasePartyName'),
            'facilityDescription': return_value_or_none(facility.get('Description1', {}), 'HostValue') if return_value_or_none(facility.get('Description1', {}), 'ProposedValue') is None else return_value_or_none(facility.get('Description1', {}), 'ProposedValue'),
            'currency': Currency.objects.get(CurrencyId=facility['Currency']['HostValue']).Description if facility['Currency'] is not None and Currency.objects.filter(CurrencyId=facility['Currency']['HostValue']).exists() else None,
            'tenor': return_value_or_none(facility.get('TenorOriginal', {}), 'HostValue') if return_value_or_none(facility.get('TenorOriginal', {}), 'ProposedValue') is None else return_value_or_none(facility.get('TenorOriginal', {}), 'ProposedValue'),
            'frequency': return_value_or_none(facility.get('FrequencyTenor', {}), 'HostValue') if return_value_or_none(facility.get('FrequencyTenor', {}), 'ProposedValue') is None else return_value_or_none(facility.get('FrequencyTenor', {}), 'ProposedValue'),
            'facilityLimit': return_value_or_none(facility.get('CommitmentValue', {}), 'HostValue') if return_value_or_none(facility.get('CommitmentValue', {}), 'ProposedValue') is None else return_value_or_none(facility.get('CommitmentValue', {}), 'ProposedValue'),
            'outstandingBalance': return_value_or_none(facility.get('BalanceValue', {}), 'HostValue') if return_value_or_none(facility.get('BalanceValue', {}), 'ProposedValue') is None else return_value_or_none(facility.get('BalanceValue', {}), 'ProposedValue'),
            'proposedLimit': None,
            'totalExposure': return_value_or_none(facility.get('ExposureTotal', {}), 'HostValue') if return_value_or_none(facility.get('ExposureTotal', {}), 'ProposedValue') is None else return_value_or_none(facility.get('ExposureTotal', {}), 'ProposedValue'),
            'assignment': representation.get('Assignment', None),
            'lienOrder': representation.get('LienOrder', None),
        }

        return to_represent
