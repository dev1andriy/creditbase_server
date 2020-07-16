from django.urls import path
from common.views.communication import EmailAPIView, EmailsAPIView

urlpatterns = [
    path('Communications/Emails', EmailsAPIView.as_view(), name='Emails'),
    path('Communications/Emails/<int:id>', EmailsAPIView.as_view(), name='Emails'),

    path('Communications/Email', EmailAPIView.as_view(), name='Email'),
    path('Communications/Email/<int:id>', EmailAPIView.as_view(), name='Email')
]
