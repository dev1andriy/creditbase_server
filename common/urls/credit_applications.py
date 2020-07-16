from django.urls import path
from common.views import credit_applications as views

urlpatterns = [
    path('CreditApplications', views.CreditApplicationsAPIView.as_view(), name='CreditApplications'),
    path('CreditApplications/<int:id>', views.CreditApplicationsAPIView.as_view(), name='CreditApplications'),

    path('CreditApplication', views.CreditApplicationAPIView.as_view(), name='CreditApplication'),
    path('CreditApplication/<int:id>', views.CreditApplicationAPIView.as_view(), name='CreditApplication'),

    path('CreditApplication/<int:id>/Statuses', views.CreditApplicationStatusesAPIView.as_view(), name='CreditApplicationStatuses'),
    path('CreditApplication/<int:id>/General', views.CreditApplicationGeneralAPIView.as_view(), name='CreditApplicationGeneral'),
    path('CreditApplication/<int:id>/Checklists/<int:tab_id>', views.CreditApplicationChecklistsAPIView.as_view(), name='CreditApplicationChecklists'),
    path('CreditApplication/<int:id>/Notes', views.CreditApplicationNotesAPIView.as_view(), name='CreditApplicationNotes'),
    path('CreditApplication/<int:id>/Config', views.CreditApplicationConfigAPIView.as_view(), name='CreditApplicationConfig'),

    path('CreditApplications/Archive', views.CreditApplicationArchiveAPIView.as_view(), name='CreditApplications/Archive'),
    path('CreditApplications/Archived/<int:id>', views.CreditApplicationArchiveAPIView.as_view(), name='CreditApplications/Archived'),
    path('CreditApplications/UnArchive', views.CreditApplicationUnArchiveAPIView.as_view(), name='CreditApplications/UnArchive'),
    path('CreditApplications/UnArchived/<int:id>', views.CreditApplicationUnArchiveAPIView.as_view(), name='CreditApplications/UnArchived')
]
