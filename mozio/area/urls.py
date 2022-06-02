from django.urls import path
from area.views import AreaView, AreaViewDetail, AreaFilterView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('area', AreaView.as_view(), name='area'),
    path('area/<int:id>', AreaViewDetail.as_view(), name='area_detail'),
    path('area/filter', AreaFilterView.filter_by_provider, name='area_filter_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)