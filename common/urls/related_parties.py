from django.urls import path
from common.views.related_party import RelatedPartyAPIView, RelatedPartiesAPIView

urlpatterns = [
    path('RelatedParties/Owners', RelatedPartiesAPIView.as_view(), name='RelatedParties'),
    path('RelatedParties/Owners/<int:id>', RelatedPartiesAPIView.as_view(), name='RelatedParties'),

    path('RelatedParties/Owner', RelatedPartyAPIView.as_view(), name='RelatedParty'),
    path('RelatedParties/Owner/<int:id>', RelatedPartyAPIView.as_view(), name='RelatedParty')
]
