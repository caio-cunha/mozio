from django.urls import path
from area.views import AreaView, AreaViewDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('area', AreaView.as_view(), name='area'),
    path('area/<int:id>', AreaViewDetail.as_view(), name='area_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)