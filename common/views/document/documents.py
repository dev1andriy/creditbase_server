from django.http import JsonResponse
from rest_framework.views import APIView

from common.models import Document
from common.serializers import DocumentsSerializer
from common.configs.views.document import generate_config


class DocumentsAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            documents = Document.objects.filter(BasePartyId=kwargs['id'])
        else:
            documents = Document.objects.all()

        response = {
            "data": DocumentsSerializer(documents, many=True, context={"host": request.get_host()}).data,
            "config": generate_config(kwargs['id'])
        }

        return JsonResponse(response)
