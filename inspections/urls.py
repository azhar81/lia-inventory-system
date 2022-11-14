from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inspections import views

urlpatterns = [
  path('inspections/', views.InspectionList.as_view()),
  path('inspections/ongoing', views.InspectionListOngoing.as_view()),
  path('inspections/<int:pk>/', views.InspectionDetail.as_view()),
  path('inspections/<int:pk>/close', views.InspectionClose.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)