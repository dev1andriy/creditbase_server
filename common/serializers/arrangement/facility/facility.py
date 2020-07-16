from rest_framework import serializers

from common.models import Coverage
from common.utils.get_facility_coverage_summary import get_facility_coverage_summary
from common.utils.params import generate_params
from common.serializers.arrangement import CollateralLinkageSerializer


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        # depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)

        super(FacilitySerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'facilityId': representation['FacilityId'],
            'creditApplicationId': representation['CreditApplicationId'],
            'dataView': representation['DataView'],
            'details': {
                'fields': {
                    'baseParty': representation['BasePartyId'],
                    'arrangementType': representation['ArrangementType'],
                    'facilityParent': representation['FacilityIdParent'],
                    'facilityId': representation['FacilityId'],
                    'hostFacilityId': representation['FacilityIdHost']
                },
                'grid': generate_params(arrangement_type=representation['ArrangementType'],
                                        request_type=representation['RequestType'],
                                        data_view=representation['DataView'],
                                        instance=representation)

            },
            'coverage': {
                'coverageSummary': get_facility_coverage_summary(representation.get('FacilityId', None)),
                'collateralLinkages': CollateralLinkageSerializer(Coverage.objects.filter(FacilityId=representation.get('FacilityId')), model=Coverage, many=True).data
            }
        }

        return to_represent
