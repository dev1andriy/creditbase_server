import base64

from django.core.files.base import ContentFile
from django.http import FileResponse, JsonResponse

from common.models import DocumentFile, Document
from common.serializers import DocumentsListSerializer


def download_file(request, file_id):
    document_file = DocumentFile.objects.get(DocumentFileId=file_id)
    document = document_file.DocumentId

    storage_location = document.StorageLocation if document.StorageLocation is not None else 1

    if storage_location == 1:
        file_data = base64.b64decode(document_file.FileObject.split(",")[1])
    elif storage_location == 2:
        with open(document.FileURL, 'rb') as file:
            file_data = file.read()

    data = ContentFile(file_data, name=document_file.FileName)
    return FileResponse(data, filename=document_file.FileName)


def get_documents_list_by_base_party(request, base_party_id):
    documents = DocumentsListSerializer(Document.objects.filter(BasePartyId=base_party_id), many=True).data

    return JsonResponse(documents, safe=False)