from django.http import JsonResponse
from rest_framework.views import APIView

from common.models import Communication
from common.serializers import CommunicationsSerializer
from common.configs.views.communication import generate_config


class EmailsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            emails = Communication.objects.filter(BasePartyId=kwargs.get('id'))
        else:
            emails = Communication.objects.all()

        response = {
            "data": CommunicationsSerializer(emails, many=True).data,
            "config": generate_config(),
        }

        return JsonResponse(response)
