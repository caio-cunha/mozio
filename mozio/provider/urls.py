from django.urls import path
from provider.views import ProviderView, ProviderViewDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('provider', ProviderView.as_view(), name='provider'),
    path('provider/<int:id>', ProviderViewDetail.as_view(), name='provider_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
