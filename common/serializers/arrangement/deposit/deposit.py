from rest_framework import serializers
from django.apps import apps

from common.models import RequestType
from common.serializers.configs import RequestTypeSerializer
from common.utils.params import generate_params


class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'
        # depth = 2

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs.pop('model', None)

        super(DepositSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        to_represent = {
            'depositId': representation['DepositId'],
            'creditApplicationId': representation['CreditApplicationId'],
            'dataView': representation['DataView'],
            'details': {
                'fields': {
                    'baseParty': representation['BasePartyId'],
                    'arrangementType': representation['ArrangementType'],
                    'depositId': representation['DepositId'],
                    'hostDepositId': representation['DepositIdHost']
                },
                'grid': generate_params(arrangement_type=representation['ArrangementType'],
                                        request_type=None,
                                        data_view=representation['DataView'],
                                        instance=representation)

            }
        }

        return to_represent
