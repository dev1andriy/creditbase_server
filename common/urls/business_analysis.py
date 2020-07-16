from django.urls import path
from common.views.business_analysis import IndustryAnalyzesAPIView, IndustryAnalysisAPIView

urlpatterns = [
    path('BusinessAnalysis/IndustryAnalyzes', IndustryAnalyzesAPIView.as_view(), name='IndustryAnalyzes'),
    path('BusinessAnalysis/IndustryAnalyzes/<int:id>', IndustryAnalyzesAPIView.as_view(), name='IndustryAnalyzes'),

    path('BusinessAnalysis/IndustryAnalysis', IndustryAnalysisAPIView.as_view(), name='IndustryAnalysis'),
    path('BusinessAnalysis/IndustryAnalysis/<int:id>', IndustryAnalysisAPIView.as_view(), name='IndustryAnalysis')
]
