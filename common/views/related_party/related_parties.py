from django.http import JsonResponse
from rest_framework.views import APIView


from common.models import RelatedParty
from common.serializers import RelatedPartiesOwnersSerializer
from common.configs.views.related_party import generate_config


class RelatedPartiesAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, **kwargs):
        if 'id' in kwargs:
            related_parties = RelatedParty.objects.filter(BaseParty1Id=kwargs.get('id'))
            config = generate_config(kwargs.get('id'))
        else:
            related_parties = RelatedParty.objects.all()
            config = generate_config(None)

        response = {
            "data": RelatedPartiesOwnersSerializer(related_parties, many=True).data,
            "config": config
        }

        # if 'id' in kwargs.keys():
        #     try:
        #         response["note"] = CamelCaseParser.to_camel_case_single(NoteSerializer(
        #             Note.objects.get(ModuleId=2, BasePartyId=kwargs['id'])).data)
        #     except:
        #         note = Note()
        #         note.ModuleId = 2
        #         note.BasePartyId_id = kwargs['id']
        #         note.save()
        #         response["note"] = CamelCaseParser.to_camel_case_single(NoteSerializer(note).data)


        return JsonResponse(response)