from rest_framework import serializers
from common.utils.return_value_or_none import return_value_or_none

from common.models.base_party import BaseParty, BasePartyNonIndividual, BasePartyIndividual


class BasePartiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseParty
        fields = ('BasePartyId', 'BasePartyName', 'BasePartyHostId', 'PrimaryLegalId', 'PrimaryEmailId',
                  'PrimaryTelephoneId', 'BasePartyType')
        depth = 2

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        base_party_id = representation.get('BasePartyId', None)
        base_party_type = return_value_or_none(representation.get('BasePartyType', {}), 'BasePartyTypeId')

        if base_party_type is not None:
            base_party_type = int(base_party_type)
            if base_party_type == 1:
                birth_date = BasePartyIndividual.objects.get(BasePartyId=base_party_id).BirthDate
                sector = None

            elif base_party_type == 2:
                base_party_non_individual = BasePartyNonIndividual.objects.get(BasePartyId=base_party_id)
                sector = base_party_non_individual.PrimarySector.Description if base_party_non_individual.PrimarySector is not None else None
                birth_date = None

            else:
                sector = None
                birth_date = None

        else:
            sector = None
            birth_date = None

        to_represent = {
            'basePartyId': base_party_id,
            'basePartyName': representation.get('BasePartyName', None),
            'basePartyHostId': representation.get('BasePartyHostId', None),
            'primaryLegalId': representation.get('PrimaryLegalId', None),
            'primaryEmail': return_value_or_none(representation.get('PrimaryEmailId', {}), 'EmailFinal'),
            'primaryTelephone': return_value_or_none(representation.get('PrimaryTelephoneId', {}), 'TelFormattedFinal'),
            'sector': sector,
            'birthDate': birth_date,
        }

        return to_represent
