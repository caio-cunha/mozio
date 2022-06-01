from django.urls import path
from provider.views import Provider

urlpatterns = [
    path('provider', Provider.as_view(), name="provider"),
]