from django.urls import path

from common.views.search import SearchGetTemplateAPIView, SearchBasePartyAPIView

urlpatterns = [
    path('Search/GetSearchTemplate', SearchGetTemplateAPIView.as_view(), name='Search-Get-Template'),
    path('Search/SearchBaseParty',  SearchBasePartyAPIView.as_view(), name='Search-Base-Party')
]