from rest_framework import serializers
from django.apps import apps

from common.models import RequestType, Coverage
from common.serializers.arrangement.coverage.facility_linkage import FacilityLinkageSerializer
from common.serializers.configs import RequestTypeSerializer
from common.utils.get_collateral_coverage_summary import get_collateral_coverage_summary
from common.utils.params import generate_params


class CollateralSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        # depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)

        super(CollateralSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'collateralId': representation['CollateralId'],
            'creditApplicationId': representation['CreditApplicationId'],
            'dataView': representation['DataView'],
            'details': {
                'fields': {
                    'baseParty': representation['BasePartyId'],
                    'arrangementType': representation['ArrangementType'],
                    'parentCollateral': representation['CollateralIdParent'],
                    'collateralId': representation['CollateralId'],
                    'hostCollateralId': representation['CollateralIdHost']
                },
                'grid': generate_params(arrangement_type=representation['ArrangementType'],
                                        request_type=representation['RequestType'],
                                        data_view=representation['DataView'],
                                        instance=representation)
            },
            'coverage': {
                'coverageSummary': get_collateral_coverage_summary(representation.get('CollateralId', None)),
                'facilityLinkages': FacilityLinkageSerializer(Coverage.objects.filter(CollateralId=representation.get('CollateralId')), model=Coverage, many=True).data
            }
        }

        return to_represent
