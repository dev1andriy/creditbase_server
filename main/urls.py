from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework.authtoken.views import obtain_auth_token

from common.urls.main import urls

from main import views

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', views.AuthView.as_view(), name='authenticate'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('GetAccount', views.get_account, name='GetAccount'),
    path('account/profile/', views.profile, name='profile'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('fill-database', views.fill_database)
]

urlpatterns += urls
