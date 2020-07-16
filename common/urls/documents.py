from django.urls import path
from common.views.document import DocumentsAPIView, DocumentAPIView, download_file, get_documents_list_by_base_party

urlpatterns = [
    path('Documents', DocumentsAPIView.as_view(), name='Documents'),
    path('Documents/<int:id>', DocumentsAPIView.as_view(), name='Documents'),

    path('Document', DocumentAPIView.as_view(), name='Document'),
    path('Document/<int:id>', DocumentAPIView.as_view(), name='Document'),

    path('ViewFile/<int:file_id>', download_file, name="ViewFile"),
    path('GetDocumentsListByBaseParty/<int:base_party_id>', get_documents_list_by_base_party, name="GetDocumentsListByBaseParty")
]
