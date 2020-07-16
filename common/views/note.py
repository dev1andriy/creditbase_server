from django.http import JsonResponse
from rest_framework.decorators import api_view
from common.models.other.note import Note
from common.serializers.other.note import NoteSerializer
from main.common.camel_case_parser import CamelCaseParser
from rest_framework.permissions import IsAuthenticated


@api_view(['PUT'])
# @ensure_csrf_cookie
def update_note(request):
    module_id = request.data['moduleId']
    base_party_id = request.data['basePartyId']
    note_level = request.data['noteLevel']
    note_data = request.data['note']

    try:
        note = Note.objects.get(ModuleId=module_id, BasePartyId=base_party_id)
    except:
        note = Note()
        note.ModuleId = module_id
        note.BasePartyId_id = base_party_id

    if note_level is not None:
        note.NoteLevel = note_level

    if note_level is not None and int(note_level) == 1:
        note.NoteKey1 = base_party_id
    elif note_level is not None and int(note_level) == 2:
        note.NoteKey1 = None

    note.Note = note_data
    note.save()

    return JsonResponse(CamelCaseParser.to_camel_case_single(NoteSerializer(note).data))
