from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Test Mozio",
        default_version='v1.0.0',
        contact=openapi.Contact(email="caiocomputacao2014@gmail.com")
    ),
    url="http://localhost:8001",
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('provider.urls')),
    path('apis/', include('area.urls')),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(
        'docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')


]


