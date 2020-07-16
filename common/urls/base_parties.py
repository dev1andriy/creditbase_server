from django.urls import path

from common.views.base_party import BasePartyAPIView, BasePartiesAPIView

urlpatterns = [
    path('BaseParties', BasePartiesAPIView.as_view()),
    path('BaseParty', BasePartyAPIView.as_view()),
    path('BaseParty/<int:id>', BasePartyAPIView.as_view()),
]
