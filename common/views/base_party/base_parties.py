from django.http import JsonResponse
from rest_framework.views import APIView

from common.models import BaseParty
from common.serializers import BasePartiesSerializer
from common.configs.views.base_party import generate_config


class BasePartiesAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        base_parties = BaseParty.objects.all()
        response = BasePartiesSerializer(base_parties, many=True).data

        response = {
            "data": response,
            "config": generate_config()
        }

        return JsonResponse(response, safe=False)
