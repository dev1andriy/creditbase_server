from django.http import JsonResponse
from rest_framework.views import APIView


from common.models import IndustryAnalysis
from common.serializers import IndustryAnalyzesSerializer
from common.configs.views.business_analysis import generate_config


class IndustryAnalyzesAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            industry_analyzes = IndustryAnalysis.objects.filter(BasePartyId=kwargs.get('id'))
        else:
            industry_analyzes = IndustryAnalysis.objects.all()

        response = {
            "data": IndustryAnalyzesSerializer(industry_analyzes, many=True).data,
            "config": generate_config(),
        }

        # if 'id' in kwargs.keys():
        #     try:
        #         response["note"] = CamelCaseParser.to_camel_case_single(NoteSerializer(
        #             Note.objects.get(ModuleId=3, BasePartyId=kwargs['id'])).data)
        #     except:
        #         note = Note()
        #         note.ModuleId = 3
        #         note.BasePartyId_id = kwargs['id']
        #         note.save()
        #         response["note"] = CamelCaseParser.to_camel_case_single(NoteSerializer(note).data)

        return JsonResponse(response)
