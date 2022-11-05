from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from assets import views

urlpatterns = [
    path('assets/', views.AssetList.as_view()),
    path('assets/<int:pk>/', views.AssetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)